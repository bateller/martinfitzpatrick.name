Date: 2011-11-07 03:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Find top 404 Error pages (Apache)
Slug: find-top-404-error-pages-apache
Tags: shell,apache,404,logs,apache2,web-dev,computing

A quick one-liner to find the most common pages giving 404 errors on your apache2 setup. Set this up as a shell alias to get easy access at any time.

<!-- PELICAN_END_SUMMARY -->



>This one liner breaks down as follows:

>

>1. `cut` splits the input (the logfile) by `-d` delimiter and returning only the fields given by `-f``

>2. Output is piped into `awk` which searches for lines where field 4 = 404, returning these as a line containing `404 URL`

>3. These are then sorted (so duplicates can be counted) with `sort`

>4. `uniq -c` counts the duplicates chucks them away and appends a number to the beginning of each row that is left

>5. The resulting output is then `sort`ed numerically `-g` and `-r` reverse (highest first - remove this to get the top ones at the bottom of the list)

>




#Method

From the Linux command line enter:



`cut -d'"' -f2,3 /var/log/apache/access.log | awk '$4=404{print $4" "$2}' | sort | uniq -c | sort -rg`


>Substitute the path `/var/log/apache/access.log` for the path to your own apache setup. On web hosts this may be under `~/logs/apache' or elsewhere.






>This method is based, with permission, on an original protocol available [here](http://i-heart-geek.blogspot.co.uk/2011/10/top-command-line-tips-apache-access-log.html).

