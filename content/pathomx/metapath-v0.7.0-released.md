Date: 2013-07-03 11:03
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: MetaPath v0.7.0 Released	
Tags: metapath,software,metabolomics,bioinformatics,python,qt,pyside
Status: published
Github: pathomx/pathomx

An update has been released today for [MetaPath][metapath-github], a metabolic pathway visualisation and analysis tool. It is available  via [PyPi][metapath-pypi] and [github][metapath-github]. A [Mac .app][metapath-macapp] bundle is also available.

<!-- PELICAN_END_SUMMARY -->

![Screenshot](/images/software/metapath_0.7.0_screenshot.png)

**Download** [Mac OS X Mountain Lion .app][metapath-macapp] &bull; [Github][metapath-github] &bull; [Python .egg or .gz][metapath-pypi].

> MetaPath requires installation of [Graphviz][graphviz] for pathway drawing.

More background on the software is given in the [original release announcement][metapath-release-initial].

# What's new?

This release is focused on improving the data-visualisation capabilities of MetaPath with both GPML pathway data-overlay and heatmap visualisations for datasets (via matplotlib). As always, [feedback and bug reports are appreciated][metapath-github-issues]!

![Screenshot](/images/software/metapath_0.7.0_screenshot-1.png)

**GPML visualisation:** MetaPath can now visualise experimental datasets on GPML-generated pathway maps. These are automatically updated as control:test combinations are changed, and further pathways can be browsed using the in-pathway links. Metabolites identified in the current database via Xref linking can also be clicked to bring up database information.

![Screenshot](/images/software/metapath_0.7.0_screenshot-3.png)

![Screenshot](/images/software/metapath_0.7.0_screenshot-2.png)

**Heatmap data visualisation:** Metabolomic datasets can now be visualised as heatmaps for raw concentration and log2 change. A number of default visualisations are automatically generated including key metabolites (as determined by the control:test analysis) as well as oxidative/reductive status, phosphate carriers and waste/energy products. Customisation of these will be added in future releases - if there are further visualisations that would be useful to you, let me know.

# What's next?

Further development of the visualisations is currently planned, for example with graphing focused on individual metabolites (customisable through the data-browser), longitudinal data visualisation and the implementation of some basic stats functions.

Analysis improvements, including in-built PCA/PLS-DA and the ability to visualise this data using the same methods available for raw datasets.

An overview of metabolite identification (the Xref translations, ppm, etc.) would be nice, perhaps with spectra visualisations/peak picking for appropriate datasetss.

Finally, as the software extends to a more general metabolomics data-analysis package, the ability to export/save the generated figures & reload analysis packages will become rather important! Look out for updates!
 
[metapath-github]: https://github.com/mfitzp/metapath
[metapath-github-issues]: https://github.com/mfitzp/metapath/issues
[metacyc]: http://metacyc.org
[metapath-macapp]: http://download.pathomx.org/Pathomx-latest.dmg
[metapath-pypi]: https://pypi.python.org/pypi/metapath
[graphviz]: http://www.graphviz.org/
[metapath-release-initial]: http://martinfitzpatrick.name/article/metapath-v0.5.1-released
[kegg]: http://kegg.jp/
[gpml2svg]: http://martinfitzpatrick.name/article/gpml2svg-a-command-line-svg-renderer-for-gpml-pathways-released
