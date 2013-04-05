Date: 2011-11-29 09:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Get a list of all processes not run by you
Slug: methods/1518/get-a-list-of-all-processes-not-run-by-you
Tags: linux,processes,user,cpu,computing

Find the currently running processes on your system that were not started by yourself. A great way to find out what is hogging your system on multiple-user setups or remote logins.









Open up a terminal session and enter:

	ps aux | grep -v `whoami`



>`ps aux` returns (a) all processes with (u) user shown, (x) listing only those without controlling ttys. We then pass this through `grep` checking for the existance of your username retrieved with `whoami`


You can tweak this to show (for example) the only the top 10 processes by cpu utilisation as follows:

	ps aux  --sort=-%cpu | grep -m 11 -v `whoami`





>`grep -m 11` stops searching after 11 matches (10th line) while `ps --sort=-%cpu` sorts on the cpu utilisation column (-) descending.




