Date: 2012-01-21 09:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Installing Google Earth on Ubuntu
Slug: methods/1527/installing-google-earth-on-ubuntu
Tags: linux,ubuntu,google-earth,google,computing

Install the latest version of Google Earth for linux direct from Google sources.


![method/1527/GoogleEarth.jpg](/static/images/method/1527/GoogleEarth.jpg)








Open a terminal window to perform the installation (`Ctrl-Alt-T`) then enter the following at the prompt:

    :::bash
    wget http://dl.google.com/dl/earth/client/current/google-earth-stable_current_i386.deb

You will see a progress bar as the download completes. This is a perfect time for a cup of tea.


>For 64bit architecture use:
>
>    :::bash
>    wget http://dl.google.com/dl/earth/client/current/google-earth-stable_current_amd64.deb
>
>And change the filename in the subsequent commands.


Next install the downloaded `.deb` package:

    :::bash
    sudo dpkg -i google-earth-stable_current_i386.deb



>If you get errors with this command due to missing dependencies you can 'force' install of Google Earth and missing dependencies with `sudo apt-get install -f`
>


You should now have a fully functional Google Earth!





