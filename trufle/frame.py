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

        self.attributes_width = width
        self.attributes_height = height
        self.attributes_frame_color = frame_color
        self.attributes_corner_radius = corner_radius
        self.attributes_border_width = border_width
        self.attributes_border_color = border_color

        self._w = QFrame(master._w)
        self._w.setFixedSize(width,height)
        self._w.setStyleSheet(f'''
            QFrame {{
                background-color: {frame_color};
                border: {border_width}px solid {border_color};
                border-radius: {corner_radius};
            }} ''')

    def reload(self):
        self._w.setFixedSize(self.attributes_width, self.attributes_height)
        self._w.setStyleSheet(f'''
                    QFrame {{
                        background-color: {self.attributes_frame_color};
                        border: {self.attributes_border_width}px solid {self.attributes_border_color};
                        border-radius: {self.attributes_corner_radius};
                    }} ''')

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