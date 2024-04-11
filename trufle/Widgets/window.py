from sys import argv, exit as _exit

import keyboard
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEvent, Qt, QTimer
from typing import Union
from pyautogui import size
from pathlib import Path
from os import path
from winsound import PlaySound

validCursors = {'default': Qt.ArrowCursor,
                # Resizing
                'resize top right': Qt.SizeBDiagCursor,
                'resize bottom left': Qt.SizeBDiagCursor,
                'resize top left': Qt.SizeFDiagCursor,
                'resize bottom right': Qt.SizeFDiagCursor,
                'resize right': Qt.SizeHorCursor,
                'resize left': Qt.SizeHorCursor,
                'resize top': Qt.SizeVerCursor,
                'resize bottom': Qt.SizeVerCursor,
                'resize all': Qt.SizeAllCursor,
                # Utility
                'what': Qt.WhatsThisCursor,
                'up arrow': Qt.UpArrowCursor,
                'plus': Qt.CrossCursor,
                'text': Qt.IBeamCursor,
                'waiting': Qt.WaitCursor,
                'busy': Qt.BusyCursor,
                'forbidden': Qt.ForbiddenCursor,
                'pointing hand': Qt.PointingHandCursor,
                'split vertical': Qt.SplitVCursor,
                'split horizontal': Qt.SplitHCursor,
                'hand': Qt.OpenHandCursor,
                'closed hand': Qt.ClosedHandCursor}

class ListLikeDictionary:
    def __init__(self, *args, **kwargs):
        self.items_list = args
        self.items_dict = kwargs
    def __getattribute__(self, item):
        if isinstance(item, int):
            return self.items_list[item]
        else:
            return self.items_dict[item]

class Window:
    _app = QApplication(argv)

    def __init__(self, title='Trufle', width=600, height=400,x=300,y='center', background='#1e1e1e',
                 title_bar=True, topmost=False, direct=False, opacity=1,
                 transparent=False, bottom_most=False, always_on_focus=False,
                 run_settings=None, # set to none to stop it from running
                 close_on_escape_press=False):
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
        attributes = {'title bar': title_bar, 'topmost': topmost, 'direct': direct, 'opacity': opacity, 'transparent': transparent, 'bottom most': bottom_most, 'always on focus': always_on_focus}
        for attribute_name, value in attributes.items():
            self.attributes(attribute_name, value)

        self._close_on_escape_press = close_on_escape_press

        if run_settings != None: self.run(run_settings['update_func'], run_settings['update_interval'])

    def hide(self): self._w.hide()
    def show(self): self._w.show()
    def reload(self):
        self._w.update()
    def set_window_pos(self, x1, y1, x2, y2):
        self.size(x1 - x2,y2 - y1,x1,y1)
    def decrease_relative_x(self, relx):
        newX = self._w.x() - relx
        self._w.setGeometry(self._w.width(), self._w.height(), newX, self._w.y() )
    def decrease_relative_y(self, rely):
        newY = self._w.y() - rely
        self._w.setGeometry(self._w.width(), self._w.height(), self._w.x(), newY )
    def increase_relative_x(self, relx):
        newX = self._w.x() + relx
        self._w.setGeometry(self._w.width(), self._w.height(), newX, self._w.y() )
    def increase_relative_y(self, rely):
        newY = self._w.y() + rely
        self._w.setGeometry(self._w.width(), self._w.height(), self._w.x(), newY )
    def run(self, update_func=None, update_interval=60, start_func=lambda:..., full_screen=False):
        # Execute events
        start_func()
        self.event_run()

        # Setup updating function
        if update_func is not None:
            timer = QTimer(self._w)
            timer.setInterval(update_interval)
            timer.timeout.connect(update_func)
            timer.start()

        if self._close_on_escape_press:
            timer = QTimer(self._w)
            timer.setInterval(30)
            timer.timeout.connect(self._check_for_close_button_pressed)
            timer.start()

        # Show Window
        if full_screen: self._w.showMaximized(); self._mode = 'max'
        else: self._w.show()
        self._app.exec_()
        self.event_close()

    def _check_for_close_button_pressed(self):
        if keyboard.is_pressed('Escape'):
            self.close()

    def move(self, x,y):
        self._w.move(x,y)
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
    def size(self, width, height, x = None, y = None):
        if x is None: x = self._w.x()
        if y is None: y = self._w.y()
        self._w.setGeometry(x,y, width, height)
    def icon(self, path: Path):
        self._w.setWindowIcon(QIcon(path))
    def _icon_to_pil_image(self, icon):
        pixmap = icon.pixmap(64, 64)
        image = QImage(pixmap.toImage())
        return Image.fromqimage(image)
    # info methods
    def info_width(self):  return self._w.width()
    def info_height(self): return self._w.height()
    def info_title(self):  return self._w.windowTitle()
    def info_x(self):      return self._w.pos().x()
    def info_y(self):      return self._w.pos().y()
    def info_icon(self):   return self._icon_to_pil_image(self._w.windowIcon())
    def info(self, attribute_name):
        dict = {'width':  self._w.width(),
                'height': self._w.height(),
                'title':  self._w.windowTitle(),
                'x':      self._w.x(),
                'y':      self._w.y(),
                'icon':   self._w.windowIcon()}
        return dict.get(attribute_name)
    # info methods with properties
    @property
    def width(self): return self.info_width()
    @property
    def height(self): return self.info_height()
    @property
    def x(self): return self.info_x()
    @property
    def y(self): return self.info_y()
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
    def set_focus(self):
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
    def _delTimer(self, t): del t
    def delayed_invoke(self, wait_time, func):
        timer = QTimer()
        timer.singleShot(wait_time, func)
        timer.timeout.connect(lambda: self._delTimer(timer) )
    def set_cursor(self, cursor_id):
        cursor = validCursors.get(cursor_id)
        assert cursor is not None, f'Invalid cursor "{cursor_id}".'
        self._w.setCursor(cursor)
    def minsize(self, min_width, min_height): self._w.setMinimumSize(min_width, min_height)
    def maxsize(self, max_width, max_height): self._w.setMaximumSize(max_width, max_height)
    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None, pressed_motion = None, scroll = None):
        if hover         is not None:  self._w.enterEvent         = hover
        if leave_hover   is not None:  self._w.leaveEvent         = leave_hover
        if pressed       is not None:  self._w.mousePressEvent    = pressed
        if leave_pressed is not None:  self._w.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self._w.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self._w.wheelEvent         = scroll
    def set_width(self, new_width):   self.size(new_width, self.info_height(), self.info_x(), self.info_y())
    def set_height(self, new_height): self.size(self.info_width(), new_height, self.info_x(), self.info_y())
    def set_x(self, new_x):           self.size(self.info_width(), self.info_height(), new_x, self.info_y())
    def set_y(self, new_y):           self.size(self.info_width(), self.info_height(), self.info_x(), new_y)
    def play_sound(self, path: Path): PlaySound(path)
    def get_screen_dpi(self): return self._app.screens()[0].physicalDotsPerInch()
