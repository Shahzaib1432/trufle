from sys import argv, platform, exit as _exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QColor, QPainter
from PyQt5.QtCore import QEvent
from functools import lru_cache
from .memhand import getMaxMemory
from threading import Thread

mem = getMaxMemory()

def var_toggle(value: any, lstOfVals: list):
    index = lstOfVals.index(value)
    if index >= len(lstOfVals)-1:
        index = 0
    else:
        index += 1
    return lstOfVals[index]

class Window:
    app = QApplication(argv)

    width  = None
    height = None
    title  = None

    @lru_cache(mem)
    def __init__(self, background='#1e1e1e'):
        self.w = QMainWindow()
        self.w.hide()
        self.w.setWindowTitle("PyView Window")
        self.w.setWindowIcon(QIcon(r'C:\Users\786\Videos\PYVIEW\PyView\Assets or Icons\icon.png'))
        self.w.setStyleSheet(f"background-color: {background};")

    @lru_cache(mem)
    def _RunWE(self):
        self.w.show()
        _exit(self.app.exec_())

    @lru_cache(mem)
    def run(self):

        if self.title is not None:  self.set_title(self.title)
        if self.width is not None:  self.w.setFixedWidth(self.width)
        if self.height is not None: self.w.setFixedHeight(self.height)

        t = Thread(target=self._RunWE)
        t.run()

    @lru_cache(mem)
    def set_title(self, winTitle):
        self.w.setWindowTitle(winTitle)

    @lru_cache(mem)
    def geometry(self, geometry):
        width = int(geometry.split('x')[0])
        height = int(geometry.split('x')[1].split('+')[0])
        try:
            x = int(geometry.split('+')[1])
            y = int(geometry.split('+')[2])
            self.w.setGeometry(x, y, width, height)
        except: self.w.setGeometry(100, 100, width, height)

    @lru_cache(mem)
    def size(self, width, height, x = 100, y = 100):
        self.w.setGeometry(x, y, width, height)

    @lru_cache(mem)
    def bind(self, binding: str, command):
        pass