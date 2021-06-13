# This is a sample Python script.
import random
import sys
from turtle import textinput

from PySide6.Qt3DInput import Qt3DInput
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget,QPlainTextEdit)


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    class MyWidget(QWidget):
        def __init__(self):
            QWidget.__init__(self)

            self.hello = [
                "Hallo Welt",
                "ה½ ו¥½ן¼ה¸–ח•",
                "Hei maailma",
                "Hola Mundo",
                "׀ׁ€׀¸׀²׀µׁ‚ ׀¼׀¸ׁ€",
            ]

            self.button = QPushButton("Get the posts from Instagram")
            self.input = QPlainTextEdit()

            self.layout = QVBoxLayout(self)
            self.layout.addWidget(self.input)
            self.layout.addWidget(self.button)

            # Connecting the signal
            self.button.clicked.connect(self.magic)

        @Slot()
        def magic(self):
            self.message.text = random.choice(self.hello)


    if __name__ == "__main__":
        app = QApplication(sys.argv)

        widget = MyWidget()
        widget.show()

        sys.exit(app.exec())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
