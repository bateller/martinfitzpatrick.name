Date: 2013-06-16 19:09
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: gpml2svg: A command-line SVG renderer for GPML pathways [Released]
Tags: gpml,pathways,metabolomics,svg,metapath,software,metabolomics,bioinformatics

[Gpml2svg][gpml2svg-github], a command-line/Python API for rendering GPML pathway markup to SVG, has been released today via [github][gpml2svg-github] and [PyPi][gpml2svg-pypi].

# Background
In order to add support for GPML pathways (and later KEGG) in [MetaPath][metapath-github] I needed a way to get SVG rendered versions of marked up pathways. The SVG available on WikiPathways looked good but doesn't have support for external links (XRef), node identifiers/CSS (to apply transition/style effects to particular nodes) or optional switching on/off of elements. I also ideally wanted something that didn't rely on an internet connection to get at. I saw there was a PHP-based tool but it was incomplete. So I set about seeing if I could write a command-line renderer: and `gpml2svg` is the result of doing so using Python.

# Status
'Quite functional'. The two images below show (1) stock SVG available on WikiPathways and (2) output from a given GPML file using gpml2svg. 

![WikiPathways](/static/images/software/gpml2svg_wikipathways.png)
![gpml2svg](/static/images/software/gpml2svg_gpml2svg.png)

There are a few things that are 'off' (for example the mitochondrion compartment is aligned wrongly) but these are cosmetic and just need some number tweaking. There is only support for shapes that were in the files I tested (mostly squares and the group 'hexagon' for complexes). The elbow-edge drawing is also potentially awful - out of the week it took to write this I probably spent at least a third of the time on trying to get my head around making that work from the limited data in the GPML files! But it seems to be there. Hardly important but the files are also smaller.

# Download & Installation
You can install gpml2svg via the PyPi Python package system. You can install via the command line with:

    pip install gpml2svg

Alternatively the code (and issue tracker) is available on [github][gpml2svg-github].

Once installed, using is as simple as entering on the command-line:

	gpml2svg -f <filename.gpml>
	
..the resulting SVG file will be saved to the current folder with an `.svg` extension. The command-line interface will be improved in future!

You can also access gpml2svg as a Python package, using

	import gpml2svg
	
	gpml2svg(<svg-as-string>)
	
Other options, including color-coding and XRef extras are available - I'll be documenting these once the API has stabilised.

If you're interested in creating and editing pathways then [PathVisio][pathvisio] & [WikiPathways][wikipathways] are both great tools well worth taking a look at.


# License
Gpml2svg is licensed under a Modified BSD 2 clause (i.e. completely free), my license of choice for interoperability software. You can do with it what you will!

# Contributions
Any [suggestions or bug reports][gpml2svg-github] are much appreciated, as are example GPML files that do not convert properly. Finally, if you have any questions please feel free to drop a note in the comments below.


 [gpml2svg-github]:https://github.com/mfitzp/gpml2svg
 [metapath-github]: https://github.com/mfitzp/metapath
 [gpml2svg-pypi]: https://pypi.python.orgpypi?:action=display&name=gpml2svg&version=0.1.3
 [pathvisio]: http://www.pathvisio.org/
 [wikipathways]: http://wikipathways.org/

