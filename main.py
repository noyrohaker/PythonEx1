# This is a sample Python script.
import random
import sys
from turtle import textinput

from PySide6.Qt3DInput import Qt3DInput
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit)
from TikTokApi import TikTokApi

TikTokApi = TikTokApi()

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
            self.instaInput = QPlainTextEdit()
            self.instaButton = QPushButton("Get the posts from Instagram")
            self.facebookInput = QPlainTextEdit()
            self.facebookButton = QPushButton("Get the posts from facebook")

            self.layout = QVBoxLayout(self)
            self.layout.addWidget(self.instaInput)
            self.layout.addWidget(self.instaButton)
            self.layout.addWidget(self.facebookInput)
            self.layout.addWidget(self.facebookButton)

            # Connecting the signal
            self.facebookButton.clicked.connect(self.showText)
            self.instaButton.clicked.connect(self.instalootuser)

        @Slot()
        def showText(self):
            print(self.facebookInput.toPlainText())

        @Slot()
        def instalootuser(self):
            user_videos = TikTokApi.byUsername(self.instaInput.toPlainText(), 10)
            print(user_videos)


    if __name__ == "__main__":
        app = QApplication(sys.argv)

        widget = MyWidget()
        widget.show()

        sys.exit(app.exec())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
