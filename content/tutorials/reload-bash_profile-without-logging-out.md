Date: 2011-11-29 08:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Reload .bash_profile without logging in again
Slug: reload-bash_profile-without-logging-out
Tags: cli,unix,linux,computing
Ads: bottom

Update your session to new settings in .bash_profile without logging out and back in again.

<!-- PELICAN_END_SUMMARY -->

At the prompt enter: 



`source ~/.bash_profile`



add the following line to your .bash_profile or .bash_aliases file

`alias reload='source $HOME/.bash_profile'`

after running `source ~/.bash_profile` the command `reload` will be available to do the same thing :)











