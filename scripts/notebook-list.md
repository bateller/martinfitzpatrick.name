@require(notebooks)
Title: Notebooks
Slug: notebooks

Here you'll find a selection of publicly-available [IPython Notebook](http://ipython.org/notebook.html) files (.ipynb) I've written. 
The list is automatically generated from my [notebook repo on Github](http://github.com/mfitzp/ipython-notebooks) here and 
will incude notebooks for common data processing tasks.

Some of the notebooks listed here may also be configured to run with [QtIPy](http://martinfitzpatrick.name/article/qtipy-the-data-automator/)
to automate your data analysis.

@for nb in notebooks:

### @nb['name']
@nb['description']

Download this notebook: [.ipynb](@nb['notebook_path'])
@if 'examples' in nb:
@for k,v in nb['examples'].items():
[@k](@v)
@endfor
@endif

@endfor

