satin-python
============

satin-python is simple UI matcher and driver library, built on top of hamcrest and PyQt

Usage
=====

Finding specific widget
-----------------------
To find a specific widget, use function widget:

    sub_widget = widget(dialog,
                        lambda sub_widget: sub_widget.objectName() == 'Item')

Labels
------
To check that a widget has label with text 'Title':

    assert_that(item, has_label('Title'))

License
=======
satin-python is copyrighted by Tuukka Turto and is placed under
GNU General Public License. For more information, please refer to license.txt
found in the main folder.
