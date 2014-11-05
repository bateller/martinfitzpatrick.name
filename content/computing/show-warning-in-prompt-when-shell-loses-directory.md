Date: 2011-09-28 01:09
Author: Cael Kay-Jackson
Email: caelkayjackson@googlemail.com
Title: Show Warning in Prompt when Shell Loses Directory
Slug: show-warning-in-prompt-when-shell-loses-directory
Tags: mac,terminal,prompt,bash,pwd,cli,computing

Show a warning in the Terminal's prompt when the current working directory is no longer where the shell expects it to be. (e.g. it was deleted or replaced by a new, different directory with the same name by some other app).

<!-- PELICAN_END_SUMMARY -->

![method/1471/TerminalPWDChecks.png](/images/method/1471/TerminalPWDChecks.png)



>Why is this useful? Take the scenario where you receive frequent updates to a file foo.zip which you proceed to extract as ~/foo/ and work within foo in Terminal for whatever reason; say copying some of the files somewhere.

>

>You receive another update to foo.zip. You delete the original ~/foo/ directory and unzip the new foo.zip in its place. The Terminal, however, is still referencing the old foo directory which is now in the trash. Any commands issued will be operating on the old files, not the new ones.

>

>This method will throw up a warning in this case.

>

>(With thanks to Andy Block for the original inspiration.)


#Requirements
Mac OS X (Lion)

Bash shell in Terminal

#Method

Open the Terminal app and if the file `~/.bash_profile` does not exist, create it with the following command.



`touch ~/.bash_profile`



Open `.bash_profile` in your favorite editor and at the bottom add the following content.



    # Warn when shell isn't referring to the directory it thinks it is.  

    inode() {  

        ls -lid $1 | awk '{print $1;}'  

    }  

    check_pwd() {  

        if [ ! -d $PWD ]; then       # PWD doesn't exist.  

            echo ' [PWD does not exist!]'  

        elif [ "`inode .`" != "`inode $PWD/`" ]; then   # PWD is not where the shell thinks it is.  

            echo ' [PWD has outmaneuvered the shell!]'  

        fi  

    }  

    export PS1="\u@\h \W\[\033[31m\]\$(check_pwd)\[\033[00m\] $ "




>This snippet simply compares the inodes of the current directory (via `.`) and that of the output of `pwd`.

>

>Depending on previous configuration changes you may have made to your system, you may already have a `PS1` variable being exported. In this case you will need to add `\$(check_pwd)` somewhere in the existing value. (The `\[\033[00m\]` parts are just for colors.)


Add the new commands to the current terminal's environment.



`source ~/.bash_profile`





Now to test this. Still in the Terminal, enter the following commands to create a test directory.



`mkdir ~/foo`  

`cd ~/foo`



Leaving the Terminal open with the working directory as `~/foo`, open Finder and find and delete the `foo` folder.



Return to the Terminal app and press enter (just enter; no command is necessary). The prompt will display a warning in red that the directory doesn't exist.



Go back to Finder and recreate the `foo` folder.



Switch back to the Terminal and again press enter. The prompt will display a different warning in red indicating that the working directory isn't what the shell thinks it is.







