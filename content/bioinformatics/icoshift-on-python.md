Date: 2013-11-01 00:35
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Icoshift on Python
Tags: icoshift,metapath,software,metabolomics,python,matlab

[*I*coshift](http://www.ncbi.nlm.nih.gov/pubmed/20004603) is a Matlab-based algorithm for the alignment of NMR spectra. Devloped by [Francesco Savorani](www.models.life.ku.dk) and [Giorgio Tomasi](www.igm.life.ku.dk), it performs correlation shifting of spectral intervals, while employing FFT engine that aligns all spectra simultaneously. I've personally found it incredibly useful in the processing of data, particularly through [Metabolab](http://beregond.bham.ac.uk/nmrlab/).

While extending the NMR spectra processing capabilities of MetaPath it became obvious that spectral alignment would be *essential* in the toolkit - and *I*coshift was the obvious choice. While a Matlab bridge is in process, I wanted to see if it was possible to re-code the Icoshift algorith natively in Python - allowing MetaPath users to get access to it without having Matlab installed.

The answer is - yes!

#Icoshift in Python

The *I*coshift script was converted to Python using a combination of [SMOP](http://chiselapp.com/user/victorlei/repository/smop-dev/home) followed by hand re-coding using test datasets to check output at various steps. The interface remains identical to the Matlab version at present - a more Pythonic interface may be added later, but a directly comparable interface will be maintained. The Python implementation of *I*coshift is available from [github](https://github.com/mfitzp/icoshift) or [PyPi](https://pypi.python.org/pypi/icoshift/0.1).

To install (assuming you have installed `pip`):

    pip install icoshift

To use from your own script:

    import icoshift
    xCS,ints,ind,target=icoshift.icoshift('average',test)

Where `test` is an `numpy.array` of data - subjects in rows, ppm in columns. The outputs match those in the Matlab script: of most interest is xCS (the shifted spectra).

# Here Be Dragons

Conversion from one programming language to another is not straightforward. Particularly problematic here was the different indexing - zero-index vs. one-indexed arrays - in Python vs. Matlab. Simple to fix in situ, but less so when downstream code depends on it, after various matrix transformations.

At present this algorithm handles the basic *default* settings and no more. Contributions, bugfixes and - most importantly - Pythonification of the code is most welcome. It is duck ugly as it stands.

It is liable to break and give weird results in various corner cases not yet explored: your help is both appreciated and needed! This is intended as a first release ripe for Pythonification.

# But it works

Here is some sample output (run through [MetaPath](http://martinfitzpatrick.name/article/metapath-gets-flexible-an-interactive-analysis-workflow-tool) - yes there is already a plugin) showing the original and shifted data from a sample manually off-shifted dataset.

![icoshift/unshifted.png](/static/images/software/icoshift/unshifted.png)

![icoshift/shifted.png](/static/images/software/icoshift/shifted.png)

# Thanks

Thanks to [Francesco Savorani](www.models.life.ku.dk) and [Giorgio Tomasi](www.igm.life.ku.dk) for the original clever and well documented [algorithm](http://www.ncbi.nlm.nih.gov/pubmed/20004603).