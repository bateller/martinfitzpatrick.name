Date: 2012-01-21 02:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Bash Command Substitution
Slug: bash-command-substitution
Tags: bash,cli,linux,computing
Ads: top,bottom

Bash command substitution performs a given command replacing the marker with the resulting standard output. It is particularly useful when you want to store the output of a command in a variable or as an alternative method of chaining multiple commands together.





#Requirements
bash

#Method

Bash command substitution is achieved by wrapping your target code in braces with a preceding $, or backticks `. For example:



    :::bash

    $ date +%d-%b-%Y

    21-Jul-2012 



You can put the output of that command into a variable using command substitution as follows:



    :::bash

    $ today =$(date +%d-%b-%Y)

    $ echo today

    21-Jul-2012 



Alternatively, with backtick style:



    :::bash

    $ today =`date +%d-%b-%Y`

    $ echo today

    21-Jul-2012 







You can also perform command substitution inside an echo command:



    :::bash

    echo -e "List of logged on users and what they are doing:\n $(w)"



You can also feed the results of command substitutions into a for loop as follows:



    :::bash

    for f in $(ls /etc/*.conf)

    do

       echo "$f"

    done


>This example is a little contrived as you can achieve the same result with `for f in /etc/*.conf`






