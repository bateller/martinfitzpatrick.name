Date: 2012-01-24 10:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Change the &#39;Desktop&#39; directory on Linux
Slug: change-the-desktop-directory-on-linux
Tags: linux,desktop,computing
Ads: bottom

On desktop setups where icons are shown on the desktop these are normally taken from the specific folder ~/Desktop. If you find you want to show icons from either your Home or another directory for a particular install/user you can do so by editing the user-dirs config file as described here.









Open your text editor and browse to `~/.config`


>`~` here refers to your home directory and `.config` is a hidden file (starts with a `.`). If you use the open dialog of most text editors you should be able to paste the path in directly to get to the correct folder.


Look for file named `user-dirs.dirs` and open it for editing.



The file should contain a line that looks like the following (or perhaps another folder depending on your setup.



   XDG_DESKTOP_DIR="$HOME/Desktop/"



Simply change that line to point to the folder you wish to use for your desktop. For example:



    XDG_DESKTOP_DIR="$HOME/"

    XDG_DESKTOP_DIR="/var/log/"

    XDG_DESKTOP_DIR="$HOME/../shared/Desktop"






>You can also change other folders in this file including your `Documents` folder for example.






