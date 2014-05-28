@require(notebooks)
Title: Notebooks
Slug: notebooks

Below is a selection of [IPython data-analysis notebooks](http://ipython.org/notebook.html) (.ipynb) I've written.
The list is automatically generated from [this repo on Github](http://github.com/mfitzp/ipython-notebooks) and all notebooks are
freely available under CC-BY-SA/MIT licenses.

Some of the notebooks listed here may also be configured to run with [QtIPy](http://martinfitzpatrick.name/article/qtipy-the-data-automator/)
to automate your data analysis.

@for nb in notebooks:

### @nb['name']
@nb['description']

<a href="@nb['notebook_view_path']">View</a> &bull;
<a href="@nb['notebook_path'][0]" download="@nb['notebook_path'][1]">Download .ipynb</a>
@if 'examples' in nb:
@for k,v in nb['examples'].items():
&bull; <a href="@v[0]" download="@v[1]">Download @k</a>
@endfor
@endif

@endfor

