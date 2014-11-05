Date: 2014-10-26 18:03
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Pathomx v3.0.2 released
Slug: pathomx-v3.0.2-released
Tags: pathomx,metapath,software,metabolomics,bioinformatics,python,qt,pyside

Pathomx v3.0.2 has been released for both  [Windows][windows-download] and [MacOS X][mac-download].
This marks the first stable, bug-fixed release for the v3.0 line featuring the new [IPython][ipython]-kernel
with cluster support for parallel processing of tools. 

<!-- PELICAN_END_SUMMARY -->

![Screenshot](/images/software/pathomx/workflow_editor_nmr_v3.0.2.png)

This latest version adds a number of important features over the previous v2.0 series:

* IPython backend including a live in-process kernel for debugging and data exploration
* Pandas dataframe-based data handling
* Inline code editor: edit the Python code for any tool
* Figure-based data selection, select regions to exclude from spectra directly on the view output
* Fully functional python implementation of the icoshift algorithm for NMR (+ other spectra) alignment
* Support for custom tools, write your own scripts to process your data and connect them up
* Fixes for PCA and PLS-DA tools, scatter plots to show sample numbers
* New tools for hierarchical clustering based on [Christopher DeBoever's](cdeboever3.github.io) [code](http://nbviewer.ipython.org/github/ucsd-scientific-python/user-group/blob/master/presentations/20131016/hierarchical_clustering_heatmaps_gridspec.ipynb)
* Improved data importing in both the Text/CSV and Bruker (NMR) tools
* BioCyc database web API and cached database included
* Python, MATLAB, R scripting from within Pathomx

The IPython backend gets us all the benefits, bug fixes and improvements from that project 
directly into Pathomx (currently using the 3.0.0-dev branch). Similarly data handling is 
now performed (by default) using the Python data analysis library [Pandas][pandas].

![Screenshot](/images/software/pathomx/code_editor_v3.png)

## Future 

* Suport for remote cluster processing (to enable jobs to be run on a different computer to 
that running Pathomx)
* BioCyc API support for both the web and Pathway Tools API through single interface
* Improved generic database API to handle management of BioCyc and other data sources
* More tools, including support for most classification approaches in the sci-kit learn library

## Installation and getting started

You can [download Pathomx v3.0.2 here][all-downloads]. [Full documentation][pathomx-docs] is available 
and there is also a quick [getting started guide][pathomx-getting-started] to teach you 
the main principles of the software.

Feedback and [bug-reports](https://github.com/pathomx/pathomx/issues) are always welcome.


[pathomx]: http://pathomx.org/
[all-downloads]: http://pathomx.org/#download
[mac-download]: http://download.pathomx.org/Pathomx-latest.dmg
[windows-download]: http://download.pathomx.org/Pathomx-latest.exe
[pathomx-demos]: http://pathomx.org/#demos
[pathomx-docs]: http://docs.pathomx.org
[pathomx-getting-started]: http://docs.pathomx.org/en/latest/getting_started.html
[ipython]: http://ipython.org/
[pandas]: http://pandas.pydata.org/
