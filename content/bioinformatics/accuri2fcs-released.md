Date: 2013-06-17 22:44
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: accuri2fcs: Convert Accuri .c6 flow cytometry files to .fcs [Released]
Tags: flow cytometry,fcs,accuri,c6
Github: mfitzp/accuri2fcs

[Accuri2fcs][accuri2fcs-github], a command line program for the conversion of Accuri `.c6` flow cytometry data files to the standard `.fcs` format, has been released today via [github][accuri2fcs-github] and [PyPi][accuri2fcs-pypi].

<!-- PELICAN_END_SUMMARY -->

# Background

Someone in our lab recently needed to convert a large number of files (>500) and 
processing each one manually in the c6 software wasn't going to be much fun. This script is the result of trying to automate that process, and it works. Usage is not *exactly* straightforward, however it is quite powerful.  In it's standard configuration it will find all `.c6` files in the current directory,
match every sample name outputting `.fcs` files named `[filename.c6]_[row|column].fcs`. This is probably perfectly fine for most uses.

However, it also supports the use of regular expressions to extract data from your `.c6` Sample Name fields, and then saving the resulting `.fcs` into named files and folders built from that data. Have fun!

# Download & Installation
You can install accuri2fcs via the PyPi Python package system. You can install via the command line with:

    pip install accuri2fcs

Alternatively the code (and issue tracker) is available on [github][accuri2fcs-github].

Once installed, using is as simple as entering on the command-line:

	accuri2fcs

…to convert everything in the current folder. You'll end up with a folder named `fcs` containing the output. For more options type `accuri2fcs --help`.

# License
Accuri2fcs is licensed under a Modified BSD 2 clause (i.e. completely free), my license of choice for interoperability software.

# Contributions
This software is not under active development (I don't do flow cytometry) but any [suggestions or bug reports][accuri2fcs-github] are still appreciated.


 [accuri2fcs]:
 [accuri2fcs-github]: https://github.com/mfitzp/accuri2fcs
 [accuri2fcs-pypi]: https://pypi.python.org/pypi/accuri2fcs/

