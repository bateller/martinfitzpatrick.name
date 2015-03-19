Date: 2015-03-09 16:37
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Wooey: Simple, automated web UIs for Python scripts
Tags: python,software,web,flask
Github: mfitzp/wooey

[Wooey](https://github.com/mfitzp/wooey) is a simple web interface (built on Flask) to run command line Python scripts. Think of it as an easy way to get
your scripts up on the web for routine data analysis, file processing, or anything else.

Inspired by what [Gooey](https://github.com/chriskiehl/Gooey) can do, turning ArgumentParser-based command-line scripts into WxWidgets-based GUIs, I thought I'd see if I could do the same for the web. I'm still not sure if the result is beautiful or horrific.

Wooey (see what I did there?) uses the same, albeit slightly modified, back-end conversion of ArgumentParser instances to JSON definitions. These definitions are used to construct a web-based UI with type-dependent widgets. Submitted configurations are parsed, using the JSON definition, to command line arguments that are then submitted to a job queue.

Jobs in the queue are automatically run and the results made available in the job view, with smart handling of outputs such as images (CSV, etc. to be supported via pandas, possibly some kind of plugin system) into a tabbed output viewer. Support for downloading of zipped output files is to follow.

The use case for myself was as a simple platform to allow running of routine data-processing and analysis scripts within a research group, but I'm sure there are other possibilities. However, I wouldn't recommend putting this on the public web just yet (pre-alpha warning). It's somewhat comparable to things like Shiny for R, except multi-user out of the box. Support for multiple command-line formats is on my todo.

Enjoy and [please fork liberally](https://github.com/mfitzp/wooey).

Built on Flask, using cookiecutter-flask then modified to use the Foundation framework. This is *My First Flask App!*
so please feel free to critique & give pointers.


## Walkthrough

The front page of a wooey install presents a list of installed scripts:

[![Welcome](/images/software/wooey/welcome_to_wooey.png)](/images/software/wooey/welcome_to_wooey.png)

Each script has it's own UI form based on the config parameters defined in the ArgumentParser:

[![bar_config example script](/images/software/wooey/bar_config.png)](/images/software/wooey/bar_config.png)

Documentation can be specified either manually via the JSON, or my providing a
[Markdown](http://en.wikipedia.org/wiki/Markdown)-format file alongside the script or config file.

[![plot_some_numbers script with docs](/images/software/wooey/plot_some_numbers_with_documentation.png)](/images/software/wooey/plot_some_numbers_with_documentation.png)

Logged-in users get a nice listing of their previous jobs:

[![User job listing](/images/software/wooey/user_job_list.png)](/images/software/wooey/user_job_list.png)

The output from successful jobs is available via an inline viewer (images only presently, .csv support via Pandas to follow):

[![Job with success 1](/images/software/wooey/job_success_1.png)](/images/software/wooey/job_success_1.png)
[![Job with success 2](/images/software/wooey/job_success_2.png)](/images/software/wooey/job_success_2.png)

Errors are output to the inline console:

[![Job with error console](/images/software/wooey/job_with_error.png)](/images/software/wooey/job_with_error.png)

