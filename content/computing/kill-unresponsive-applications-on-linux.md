Date: 2012-01-24 11:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Kill unresponsive applications on Linux
Slug: methods/1530/kill-unresponsive-applications-on-linux
Tags: linux,desktop,x11,xkill,computing

Sometimes things go a bit wrong. Sometimes they go very wrong. XKill is a simple little application that allows you to kill a running X application that has got out of kilter. Think of this as a quick way to get back control of your Desktop.





#Requirements
xkill (installed by default on most distributions)

#Method

When a program you are running has hung hit Alt + F2 to bring up the Run dialog.  Enter `xkill` an press enter.


>Alternatively if you have a terminal window already open you can use that to run `xkill` too.


Depending on your theme/desktop setup you will now see either an X symbol or a skull and crossbones. Simply hover the mouse of the application that is being naughty and left-click with the mouse. The application should immediately disappear. 


>If you find you've run `xkill` by mistake you can right-click to cancel. If the application that has hung is not in the foreground you can use `Alt+Tab` to cycle applications even while `xkill` is running.




