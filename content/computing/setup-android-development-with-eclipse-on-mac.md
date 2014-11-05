Date: 2011-09-22 09:09
Author: Cael Kay-Jackson
Email: caelkayjackson@googlemail.com
Title: Setup Android Development with Eclipse on Mac
Slug: setup-android-development-with-eclipse-on-mac
Tags: osx-lion,android,mac,mobile,computing

Install and setup the tools necessary for Android development with Eclipse on Mac OS X (Lion)

<!-- PELICAN_END_SUMMARY -->

![method/1470/AndroidStuff.jpg](/images/method/1470/AndroidStuff.jpg)




#Requirements
Mac running Mac OS X (Lion) (Intel)

#Method

Download Eclipse Classic for Mac from the [Eclipse download page](http://www.eclipse.org/downloads/ "Eclipse download page").


>Eclipse Classic is recommended but those who know they need a different version can download that instead.


Extract the .tar.gz file by, for example, locating it in Finder and double clicking on it.



Drag the `eclipse` folder that was created to the `Applications` folder.



Download the Android SDK for Mac from the [Android SDK download page](http://developer.android.com/sdk/index.html "Android SDK download page").





Extract the .zip file and move the created `android-sdk-macosx` directory to somewhere you wish to keep it on your system (for example, `~/android-sdk-macosx`).



Include the Android tools in your path by adding the following to your `~/.bashrc` file, replacing `{user}` with your username or otherwise modifying the path to match where the SDK folder was moved.



`export PATH=$PATH:/Users/{user}/android-sdk-macosx/tools:/Users/{user}/android-sdk-macosx/platform-tools`



Run Eclipse and go to the *Help* menu and *Install new software...*



Click the *Add...* button at the top right of the *Install* dialog, enter the following details and then click *OK*.



Name: `ADT Plugin`  

Location: `https://dl-ssl.google.com/android/eclipse/`





Ensure the *ADT Plugin* is listed in the *Work with* drop-down and once the software list has been updated check the box next to *Developer Tools*. Click through, agree to the licenses as applicable and allow the items to install.



Restart Eclipse and you are ready to produce your Android apps.







