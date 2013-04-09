Date: 2013-04-09 15:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: MetaPath: Metabolic pathway visualisation and analysis [Released]
Slug: metapath-v0.5.1-released
Tags: metapath,software,metabolomics,bioinformatics,python,qt,pyside

[MetaPath][metapath-github], a metabolic pathway visualisation and analysis tool I've developed as part of my PhD, has been released today via [PyPi][metapath-pypi] and [github][metapath-github]. A [Mac .app][metapath-macapp] bundle is also available.

![Screenshot](/static/images/software/metapath_0.5.1_screenshot.png)

**Download** [Mac OS X Mountain Lion .app][metapath-macapp] &bull; [Github][metapath-github] &bull; [Python .eggs or .gz source][metapath-pypi].

> MetaPath requires installation of [Graphviz][graphviz] for pathway drawing.

# Who's it for?

MetaPath is developed as an ongoing part of my PhD to build analysis software for metabolic pathways that is user-friendly, intuitive, informative and quick. However, it is equally suited for educational purposes, particularly metabolic pathway exploration. 

It is based on the [MetaCyc][metacyc] database. If you use that, you might want to use this.

# What does it do?

MetaPath has two key use-cases:

**Metabolic pathway exploration:** Browse through the metabolic pathway database, with automated clean rendering of pathways. Add and remove metabolic pathways, show intra-pathway linkages, and map metabolic routes through the system. Browse the in-built database, following links to online resources for further information.

**Metabolic data visualisation:** Load experimental data gathered by mass-spectroscopy  (MS) or nuclear magnetic resonance (NMR) spectroscopy and visualise metabolic changes overlaid on a a map of the sytem. Visualise gene-expression or protein quantity data alongside to explore relationships between enzyme regulation and metabolic processes. Use the built-in "Pathway Mining" tools to select the most up, down, or overall regulated pathways in the given system to identify the key mechanisms at work.


# How much does it cost?

Nothing. It's released open-source under the the GPLv3 license and is therefore free to use for whatever purposes you wish. You can [clone the repository][metapath-github], [download .eggs or .gz source][metapath-pypi] or download a built [Mac app][metapath-macapp]. Builds for other platforms will follow shortly.

> MetaPath is built on the [MetaCyc](http://metacyc.org) pathway database itself part of 
the [BioCyc](http://biocyc.org) family. The supplied database is generated via the 
MetaCyc API and stored locally. Licenses for the entire MetaCyc database
[are also available](http://metacyc.org/contact.shtml) free of charge for academic
and government use.

# What else?

Contributions from users and developers at other institutions are most welcome. Fork the [repo on github][metapath-github]. If you have issues, bugs or feature requires [please report them][metapath-github-issues] and I'll do what I can. Finally, if you have any questions drop a note in the comments below.
 
[metapath-github]: https://github.com/mfitzp/metapath/issues
[metapath-github-issues]: https://github.com/mfitzp/metapath
[metacyc]: http://metacyc.org
[metapath-macapp]: http://downloads.martinfitzpatrick.name/MetaPath.dmg
[metapath-pypi]: https://pypi.python.org/pypi/metapath
[graphviz]: http://www.graphviz.org/