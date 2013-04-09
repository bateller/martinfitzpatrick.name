Date: 2012-01-26 12:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Display external RSS feeds on your WordPress blog
Slug: display-external-rss-feeds-on-your-wordpress-blog
Tags: web-dev,wordpress,php,rss,computing

Show another of your blogs or any other RSS news feed on your WordPress blog with this simple template code.









Open your template file in either the WordPress admin editor or via FTP/SSH access to your hosting server. If you want to put the feed links in your sidebar either look for a `sidebar.php` or similar file.



Locate where you want to include the feed and add the following code:

    :::php
    <?php include_once(ABSPATH.WPINC.'/feed.php');
    $rss = fetch_feed('http://root.abl.es/rss/latest/');
    $maxitems = $rss->get_item_quantity(5);
    $rss_items = $rss->get_items(0, $maxitems);
    ?>
    <ul>
    <?php if ($maxitems == 0) echo '<li>No items.</li>';
    else
    // Loop through each feed item and display each item as a hyperlink.
    foreach ( $rss_items as $item ) : ?>
    <li>
    <a href='<?php echo $item->get_permalink(); ?>'
    title='<?php echo 'Posted '.$item->get_date('j F Y | g:i a'); ?>'>
    <?php echo $item->get_title(); ?></a>
    </li>
    <?php endforeach; ?>
    </ul>


>You will want to modify the code as follows:
>
>* Change the `fetch_feed` URL to your own blog (or show ours!).
>* Change the `get_item_quantity(5)` to the number of items you wish to show.
>


Save the file and refresh your blogpage. You should now see the feed entries in your page!







