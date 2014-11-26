Date: 2011-11-08 08:11
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Quickly serve a folder via Web Server
Slug: quickly-serve-a-folder-via-web-server
Tags: python,http,web-server,programming,computing
Ads: top,bottom

A short one liner to quickly serve any folder via a http server.

<!-- PELICAN_END_SUMMARY -->



#Requirements
python

#Method

`cd` to the directory you want to serve.



At the shell prompt enter `python -m SimpleHTTPServer`


>When run the command will output the port which the server is available on. You can optionally provide a port number e.g. `python -m SimpleHTTPServer 8080` to set this yourself. You can only serve a single folder at each port.


Open your web browser and access `http://localhost:PORT/`


>If the server is running on port :80 you can omit it from the address. If you set the port number yourself access via `http://localhost:8080` changing 8080 to the port number you picked.






