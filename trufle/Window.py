from sys import argv, platform, exit as _exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QColor, QPainter
from PyQt5.QtCore import QEvent, QTimer
from functools import lru_cache
from typing import Union
from pathlib import Path
from .memhand import getMaxMemory

mem = getMaxMemory()

class Window:
    _app = QApplication(argv)

    @lru_cache(mem)
    def __init__(self, background='#1e1e1e'):
        self._w = QMainWindow()
        self._w.hide()
        self._w.setWindowTitle("PyView Window")
        self._w.setWindowIcon(QIcon(r'C:\Users\786\Videos\Trufle\trufle\Assets or Icons\window.png'))
        self._w.setStyleSheet(f"background-color: {background};")
        self._w.setGeometry(100, 100, 600, 400)

    @lru_cache(mem)
    def run(self):
        self._w.show()
        self._app.exec_()

    @lru_cache(mem)
    def title(self, winTitle):
        self._w.setWindowTitle(winTitle)

    @lru_cache(mem)
    def geometry(self, geometry):
        width = int(geometry.split('x')[0])
        height = int(geometry.split('x')[1].split('+')[0])
        try:
            x = int(geometry.split('+')[1])
            y = int(geometry.split('+')[2])
            self._w.setGeometry(x, y, width, height)
        except: self._w.setGeometry(100, 100, width, height)

    @lru_cache(mem)
    def size(self, width, height, x = 100, y = 100):
        self._w.setGeometry(x, y, width, height)

    @lru_cache(mem)
    def bind(self, binding: str, command):
        pass

    def icon(self, icon_path: Union[str, Path]):
        self._w.setWindowIcon(QIcon(icon_path))