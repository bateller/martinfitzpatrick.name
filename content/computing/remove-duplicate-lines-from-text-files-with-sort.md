Date: 2012-01-08 04:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Remove duplicate lines from text files (with sort)
Slug: remove-duplicate-lines-from-text-files-with-sort
Tags: bash,cli,sort,unique,computing
Ads: bottom

A quick method to remove duplicates from text files - including for example CSV files - 
where multiple records have been added (perhaps automatically) at different times resulting 
in multiple copies of the same record scattered throughout the file. Here is a simple 
one-liner bash command to remove duplicates using sort.

<!-- PELICAN_END_SUMMARY -->

>This method is sensitive to the line endings of the file. If you have files editing in a combination of Unix/Linux/Mac/Windows you may have a variety of line-endings in place. 

>

>The simplest route is to run the file through `dos2unix` before attempting the sort/unique filter.


#Requirements
sort

#Method

In a bash shell enter:



    sort -u file.csv -o file.csv



This takes your file, sorts it (using sort), gets the unique entries (-u) and writes it to the outfile (-o) which here is the same as the initial file.







