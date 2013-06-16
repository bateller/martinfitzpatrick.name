Date: 2013-04-18 09:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: cx_Freeze and PySide on Mac
Slug: cx-freeze-and-pyside-on-mac
Tags: python,mac,py2app,cx_freeze

I'd had success using py2app for building Mac binaries for distribution but wanted to give cx_Freeze a go since it's cross platform - allowing builds for Windows, Linux, and more. Unfortunately, attempting to build using cx_Freeze was resulting in errors:

    libpyside-python2.7.1.1.dylib: No such file or directory
    
If found a tip suggesting you can do a `touch libpyside-python2.7.1.1.dylib` in you're applications folder to get rid of this error by creating a dummy file. But then you just end up with this instead:

    copying Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/               PyQt4/Qt.so -> build/exe.macosx-10.6-intel-2.7/PyQt4.Qt.so
    copying /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PyQt4/QtCore.so -> build/exe.macosx-10.6-intel-2.7/PyQt4.QtCore.so
    copying QtCore.framework/Versions/4/QtCore -> build/exe.macosx-10.6-intel-2.7/QtCore error: QtCore.framework/Versions/4/QtCore: No such file or directory
    
It's looking for the file in the wrong place: QtCore should be prefixed with the same path as PyQt4 before it. There are various version of PySide available - but whether you try to `pip install` or `git clone https://github.com/PySide/pyside-setup` and then `python setup.py install` you'll find that you end up in much the same place. In most cases however the installation simply fails.

# Homebrew

So try a different tack: [Homebrew][homebrew]. Homebrew is a package manager for Mac, that has a large number of successfully buildable software packaged specifically for the Mac. I've successfully used it to install a number of things, but steered clear of it for Python things that could be pip installed. However, there seemed to be little alternative - and actually I think brewed Python has it's advantages (being more up to date being one, being guaranteed to work with other brewed packages the other).

At this point my default Python install was the Mac default (Darwin, llvm-compat) version, installed under `/Library/Python/2.7/` so first that needed to change.

# Python

    brew install python

The above will take quite a long time (particularly the Python bit) but you should now have a successfully brewed Python on which to base your apps. If you've had a different Python (e.g. system python) installed you may need to update your paths to ensure that the brewed one is being used - Homebrew actually gives you the instructions to correctly do this: but just add `/usr/local/lib/python2.7/site-packages:/usr/local/share/python` to your `PATH` variable in `.bash_profile` e.g.

    export PATH=/usr/local/lib/python2.7/site-packages:/usr/local/share/python:$PATH

# Pyside

An important fact about brewed Python is that it will continue to look in your system site-packages folder, and do so in preference to your brewed site-packages. If you have attempted to install Pyside (or anything else) before you may wish to remove them to stop conflicts.

Next install PySide via brew (the pip install does not work).

    brew install pyside

The install cx_Freeze via pip (it's not in brew, and the pip works fine).

    pip install cx_Freeze

Finally, check PySide are cx_Freeze are set up correctly by starting a Python interactive shell and entering the following (you should get the same output):

    >>> import PySide
    >>> import cx_Freeze
    >>> PySide.__version__
    '1.1.2'
    >>> cx_Freeze.version
    '4.3.1'
   
You're now free to build your apps.


[homebrew]: http://mxcl.github.io/homebrew/

