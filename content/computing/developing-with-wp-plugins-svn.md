Date: 2007-03-26 09:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Developing with WP-Plugins SVN
Slug: 2007/03/26/developing-with-wp-plugins-svn
Tags: wordpress,plugins,svn

The new plugin download interface, hooked into [wp-plugins.org][1] adds extra incentive for plugin developers to use SVN.

There are a number of detailed SVN guides available, as well as an entire online book. But for casual plugin developers wanting to get the benefits of using the system most of the information is over detailed or not specific to the [wp-plugins.org system][1]. This tutorial covers adding and updating plugins through the [wp-plugins.org][1] SVN.  


# Creating a New Repository

Before uploading code you need to create the repository for it on the SVN (Subversion) server. Thankfully, this is done for you by the WordPress sytem. To set up a new repository for your plugin simple follow the steps below:

*   On the WordPress » Extend site, click [Add your plugin][2]
*   Enter your details into the fields provided: 
    *   **Name** is the name of your plugin. You will probably want to specify the standardised name here, e.g. im-online rather than IM Online to make sure it matches your main plugin file. It’s not important but it could save some confusion.
    *   **Description** is a *short* outline of what your plugin is and does. 
    *   **Homepage** is the URL of the *plugins* own page on your site. This is option but is useful for admins to check the suitability of the plugin. You can specify a different page or location later if you don’t do it here.
*   Click **Request »**

Once this is done your plugin will be checked by the admins and the repository space will be created on the [wp-plugins.org SVN][1]. An email will be sent to your registered WordPress account email (click “View Your Profile” at the top to check which email you have registered with the system).

# Accessing Your Repository

There are a number of methods available for accessing a Subversion repository from GUI based applications to command line. However, regardless of the software used the processes for interacting with the SVN are the same.

Before you get started you’ll need to get your hands on some software. The wp-plugins Wiki lists recommended [SVN software][3] for Mac OS X and Windows.

For KDE I would personally recommend [KDESVN][4] which is available through Ubuntu’s repositories. It has a bizarre interface but it works effectively and features shell integration. You can also gain read-only access through [KDE’s file system][5].

With the software installed you can now connect to your plugin’s repository the location given in the confirmation email. This follows the standard form:

`<a href="http://svn.wp-plugins.org/plugin-name/" rel="nofollow">http://svn.wp-plugins.org/plugin-name/</a>`

Once connected you should be presented with three folders: branches, tags and trunk.

# SVN Concepts

There are a few basic concepts you need to get your head around to use SVN for plugin development. The different folders `branches`, `tags`, and the `trunk`, along with the development process using `update` and `commit`.

## Repository Folders

**Trunk** is where you do the major development for your plugin. Your trunk repository should contain the latest, greatest, in development code. Your editing takes place here with updates being added to this location regularly.

**Tags** contain snapshots of your code, frozen in time. For this reason you commonly use tags to mark releases – e.g. a tag called `1.1` for that release. Once the tag is created (see later) you can then continue to develop the trunk code knowing a stable, permanent and more importantly *working* is available for download. For this reason it is not a good idea to edit or modify tags once created – to do this create a branch.

**Branches** are effectively tags which continue to be developed. These are useful when you need to develop two or more versions of your code in parallel, for example one version compatible with WordPress v1.x and another for WordPress v2.x You won’t be using these in normal WordPress plugin development so until then you can forget all about them!

## Update & Commit

Update and Commit are the two central processes in version management. Updating, often called “checking out” is the process of updating your local copy to match what is in the repositories. Commit, often called “checking in” is the process of uploading your changes to the repository.

During commit SVN will report changes and conflicts between your local copy and the remote version stored on the SVN server. If you are developing a plugin alone and there are not likely to be contributions uploaded during your update and commit cycle it’s quite possible you’ll never see this happening. If you are developing a larger project, you may want to [read up on version control][6].

This is only a basic introduction to SVN concepts. More information is available in [Version Control with Subversion][7] a free online SVN book from O’Reilly.

# Preparing Files for Upload

Now we know what we’re doing, we’re going to set up our repository. If you’ve been developing your plugin off-line you will have a set of plugin files in a directory on your system. You can upload these files to your SVN as they are, but there are a couple of additional files you will want to add for [GPL compliance][8] and [WordPress plugin download][9] compatibility.

First of all, download a copy of the [the GPL license][10] and save this in the folder with your plugin. You may want to have a read of it first to check that you agree to the terms, but remember than GPL compliance is a requirement for hosting on [wp-plugins SVN][11].

Next, if you want to make use of [the plugin download system][9] you’ll need to add another file, named `readme.txt` to your plugins directory. This file contains information about your plugin to be displayed to visitors. An [example file is available][12], along with a [validator][13] to check before upload.

With these files in place, you’re now ready to upload your files to SVN for the first time.

# First Upload

The first step is to check-out (or “update”) the trunk folder of your repository to the local folder containing the plugin files. This links your local folder to the remote repository. When you do this your SVN software will read the directory and may indicate which files are not currently in the repository (which should be all of them). Using your SVN interface simply add each file (or directory) to the SVN.

Because you currently have the repository checked out, the changes you have made will not be reflected on the remote server. In order to apply the changes, simply `commit` the directory back to the repository – you may also want to add a comment to indicate the changes made. Your files are now in the SVN (and can be downloaded).

# Updating & Developing Code

Revision control with SVN follows the same basic process of checking in/out and making changes to files. In between these steps there are various checks (e.g. `diff`) which you can do to compare changes made by yourself to versions submitted by other people. However, because this article is mainly concerned with solo plugin development we won’t be covering that here. More information about resolving conflicts is available from [the SVN book][14].

## Check Out (Update)

Before developing your plugins you want to check out the current version from your repository. If you are developing your plugin single-handedly on a local installation this may seem like an unnecessary step – and in many ways it is. It is only necessary if you believe that someone else could have updated the files in the repository (e.g. applied a patch) since you last updated the files and you want to take those changes into account.

Note, if you elect not to check out the code you will receive a warning if there are any conflicts when you come to re-upload. At this point you can [resolve them][14] as neccessary.

## Make Changes

Now you can edit your files and fix your plugin as you like – this part of development will be no different to developing software without SVN. Remember, if you’re using tagged releases you can check in your plugin code at any time (whether it works or not) allowing you to access it from anywhere you are.

You may also want to keep your `readme.txt` up to date as you go. Installation instructions which do not match the release can be a big headache for users.

## Check In (Commit)

You’ve done your fixing and now you’re ready to upload the latest version of the code. This is simple a case of checking in (committing) the changes from your local files to the repository. Most GUI systems allow you to do this in one go, applying the change to an entire folder.

The system should check the files and identify which (if any) have changed. These files should be flagged to allow you to confirm that you want to apply the changes to the remote repository. If there are any conflicts your system should notify you of these now and allow you to fix them (either manually or by dropping one set of changes).

You can also add a comment at this point to indicate the changes you have made. This is useful on multi-developer projects for keeping track of who is doing what and when. You may also want to add comments so you can see when different changes were made – for example if you want to work back through previous modifications.

Once the files have been committed you can exit the repository, content in the knowledge your files are safe.

# Tagging for Download

## Testing

Once you have developed your plugin to the point where you feel ready to release a new version, check it. Below is a list of recommended steps for testing a plugin release:

*   Test the plugin on your local installation.
*   Test again on your remote setup.
*   Test the plugin with all other plugins disabled.
*   Test the plugin with all your other plugins enabled.
*   Install on a pristine WordPress install.

## Tagging

Now the plugin is ready to go you are ready to tag. Basically, tagging means taking a copy of the current trunk code and freezing it for release purposes. Again the process for doing this will differ from one SVN interface to another, but the basic steps are:

1.  Copy `/trunk` to `/tags/x.x` where x.x is the version number of your release (e.g. 1.2)

That’s it.

The release is now “tagged” and available for download. However, if you want this latest tag to appear in the [WordPress plugin download][15] system you need to let it know the tag is available and is the latest version.

If you haven’t done this already, you need to go back to the `readme.txt` file you created earlier and find the line, near the beginning, where it lists the Stable tag. Next to this you need to add the name of the tag which you have just created and re-save the file.

Once complete simply check-in the `readme.txt` file again using your SVN software.

# Downloading Plugins

Once the files are in the SVN there will be a short delay before they show up in the [plugin download interface][9].

If you have tagged a “latest release” and marked this in the `readme.txt` file in the trunk, the download interface will point to this latest tag. However, all other tags can be accessed using the standard file format, with x.x reflecting the tag name:

`plugin-name.x.x.zip`

If you opt not to use tagged releases, the download file format will instead point to the trunk:

`plugin-name.zip`

Note that this second download location, pointing to trunk, is always available to use if you want a permanent download URL which will continue to work throughout release. Note that if you do this you will want to keep trunk as a working copy to avoid unnecessary bug reports.

# Finally…

Stick with it. While SVN can seem an overly complicated system for basic plugin development, if you learn the basics above it should fit easily into your development cycle. You’ll also gain a set of skills useful not just for WordPress development, but for any open-source project.

Any suggestions, comments and improvements are always welcome.

 [1]: http://dev.wp-plugins.org/
 [2]: http://wordpress.org/extend/plugins/add/
 [3]: http://dev.wp-plugins.org/wiki/VersionControl
 [4]: http://www.alwins-world.de/wiki/programs/kdesvn
 [5]: http://golifescience.com/mu/kde-fileprotocoltransportprotocol/
 [6]: http://betterexplained.com/articles/a-visual-guide-to-version-control/
 [7]: http://svnbook.red-bean.com/
 [8]: http://www.gnu.org/copyleft/gpl.html
 [9]: http://wordpress.org/extend/plugins/
 [10]: http://www.gnu.org/licenses/gpl.txt
 [11]: http://www.wp-plugins.org
 [12]: http://wordpress.org/extend/plugins/about/readme.txt
 [13]: http://wordpress.org/extend/plugins/about/validator/
 [14]: http://svnbook.red-bean.com/nightly/en/svn.tour.cycle.html#svn.tour.cycle.resolve
 [15]: http://www.wordpress.org/extend/plugins

