Date: 2014-02-19 14:24
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Pathomx does MATLAB, R, Python
Slug: pathomx-does-matlab-r-python
Tags: pathomx,software,metabolomics,matlab,r,python

The development version of Pathomx now supports custom scripting in Python, MATLAB and R. 

![Screenshot](/images/software/pathomx/pathomx-scripting-demo.png)

Integration with existing omics workflows is a key goal of Pathomx, and to do this requires interoperability with other platforms. In the upcoming release you'll now get access to custom scripting in MATLAB, R or Python direct from within Pathomx.

MATLAB and R scripting gives you access to any previously-installed toolboxes on your system directly. Data can be fed into the script via the workflow editor, manipulated by the script, then exported for subsequent analysis or plotting within Pathomx.

<iframe width="560" height="315" src="http://www.youtube.com/embed/V1uE8ILf4TE" frameborder="0" allowfullscreen></iframe>

Pathomx handles conversion of it's internal data format to a standard matrix for processing. Any tools available in your local install of MATLAB or R can be accessed in this way - for example in the video above we demonstrate using the baselinenl function from MATLAB-based NMR toolbox NMRLab.

All these tools will be available in the next release of Pathomx (v2.3) coming shortly.
