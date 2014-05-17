Date: 2011-10-21 05:10
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Install HomeBrew package manager for Mac
Slug: install-homebrew-package-manager-for-mac
Tags: mac,ports,computing
Picture: /images/method/1490/Screen%20Shot%202012-04-21%20at%2017.37.33.png

Homebrew is the easiest and most flexible way to install the UNIX tools Apple didn't include with OS X. It provides a simpler alternative to MacPorts, installing under an isolated non-root prefix, symlinked to `/usr/local`

<!-- PELICAN_END_SUMMARY -->

![method/1490/Screen Shot 2012-04-21 at 17.37.33.png](/images/method/1490/Screen%20Shot%202012-04-21%20at%2017.37.33.png)


>You do not need to use `sudo` when using Homebrew as software is installed to a non-root prefix. 


#Requirements
An Intel CPU

OS X 10.5 or higher

Command Line Tools for Xcode or Xcode with X11

Java Developer Update

#Method

Open up Terminal.app to get a shell prompt.



Copy & paste the following line at the prompt:

`/usr/bin/ruby -e "$(/usr/bin/curl -fksSL https://raw.github.com/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"`


>No need to use `sudo`!


Once installed you can install any software you like as follows:



`$ brew install wget`







>This method is based, with permission, on an original protocol available [here](http://mxcl.github.com/homebrew/).

