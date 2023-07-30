import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent

class PositionGrip:
    def __init__(self,
                 master,
                 move: QMainWindow,
                 width=200,
                 height=50,
                 position_grip_color='#FFFFFF',
                 border_width=0,
                 border_color='#000000',
                 corner_radius=0):
        corner_radius = self._bwCheck(corner_radius)

        self.attributes_width               = width
        self.attributes_height              = height
        self.attributes_position_grip_color = position_grip_color
        self.attributes_border_width        = border_width
        self.attributes_border_color        = border_color
        self.attributes_corner_radius       = corner_radius

        self._m = move

        self._l = QLabel('', master._getM() )
        self._l.setStyleSheet(f'''
            QLabel {{
                background-color: {position_grip_color};
                border: {border_width}px solid {border_color};
                
                border-top-left-radius: {corner_radius[0]};
                border-top-right-radius: {corner_radius[1]};
                border-bottom-left-radius: {corner_radius[2]};
                border-bottom-right-radius: {corner_radius[3]};
                
            }}''')
        self._l.move(10,10)
        self._l.setFixedSize(width, height)
        self._l.mouseMoveEvent = self._mouseMoveEvent
        self._l.mousePressEvent = self._mousePressEvent

        self.newPos = self._m._w.pos()

    def event_move(self):pass

    def _bwCheck(self, bw):
        if type(bw) == int:
            bw = [bw,bw,bw,bw]
        return bw

    def place(self, x, y):
        self._l.move(x, y)
        self._l.show()

    def _mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.pos()

    def _mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            delta = event.pos() - self._drag_pos
            self.newPos = self._m._w.pos() + delta
            if self.newPos.x() < 30: self.newPos.setX(30)
            if self.newPos.y() < 30: self.newPos.setY(30)
            self._m._w.move(self.newPos)
            self.event_move()

    def update_xy(self):
        self.newPos = self._m._w.pos()

    def get_xy(self):
        return [self.newPos.x(), self.newPos.y() ]

    def reload(self):
        self.attributes_corner_radius = self._bwCheck(self.attributes_corner_radius)
        self._l.setStyleSheet(f'''
            QLabel {{
                background-color: {self.attributes_position_grip_color};
                border: {self.attributes_border_width}px solid {self.attributes_border_color};
                
                border-top-left-radius: {self.attributes_corner_radius[0]};
                border-top-right-radius: {self.attributes_corner_radius[1]};
                border-bottom-left-radius: {self.attributes_corner_radius[2]};
                border-bottom-right-radius: {self.attributes_corner_radius[3]};
            }} ''')
        self._l.setFixedSize(self.attributes_width, self.attributes_height)

    def configure(self,
                 width               = None,
                 height              = None,
                 position_grip_color = None,
                 border_width        = None,
                 border_color        = None,
                 corner_radius       = None):
        if width is not None:               self.attributes_width               = width
        if height is not None:              self.attributes_height              = height
        if position_grip_color is not None: self.attributes_position_grip_color = position_grip_color
        if border_width is not None:        self.attributes_border_width        = border_width
        if border_color is not None:        self.attributes_border_color        = border_color
        if corner_radius is not None:       self.attributes_corner_radius       = corner_radius
        self.reload()

    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'width':               self.attributes_width               = new_value
            case 'height':              self.attributes_height              = new_value
            case 'position_grip_color': self.attributes_position_grip_color = new_value
            case 'border_width':        self.attributes_border_width        = new_value
            case 'border_color':        self.attributes_border_color        = new_value
            case 'corner_radius':       self.attributes_corner_radius       = new_value
            case 'x':      self.place(new_value, self.info_y())
            case 'y':      self.place(self.info_x(), new_value)
        self.reload()

    def info_x(self): return self._l.x()
    def info_y(self): return self._l.y()

    def hide(self):
        self._l.hide()
    def show(self):
        self._l.show()

    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self._l.enterEvent         = hover
        if leave_hover   is not None:  self._l.leaveEvent         = leave_hover
        if pressed       is not None:  self._l.mousePressEvent    = pressed
        if leave_pressed is not None:  self._l.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self._l.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self._l.wheelEvent         = scroll