Date: 2011-11-28 10:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Piping between shells
Slug: methods/1513/piping-between-shells
Tags: mac,unix,linux,pipe,computing

Create your own bash pipes to send program output between shells, processes and users.

You may already be familiar with the | command commonly used to send the output of one command into another, e.g. `cat /var/log/messages | less`. Here we create user-defined pipes to carry output between shells or users.




>You will need to set appropriate permissions on the pipe file to share data between users. Try `chmod 644 fifo_pipe`.




#Method

First create the pipe through which you'll send the data using the `mkfifo` command. This refers to the type of buffer you are creating: 'first in first out' i.e. a pipe.

`mkfifo ~/fifo_pipe`




Open up a new shell - either open a new terminal window or start a new session.  Keep your previous one running so you can send the data from there. In the new window enter:

`tail -f ~/fifo_pipe`

This runs `tail` (which outputs the end of the buffer) with the `-f` option to 'follow' output - that is continue outputting what it finds in the fifo pipe.



Return to the original shell session and now enter:

`ls >> ~/fifo_pipe`

Running this will perform a directory listing of the current directory, outputting the result into the `fifo_pipe` we previously created. Now switch back to your second session and see the output of `ls`! 


>You can send any data output from one process through a pipe in this way. Got a neat use for this trick? Post it!




