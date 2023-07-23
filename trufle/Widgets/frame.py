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
                 border_color='white'):

        corner_radius = self._bwCheck(corner_radius)

        self.attributes_width = width
        self.attributes_height = height
        self.attributes_frame_color = frame_color
        self.attributes_corner_radius = corner_radius
        self.attributes_border_width = border_width
        self.attributes_border_color = border_color

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

    def hide(self):
        self._w.hide()
    def show(self):
        self._w.show()

    # Allow widgets to be placed inside frame
    def _getM(self):
        return self._w