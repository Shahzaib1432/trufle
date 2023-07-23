from sys import argv, exit as _exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEvent, Qt
from typing import Union
from pyautogui import size
from pathlib import Path
from os import path

class Window:
    _app = QApplication(argv)

    def __init__(self, title='Trufle', width=600, height=400,x=300,y='center', background='#1e1e1e',
                 title_bar=True, topmost=False, direct=False, opacity=1,
                 transparent=False, bottom_most=False, always_on_focus=False):
        self._w = QMainWindow()
        self._w.hide()
        if x == 'center': x = (size()[0]//2) - (width//2)
        if y == 'center': y = (size()[1]//2) - (height//2)

        self._w.setWindowTitle(title)
        self._w.setWindowIcon(QIcon(f'{path.dirname(path.abspath(__file__))}/Assets or Icons/window.png'))
        self._w.setStyleSheet(f"background-color: {background};")
        self._w.setGeometry(x,y, width, height)
        self._mode = 'not max'
        self._hasTitleBar = True

        # Set Attributes
        self.attributes('title bar', title_bar)
        self.attributes('topmost', topmost)
        self.attributes('direct', direct)
        self.attributes('opacity', opacity)
        self.attributes('transparent', transparent)
        self.attributes('bottom most', bottom_most)
        self.attributes('always on focus', always_on_focus)

    def set_window_pos(self, x1, y1, x2, y2):
        self.size(x1 - x2,y2 - y1,x1,y1)

    def decrease_relative_x(self, relx):
        newX = self._w.x() - relx
        self._w.setGeometry(self._w.width(), self._w.height(), newX, self._w.y() )

    def decrease_relative_y(self, rely):
        newY = self._w.y() - rely
        self._w.setGeometry(self._w.width(), self._w.height(), self._w.x(), newY )

    def run(self, start_func=lambda:..., full_screen=False):
        start_func()
        self.event_run()
        if full_screen: self._w.showMaximized(); self._mode = 'max'
        else: self._w.show()
        self._app.exec_()
        self.event_close()


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

    def icon(self, icon_path: Union[str, Path]):
        self._w.setWindowIcon(QIcon(icon_path))

    def info_width(self):  return self._w.width()
    def info_height(self): return self._w.height()
    def info_title(self):  return self._w.windowTitle()
    def info_x(self):      return self._w.x()
    def info_y(self):      return self._w.y()
    def info_icon(self):   return self._w.windowIcon()
    def info(self, attribute_name):
        dict = {'width':  self._w.width(),
                'height': self._w.height(),
                'title':  self._w.windowTitle(),
                'x':      self._w.x(),
                'y':      self._w.y(),
                'icon':   self._w.windowIcon()}
        return dict.get(attribute_name)

    def attributes(self, attribute_name: str, value: any):
        match attribute_name:
            case 'title bar':
                if value is False: self._w.setWindowFlags(self._w.windowFlags() | Qt.FramelessWindowHint); self._hasTitleBar = False
                if value is True:  self._w.setWindowFlags(self._w.windowFlags() & ~Qt.FramelessWindowHint)
            case 'topmost':
                if value is True:  self._w.setWindowFlags(self._w.windowFlags() | Qt.WindowStaysOnTopHint)
                if value is False: self._w.setWindowFlags(self._w.windowFlags() & ~Qt.WindowStaysOnTopHint)
            case 'direct':
                if value is True: self._w.setWindowFlags(self._w.windowFlags() | Qt.WA_TranslucentBackground)
                """ This cannot be set to false. """
            case 'bottom most':
                if value is True:  self._w.setWindowFlags(self._w.windowFlags() | Qt.WindowStaysOnBottomHint)
                if value is False: self._w.setWindowFlags(self._w.windowFlags() & ~Qt.WindowStaysOnBottomHint)
            case 'opacity':
                self._w.setWindowOpacity(value)
            case 'transparent':
                if value is True:
                    self._w.setAttribute(Qt.WA_TranslucentBackground, value)
                    self._w.setWindowFlags(self._w.windowFlags() | Qt.FramelessWindowHint | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)
                if value is False:
                    self._w.setAttribute(Qt.WA_TranslucentBackground, value)
                    if self._hasTitleBar == True: self._w.setWindowFlags(self._w.windowFlags() & ~Qt.FramelessWindowHint)
            case 'always on focus':
                if value is True:  self._w.hideEvent = self._focus
                if value is False: self._w.hideEvent = self._dummyFocus

    def _dummyFocus(self, event): pass

    def _focus(self, event):
        if event.spontaneous():
            self._w.showNormal()

    def setFocus(self):
        self._w.show()

    def maximize(self, is_maximized):
        if is_maximized:
            self._w.showMaximized()
        else: self._w.showNormal()

    def minimize(self):
        self._w.showMinimized()

    def toggle_fullscreen(self):
        if self._mode == 'max':
            self._w.showFullScreen()
            self._mode = 'not max'
        else:
            self._w.showNormal()
            self._mode = 'max'

    def event_run(self):...
    def event_close(self):...

    def _getM(self):
        """ Info: Internal Function """
        """ This is a required method when making custom windows """
        """ This simply returns the parent where a widget is placed. """
        return self._w
