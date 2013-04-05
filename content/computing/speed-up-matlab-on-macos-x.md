Date: 2013-03-24 12:03
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Speed up MATLAB on MacOS X
Slug: methods/1539/speed-up-matlab-on-macos-x
Tags: mac,osx,computing,matlab

On MacOS X 10.5 there is considerable slow-down in the MATLAB editor and other GUI elements. The issue is related to a change in the default Mac Java 2D rendering engine from Quartz2D (10.4) and Sun2D (10.5). This newer rendering engine improves performance for figure drawing, but other GUI operations are slower. 

The temporary fix is to instruct MATLAB to use the old rendering engine (Quartz2D). This will speed up scrolling and most GUI operations, at the cost of reduced figure drawing speed. 


![method/1539/Screen Shot 2013-03-24 at 12.20.16.png](/static/images/method/1539/Screen%20Shot%202013-03-24%20at%2012.20.16.png)








Open a terminal and browse to to your Matlab app bundle, eg.

    cd /Applications/MATLAB_R2011a_Student.app




>Your MATLAB folder will likely be different to this. A quick way to find it is to use the `tab` key. At the command-line enter `cd /Applications/MATLAB` then hit `<tab>` and the name should autocomplete.




If you're on 2008a or later, you need to browse down to the maci folder. 

    cd bin/maci

or for 64 bit

    cd bin/maci64




>Again, typing `cd bin/maci<tab>` should get you there.


At the command line type `nano java.opts` to create a new empty file and open a command-line text editor. You can copy and paste into this window, so simply copy the text below and paste it onto a new line in the file.

    -Dapple.awt.graphics.UseQuartz=true

To save hit `Ctrl-X`(exit) then press `Y` to save and `Return` to accept the filename





>You can also optionally add `-Dapple.laf.useScreenMenuBar=false` to turn off the Mac top-of-screen menu bar. This appears to also slightly increase speed.



Restart MATLAB and you should see a speed improvement.


>As this fix may reduce drawing speed of figures, you may want to switch off the workaround while doing a lot of figure drawing. You can do so by exiting MATLAB, renaming the java.opts file e.g. to java.opts.off with `mv java.opts java.opts.off` and restarting MATLAB. To re-enable simply quit, rename the file back to java.opts with `mv java.opts.off java.opts` and restart.




