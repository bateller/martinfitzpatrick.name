Date: 2011-11-08 08:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Set CDPATH to ease folder navigation
Slug: set-cdpath-to-ease-folder-navigation
Tags: bash,cli,path,cdpath,sh,computing

CDPATH is an environment variable which tells the `cd` command where to look for the specified folder. By including the parent folders of commonly used locations you can access folders more easily - and without typing an entire path.









Open up your shell profile file `.bashrc` (Linux) or `.bash_profile` (Mac).



Somewhere near the bottom of the file add a line to set the CDPATH environment variable:

`CDPATH=:..:~:~/data:~/projects`

In order left to right this tells `cd` to look in:

1. The current directory (blank; before the first `:`)
2. The parent directory `..`
3. Your home directory `~`
4. Your projects directory in your home `~/projects`



>You can add as many folders to search as you like and these will be checked in order from left to right.


Restart your shell (close and reopen or enter `restart`) and then try to `cd` to folders in your home directory from anywhere on your filesystem with `cd <foldername>` and no path.







