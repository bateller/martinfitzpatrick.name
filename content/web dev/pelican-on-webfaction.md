Date: 2013-04-07 09:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Pelicans on Webfaction
Slug: pelicans-on-webfaction
Tags: pelican,webfaction,python

As mentioned in the previous post, I recently migrated this site over to the very clever [Pelican][pelican]. Setting it up was relatively straightforward using a combination of the 
official docs, [this post][1] and linked github repo from [Dominic Rodger][2]. That said, there were a few things that I stumbled at and non-obvious decisions that I've documented below.

# Setting up

Before starting you need to install the packages. Thankfully everything you need is available via the python packaging service PIP. Unfortunately PIP isn't installed by default on Webfaction  so you'll need to get that set up as per the [instructions from Webfaction](http://docs.webfaction.com/software/python.html). So SSH into your account and do the following:

## PIP

1. Make sure the destination directory exists. Enter `mkdir -p $HOME/lib/pythonX.Y`, where X.Y is the Python version, and press Enter.
2. Install pip. Enter `easy_install-X.Y pip`, where X.Y is the version of Python you wish to use, and press Enter.

> In my case X.Y was 2.7

## Pelican dependencies

I then manually installed these dependencies, I'm not sure if all are required (or already present on Webfaction) - give it a go and let me know in the comments.

	#!bash
	pip install feedgenerator 	# to generate the Atom feeds
	pip install jinja2 			# for templating support
	pip install pygments 		# for syntax highlighting
	pip install docutils 		# for supporting reStructuredText as an input format
	pip install pytz 			# for timezone definitions
	pip install blinker 		# an object-to-object and broadcast signaling system
	pip install unidecode 		# for ASCII transliterations of Unicode text

> If you’re not using Python 2.7, you will also need to `pip install argparse`.

In the Pelican setup it lists the following two as optional, but you'll need the first to use markdown flavoured markup. The second makes your text output prettier, I installed it.

	#!bash
	pip install markdown 		# for supporting Markdown as an input format
	pip install typogrify 		# for typographical enhancements

## Pelican

Now with all that out the way, we can install pelican. As with the above, it's a simple case of entering at the command line:

	#!bash
	pip install pelican

## Webfaction

First things first, we need to create a Webfaction webapp to hold our site. In fact, we need 2: one for the source code and settings, one for the output. Only the second of these is actually served publically - and Webfaction allows for this by making it possible to have applications with no association website. You do this through the Webfaction panel.

> If you want to, you can put the generator code in your home folder instead but I think that is a bit confusing.

You can also decide here how you want to name the two apps. Initially I had `golifescience` holding the source, and `golifescience_public` holding the generated output. However, it dawned on me that if I wanted more than one Pelican site (quite possible) I was going to end up with multiple dud apps scattered around. To prevent this I created two apps, one `pelican` that will hold any Pelican site settings repos in a subfolder, and `golifescience` which is the public served version of this site.

The first, `pelican`, was created as 'Static only (no .htaccess)', the second `golifescience` as 'Static/CGI/PHP-5.4'. This latter decision only really has an impact if you need to use URL rewriting, or other `.htaccess` directives further down the line. I did, so I did. If you like this can also be 'Static only (no .htaccess)' and it'll be served by Webfaction's potentially-faster nginx server. 

Remember to associate the public one with an active domain under 'websites'. Make sure it's working (if you've just set it up DNS could hold you up here).

## Back to black

Back in the SSH session you can now cd ~/webapps and see the two new created folders `pelican` and `yoursitenamehere`. Now change into your pelican folder with

	#!bash
	cd pelican 				# change into your pelican folder
	mkdir yoursitenamehere  # create a directory to hold your site config
	cd yoursitenamehere 	# change into your site's folder

We can now use the Pelican command to initiate the setup:

	#!bash
	pelican-quickstart

Answer the questions and Pelican will create your initial folder. The important things to remember are that your output folder, relative to the current location is `../../yoursitenamehere`. 

## Github
	
Following in Dominic's footsteps I decided to use [github][github] for my content hosting. However, Pelican has a handy tool to generate your setup, so you'll need to initiate the repo on the Webfaction side and re-home it onto github. Bear with me.

So now we have the folder created for our config setup, we want to get it into our git repo so we can track the changes. The first step is to log into your Github account and create the new repo, calling it whatever you like. **Do not add a README.md** as we need the repo empty to do the next thing - if you mess it up, just delete and recreate. Github is fine with that. Once created make note of your repo's read & write git url (SSH).

> If you haven't set up github with your SSH keys you'll need to do that now. Generate a key on your Webfaction host using `ssh-keygen` and copy-paste it into your [Github SSH settings](https://github.com/settings/ssh).

Back in the shell, initiaise the github repo and then re-home it to your github repo.

	#!bash
	git init
	git git remote add origin git@github.com:<github-username>/<github-repo-name>.git
	git push -u origin master
	
Sorted. The repo for your site is setup, and the repo now things Github is it's origin, so it will pull down from it to get updates. This means you can now clone that repo yourself to another machine and push your changes up via github.


# Getting going

To all intents and purposes you are now finished and ready to make a beautiful website. But there are a few final things to consider.

## Folders

Firstly, folder structure. Things are 'expected' to be laid out as follows by the system, but it's not immediately clear - meaning it can get a bit confusing why certain content is not showing up. 

	:::text
	/content
		/images
		/pages
		/extra
		/<category-1>
		/<category-2>
	/theme
	
The folder `images` is automatically copied through to appear at `/static/images` on your live site. Similarly `pages` is a special folder that anything contained within will be created as a static page, will not appear in feeds and may appear on link lists in certain forms. The URL structure for articles and pages is different (see later). Finally, `extra` is an optional folder, but extremely useful for copying through completely static content to the a particular destination. For example, on this site I'm using the following in my `pelicanconf.py` to copy through a static robots.txt and .htaccess:

	#!python
	FILES_TO_COPY = ( ('extra/robots.txt', 'robots.txt'),
    	              ('extra/.htaccess', '.htaccess') )

## URLs

Pretty-urls are a nice thing to have. Unfortunately, by default Pelican gives you a lot of `.html` everywhere. The official docs suggest solving this by setting your URL/SAVE_AS directives to put files as `index.html` under folders for the slug, so for example `posts/your-slug-here/index.html`. This works, as you can now put the URL as `posts/your-slug-here/` and hit the file. Pretty URLs no redirects or `.htaccess`.

However, it doesn't work if you want to use custom themed error pages generated by Pelican (you can of course manually create them and copy them in the FILES_TO_COPY above, but you will need to maintain them in line with the theme by hand). To do that you either need to access that all pages will have URLs like `/about.html` or use `.htaccess`. And if you're going to use `.htacess` redirects you may as well make it handle the pretty URLs too.

So to start with add the following to your `pelicanconf.py` file.

	#!python
	ARTICLE_URL = 'posts/{slug}'
	ARTICLE_SAVE_AS = 'posts/{slug}.html'
	PAGE_URL = '{slug}'	
	PAGE_SAVE_AS = '{slug}.html'
	AUTHOR_URL = 'author/{slug}/'
	AUTHOR_SAVE_AS = 'author/{slug}.html'
	CATEGORY_URL = 'category/{slug}'
	CATEGORY_SAVE_AS = 'category/{slug}.html'
	TAG_URL = 'tag/{slug}'
	TAG_SAVE_AS = 'tag/{slug}.html'

This creates a set of URL formats where articles are linked to at `posts/your-slug-here` (note, no trailing slash, all the cool kids do it) and saved as the same name but with .html extension. Now save the config and create a new file names `.htaccess` in your `content/extra` folder - this will hold your .htaccess config for the live site.  Add the following:

	:::text
    Options +FollowSymLinks
    RewriteEngine On

    # Remove trailing slashes.
    # e.g. example.com/foo/ will redirect to example.com/foo
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.+)/$ /$1 [R=permanent,QSA]

    # Redirect to HTML if it exists.
    # e.g. example.com/foo will display the contents of example.com/foo.html
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME}.html -f
    RewriteRule ^(.+)$ $1.html [L,QSA]

    ErrorDocument 404 /404.html
    ErrorDocument 403 /403.html

What it does is explained in the comments for each directive. The first chunk removes trailing slashes. The second chunk checks what is requested is not an actual file (e.g. static file), not a directory, and that `<filename>.html` exists, before rewriting the request to return that. The final two are for our error files. 

Save the file and you're good to go.

## Miscellaneous `peliconf.py`

Here are some additional extras for `peliconf.py` you might want to try out. Since I installed it I also turned on Typogrify by adding the following:

	#!python
	TYPOGRIFY = True

Because of the new feed variables in 3.0 some old themes won't work. Add this to fix:
	
	#!python
	FEED_DOMAIN = SITEURL
	FEED_ATOM = 'feeds/atom.xml'
	
# Express yourself (hey, hey)

It's time to write someting (finally). We'll create a test post and our two error document pages. So, first, simply create a new text file and enter the following:

	:::text
	Date: 2013-04-07 09:00
	Author: Your Name
	Email: your.email@your.email.provider
	Title: A test post
	Slug: a-test-post
	Tags: test,post
	
	Hello!
	
Save it in the content folder with the name `a-test-post.md`. You can save it under a sub-folder (create it) to categorise the post if you like. Then create another empty text file and add the following:

	:::text
	Title: 404
	Slug: 404
	Status: hidden
	
	Not found
	=========
	
	Nothing to see here, move along.

Save it under the `content/pages` folder with the name `404.md`. Edit a similar file for 403 Forbidden errors and save as `403.md`.

# Pelicans are go

Let's commit and push this to github incase we lose all our hard work. At the command line, in your pelican content source folder `pelican/yoursitenamehere` enter the following:

	#!bash
	git add .
	git commit -a -m "Initial commit"
	git push

Now lets generate a site. In the same folder enter the following to create the content:

	#!bash
	make html
	
You can also use:
	
	#!bash
	make publish
	
The only difference is the latter *also* uses the config settings in `publishconf.py` including the quite useful `RELATIVE_URLS = False` directive (uncomment it first). 

If you now access your site from the web, you should see your post in all it's glorious creativitiy. If it hasn't worked, drop a note in the comments and I'll work it out with you. 
	
# Automatic for the people

I'm lazy, so I don't really like doing the whole commit-push-pull-make thing. Thankfully it's relatively easy to automate the whole thing with a short shell script. Still on your SSH session to webfaction enter:

	#!bash
	nano ~/auto_pelican_publish.sh
	
This starts a simple editor to create a shell script. Simply copy and paste the following into the file, editing the paths as appropriate:

	#!/usr/bin/env bash

	cd <path-to-your-pelican-content-folder> # e.g. /pelican/yoursitenamehere
	git pull
	make publish

Save by pressing `Ctrl-X` and then `Y`. That's it. Back at the command line type:

	#!bash
	chmod +x ~/auto_pelican_publish.sh 	# to make the file executable

Next to add this to cron. Back at the command line enter:

	#!bash
	crontab -e
	
Add the following to the top of the file, replacing your username:

	:::text
	PATH=/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/opt/dell/srvadmin/bin:/home/<webfaction-username>/bin
	*/15 * * * * ~/auto_publish_pelican.sh

Again `Ctrl-X` and `Y` to exit and save. This will run the auto-publish script every 15 minutes, pulling from your remote git repository and then publishing the files it finds. All you need to do is make your commits on your local machine, push them to github, and within 15 minutes they'll be on your site. You can adjust the timer by changing the 15 to another number, e.g. 30 means every half an hour.
	
# Wrapping up

Pelican is a really neat bit of software, that gets you away from all the faffing of dynamic web stuff to just concentrating on the important thing - writing. Hopefully this guide makes setting yourself up on Webfaction a little easier. If you hit any stumbling blocks in spite of this let me know in the comments! Happy pelicaning - whatever that involves.


[1]: http://www.dominicrodger.com/pelican.html
[2]: http://www.dominicrodger.com
[github]: http://www.github.com/
[pelican]: http://getpelican.com
[webfaction]: http://www.webfaction.com?affiliate=spenglr