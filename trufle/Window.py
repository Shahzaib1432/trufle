from sys import argv, exit as _exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEvent
from typing import Union
from pathlib import Path
from os import path

class Window:
    _app = QApplication(argv)

    def __init__(self, title='Trufle', width=600, height=400,x=100,y=100, background='#1e1e1e'):
        self._w = QMainWindow()
        self._w.hide()
        self._w.setWindowTitle(title)
        self._w.setWindowIcon(QIcon(f'{path.dirname(path.abspath(__file__))}/Assets or Icons/window.png'))
        self._w.setStyleSheet(f"background-color: {background};")
        self._w.setGeometry(x,y, width, height)

    def run(self):
        self._w.show()
        self._app.exec_()

    def close(self):
        self._w.close()

    def title(self, winTitle):
        self._w.setWindowTitle(winTitle)

    def geometry(self, geometry):
        width = int(geometry.split('x')[0])
        height = int(geometry.split('x')[1].split('+')[0])
        try:
            x = int(geometry.split('+')[1])
            y = int(geometry.split('+')[2])
            self._w.setGeometry(x, y, width, height)
        except:
            self._w.setGeometry(100, 100, width, height)

    def size(self, width, height, x = 100, y = 100):
        self._w.setGeometry(x, y, width, height)

    def bind(self, binding: str, command):
        pass

    def icon(self, icon_path: Union[str, Path]):
        self._w.setWindowIcon(QIcon(icon_path))