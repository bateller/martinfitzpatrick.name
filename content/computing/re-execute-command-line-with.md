Date: 2011-10-22 04:10
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Re-execute command line with !
Slug: re-execute-command-line-with
Tags: bash,cli,linux,computing
Ads: bottom

Bash history expansion allows you to quickly re-run previous commands using ! and the number of the command in your history.

<!-- PELICAN_END_SUMMARY -->

![method/1492/Screen Shot 2012-04-22 at 16.03.03.png](/images/method/1492/Screen%20Shot%202012-04-22%20at%2016.03.03.png)



>You can adjust the size of the history by setting the HISTSIZE variable in the shell e.g. `export HISTSIZE=1000`. You can clear the current history with `history -c`. 




#Method

Bash keeps a history of all commands executed in the shell and this can be referenced using the `!` command. Typing two !'s at the prompt will execute the previous command:



	$ echo "HELLO"

	HELLO

	$ !!

	echo "HELLO"

	HELLO







The history of the bash shell can be accessed by entering `history`



	501  echo "HELLO"

	502  echo "HELLO"

	503  history



Notice that each entry has an associated number which can be used to refer to the command.



Entering ! followed by a line number from the history will run that command



	$ !501

 	echo "HELLO"

	HELLO







You can also search the history by using a search string to match the command instead of a number



	$ !echo

	echo "HELLO"

	HELLO











>This method is based, with permission, on an original protocol available [here](http://hacktux.com/bash/fast/cli).

