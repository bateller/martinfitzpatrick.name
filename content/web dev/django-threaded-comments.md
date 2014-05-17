Date: 2012-01-17 06:01
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Django Threaded Comments
Slug: django-threaded-comments
Tags: mptt,django-threadedcomments,comments,django,web-dev,computing
Picture: /images/method/1524/Screenshot%20from%202012-07-17%2018%3A52%3A26-2.png

Django ships with it's own comments contrib app that provides commenting on arbitrary models. However this is a flat-comment system which doesn't allow replying to comments. An app called django-threadedcomments exists but has not been updated for a number of versions and is broken. Other alternatives are less flexible than the Django commenting system itself.

<!-- PELICAN_END_SUMMARY -->


Here we demonstrate a simple method to get threaded comments in Django using a combination of the inbuilt comment app and the mptt app. 


![method/1524/Screenshot from 2012-07-17 18:52:26-2.png](/images/method/1524/Screenshot%20from%202012-07-17%2018%3A52%3A26-2.png)



>Other solutions available at [django-threadedcomments](https://github.com/HonzaKral/django-threadedcomments) or [codeblogging](http://codeblogging.net/blogs/1/3/)

>

>For this method you will also need [django-mptt](https://github.com/django-mptt/django-mptt/)


#Requirements
Django (with standard comments)

django-mptt

#Method

Django-mptt implements Modified Preorder Tree Traversal with your Django Models to produce working trees of Model instances. It achieves this by adding a number of hidden fields to your model. We're we're going to amend the inbuilt comments model (through class inheritence) to add these fields for django-mptt, then add some tweaks and hooks to make it all work together nicely.


>The full [django-mptt documentation](http://django-mptt.github.com/django-mptt/) is worth a look.


To begin with you will need to install all the constituent parts. First install [django-mptt](https://github.com/django-mptt/django-mptt/) and add mptt and Django contrib comments apps to your `INSTALLED_APPS` in your `settings.py`



Also you need to add your own comment app (that we're creating here) to your INSTALLED_APPS so you may as well do that now - we've called ours rather simply comments'.



    :::python

    INSTALLED_APPS = (

    ...

        'django.contrib.comments',

        'mptt',

        'comments',

    ...

    )



Next add the following somewhere in your `settings.py` file:



    :::python

    COMMENTS_APP = 'comments'



This tells Django where to go looking for comment-related tweaks you've created.



Now let's create the app! In your `~/my_project/apps/` folder create a new app with:



    :::python

    python manage.py startapp comments



This will create a folder with `__init__.py`, `models.py`, `tests.py` and `views.py`







Now we need to create the amended model, adding in the mptt fields. Thankfully django-mptt makes this remarkably easy, we only need to inherit from the MPTT model class and add a single field. So, here is our completed model (in models.py):



    :::python

    from django.contrib.comments.models import Comment

    from mptt.models import MPTTModel, TreeForeignKey

    

    class MPTTComment(MPTTModel, Comment):

        """ Threaded comments - Add support for the parent comment store and MPTT traversal"""

        # a link to comment that is being replied, if one exists

        parent = TreeForeignKey('self', null=True, blank=True, related_name='children')



        class MPTTMeta:

            # comments on one level will be ordered by date of creation

            order_insertion_by=['submit_date']



        class Meta:

            ordering=['tree_id','lft']



That's it. Note we've added the submit_date insertion for ordering.





Next we need to provide an amended form that will contain this `parent` field, so it can be correctly set and saved to the database. So create a new file called forms.py and enter the following:



    :::python

    from django import forms

    from django.contrib.admin import widgets        

    from django.contrib.comments.forms import CommentForm                            

    from models import MPTTComment



    class MPTTCommentForm(CommentForm):

        parent = forms.ModelChoiceField(queryset=MPTTComment.objects.all(), required=False, widget=forms.HiddenInput)



        def get_comment_model(self):

            # Use our custom comment model instead of the built-in one.

            return MPTTComment



        def get_comment_create_data(self):

            # Use the data of the superclass, and add in the parent field field

            data = super(MPTTCommentForm, self).get_comment_create_data()

            data['parent'] = self.cleaned_data['parent']

            return data





Django comments extensions work on a simple principle: you tell the comments app about what you've changed through the use of some simple hooks. Django then uses these hooks to lookup your altered models and forms and overrides the default set. So now that we've created our modified forms and models, we need to point Django at them.



To create these hooks you'll need to edit the `__init__.py` file, so open it now. Enter the following:



    :::python

    from models import MPTTComment

    from forms import MPTTCommentForm



    def get_model():

        return MPTTComment



    def get_form():

        return MPTTCommentForm


>For more information on what is going on here have a look at [the Django documentation for customizing comments](https://docs.djangoproject.com/en/dev/ref/contrib/comments/custom/).


Now create a template for handling the comments. It is useful to have this as a separate include file, e.g. called `_comments.html` that you can then call into another template. The example here expects the comment to be attached to an object called `object` so you may need to wrap the include `{% with <yourmodel> as object %}{% include "_comments.html" %}{% endwith %}`.



    {% load comments %}

    {% load mptt_tags %}



    {% get_comment_list for object as comments %}



    {% if comments %}

    {% recursetree comments %}

                <a name="c{{ node.id }}"></a>

                {{ node.comment }}

                {{ node.user }}

                {{ node.submit_date|timesince }} ago

                <a href="{{ object.get_absolute_url }}#c{{ node.id }}">#</a>

            {% render_comment_form for object %}



        {# recursion! children of a given comment #}

        {% if not node.is_leaf_node %}

            {{ children }}

        {% endif %}

    {% endrecursetree %}

    {% endif %}



    {% render_comment_form for object %}



Finally, you'll need to amend your comment form to include the `parent_id` when posting a reply to another comment. So open the template in `comments/form.html` and enter:



    {% load comments i18n %}

    <form action="{% comment_form_target %}" method="post">{% csrf_token %}

        {{ form.object_pk }}

        {{ form.content_type }}

        {{ form.timestamp }}

        {{ form.security_hash }}

        {% if node.id %}    

            <input type="hidden" name="parent" id="parent_id" value="{{ node.id }}" />

        {% endif %}

        {{ form.comment }}

        <input type="submit">

    </form>



The key point is the inclusion of the parent field.


>If you haven't already you can copy the default Django template from the contrib folder into your own templates folder to allow you to edit it.


Fire it up! Have a test replying to comments both at the page, and threaded level. It should all work perfectly, but if not feel free to ask for help in our - threaded! - comments.







