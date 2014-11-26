Date: 2012-03-10 09:03
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Customize directory colors
Slug: customize-directory-colors
Tags: bash,cli,bashrc,colors,computing
Ads: top,bottom

You can use the command ls --color (or an alias) to show directories with colours for folders, files, links, etc. However, you may not realise these colours can be easily configured using bashrc and a configuration file.

#Requirements
bash

#Method

Edit your `.bashrc` file (in your home directory) to include the following line:

    alias lc="ls --color=always"

This will enable coloured listings on all uses of ls (to save you typing `--colors`. Save the file and in your terminal window enter `source ~/.bashrc` to reload your bash config. Try an `ls` to confirm that you have got colors working.


>On some systems (including Mac) the bash configuration is stored in `~/.bash_profile` instead.

You have a lot of options for configuring the directory colours. They can be stored in


1. Shell variable `LS_COLORS` which can be set in .bashrc via `export LS_COLORS="COLOR_CONFIG"`

1. In the file `/etc/DIR_COLORS` (you will need to be root to configure and this is global for all users)

1. In the file pointed by the variable `COLORS` (can be in your home directory)





Color configuration is done through a special formatted string:



    FILE-TYPE Attribute codes: Text color codes:Background color codes



    FILE-TYPE: is file type like DIR (for directories)

    Attribute codes:

        00=none

        01=bold

        04=underscore

        05=blink

        07=reverse

        08=concealed

    Text color codes:

        30=black

        31=red

        32=green

        33=yellow

        34=blue

        35=magenta

        36=cyan

        37=white

    Background color codes:

        40=black

        41=red

        42=green

        43=yellow

        44=blue

        45=magenta

        46=cyan

        47=white



For example `DIR 01;34` gives you a bold blue directory.



So to change the configuration globally edit the `/etc/DIR_COLORS` file as follows:



    sudo nano /etc/DIR_COLORS



Look for:



    DIR 01;34 # default is Bold blue with black background



And change it to:



    DIR 01;34;41 # NEW default is Bold blue with RED background





Using LS_COLORS (in your own `.bashrc` file) the format is slightly different:



    LS_COLORS='di=1:fi=0:ln=31:pi=5:so=5:bd=5:cd=5:or=31:mi=0:ex=35:*.rpm=90'



Here the codes are as follows:



    di = directory

    fi = file

    ln = symbolic link

    pi = fifo file

    so = socket file

    bd = block (buffered) special file

    cd = character (unbuffered) special file

    or = symbolic link pointing to a non-existent file (orphan)

    mi = non-existent file pointed to by a symbolic link (visible when you type ls -l)

    ex = file which is executable (ie. has 'x' set in permissions).

    

    0   = default colour

    1   = bold

    4   = underlined

    5   = flashing text

    7   = reverse field

    31  = red

    32  = green

    33  = orange

    34  = blue

    35  = purple

    36  = cyan

    37  = grey

    40  = black background

    41  = red background

    42  = green background

    43  = orange background

    44  = blue background

    45  = purple background

    46  = cyan background

    47  = grey background

    90  = dark grey

    91  = light red

    92  = light green

    93  = yellow

    94  = light blue

    95  = light purple

    96  = turquoise

    100 = dark grey background

    101 = light red background

    102 = light green background

    103 = yellow background

    104 = light blue background

    105 = light purple background

    106 = turquoise background







