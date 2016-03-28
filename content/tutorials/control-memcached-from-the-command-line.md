Date: 2012-02-05 05:02
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Control memcached from the command line
Slug: control-memcached-from-the-command-line
Tags: unix,webdevelopment,memcached,computing
Ads: bottom

memcached is a general-purpose distributed memory caching system originally developed by Danga Interactive for LiveJournal but now used by many other sites. It is often used to speed up dynamic database-driven websites by caching data and objects in RAM to reduce the number of times an external data source (such as a database or API) must be read. Here we describe the options available from the command line to control a memcached instance via unix socket or IP:port.

![method/1536/Screen Shot 2012-08-05 at 17.28.09.png](/images/method/1536/Screen%20Shot%202012-08-05%20at%2017.28.09.png)

#Requirements
memcached

#Method

Memcached can be set up to either take control commands via an IP address and port or via a unix socket. 

When listening via IP:port by default memcached listens for connections on port `11211` and accepts connections from `INADDR_ANY`. To prevent possibly malicious access you may want to consider restricting connections to an internal or firewalled connection. Alternatively you can set memcached to only listen for connections on `localhost` - i.e. the server running the instance of memcached using  `127.0.0.1`. 

To start up an instance of memcached listening on `localhost` port `11211` only use the following:


    ::sh

    memcached -d -m memory -l 127.0.0.1


>`memory` is the maximum number of megabytes of memory you want memcached to use.

>

> If you want to specify a different port to listen on use the `-p PORT` option.


Alternatively you can use unix sockets to communicate directly with the memcached instance. In this case commands can only be sent from a login shell that has access to the socket file - for example if you ssh into the server hosting it.



To start up memcached using unix sockets you would use the following command:



    ::sh

    memcached -d -m memory -s ~/memcached.sock 



This will create a file named `memcached.sock` in your home directory to communicate through.


>`memory` is the maximum number of megabytes of memory you want memcached to use.


Memcached comes with a number of useful [management commands](http://code.google.com/p/memcached/wiki/NewCommands). Of these the most frequently useful are `flush_all` and the stats commands including `stats`, `stats items` and `stats slabs`.



To send a command to memcached you can use `nc` (netcat). The general form for all commands is:



    :::sh

    echo "command" | nc 127.0.0.1 11211



Or for socket connections:



    :::sh

    echo "command" | nc -U ~/memcached.sock







To flush the entire contents of your memcached instance you could issue the `flush_all` command with one of the following:



    :::sh

    echo "flush_all" | nc 127.0.0.1 11211

    echo "flush_all" | nc -U ~/memcached.sock



Results in:



    :::sh

    [user@web37 ~]$ echo "flush_all" | nc -U ~/memcached.sock

    OK

    [user@web37 ~]$ 





![step/None/Screen Shot 2012-08-05 at 18.19.20.png](/images/step/None/Screen%20Shot%202012-08-05%20at%2018.19.20.png)



You can use the stats commands to get information about the state of your memcached instance. For example:



   :::sh

    echo "stats" | nc 127.0.0.1 11211

    echo "stats" | nc -U ~/memcached.sock



Will output a list of stats for the current instance. Additional information can be found using `stats items` to give total stats about items stored in the cached and `stats slabs` which provides more information including performance hints.

![step/None/Screen Shot 2012-08-05 at 17.28.09.png](/images/step/None/Screen%20Shot%202012-08-05%20at%2017.28.09.png)







>This method is based, with permission, on an original protocol available [here](http://community.webfaction.com/questions/7275/how-to-communicate-with-memcached-socket-via-shell).

