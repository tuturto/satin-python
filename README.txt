satin-python
============

satin-python is simple UI matcher and driver library, built on top of hamcrest and PyQt

Usage
=====

Finding specific widget
-----------------------
To find a specific widget, use function widget:

    sub_widget = widget(dialog,
                        matcher)

Where dialog is Qt object to examine and matcher is hamcrest matcher capable
of detecting specific widget.

Labels
------
To check that a widget has label with text 'Title':

    assert_that(item, has_label('Title'))

Event loop
----------
To start event loop, use @satin_suite class decorator. This will modify your
test class to start QApplication behind the scenes in order to have the event
loop running. When the test method completes, QApplication is automatically
shutdown.

    @satin_suite
    class TestWidget():

       def setup(self):
           ...

       def teardown(self):
           ...

       def test_clicking_around(self):
           ...

License
=======
satin-python is copyrighted by Tuukka Turto and is placed under
GNU General Public License. For more information, please refer to license.txt
found in the main folder.
