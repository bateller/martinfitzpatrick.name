Date: 2012-02-05 03:02
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Install Haiku under Mac OS X with Virtualbox
Slug: install-haiku-under-mac-os-x-with-virtualbox
Tags: haiku,beos,macosx,virtualbox,computing

Haiku is an open source operating system currently in development that specifically targets personal computing. Inspired by the Be Operating System, development began in 2001, and the operating system became self-hosting in 2008 with the first alpha release in September 2009, the second in May 2010 and the third in June 2011. Here we describe how to run a Virtualbox hosted Haiku OS on Mac OS X.


![method/1535/Haiku.png](/static/images/method/1535/Haiku.png)



>This has been tested on Mac OS X 10.8 (Mountain Lion) MacBook Air. You might need to tweak some settings on other hardware/OS versions. 




#Method

To run Haiku on top of Mac OS X first download and install [Virtualbox](https://www.virtualbox.org/wiki/Downloads).

![step/None/Screen Shot 2012-08-05 at 14.31.31.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2014.31.31.png)



Download the version of Virtualbox for Mac OS X and open up the .dmg. Double-click on `Virtualbox.mpkg` to start the installation.

![step/None/Screen Shot 2012-08-05 at 14.34.10.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2014.34.10.png)



While Virtualbox is installing download a copy of Haiku. The simplest way to get Haiku running in Virtualbox is to [download the pre-built VM image](https://www.haiku-os.org/get-haiku). Download the .zip file and double-click to unpack to a folder. Put this somewhere safe: this will hold your Haiku install.

![step/None/Screen Shot 2012-08-05 at 14.33.15.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2014.33.15.png)



Start up Virtualbox and click to create a new virtual machine. There is a short wizard to set this up. Set the operating system to Other and version to Other/Unknown.

![step/None/Screen Shot 2012-08-05 at 14.36.07.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2014.36.07.png)



Set the memory according to your host computer but 512MB should be enough for a comfortable Haiku install.

![step/None/Screen Shot 2012-08-05 at 15.21.13.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2015.21.13.png)



On the Virtual Hard Disk ensure that Start-up disk is checked and select "Use existing hard disk". Click the folder icon to the right on the drop down and browse to the location on your downloaded and unpacked Haiku folder.  Select the file named `haiku-r1alpha3.vmdk` (or similar on later releases).

![step/None/Screen Shot 2012-08-05 at 15.21.21.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2015.21.21.png)



The default settings of Virtualbox work perfectly fine. However, Haiku occasionally locks up on the boot loader screen. A simple fix is to enable dual processor support. To do this right click on the created virtual machine and choose settings. Navigate to System -> Processor and increase the processor(s) to `2`. Click OK to save the configuration.

![step/None/Screen Shot 2012-08-05 at 15.27.47.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2015.27.47.png)



In order to make networking work from within Haiku you will also need to change the virtualised networking card to any of the Intel ones. In settings navigate to Network -> Adapter 1 -> Advanced (hidden drop down section) and change the adapter type for example to `Intel PRO/1000 MT Desktop`. 


![step/None/Screen Shot 2012-08-05 at 15.46.09.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2015.46.09.png)


>You can leave the attached to setting as NAT or alternatively bind it to a specific adapter in your host computer by choosing Bridged Adapter and then (for example) wlan0 for Wi-Fi/Airport.


Double click the virtual machine to start Haiku!

![step/None/Screen Shot 2012-08-05 at 14.37.53.png](/static/images/step/None/Screen%20Shot%202012-08-05%20at%2014.37.53.png)


>Your mouse and keyboard will be captured by Virtualbox/Haiku if you click in the window. To get it back for use in Mac OS X press the `Command` (`Cmd`) key.






