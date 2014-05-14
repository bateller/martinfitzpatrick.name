Date: 2014-05-14 21:57
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: QtIPy: The data automator
Slug: qtipy-the-data-automator
Tags: qtipy,ipython,automation,software,metabolomics,bioinformatics,python,qt,pyside

I've released a first version of a new package today - **QtIPy: *The data automator* **

![Screenshot](/images/software/qtipy/QtIPy-screenshot.png)

QtIPy is a simple GUI-based automator for IPython notebooks. It allows you to attach triggers to files, folders or timers to automatically run notebooks. 

IPython notebooks are great for interactively working through analysis problems, so why would you want to automatically run them? To get a record of how you ran your analysis! By running a notebook through QtIPy you get the data output, the figures and everything else output into a folder.

A dictionary of variables describing the current state is passed to the script (as a variable named `qtipy`) and can be used to control inputs, outputs and behaviours in the script. Watching a folder optionally iterates over all the files in a folder, which are also passed (in turn) to the notebook for processing. 

Using the triggers and variables, QtIPy allows you to automatically process data files, generate figures, etc. without lifting a finger. Automator sets can also be saved and loaded for future use.

![Screenshot](/images/software/qtipy/QtIPy-log.png)

Errors and progress is automatically logged to the log window.

![Screenshot](/images/software/qtipy/QtIPy-pause.png)

Automators can be paused to stop them processing, activated and run immediately.

Requires PyQt5. Compatible with both Python2.7 and Python3.4.

The back-end running is powered by [runipy](https://github.com/paulgb/runipy/), which is a great tool for running notebooks and getting output from the command line.
