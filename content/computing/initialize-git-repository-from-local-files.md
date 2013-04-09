Date: 2011-09-20 03:09
Author: Cael Kay-Jackson
Email: caelkayjackson@googlemail.com
Title: Initialize Git Repository from Local Files
Slug: initialize-git-repository-from-local-files
Tags: git,version-control,computing

Initialize a Git repository from a local directory, and the files therein, pushing it to an existing but empty remote.


![method/1468/GitStuff_1.png](/static/images/method/1468/GitStuff_1.png)



>Assumes that the remote bare repository has been created.


#Requirements
Git
An empty bare remote repository

#Method

Open a terminal/console (Terminal on Mac/Linux, cmd.exe on Windows) and cd to the directory that will be added to Git.



Initialize the directory as an empty Git repository using the following command:

`git init`



Add the contents of the directory to the repo:

`git stage .`

`git commit -m "Initial commit."`


>Alternatively add only some of the files by staging only those of interest and perhaps '.gitignore'ing the rest.


Add the remote, replacing {remote} with the URI for the remote repository (for example, ssh://git.example.com/myrepo.git):

`git remote add origin {remote}`



Push the commit to the remote:

`git push -u origin master`



>-u adds a tracking reference for the branch which is useful for argument-less pull commands amongst others.
>






