Date: 2011-11-29 07:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Find all running processes of a program
Slug: methods/1514/find-all-running-processes-of-a-program
Tags: bash,cli,command-line,computing

Find the pids of all instances/processes of a given program running on your system









Open a terminal and enter `ps ax | grep "firefox"` ...replacing 'firefox' with the name of the program you are looking for.


>The columns in the output are as follows: (1) pid 'process id' (2) tty (3) process state - see `man ps` (4) process runtime (5) process command.




