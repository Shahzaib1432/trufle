import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt5.QtGui import QColor

class Frame:
    def __init__(self,
                 master,
                 width=300,
                 height=300,
                 frame_color='#2D2D2D',
                 corner_radius=5,
                 border_width=2,
                 border_color='white',
                 x=None,y=None):

        corner_radius = self._bwCheck(corner_radius)

        self.attributes_master        = master
        self.attributes_width         = width
        self.attributes_height        = height
        self.attributes_frame_color   = frame_color
        self.attributes_corner_radius = corner_radius
        self.attributes_border_width  = border_width
        self.attributes_border_color  = border_color

        self._w = QFrame(master._getM() )
        self._w.setFixedSize(width,height)
        self._w.setStyleSheet(f'''
            QFrame {{
                background-color: {frame_color};
                border: {border_width}px solid {border_color};
                
                border-top-left-radius: {corner_radius[0]};
                border-top-right-radius: {corner_radius[1]};
                border-bottom-left-radius: {corner_radius[2]};
                border-bottom-right-radius: {corner_radius[3]};
            }} ''')

        self._w.hide()
        if (x,y) != (None,None): self.place(x,y)

    def _bwCheck(self, bw):
        if type(bw) == int:
            bw = [bw,bw,bw,bw]
        return bw

    def place(self, x,y):
        self._w.move(x,y)
        self._w.show()

    def reload(self):
        self.attributes_corner_radius = self._bwCheck(self.attributes_corner_radius)

        self._w.setFixedSize(self.attributes_width, self.attributes_height)
        self._w.setStyleSheet(f'''
            QFrame {{
                background-color: {self.attributes_frame_color};
                border: {self.attributes_border_width}px solid {self.attributes_border_color};
                
                border-top-left-radius:     {self.attributes_corner_radius[0]};
                border-top-right-radius:    {self.attributes_corner_radius[1]};
                border-bottom-left-radius:  {self.attributes_corner_radius[2]};
                border-bottom-right-radius: {self.attributes_corner_radius[3]}; }} ''')

    def setSize(self, width, height):
        self._w.setFixedSize(width,height)

    def configure(self,
                 width=None,
                 height=None,
                 frame_color=None,
                 corner_radius=None,
                 border_width=None,
                 border_color=None):
        if width is not None:         self.attributes_width  = width
        if height is not None:        self.attributes_height = height
        if frame_color is not None:   self.attributes_frame_color = frame_color
        if corner_radius is not None: self.attributes_corner_radius = corner_radius
        if border_width is not None:  self.attributes_border_width = border_width
        if border_color is not None:  self.attributes_border_color = border_color
        self.reload()

    def get(self, attribute_name):
        attributes = {'width': self.attributes_width,
                      'height': self.attributes_height,
                      'frame_color': self.attributes_frame_color,
                      'corner_radius': self.attributes_corner_radius,
                      'border_width': self.attributes_border_width,
                      'border_color': self.attributes_border_color}
        return attributes.get(attribute_name)

    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'width':         self.attributes_width         = new_value
            case 'height':        self.attributes_height        = new_value
            case 'frame_color':   self.attributes_frame_color   = new_value
            case 'border_color':  self.attributes_border_color  = new_value
            case 'border_width':  self.attributes_border_width  = new_value
            case 'corner_radius': self.attributes_corner_radius = new_value
            case 'x':             self.place(new_value, self.info_y())
            case 'y':             self.place(self.info_x(), new_value)
        self.reload()

    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self._w.enterEvent         = hover
        if leave_hover   is not None:  self._w.leaveEvent         = leave_hover
        if pressed       is not None:  self._w.mousePressEvent    = pressed
        if leave_pressed is not None:  self._w.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self._w.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self._w.wheelEvent         = scroll

    def info_x(self): return self._w.x()
    def info_y(self): return self._w.y()

    def hide(self):
        self._w.hide()
    def show(self):
        self._w.show()

    # Allow widgets to be placed inside frame
    def _getM(self):
        return self._w