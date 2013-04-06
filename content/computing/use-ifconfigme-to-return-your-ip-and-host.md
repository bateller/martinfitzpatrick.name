Date: 2011-11-08 08:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Use ifconfig.me to return your IP and Host
Slug: use-ifconfigme-to-return-your-ip-and-host
Tags: cli,ip,hostname,ifconfig,ip address,computing

ifconfig.me is a web service that displays information about your connection, including IP address, hostname and User Agent string. Helpfully it provides a simplified interface that can be easily queried to get this information from the command line.




>All commands are variations on the below. The full list is also available on the ifconfig.me website:
>
>`curl ifconfig.me`
>`curl ifconfig.me/<request-data>`




#Method

To get your remote IP address as seen by other users online enter the following at a command line:

`curl ifconfig.me` or `curl ifconfig.me/ip`


>`curl` is a command-line tool for requesting data from a specified URL


Other commands are variations on this theme such as:

`curl ifconfig.me/host` for your remote hostname

`curl ifconfig.me/ua` for your User Agent


>Note that your User Agent will be that as sent by `curl` and will differ from that reported when accessing ifconfig.me in your actual browser.
>
>


A full set of all the data returnable is available using:

`curl ifconfig.me/all`







>This method is based, with permission, on an original protocol available [here](http://ifconfig.me/).

