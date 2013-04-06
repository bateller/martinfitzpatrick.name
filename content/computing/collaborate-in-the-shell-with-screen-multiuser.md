Date: 2012-01-22 12:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Collaborate in the shell with screen (multiuser)
Slug: collaborate-in-the-shell-with-screen-multiuser
Tags: mac,bash,cli,screen,linux,computing

Screen is a neat little program that allows you to use multiple virtual terminals in a single session on Unix/Linux and Mac. However, it does more than just that. It can also allow you to share your current session on a machine with another user - allowing you to collaboratively hack away at a problem in real time. 




>Issue commands to screen using `Ctrl-A` followed by one of the command instructions, or a further key combination.
>
>While you can use this method to connect as many people to a given screen session as you like, only one person can be typing in a given window at once. That person is described as having the 'writelock' on the window. By default these are set to 'auto', meaning the first user to start typing gets the writelock and keeps it until they leave the window.
>
>A user's writelock can be removed manually by using the command `writelock off`. In contrast the command `writelock on` means that user will keep the writelock even after leaving the window.


#Requirements
screen
Add any additional notes.
tools:	
List of materials needed, one per line.

#Method

Before getting started there is an important permissions setup to perform. In order to share screens between two separate users on a system screen must be set `suid root`. Doing this has a slight security risk (if there are bugs in screen that allow compromise by a logged in user) but is neccessary to ensure that both users have the permissions to see each other's sessions.

To set up the permissions open a terminal and enter:

    :::bash
    sudo chmod +s /usr/bin/screen  # Make screen suid root
    sudo chmod 755 /var/run/screen # Make the screen dir more open


>Note that if you want to share a screen between two sessions of the **same** user on a system you can skip this step entirely. This is useful for example if you have a shared login on a system.


Now that's out of the way we can create the screen session as normal. So first start screen to create a named session - here called `test`

    :::bash
    screen -S test



Once in the screen session we need to tell screen to allow the screen sharing to commence. Commands to screen are performed using `Ctrl-A` key combination followed by a command (or another key combination). So do the following;

    CTRL-A
    :multiuser on

    CTRL-A
    :acladd <username>

Replacing `<username>`  with the name of the user you are granting screen sharing access to.


>You can save yourself some time by putting these commands in the `.screenrc` configuration file.
>
>You can also control permissions more closely for example `:aclchg <username> +rx` will give `<username>` read-only access to the screen.


Finally ask your guest to connect to your server via ssh and enter the following to access your screen:

    :::bash
    screen -x <your-username>/test

The screen follows the general format of `<your-username>/<your-screename>` meaning you can have and share multiple screen sessions at once if you so wish!







