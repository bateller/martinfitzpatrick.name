Date: 2014-06-27 17:05
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: PyQt5 support in Matplotlib
Slug: pyqt5-support-in-matplotlib
Tags: python,qt,pyside,matplotlib

My [pull-request](https://github.com/matplotlib/matplotlib/pull/3072) for [matplotlib]() to add PyQt5 support has been accepted and merged, meaning PyQt5 support will be available in the upcoming v1.4.0 release of matplotlib.

<!-- PELICAN_END_SUMMARY -->

Based off original work by [@badders](https://github.com/badders) this re-implements the Qt backend structure as Qt5-first, with Qt4 wrappers for compatibility. It's hoped that this will simplify things going forward, keeping the latest API cleanest with minimal code-cruft.

Thanks to the matplotlib team for the support in getting the PR up to scratch.

[matplotlib]: http://matplotlib.org/


