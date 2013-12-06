Date: 2011-11-29 08:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Install Cinnamon on Ubuntu 12.04
Slug: install-cinnamon-on-ubuntu-1204
Tags: linux,desktop-environment,linux-mint,ubuntu,computing

Cinnamon is a re-implementation of the Gnome 2 desktop in GTK3 developed by the Linux Mint project as an alternative to both Gnome3/Shell and Ubuntu Unity. Here we explain how to install Cinnamon on top of your Ubuntu installation, without installing Linux Mint.


![method/1517/cinnamon1.2.0-2.jpg](/images/method/1517/cinnamon1.2.0-2.jpg)








As with all Ubuntu unsupported software you cannot install cinnamon through the Ubuntu Software Centre. However there is a launchpad-hosted PPA for Cinnamon available at [ppa:gwendal-lebihan-dev/cinnamon-stable](https://launchpad.net/~gwendal-lebihan-dev/+archive/cinnamon-stable "")



Open a terminal and at the command line enter:

`sudo add-apt-repository ppa:gwendal-lebihan-dev/cinnamon-stable`

You will be prompted for your password to add the repository.



`sudo apt-get update`

Your software listings will now update (this is required to let apt know about the software in the new repository you just added). 



`sudo apt-get install cinnamon`

Cinnamon will now install. You will be asked to confirm the addition of a number of extra packages including `caribou gir1.2-muffin-3.0 libmuffin0 muffin-common`



Once installation is complete close the terminal and log out of your session.




At the login screen select your desktop from the drop down list above your name. Choose Cinnamon and click login. You will now find yourself at the Cinnamon desktop!

![step/7491/Screenshot from 2012-05-31 20:36:43.png](/images/step/7491/Screenshot%20from%202012-05-31%2020%3A36%3A43.png)







