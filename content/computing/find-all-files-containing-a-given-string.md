Date: 2012-02-01 01:02
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Find all files containing a given string
Slug: methods/1534/find-all-files-containing-a-given-string
Tags: mac,bash,cli,linux,computing

A quick one-liner to recursively search files for a given text string.









Open up a terminal session and enter the following - replacing `"foo"` with the text to search for. 

    :::sh
    find . -exec grep -l "foo" {} \;






You can also limit the search to files with a particular extension (e.g. HTML or CSS). The first form will only return files in the current directory

    :::sh
    find *.html -exec grep -l "foo" {} \;

Alternatively you can search recursively while matching filenames using the `-name` parameter:

    :::sh
    find . -name *.html -exec grep -l "foo" {} \;



>You can pass other options to find including for example `-mtime -1` to specify only files modified within the past day.  


You can also replace `.` with the name of any other folder to search:

    :::sh
    find /var/www -name *.html -exec grep -l "foo" {} \;

This will search `/var/www` recursively for files named `*.html` and containing `foo`.





