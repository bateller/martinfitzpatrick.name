Date: 2014-04-14 20:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: mplstyler: A simple API to keep line and marker styles consistent throughout plots
Slug: mplstyler-matplotlib-line-and-marker-styler
Tags: matplotlib,software,bioinformatics,python

I've just released a simple API for managing matplotlib line and marker styles for plots. It's called **mplstyler** and you can get it from [Github][mplstyler-github] or [PyPi][mplstyler-pypi].

    :::python

    from mplstyler import StylesManager
    
    styles = StylesManager()
    :::python

    from pylab import *
    :::python

    x = linspace(0, 5, 10)
    y1 = x ** 2
    y2 = x ** 3
    :::python

    figure()
    
    s = styles.get_style_for_class('Series 1')
    plot(x, y1, **s.kwargs)
    
    s = styles.get_style_for_class('Series 2')
    plot(x, y2, **s.kwargs)
    
    show()


![Image 2](https://raw.githubusercontent.com/mfitzp/mplstyler/master/output_3_0.png)

    :::python

    figure()

    from collections import OrderedDict

    l = OrderedDict()
    s = styles.get_style_for_class('Series 1')
    l['Series 1'] = bar(x, y1, **s.bar_kwargs)
    
    s = styles.get_style_for_class('Series 3')
    l['Series 3'] = bar(max(x)+x, y2, **s.bar_kwargs)
    
    leg = legend(l.values(), l.keys(),
       loc='best') 
    leg.get_frame().set_facecolor('k')                      
    leg.get_frame().set_alpha(0.05)     
    
    
    show()


![Image 2](https://raw.githubusercontent.com/mfitzp/mplstyler/master/output_4_0.png)

Notice that Series 1 has again been displayed using the same colour, since the classname ('Series 1')
is unchanged. However, Series 3 is assigned a new colour as it doesn't match any of the previous classes.

[mplstyler-github]: https://github.com/mfitzp/mplstyler
[mplstyler-pypi]: https://pypi.python.org/pypi/mplstyler

