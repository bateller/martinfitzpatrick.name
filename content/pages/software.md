Title: Software
Slug: software

Below is a list of all software I've released to date as part of my research. Unless I have taken
temporary leave of my senses all of it will be under some form of open-source
license (GPLv3 or MIT/BSD).

### [Accuri2FCS: Convert Accuri .c6 files to .fcs standard][accuri2fcs-github]
Accuri2svg is a command line program for the conversion of Accuri .c6 flow cytometry data files to the standard .fcs format. Either extract all the files directly, or use complex text-processing to name the resulting files using features of sample names.

[Github][accuri2fcs-github] &bull; [PyPi][accuri2fcs-pypi]  
*Available for free under the modified 2-clause BSD license.*

### [GPML2SVG: A command-line/Python GPML to SVG pathway renderer][gpml2svg-github]
GPML2SVG is a command line program and Python API for the conversion of pathways marked up using the GPML format, as supported by PathVisio and WikiPathways. It additionally
supports XRef linking, node colouring and synonym-recoding (so you can use alternative IDs if you have an appropriate conversion list). 

[Github][gpml2svg-github] &bull; [PyPi][gpml2svg-pypi]  
*Available for free under the modified 2-clause BSD license.*

### [IcoShift: A Python implmentation of the Icoshift algorithm][icoshift-github]
Icoshift is a versatile tool for the rapid alignment of 1D NMR spectra. This package is a Python implementation of the [icoshift][icoshift-original] algorithm as described by Francesco Savorani and Giorgio Tomasi. It uses correlation shifting of spectral intervals and employs an FFT engine that aligns all spectra simultaneously.

[Github][icoshift-github] &bull; [PyPi][icoshift-pypi]  
*Available for free under the modified 2-clause BSD license.*

### [Pathomx: Metabolic pathway visualisation and analysis][pathomx-www]  
<img src="/images/software/metapath_0.5.1_screenshot_sm.png" class="inline left">Pathomx is a workflow-based tool for the analysis of metabolic pathway and associated
visualisation of experimental data. Built on the MetaCyc database it provides
an interactive map in which multiple pathways can be simultaneously visualised.
Multiple annotations from the MetaCyc database are available including synonyms,
associated reactions and pathways and database unification links.

[Website][pathomx-www] &bull; [Github][pathomx-github] &bull; [PyPi][pathomx-pypi]  
*Available for free under the GNU General Pubic License v3*

### [QtIPy: The data automator!][qtipy-github]  
QtIPy is an automation tool for IPython notebooks. It allows notebooks to be automatically
run on triggers, e.g. file changes, folder changes or timers, as well as manually.

[Github][qtipy-github] &bull; [PyPi][qtipy-pypi]  
*Available for free under the GNU General Pubic License v3*





[pathomx-www]: http://pathomx.org/
[pathomx-github]: https://github.com/pathomx/pathomx/
[pathomx-pypi]: https://pypi.python.org/pypi/Pathomx/

[gpml2svg-github]: https://github.com/mfitzp/gpml2svg/
[gpml2svg-pypi]: https://pypi.python.org/pypi/gpml2svg/

[accuri2fcs-github]: https://github.com/mfitzp/accuri2fcs/
[accuri2fcs-pypi]: https://pypi.python.org/pypi/accuri2fcs/

[icoshift-github]: https://github.com/mfitzp/icoshift/
[icoshift-pypi]: https://pypi.python.org/pypi/icoshift/
[icoshift-original]: http://www.models.life.ku.dk/icoshift

[qtipy-github]: https://github.com/mfitzp/qtipy
[qtipy-pypi]: https://pypi.python.org/pypi/QtIPy



