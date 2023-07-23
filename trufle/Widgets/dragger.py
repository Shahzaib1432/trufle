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

            self._m._w.move(self.newPos)
            self.event_move()

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

    def hide(self):
        self._l.hide()
    def show(self):
        self._l.show()