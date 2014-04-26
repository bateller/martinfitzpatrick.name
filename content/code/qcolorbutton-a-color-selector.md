Date: 2014-04-25 17:00
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: QColorButton: A color-selector tool for PyQt
Slug: qcolorbutton-a-color-selector-tool-for-pyqt
Tags: qt,pyqt,pyside,qcolorbutton,custom widgets,

Below is a short snippet to implement a color-picker attached to a button in Qt. Clicking on the button pops up a dialog (native) to select a color. The color is shown by the color of the button face. A right-click option is included to allow clearing of the color setting (returning the value to None).

![Screenshot](/images/code/qcolor_dialog.png)

The below snippet is written for PyQt5, but changing it to PySide should require no more than altering the pyqtSignal call.

    class QColorButton(QPushButton):
        '''
        Custom Qt Widget to show a chosen color.
    
        Left-clicking the button shows the color-chooser, while
        right-clicking resets the color to None (no-color).    
        '''

        colorChanged = pyqtSignal()

        def __init__(self, *args, **kwargs):
            super(QColorButton, self).__init__(*args, **kwargs)

            self._color = None
            self.setMaximumWidth(32)
            self.pressed.connect(self.onColorPicker)

        def setColor(self, color):
            if color != self._color:
                self._color = color
                self.colorChanged.emit()

            if self._color:
                self.setStyleSheet("background-color: %s;" % self._color)
            else:
                self.setStyleSheet("")

        def color(self):
            return self._color

        def onColorPicker(self):
            '''
            Show color-picker dialog to select color.
            
            Qt will use the native dialog by default.
        
            '''
            dlg = QColorDialog(self)
            if self._color:
                dlg.setCurrentColor(QColor(self._color))

            if dlg.exec_():
                self.setColor(dlg.currentColor().name())

        def mousePressEvent(self, e):
            if e.button() == Qt.RightButton:
                self.setColor(None)

            return super(QColorButton, self).mousePressEvent(e)
