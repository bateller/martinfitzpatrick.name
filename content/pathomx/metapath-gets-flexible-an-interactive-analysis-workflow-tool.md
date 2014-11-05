Date: 2013-10-13 10:37
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: MetaPath gets flexible: An interactive analysis workflow tool
Tags: metapath,software,metabolomics,qt,programming

It's been a while since I've posted an update on MetaPath development, which is finally forming into a solid package ready for publication. The latest version is [available here on Github](metapath-github), with binary packages to follow in the near future.

It's quite a transformation from earlier versions, so I thougth I'd take some time to walk through the new features and ideas, with a few notes on implementation.

<!-- PELICAN_END_SUMMARY -->

# Where we were

With the first release of the software, we had a nice package in place offering pathway exploration, some limited pathway analysis and visualisation of experimental data on those pathways. The key feature of the package was the automated layout of metabolic pathways making visualisation of obscure (and compound) pathways relatively simple.

Over time it became apparent that other views of data would be potentially useful. A basic heatmap viewer was implemented, plus support from GPML and WikiPathways. While these worked fine, the interface was becoming slightly illogical - you could load data, design an 'experiment' but that would apply only to some visualisations. Similarly, there was no way to support incremental - or conditional - analysis, or processing, or data sets.

# Scientific workflows

> A scientific workflow system is a specialized form of a workflow management system designed specifically to compose and execute a series of computational or data manipulation steps, or a workflow, in a scientific application - [WikiPedia](scientific-workflows-wiki)

I'd got interested in scientific workflows having read about existing solutions such as [Taverna](taverna). However, these existing tools are typically tailored towards fully-automated *big data* analysis - and require more than a passing familiarity with programming/data formats. I wanted to take *some* of this power and offer it in a user-friendly application for the local analysis of experimental *small data* sets. 

The result is an application with a workflow-like internal structure, that presents data analysis in a familiar view (similar in structure to [GraphPad Prism](graphpad-prism)). Tasks are broken down into distinct phases - import, processing, identification, analysis and visualisation - to mimic the normal phases of experimental data handling, although this order is not fixed. A workflow overview is provided for a conceptual view of what you've done, and processing details are available for all resulting images.

Development has particularly focused on metabolomics data, largely since that is the focus of my PhD - however support for integration of other datasets (or multiple metabolomics datasets) was a bonus. 

![software/metapath/nh-demo-start.png](/images/software/metapath/nh-demo-start.png)

# Data import

Import is supported from a number of sources including BML-NMR, Chenomx, PeakML, CSV, Metabolights and raw NMR spectra (Bruker currently, more to follow). One of the key features of MetaPath is that all data is stored in a regular internal format, meaning that whatever the source, downstream plugins can made use of it without knowing what it is. What data types are acceptable for each processing step is defined using 'consumers' on each one (…but this is an internal plugin feature, and users don't need to know a thing about it!)

# Processing

Processing steps are those that transfer the raw data into a form more useable for subsequent analysis. For metabolomics analysis this includes processes such as binning, phase correction, baseline-correction etc.

Currently binning is supported (the others to follow as provided by the [NMRGlue](nmrglue) library). Importantly, MetaPath supports *live* binning, whereby you can see the effects of your changes on the spectra (bin size, offset), together with a data-loss visualisation indicating areas of the spectrum that are most affected. The plan is to integrate this data into the data model object, so subsequent analysis can inform you if that whopping significant difference you're observing is really an artefact of processing.

![software/metapath/nh-demo-spectra.png](/images/software/metapath/nh-demo-spectra.png)

![software/metapath/nh-demo-binning.png](/images/software/metapath/nh-demo-binning.png)

Other basic transformations are available including mean-centering, log transforming, baselining, setting minima both locally and globally. 

![software/metapath/nh-demo-mean-centre.png](/images/software/metapath/nh-demo-mean-centre.png)

Exclusion and filtering of data is also supported by various characteristics.

# Identification

A key step in analysis is relating what you've found to other data sources. In order to facilitate this MetaPath supports data unification and entity-mapping for imported data sources. In English this means that it can map your data labels to biological entities. 

The most basic implementation of this is using synonym name matching, but other alternatives are available including remote NMR spectra processing via [MetaboHunter](metabohunter).

![software/metapath/nh-demo-synonyms.png](/images/software/metapath/nh-demo-synonyms.png)

# Analysis

"The stats bit". Analysis plugins currently included include support for principal components analysis (PCA) via SVD, PLS-DA and fold-change calculations. Every other statistical test you can think of will be implemented shortly, and resulting statistical findings (p values etc.) can be passed for subsequent visualisation on graphs. As with everything else this will be a semi-automated feature, set it up and see the results applied to subsequent data exactly the same.

![software/metapath/nh-demo-plsda.png](/images/software/metapath/nh-demo-plsda.png)

On particularly neat feature is that because identification has already been carried out prior to analysis, the resulting figures can be automatically annotated with entity information. Here for example is the PLS-DA weights plot showing identified metabolites key to the separation.

![software/metapath/nh-demo-plsda-weights.png](/images/software/metapath/nh-demo-plsda-weights.png)

Metabolites identified in blue have been automatically mapped to internal Biocyc entities, and can be view through the internal database browser.

![software/metapath/nh-demo-db-unification.png](/images/software/metapath/nh-demo-db-unification.png)

# Visualisation

Finally. You have your data, you've done your processing, identification and analysis, and now you want to make some nice figures for the Nature paper. MetaPath comes with a mix of standard visualisation tools and some more experimental things, in addition the pathway rendering where this all started! Most new visualisations are powered by the [d3](d3) Javascript visualisation library, which offers beautiful, scalable and interactive visuals. Below are a few examples of the output for the sample dataset:

![software/metapath/nh-demo-bar.png](/images/software/metapath/nh-demo-bar.png)
![software/metapath/nh-demo-correlation-matrix.png](/images/software/metapath/nh-demo-correlation-matrix.png)
![software/metapath/nh-demo-pathway-connects.png](/images/software/metapath/nh-demo-pathway-connects.png)
![software/metapath/nh-demo-metaviz.png.png](/images/software/metapath/nh-demo-metaviz.png)


# The end

The end product of all this is a completed analysis workflow and a workspace of processed data. Perhaps the most neatest aspect of this is that the completed workflow can be simply re-applied to a new dataset without modification.  Processing is automatic (although individual steps may be 'paused', e.g. when they depend on remote queries) with status flags updating on the current processing progress. Tweaking any step will automatically update all children.

![software/metapath/nh-demo-workspace.png](/images/software/metapath/nh-demo-workspace.png)

The workflow hierarchy of data is available at any point from the Home tab. It's currently view-only, but will be extended to allow live editing of data dependencies within the workspace.

![software/metapath/nh-demo-workflow.png](/images/software/metapath/nh-demo-workflow.png)

# What's next?

The software is now in a bugfixing state with some minor tweaks to usability, options and configurability before publication (hopefully in the coming months) and release of built binaries. 

Help is always appreciated - including translations, plugins, or suggestions. I'd also love to hear examples of other people using MetaPath in their analysis. Get in touch!


[scientific-workflows-wiki]: http://en.wikipedia.org/wiki/Scientific_workflow_system
[graphpad-prism]: http://www.graphpad.com/scientific-software/prism/
[metapath-github]: https://github.com/mfitzp/metapath
[taverna]: http://en.wikipedia.org/wiki/Taverna_workbench
[metabohunter]: http://www.nrcbioinformatics.ca/metabohunter/
[d3]: http://d3js.org/
