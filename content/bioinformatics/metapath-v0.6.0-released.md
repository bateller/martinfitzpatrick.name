Date: 2013-06-20 16:55
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: MetaPath v0.6.0 Released	
metapath,software,metabolomics,bioinformatics,python,qt,pyside

An update has been released today for [MetaPath][metapath-github], a metabolic pathway visualisation and analysis tool. It is available  via [PyPi][metapath-pypi] and [github][metapath-github]. A [Mac .app][metapath-macapp] bundle is also available.

![Screenshot](/static/images/software/metapath_0.6.0_screenshot.png)

**Download** [Mac OS X Mountain Lion .app][metapath-macapp] &bull; [Github][metapath-github] &bull; [Python .egg or .gz][metapath-pypi].

> MetaPath requires installation of [Graphviz][graphviz] for pathway drawing.

More background on the software is given in the [original release announcement][metapath-release-initial].

# What's new?

This latest release of MetaPath brings a number of useful new features for both data analysis and educational uses, together with a number of bug fixes and stability improvements. As always, [feedback and bug reports are appreciated][metapath-github-issues]!

![Screenshot](/static/images/software/metapath_0.6.0_screenshot-1.png)

**Compartmentalisation:** MetaPath is now aware of reaction compartamentalisation, as derived from BioCyc protein localisation data. Using this data, it is now possible to draw overviews of reaction locations within the cell and use this to guide analysis. Compartment-based scoring will be introduced in later versions.

![Screenshot](/static/images/software/metapath_0.6.0_screenshot-2.png)

**Metabolite structure images:** Built with permission from [KEGG][kegg] metabolite structure data. You can now visualise reactions with metabolite structure images to see actual molecular changes taking place at each step. Images can also be coloured for data analysis purposes. Atom-tracking is the eventual goal, of particular use in metabolic flux experiments.

![Screenshot](/static/images/software/metapath_0.6.0_screenshot-3.png)

**GPML (WikiPathways) support:** Based on my recent work on [gpml2svg][gpml2svg], MetaPath now supports GPML natively and can display GPML marked up pathways within the application. Data visualisation is not currently supported (it is present in the underlying gpml2svg code, but needs a bit of work translating database identifiers).

# What's next?

Current plans include data visualisations on GPML format pathways (including longitudinal analysis to match MetaCyc pathway capabilities), data analysis and visualisation tools including graphing, heatmaps and other meta-summaries of metabolite changes (oxidative state, ATP-ADP balance, etc.), support for data input, annotation and display (spectra, peak picking, etc.). Look out for updates!
 
[metapath-github]: https://github.com/mfitzp/metapath
[metapath-github-issues]: https://github.com/mfitzp/metapath/issues
[metacyc]: http://metacyc.org
[metapath-macapp]: http://download.martinfitzpatrick.name/MetaPath.dmg
[metapath-pypi]: https://pypi.python.org/pypi/metapath
[graphviz]: http://www.graphviz.org/
[metapath-release-initial]: http://martinfitzpatrick.name/article/metapath-v0.5.1-released
[kegg]: http://kegg.jp/
[gpml2svg]: http://martinfitzpatrick.name/article/gpml2svg-a-command-line-svg-renderer-for-gpml-pathways-released
