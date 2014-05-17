Date: 2012-01-26 12:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Highlight author&#39;s comments on WordPress blog
Slug: highlight-authors-comments-on-wordpress-blog
Tags: web-dev,wordpress,php,computing

A simple trick to make comments from the original post author stand out a bit more in the comment listing - useful for seeing replies to comments.

<!-- PELICAN_END_SUMMARY -->








First you need to create a style to apply to highlighted comments on your blog. To do this, either in the admin editor or via SSH/FTP edit the file `style.css`.



Add a line that applies a style to a class called `authorstyle`:



    :::css

    .authorstyle { background-color: #fffddf !important; }



Here we've set the background to a nice yellow.



Next find the `comments.php` file in your theme folder and look for the following line:



    :::php

    <li <?php echo $oddcomment; ?>id="comment-<?php comment_ID() ?>"></li>



And replace it with:



    :::php

    <li class="<?php if ($comment->user_id == 1) $oddcomment = "authorstyle"; echo $oddcomment; ?>"></li>




>What this is doing is checking whether the user_id of the comment poster equals 1 (the admin user - who set up the blog) and if so showing the comment as highlighted. This will only work on a single-user blog (i.e. if you have more than one author their posts will not be highlighted).






>This method is based, with permission, on an original protocol available [here](http://www.mattcutts.com/blog/highlight-author-comments-wordpress/).

