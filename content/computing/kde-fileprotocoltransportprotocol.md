Date: 2007-03-20 09:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: KDE fileprotocol+transportprotocol://
Slug: kde-fileprotocoltransportprotocol
Tags: linux,kde,filetransport

While getting started using the new [wp-plugins.org SVN][1] I was looking for a quick way to download the contents of an SVN to local disk. This can be useful when doing research on methods employed by other plugins or for getting a local development copy where SVN access is unavailable. Under KDE you can normally access any remote location using the standard URL format. For example, an SVN (using the `svn://`) protocol would normally be accessed using the URL style `svn://svn.wp-plugins.org`.  
  
Many SVNs, e.g. `svn://svn.kde.org` can be accessed as expected. However, this is reliant on the server providing an `svn://` protocol access which some do not – notably the wordpress.org SVN which instead provides access to the SVN through `http://` only.

In these cases you need a method for accessing `svn://` via `http://` ..and surprise, surprise, KDE can do that. As [Sabin Iacob][2] noted, it’s possible in KDE to provide separate file and transport protocol within a single URL. Doing this allows the filesystem to connect through one (transport protocol) and act on the result as if it were the other (file protocol).

<!-- PELICAN_END_SUMMARY -->

For example, using Konqueror (or any KDE app) to connect the WordPress SVN enter the following URL to browse the WordPress repository as if it were a standard directory:

`<a href="//svn.wp-plugins.org/">svn+http://svn.wp-plugins.org/</a>`

Of course, this is not just restricted to use on the WordPress SVN, or indeed SVN alone. This capability is useful in any situation where you need to bypass the protocol restrictions of the server yet still use the result as if it had come from a standard setup.

If you have suggestions of other uses share in the comments!

# Note

When working with SVN files directly (e.g. for the purposes of developing) it is always preferable to go through the standard check-out, modify, check-in process to allow the system to keep track of changes properly. However, some times you may want to just take a copy of remote files for personal use. Pick your use-case carefully.

 [1]: http://dev.wp-plugins.org/
 [2]: http://www.nabble.com/SVN-Question-t3416813.html
