Date: 2013-11-29 16:27
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Multithreading with PyQt 
Tags: multithreading,threading,pyqt,python,qt
Status: draft

In the process of generating final builds of MetaPath for v1.0 release, one of the outstanding issues was the frequent loss of interactivity when analysing large datasets. This manifested most severely when requesting data from remote services (e.g. MetaboHunter), but also applied equally to large dataset transformation, reshaping, and filtering operations.

Qt applications (and PyQt) normally operate a single event-processing thread. Events, such as UI interactions, trigger code attached to these events (e.g. processing) which continue until complete. Because a Qt application is by default single threaded, all of this processing is *blocking*. That means, while your downstream code is running no further events (UI or otherwse) can be processed and, from a user's point of view, your application is frozen.

There is a rough and ready solution to this problem.

`QApplication.processEvents()`.


