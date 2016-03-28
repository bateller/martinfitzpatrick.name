Date: 2015-10-17 09:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: 1D 1H NMR data processing
Slug: 1d-1h-nmr-data-processing
Tags: 1d,nmr,python

1D <sup>1</sup>H NMR is a common technique applied to metabolomic studies, being well suited
to untargeted analysis of complex biofluids. It has been successfully applied to
the classification and diagnosis of a number of diseases including [ref].

There are a number of important steps that must be applied prior 1D <sup>1</sup>H NMR data
to statistical analysis, all gearded towards ensuring that the variation observed
in the data is representative of real biological variation and not a artifact of
sample handling, metabolite extraction or NMR acquisition. These steps are
described briefly below and approached in turn in the following method. It is
important to familiarise yourself with both the purpose of these steps, and
any associated caveats or limits, so that you can correctly apply them to your
own data.

# Setting up

To process raw NMR data we will be making use of of the `nmrglue` library. In
addition we will make use of features from the `numpy`, `scipy` and `matplotlib`
libraries, which you should already have installed.
To make sure you can run the following command on the terminal:

    pip install numpy scipy nmrglue matplotlib

The demo data for this example is [available for download](http://download.martinfitzpatrick.name/1d-1h-nmr-data-processing.zip).

Download and unzip the file into your data folder.

# Loading Bruker FID spectra

Create a new Jupyter notebook using the Python 3 kernel, and in the first cell
enter and run the following. This will import all the neccessary libraries, as
well as using the `%matplotlib` magic to display output figures in the notebook.

    %matplotlib inline
    import matplotlib.pyplot as plt
    import nmrglue as ng
    import numpy as np
    import scipy as sp
    import os
    plt.style.use('ggplot')

Bruker-format data is processed using a digital filter before saving as FID, this
filter must be removed for subsequent analysis to work. To open a given spectra,
pass the parent folder of the `fid` file.

    dic, data = ng.fileio.bruker.read('87')
    data = ng.bruker.remove_digital_filter(dic, data)

We can plot the spectra using `matplotlib`.

    fig = plt.figure(figsize=(12,4))
    ax = fig.add_subplot(1,1,1)
    ax.plot(np.arange(0, data.shape[0]), data) # <1>

1. We don't have the x-axis _ppm_ scale yet, so we generate a linear
   scale of the same size as the data. Here `.shape[0]` is the length of the fid along
   the first (and only) axis of the 1D spectra.

![The raw FID data for spectra 87](/images/tutorials/1d-1h-nmr-data-processing/single-spectra-raw.png)


# Fourier transform (FT)

A _fourier transform_ is a signal transformation that decomposes a signal
into it's constituent frequencies. In the case of NMR data, this decomposition
is to a series of peaks, that represent the resonance of chemical subgroups. These
peaks contain both our identification (frequency) and quantification (amplitude)
information.

The `nmrglue` package provides a _fast fourier transform_ (FFT) for this purpose

    data_fft = ng.proc_base.fft(data)

    fig = plt.figure(figsize=(12,4))
    ax = fig.add_subplot(1,1,1)
    ax.plot(np.arange(0, data_fft.shape[0]), data_fft)

![The fourier transformed FID data for spectra 87](/images/tutorials/1d-1h-nmr-data-processing/single-spectra-fft.png)

You'll notice that the spectra is out of _phase_, i.e. the peaks are not
symmetrical and well defined. We will fix this shortly, but first lets load
a complete set of spectra so we can view them all at once.

# Batch loading + FFT for multiple spectra

    root_folder = '.'
    zero_fill_size = 32768
    data = [] # <1>
    for folder in os.listdir(root_folder):
        dic, fid = ng.fileio.bruker.read(os.path.join(root_folder,folder))
        fid = ng.bruker.remove_digital_filter(dic, fid)
        fid = ng.proc_base.zf_size(fid, zero_fill_size) # <2>
        fid = ng.proc_base.rev(fid) # <3>
        fid = ng.proc_base.fft(fid)
        data.append(fid)
    data = np.array(data)

1. We build as a list, then transform to an array for speed.
2. Zero-filling to a power of 2 speeds up FFT.
3. Reverse the data to match common representation (for convenience only).

The data is output in a 2D array, with samples along the first axis.

    data.shape

    (17, 32768)

We want to be able to plot multiple spectra on the same plot, so we'll write
a simple function to do this.

    def plotspectra(ppms, data, start=None, stop=None):

        if start: # <1>
            ixs = list(ppms).index(start)
            ppms = ppms[ixs:]
            data = data[:,ixs:]
        if stop:
            ixs = list(ppms).index(stop)
            ppms = ppms[:ixs]
            data = data[:,:ixs]


        fig = plt.figure(figsize=(12, 4))
        ax = fig.add_subplot(1,1,1)
        for n in range(data.shape[0]):
            ax.plot(ppms, data[n,:])

        ax.set_xlabel('ppm')
        ax.invert_xaxis()

        return fig

1. This block allows us to select regions of the spectra to view by filtering
   on the supplied ppms.

We can use this function to look at all spectra following fourier transform:

    ppms = np.arange(0, data.shape[1])
    fig = plotspectra(ppms, data)

![All spectra following fourier transformation](/images/tutorials/1d-1h-nmr-data-processing/all-spectra-fft.png)

We can take a close up view of the TMSP peak, which is currently on the left
hand side of the spectra in the region 28000-30000.

    ppms = np.arange(0, data.shape[1])
    fig = plotspectra(ppms, data, start=28000, stop=30000)


![The cropped TMSP region of all spectra following fourier transformation](/images/tutorials/1d-1h-nmr-data-processing/all-spectra-crop-fft.png)


Clearly the spectra are all out of phase and poorly aligned. We will fix the
phasing problem first, but lets start off by getting the correct ppm values for
the spectra.

# Calculating ppm values

The method for calculating ppm values is rather complicted for Bruker format
files. However, the following will give the correct output:


    offset = (float(dic['acqus']['SW']) / 2) - (float(dic['acqus']['O1']) / float(dic['acqus']['BF1']))
    start = float(dic['acqus']['SW']) - offset
    end = -offset
    step = float(dic['acqus']['SW']) / zero_fill_size

    ppms = np.arange(start, end, -step)[:zero_fill_size]

We can now plot the spectra with the correct ppms.

    fig = plotspectra(ppms, data)


![All spectra following fourier transformation with correct ppm values](/images/tutorials/1d-1h-nmr-data-processing/all-spectra-fft-ppm.png)


# Phase correction

The next step is to phase correct all the spectra. The package `nmrglue` provides
a few automated algorithms that do a reasonable job with most normal, good quality
spectra. Thankfully, that's what we have here.

    for n in range(0, data.shape[0]):
        data[n, :] = ng.proc_autophase.autops(data[n,:], 'acme')
    fig = plotspectra(ppms, data)


![Phase corrected spectra](/images/tutorials/1d-1h-nmr-data-processing/all-spectra-phase-correct.png)
