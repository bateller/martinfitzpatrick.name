Date: 2014-01-13 23:55
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: Transmit extra data with signals in PyQt
Tags: pyqt, pyside, qt

Signals are a neat feature of Qt that allow message-passing between different areas of your program. To use a signal you attach a function to be called in the event of the signal firing, usually accepting a small item of data about the signal state.

However, there is a limitation: the signal can only emit the data it was designed to do. So for example, a `QAction` has a `.triggered` that fires when that particular action has been activated. Unfortunately the receiving connected function only receives one thing: `checked=True` or `False`. In other words, the receiving function has no way of knowing which action triggered it.

This is usually fine. You can tie a particular action to a particular function. However, sometimes you want to trigger multiple actions off the same *type* of action, and treat them differently. Here's a neat trick to do just that.

# Degrees of separation

Instead of binding the target function to the signal, you can instead bind a wrapper function that accepts the original signal, attaches some more data, then passes it on. The code to do this (using a lambda) would be:

    lambda checked: self.onTriggered(obj, checked)
    
Here we take the `checked` signal, add the object it's come from, then pass it onto the handler. All we need to do is set the object correctly when building the connect:

	action = QAction()
    action.triggered.connect( lambda checked: self.onTriggered(action, checked) )

Now the `onTriggered` handler can receive the calling action along with the check state when it's triggered.

# But wait!

Unfortunately things aren't always that simple. If you try and build multiple actions like this by looping over a set of objects you'll get hit by namespace problems. All the lambdas will be evaluated in the state of the loop at the *end* and so clicking any of them will result in the same trigger. The solution is to wrap the lambda function in a creator.

    def make_callback(i):
        return lambda n: self.onAddView(n,i)
    
Here's an example of me doing exactly that to handle outputting a list of QAction labels into a QMenu for the visual editor in [MetaPath](http://getmetapath.org)

    for wid in range( self.app.views.count() ):
        if self.app.views.widget(wid).is_floatable_view:
            def make_callback(i):
                return lambda n: self.onAddView(n,i)

            ve = QAction(self.app.views.tabText(wid), o)
            ve.triggered.connect( make_callback(wid) )
            vmenu.addAction(ve)
