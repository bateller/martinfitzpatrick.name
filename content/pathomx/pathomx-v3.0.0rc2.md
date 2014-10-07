Date: 2014-10-07 21:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Pathomx v3.0.0 Release Candidate 2
Slug: pathomx-v3.0.0rc2-for-windows-and-mac
Tags: pathomx,metapath,software,metabolomics,bioinformatics,python,qt,pyside

The final release candidate for Pathomx v3.0.0 is available for both [Mac](http://download.pathomx.org/Pathomx-3.0.0rc2.dmg) and
[Windows](http://download.pathomx.org/Pathomx-3.0.0rc1.exe). This latest version features the new IPython
backend providing parallel processing (via IPython `ipcluster` support), numerous bugfixes and improvements
to the UI and figure outputs.

While a development version it is considered stable enough for normal use. It'd be great
if you could download and test it with your own hardware and data and see how it holds up. 
Report any problems via [Github issue tracker][https://github.com/pathomx/pathomx/issues]. 

<!-- PELICAN_END_SUMMARY -->


### What's new in v3.0.0rc2

New and improved user-interface offering quick access to tool configuration and output figures/data.

![software/pathomx/getting_started_pathomx_ui.png](/images/software/pathomx/getting_started_pathomx_ui.png)

Improved workflow editor with status-aware connectors and I/O ports to show calculation outcomes.

![software/pathomx/status_aware_workflow_editor.png](/images/software/pathomx/status_aware_workflow_editor.png)

Support for IPython `ipcluster` based parallel processing for complex workflows/tools.

![software/pathomx/multiprocessing.png](/images/software/pathomx/multiprocessing.png)

IPython-notebook `_repr_html_` aware visualisation of workspace variables.

![software/pathomx/ipython_repr_html_aware.png](/images/software/pathomx/ipython_repr_html_aware.png)

Inline per-tool code editor. Modify tool code to customise behaviour for your needs.

![software/pathomx/code_editor.png](/images/software/pathomx/code_editor.png)

Per-tool status, progress and error output.

![software/pathomx/per_tool_output_logging.png](/images/software/pathomx/per_tool_output_logging.png)




