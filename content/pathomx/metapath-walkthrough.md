Date: 2013-11-18 00:35
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: MetaPath walkthrough
Tags: metapath,software,metabolomics,python,matlab
Status: draft
Github: pathomx/pathomx

MetaPath started out as pathway analysis software, using the MetaCyc/BioCyc database to 
render metabolic data onto dynamically drawn pathways. That functionality still exists,
but as mentioned in a previous post it has been extended to enable more complex,
extended and interesting analysis - and quickly!

<!-- PELICAN_END_SUMMARY -->

Below is a brief walkthrough of MetaPath: a metabolomic data analysis package. It's
currently in a pre-release bugfix state, in the run up to publication. But I thought I'd
give a brief overview of the functionality that's already in place, and plans for the future.

# Transcript

> Hello, this is a brief walkthrough of MetaPath: a metabolomic data analysis package. It's
currently in a pre-release bugfix state, in the run up to publication. But I thought I'd
give a brief overview of the functionality that's already in place, and plans for the future.

> MetaPath is a modular processing and analysis workflow system. In practise this means you
build analyses out of a series of modules that perform a particular function. By chaining
these together you can achieve quite complex things that are reproducible, shareable,
configurable. Modules (called apps in MetaPath) are provided by plugins, a set of
which are provided in the default MetaPath install.

> When opened, MetaPath greets you with this help screen. To start with, lets add some data.
We click the 'Import' section, and select Text/CSV to import from a .csv file. The plugin
comes with a help file with a step-by-step quick start intro. Select the file to open
and it is loaded. You can view the data on the Table tab, and a spectra representation on
the View tab - this wont be available for non-spectra datasets.

> Let's do something with the data. One common step in processing NMR spectra is binning, so let's do that. Processing -> Binning. A new binning app is added to the workspace and now available in the left sidebar. It will open with the spectra of the imported data with binning applied.

> We can adjust the bin size using the toolbar settings, and shift. Usefully, this MetaPath plugin 
also provides a visual representation of data loss resulting from binning.

> If you were paying attention you will have noticed that the data from the import app was  automatically pulled through to the binning. Let's see how that works. Click on the Home tab which is now showing the Workspace view. You can see the imported data in blue, and the  binning processing app in orange. Notice also the yellow output ports and dark-orange input ports. These control how data is moved in and out of different apps. By connecting output ports to input ports you can control the flow of data processing. 

> To show the sort of thing you can achieve, we'll open a saved workflow.

> Loading the workflow re-creates the apps and connections as you saved them, but not the data. So we'll next load in a new data file, just as before. The processing proceeds automatically, and selecting for example the PLS-DA app gives us the resulting figure. Notice that all downstream figures, calculations, analysis, etc. was re-produced immediately on loading the new dataset. In this way workflows can be used to automate common processing  procedures in repeatable and reproducible ways.

> Returning to the Workspace viewer you'll notice there are two streams here. On the left is a processing workflow for  1D NMR spectra, so lets load some data. You'll notice the processing started, but we're left with this small white flag. This is a pause indicator, showing that the processing in that app requires us to manually start it - this is optional, but set on by default for apps that request remote services - in this case MetaboHunter. So lets click the app, and set it running. After communicating with the server we will get back a list of mapped spectra peak identities, great.

> But how can we use this for analysis. If we return to the Workspace, click on the output port for MetaboHunter and drag it into our downstream analysis - here linked via a pass-through app (that simply passes the data on). Immediately the recalculation
occurs, and we get our figures.


So that concludes the brief tour of MetaPath. If you have any questions, comments or suggestions I'd love to hear them.
MetaPath is written in Python and all source code is available on github licensed under the GPL. A publication is coming soon.
