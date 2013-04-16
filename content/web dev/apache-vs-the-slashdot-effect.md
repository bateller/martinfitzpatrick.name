Date: 2007-02-09 09:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Apache vs. the Slashdot Effect
Slug: apache-vs-the-slashdot-effect
Tags: apache,linux,lamp,slashdot,traffic

Increasing traffic is the measure of success for a website. More visitors equals more exposure which in turns generates more income. However, if you have hosted your site on a low-end package you could get hit by excess use charges just as your start celebrating your success.

Here at [mutube.com][1] the combination of 4,625 visitors (8,531 hits) a month and popular [free downloads][2] quickly helped trip our 1Gb bandwidth limit.

In this article I’ll look at how I’ve used the combined power of [Apache Server][3] and [Coral Cache][4] to distribute all kinds of requests away from your server transparently.


# Introduction to the Coral Content Distribution Network

[Coral CDN][4] (aka [Coral Cache)][4] is at it’s simplest a remote caching service for websites. When your site is viewed through the CDN the content is downloaded *only once* and then distributed from the network’s own servers.

You can view any page through the Coral CDN simply by appending `.nyud.net:8080` to the end of the server name. You can try it now by [viewing this page through the Coral CDN][5].

Note: If you gave the URL above to 1000 people and asked them to click, only one hit (from the Coral server’s themselves) would be registered on the site.

You can make immediate savings by using the Coral CDN to serve up images in your posts by adding `.nyud.net:8080` after the server in the URL. However, a better solution would be to configure your host to perform these actions automatically and transparently on the server side using Apache Rewrite rules.

# Introduction to Apache Rewrite

If you have a hosted website [the chances are it runs on Apache][6]. If it does you now have access to an incredibly powerful method of managing requests: Rewrite Rules.

In simple terms Rewrite Rules allow your web server to take a web address and *Re-Write* it to point to another location. A familiar example of this in action is WordPress Permalinks where requests are redirected from friendly URLs to where they actually are on your installation. However, for the purposes of managing bandwidth we are going to redirect requests off our server and onto the Coral Cache.

Rewrite rules are placed in the [.htaccess][7] file, normally in the *web root* on your host. Occasionally you may also want to place additional .htaccess files in specific directories to control more precisely where individual Rewrite rules are to apply.

If none of this makes any sense, you may want to consult your web host before making any changes. A good host will be able to explain the files to change and where to put them.

# Redirect by Referrer

Starting with a simple example we are going to describe how to set your website up to automatically redirect all requests from high-bandwidth hosts digg, Slashdot & blogspot.

The Rewrite rule to achieve this is as follows:

`<IfModule mod_rewrite.c><br />
RewriteEngine On<br />
RewriteCond %{HTTP_USER_AGENT} !^CoralWebPrx<br />
RewriteCond %{HTTP_REFERER} digg\.com [NC,OR]<br />
RewriteCond %{HTTP_REFERER} blogspot\.com [NC,OR]<br />
RewriteCond %{HTTP_REFERER} reddit\.com [NC,OR]<br />
RewriteCond %{HTTP_REFERER} slashdot\.org<br />
RewriteRule ^(.*)$ <a href="http://golifescience.com.nyud.net:8080/$1" rel="nofollow">http://golifescience.com.nyud.net:8080/$1</a> [R,L]<br />
</IfModule><br />
`

Apache processes the above in the following way:

1.  **RewriteCond:** 
    *   Checks the *user agent* of the current request against the known Agent for the Coral Web Cache. This prevents endless loops resulting from the first request as browsers send Referrers despite being redirected.
    *   Checks the *referring source* of the current request is checked to see whether it contains `digg.com` or `blogspot.com` or `slashdog.org`. In other words it checks whether you got to the current site by a link on one of these sites.
    *   [NC,OR] means “No Case, OR”. No Case means the comparison with the hostnames is case insensitive. OR means Apache tests both conditions and performs the RewriteRule if *either* is true.</em>
2.  **RewriteRule:** 
    *   RewriteRule is acted on only if one of the previous conditions is true.
    *   Takes the whole URL using ^(.*)$, where ^ means the beginning of the URL, $ means the end, and (.*) matches everything between. Note that this URL information is all relative to the saved location of the .htaccess file. If you are going to put this file in particular directories, read on for some tips.
3.  **Result:** 
    *   The new URL is then created by appending this to a base URL of <http://golifescience.com.nyud.net:8080/>

With this Rewrite rule in place any request for <http://golifescience.com/> that comes from the listed hosts (digg, Slashdot, etc.) will automagically be redirected to [http://golifescience.com.nyud.net:8080][8]. The end result is that requests from these hosts will not be served using your resources.

In the event of a being linked on one of these high-load websites, your site will be protected and your bandwidth should not exceed your host’s limits.

# Redirect by Directory

If you have files available for download in a particular directory Coral CDN can be used to serve these the public. The advantage is that for the cost of ~1 download/24hrs an unlimited number of people can have access to your files – with related bandwidth savings.

I employ this method here at [mutube.com][1] to manage hosting for my [WordPress plugins][9] amongst other things.

The Rewrite rule to achieve this is as follows:

`<IfModule mod_rewrite.c><br />
RewriteEngine On<br />
RewriteCond %{HTTP_USER_AGENT} !^CoralWebPrx<br />
RewriteRule ^(.*)$ <a href="http://golifescience.com.nyud.net:8080/downloads/$1" rel="nofollow">http://golifescience.com.nyud.net:8080/downloads/$1</a> [R,L]<br />
</IfModule><br />
`

There are a few basic differences between this RewriteRule and the previous example. The most significant is that this ruleset contains a *negative* check. In other words the Rule is executed on when the condition we are checking is false.

Secondly, since this rule applies only to files in the `/downloads` directory it has to be placed in a seperate .htaccess file in this location. Since `^(.*)$` match is relative to the location of the .htaccess file it will return only that part of the URL after this point – so we need to use the following base URL:

`<a href="http://golifescience.com.nyud.net:8080/downloads/" rel="nofollow">http://golifescience.com.nyud.net:8080/downloads/</a>`

So, stepping through the RewriteRule as before…

1.  **RewriteCond:** 
    *   Before redirecting to the cache we need to make sure that the cache is able to access the site itself. The above rule checks the User Agent (i.e. the application that is requesting the page) to make sure it **does not** match CoralWebPrx – the name of Coral’s bot.
    *   *Note: `!` is the method for identifying a negative condition*
2.  **RewriteRule:** 
    *   As before we’re simply getting the URL and building a redirect to Coral CDN. However because directory paths are all relative to the location of the .htaccess we have to include everything *beneath* the current location when rebuilding the new URL.
    *   If we place this rule in a .htaccess file in /downloads then the RewriteRule must contain the path up to this point.

With this Rewrite rule in place any request for <http://golifescience.com/downloads/myfile.zip> will be redirected to [http://golifescience.com/downloads/myfile.zip][10] distributing the majority of load away from your servers onto the Coral CDN.

# Notes

## Testing

It is important when adding Rewrite Rules to your site to test them adequately. Modifying URLs can easily lead to some weird and wonderful (as well as difficult to debug) errors on your site. When combined with a cache the problems can be multiplied as errors can be stored and re-served despite your changes.

## Maintenance

Once you have these systems set up they can for the most part be left along & forgotten about completely. A correctly configured Rewrite should require minimal maintenance.

## Proxies & Errors

As with all good things, there will be people who have problems accessing files stored on the Coral Cache (the port :8080 restriction is a common issue for poorly configured networks). In these instances it is often sensible to add a method to bypass the cache, e.g.

`RewriteCond %{QUERY_STRING} !(^|&)coral-no-serve$`

The above code allows you to bypass the Coral Cache by appending `?coral-no-serve` to the end of any URL. 

# Summary

With the power of Coral CDN you can successfully run a high-bandwidth site from a low bandwidth host. Combine this with Apache Rewrite Rules and you can do it transparently and with no inconvenience to your users.

This article has only touched on the basics of what it is possible to do with both Coral CDN & Apache Rewrite. If you have any suggestions for additions or alternatives post your comments below & I’ll keep this updated. If you’re a WordPress user keep an eye out for my WordPress-specific tips coming soon.

 [1]: http://golifescience.com
 [2]: http://golifescience.com/projects/wordpress/
 [3]: http://www.apache.org
 [4]: http://www.coralcdn.org
 [5]: http://golifescience.com.nyud.net:8080/articles/wordpress-vs-the-digg-effect
 [6]: http://news.netcraft.com/archives/web_server_survey.html
 [7]: http://javascriptkit.com/howto/htaccess.shtml
 [8]: http://golifescience.com.nyud.net:8080/
 [10]: http://golifescience.com.nyud.net:8080/downloads/myfile.zip