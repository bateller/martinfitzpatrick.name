Date: 2014-06-24 11:32
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Pathomx meets IPython - Workflow construction with IPython notebooks (and vice versa)
Slug: pathomx-meets-ipython-workflow-construction-with-ipython-notebooks
Tags: pathomx,ipython,software,metabolomics,bioinformatics,python,qt,pyside
Github: pathomx/pathomx

A new developer release of Pathomx (v3.0.0a) is out today via Github and PyPi. This release
brings an IPython backend and support for IPython-notebook based plugins. 

<!-- PELICAN_END_SUMMARY -->

This short demo demonstrates a few neat features -

<iframe width="560" height="315" src="http://www.youtube.com/embed/L5HxshxH67o" frameborder="0" allowfullscreen></iframe>

* Build workflows using IPython-notebook backed tools (all tools have been converted)
* Auto-display of Matplotlib figures and pandas dataframes from workbooks
* Auto-export of (selected) variables from workbooks to pass to other tools
* Save and reload workflows to share analysis approaches
* Export completed workflows to compound IPython notebooks to run independently

Building on IPython notebooks required that all the tools used for them are available in the Python install. This in turn means that all the (more complex) algorithms needed to be packaged. As a result I've released some of the key internals as separate packages including: [biocyc]() (a Python BioCyc interface with cacheing), [pyqtconfig]() (a package for syncing Qt widgets with a config dictionary/QSettings instance), [metaviz]() (a metabolic pathway automated drawing tool, built on GraphViz) and [pathminer]() (a pathway and reaction-mining algorithm). All these packages are available for use in other projects

Additionally, for compatibility all the code has been moved over to use Pandas dataframes, which offer a lot more flexibility - and speed for data transformations.

## Caveats

This developer release has a number of issues compared to the previous release (hey, it's alpha), including:

* No support for multi-threading. Getting Qt threads to work with IPython is rather difficult, leading to a lot of segfaulting. This should be rendered uneccessary once a Qt5 implementation of the IPython kernel is available (will probably work on it).
* Some graphs (bar) are not working.
* Colour data annotations not implemented (working on a standard implementation across tools).
* Missing entities in database lookup non-handled (this is a biocyc plugin issue).

But apart from that it's awesome.

## Plans

* Support will be added for drag-drop addition of IPython notebooks direct into the workspace.
* Configuration of inputs/ouputs from within the software. 
* Completely remove Python bootstraps for most plugins (may still be required for more complex configuration interfaces).
* Fix the things the remaining regressions from version 2.7.

Help is most appreciated, either in cosntruction of IPython notebooks to use with Pathomx or for work on the main code itself. Comments and suggestions most welcome.




