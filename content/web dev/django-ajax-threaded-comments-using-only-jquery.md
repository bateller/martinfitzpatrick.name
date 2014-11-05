Date: 2012-01-30 07:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Django AJAX threaded-comments using only jQuery
Slug: django-ajax-threaded-comments-using-only-jquery
Tags: mptt,comments,django,web-dev,jquery,threaded-comments,computing

Upgrade threaded comments using mptt to allow AJAX submission of comments and update the template - without any backend hacking of Django. Everything is accomplished via Javascript and template tags.

<!-- PELICAN_END_SUMMARY -->

![method/1533/Screenshot from 2012-07-31 20:53:24.png](/images/method/1533/Screenshot%20from%202012-07-31%2020%3A53%3A24.png)



>Use the [threaded comments implementation outlined here](http://root.abl.es/methods/1524/) to build the basis for this hack. This is based on [code outlined here](http://ca.rroll.net/2009/05/10/improving-django-comments-user-experience-with-ajax/) with extension to support extracting the resulting comment from the completed page returned (rather than using a minimal template).




#Method

Set up Django threaded comments using the [mptt method outlined previously](http://root.abl.es/methods/1524/).



First open up your comment form template `form.html` created in the threaded-comments tutorial and make the following changes:



    :::html

    <div class="comment-form" id="comment-form-{{ node.id }}" {% if node.id %}style="display:none;"{% endif %}>

    <form action="{% comment_form_target %}" method="post" id="comment-form-{{ node.id }}f">



This simply ensures that the form and the wrapper both have unique ids on the page. This is required for the jQuery interactions to function reliably.



Next in the comment output template just beneath the `{% recursetree comments %}` wrap the comment output with the following `div`:



    :::html

    <div {% if request.REQUEST.c|add:"0" == node.id %}id="newly_posted_comment"{% endif %}>

    ...comment content...

    </div>



This looks for the `c` value set on the query string - as is done by the comment framework on the redirected-to page after submitting the comment. The odd looking `c|add:"0"` here is simply to coerce the string from the query string into an `int` for comparison with the node.id. Ugly but works.



The effect of this is giving the comment you posted the id `newly_posted_comment` - making it simple to find in the AJAX returned html.


>You can also use this id to style the comment differently - e.g. highlighting it in some way. This will also work on non-AJAX requests.


Create a new template file in your comments templates folders named `_ajax_comments.html`. Add the following code below to this file and save. Note that you can alternatively put this in a `.js` file and include it as normal however you will need to hard-code the comment posting url.



    {% load comments %}



     <script type="text/javascript" charset="utf-8">



            (function( $ ){

            $.fn.bindPostCommentHandler = function() {

                // We get passed a list of forms; iterate and get a unique id for each

                // attach a submit trigger to handle saving and returning

                this.each(function() {

                    //$(this).find('input.submit-preview').remove();

                    $(this).submit(function() {

                        commentform = this;

                        commentwrap = $(this).parent();

                        $.ajax({

                            type: "POST",

                            data: $(commentform).serialize(),

                            url: "{% comment_form_target %}",

                            cache: false,

                            dataType: "html",

                            success: function(html, textStatus) {   

                                // Extract the form from the returned html

                                postedcomment = $(html).find('#newly_posted_comment');

                                $(commentform).replaceWith(postedcomment.html());

                                $(commentwrap).hide();

                                $(commentwrap).slideDown(600);

                                $(commentwrap).find('.comment-form form').bindPostCommentHandler();

                            },

                            error: function (XMLHttpRequest, textStatus, errorThrown) {

                                $(commentform).replaceWith('Your comment was unable to be posted at this time.  We apologise for the inconvenience.');

                            }

                        });

                        return false;

                    });

                }); //each

            };  

            })( jQuery );





            $(function() {

                $('.comment-form form').bindPostCommentHandler();

            });

             

    </script>


>If you're interestd in what is happening in the code read on; if not you can safely skip this bit:

>

>     $('.comment-form form').bindPostCommentHandler();

>      $(this).submit(function() {

>

>Together these bind our function onto the submit handler for all the comment forms on the page. This means when you hit submit it gets passed to our function below.

>

>    commentform = this;

>    commentwrap = $(this).parent();

>

>In the function `this` is a reference to the form - we store this in variable `commentform` so it's accessible within the ajax sucess function. We also store `commentwrap` which refers to the div wrapper of the comment form - it's useful shorthand later.

>

>    $.ajax({

>        type: "POST",

>        data: $(commentform).serialize(),

>        url: "{% comment_form_target %}",

>        cache: false,

>        dataType: "html",

>

>This is the submission handler for the AJAX request. We serialize the form `commentform` and submit it to `{% comment_form_target %}` and note that the data type returned will be HTML. This is the standard form submission URL we're talking to so there will not be JSON/other things available.

>

>        success: function(html, textStatus) {   

>            // Extract the form from the returned html

>            postedcomment = $(html).find('#newly_posted_comment');

>            $(commentform).replaceWith(postedcomment.html());

>

>The success function is passed the html from the submission which - hopefully - will include the newly posted comment. So we use jQuery to find that element (which we've flagged with id `newly_posted_comment`) and replace the originating form with that content.

>

>            $(commentwrap).find('.comment-form form').bindPostCommentHandler();

>

>Finally we bind our handler to this new comment form so the AJAX submission will keep on working.

>

>        error: function (XMLHttpRequest, textStatus, errorThrown) {

>            $(commentform).replaceWith('Your comment was unable to be posted at this time.  We apologise for the inconvenience.');

>

>This final bit is the error handler for when the AJAX submission goes wrong in any way. Here we replace the commentform with the error but you might instead want to insert the error before so the user can re-attempt submission.


Finally include the `_ajax_comments.html` on the template hosting your comments (or include the Javascript file if you chose that route). It needs to go into the `head` section of the html page so here I use `{% block extrahead %}` but your template may be different.



    {% block extrahead %}

        {{ block.super }}

        {% include "comments/_ajax_comments.html" %}

    {% endblock %}



Refresh your page and attempt to submit a comment. You should find it magically sliding down from the comment above! No framework hacking neccessary.







>The above is based on original code from [this article](http://ca.rroll.net/2009/05/10/improving-django-comments-user-experience-with-ajax/).

