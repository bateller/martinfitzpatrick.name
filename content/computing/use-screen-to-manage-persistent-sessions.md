Date: 2011-10-02 06:10
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Use screen to manage persistent sessions
Slug: use-screen-to-manage-persistent-sessions
Tags: shell,cli,gnu,screen,unix,linux,computing
Ads: bottom

GNU Screen is a command-line application that allows use of multiple virtual sessions within a single real terminal or remote session. Importantly, it allows for persistent running of command-line applications independent of the shell that initiated them program, meaning active applications can persist during disconnection.

<!-- PELICAN_END_SUMMARY -->


>This is just one of many things that screen is useful to accomplish! You can also use multiple screens to run concurrent applications on a remote or local server from a single terminal window.




#Method

Connect to the remote server, for example using ssh



    ssh user@example.com







On the remote server start `screen` before any other commands. You will see the screen welcome text shown. Press any Space or Return to exit back to the shell.

![step/None/screen-screenshot.png](/images/step/None/screen-screenshot.png)



You can now start any long running process that you wish to persist over the connection.



    ping example.com



While this command is running you can now 'detach' the running screen from the active session by pressing `Ctrl-A` followed by `Ctrl-D` on the keyboard. You will notice that the active session returns to the point where you first typed screen.



Exit the running ssh session by typing `exit`.  Make a cup of tea. You can now reconnect to the server as before.



    ssh user@example.com



Back at the remote prompt you can re-attach the previously started screen to the current session. 



    screen -r



You will see your command continued to run while you were away!







