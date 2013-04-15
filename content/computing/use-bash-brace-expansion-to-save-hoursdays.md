Date: 2011-12-05 04:12
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Use bash brace expansion to save {hours,days}
Slug: use-bash-brace-expansion-to-save-hoursdays
Tags: bash,cli,linux,computing

Brace expansion is one of the most powerful bash tricks with the potential to save you considerable time. Here are some common use cases.




>Be careful with the use of spaces as these will stop expansion working. If you have any text containing spaces, wrap it in quotes. However, the expansion won't work inside quotes either, for example:
>
>Will not work:
>
>	echo Use bash brace expansion to save {hours,days}
>	echo "Use bash brace expansion to save {hours,days}"
>
>Works!:
>
>	echo "Use bash brace expansion to save "{hours,days}
>	echo "Use bash brace expansion to save"{" hours"," days"}
>
>In the second example, note that the space has been moved inside the expansion set, so each of them must be wrapped in quotes.




#Method

Bash brace expansion takes a list of arguments and expands them into separate arguments to the command. 

	$ echo hello{1,2,3}
	hello1 hello2 hello3


>Braces can also be nested for more complex combinations.


Brace expansion is extremely useful for the creation of backup files.

	$ cp ~/.bash_profile{,.bak}

You will now have your bash_profile file backed up in `~/.bash_profile.bak`




>Note the `,` at the beginning of the brace expansion - indicating an empty field. In the first instance this brace expansion will expand to the command with nothing after it (i.e. the original file), then secondly adding the `.bak` to create the backup.


You can do this in reverse to copy the file back

	$ cp ~/.bash_profile{.bak,}

Or check for file changes from backup with diff

	$ echo Hello! >> ~/.bash_profile.bak
	$ diff ~/.bash_profile{.bak,}
	23d22
	< Hello!




Brace expansion also supports number ranges which can be useful for when you need to create a lot of sequentially ordered objects. For example

	$ mkdir tmp{1..100}

Will produce a number of folders named tmp1, tmp2, tmp3, tmp4, etc.. in the current directory.







