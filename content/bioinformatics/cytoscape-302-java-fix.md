Date: 2013-06-06 10:45
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Cytoscape v3.0.2 on Mac OS X
Tags: cytoscape,bioinformatics

[Cytoscape 3.0.2](http://cytoscape.org/releasenotes.html) was released on 1st August, a bugfix release for the 3.x series. However, there is a compatibility issue with the latest Java update from Apple resulting in Cytoscape hanging on startup.

I had followed the advice found elsewhere to update to the latest Java version with no success, until I found [this post](https://groups.google.com/d/msg/cytoscape-discuss/3iCDXQ4lOTM/arovMUx0_DAJ) from Tim Hull, outlining a simple way to check what version you have installed.

  /usr/libexec/java_home -v 1.6 -exec java -version

> If the output contains “xM4508”, you have the broken
> version. If it contains "xM4509", this is probably a
> different issue...

If you find that you have the bad version, you can download the updated from Apple using the links below:

* [Java Update for OS X 10.7, 10.8+](http://support.apple.com/kb/DL1572)
* [Java Update for OS X 10.6-only](http://support.apple.com/kb/DL1573)