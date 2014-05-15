@require(notebooks)
Title: Notebooks
Slug: notebooks

Below are a list of my publicly available IPython Notebook files (.ipynb). This listing is
automatically generated from my [notebook repo on Github](http://github.com/mfitzp/ipython-notebooks) here.

@for nb in notebooks:

### @nb['name']
@nb['description']

Download this notebook: [.ipynb](http://githubusercontent.com/mfitzp/ipython-notebooks/@nb['notebook_path'])
@if 'examples' in nb:
@for k,v in nb['examples'].items():
[@k](http://githubusercontent.com/mfitzp/ipython-notebooks/@v)
@endfor
@endif

@endfor

