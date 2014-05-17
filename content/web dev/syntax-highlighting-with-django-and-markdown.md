Date: 2012-01-19 09:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Syntax highlighting with Django and Markdown
Slug: syntax-highlighting-with-django-and-markdown
Tags: django,programming,syntax-highlighting,web-dev,computing
Picture: /images/method/1525/Screenshot%20from%202012-07-19%2022%3A04%3A21.png

Syntax highlighting is more than just eye candy. It can turn a block of impenetrable code into a simple grok (although it has it's limits). To boost the usability of our code guides on this site we wanted to implement nice clear syntax highlighting of our hacks. Code samples are already marked up with markdown syntax so an extension to this is the obvious choice.

<!-- PELICAN_END_SUMMARY -->


Here we document the process of implementing syntax highlighting on markdown marked-up(!) code blocks.


![method/1525/Screenshot from 2012-07-19 22:04:21.png](/images/method/1525/Screenshot%20from%202012-07-19%2022%3A04%3A21.png)



>The resulting markup is heavily dependent on whether the language is detected. You can tell the parser what language you are using with a few simple lines at the top of your code:

>Start your code with a shebang with path, and the language will be derived from that, with line numbers

>

>    #!/usr/bin/python

>

>Use a shebang without the path and the shebang line will be removed: 

>

>    #!python

>

>Start the first line with three colons (:::) and the following text will be used to identify the language. The line is removed and no numbers are used:

>

>    :::python

>

>If you use none of these systems the codehilite plugin will attempt to guess the language, but it might not get it right (resulting in some inconsistent code highlighting).

>




#Method

If you haven't already, install `python-markdown`. You need this to mark up your code, but this is not a tutorial for python-markdown use. 



Download and install [pygments](http://pygments.org/).



Add both to `INSTALLED_APPS` in your `settings.py` file in Django.



    :::python

    INSTALLED_APPS = (

    ...

        'django.contrib.comments',

        'mptt',

        'comments',

    ...

    )





In your template file you can use markdown by including the **markup** tags :



    {% load markup %}

    {{ object.content|markdown }}







Markdown supports extensions, which you can supply to the template tag filter. Django-markdown already comes with support for pygments included, as long as pygments is installed. So you can activate it using:



    {{ object.content|markdown:"codehilite" }}



This will mark up the code as it's output - but it won't look any different! To make that happen, you'll need to include a CSS file describing the style you want to apply.



For reasons best left to the imagination, pygments supplies the hilighting styles as  [Python formatted files](http://pygments.org/docs/styles/)  rather than CSS. In order to use them on your site therefore you need to convert them which you can do with the [pygmentize](http://pygments.org/docs/cmdline/) command:



    pygmentize -S default -f html > default.css



Alternatively, you could save yourself a lot of bother and use the set available here:



    https://github.com/richleland/pygments-css



Simply download the style you want (we're using [colorful](https://github.com/richleland/pygments-css/blob/master/colorful.css)) and include it on your page. You should now have beautifully syntax highlighted code.







>This method is based, with permission, on an original protocol available [here](http://freewisdom.org/projects/python-markdown/CodeHilite).

