from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from functools import lru_cache
from .memhand import getMaxMemory

mem = getMaxMemory()


class Label:
    def __init__(self,
                master,
                text         ='PyView Label',
                text_color   ='#FFFFFF',
                outside_color='transparent',
                font         ='Century Gothic',
                font_size    =10):
        self.l = QLabel(text, master.w)  # Create an instance of QLabel

        # StyleSheet
        self.mainStyleSheet = f"""
            QLabel {{
                background-color: {outside_color};
                color: {text_color};
            }}
            """

        # params:
        self.attributes_text = text
        self.attributes_text_color = text_color
        self.attributes_outside_color = outside_color
        self.attributes_font = font
        self.attributes_font_size = font_size

        # /StyleSheet
        self.l.setStyleSheet(self.mainStyleSheet)

        self.l.setFont(QFont(font, font_size))
        self.l.hide()

    @lru_cache(mem)
    def place(self, x, y):
        self.l.move(x, y)
        self.l.show()

    @lru_cache(mem)
    def configure(self,
                text         = None,
                text_color   = None,
                outside_color= None,
                width        = None,
                height       = None,
                font         = None,
                font_size    = None):

            if text is not None:          self.attributes_text         = text
            if text_color is not None:    self.attributes_text_color   = text_color
            if outside_color is not None: self.attributes_button_color = outside_color
            if width is not None:         self.attributes_hover_color  = width
            if height is not None:        self.attributes_width        = height
            if font is not None:          self.attributes_height       = font
            if font_size is not None:     self.attributes_border_width = font_size
            self.reload()

    @lru_cache(mem)
    def reload(self):
        self.l.setText(self.attributes_text)
        self.mainStyleSheet = f""" background-color: {self.attributes_outside_color};
                                  color: {self.attributes_text_color}; """

        self.l.setStyleSheet(self.mainStyleSheet)
        self.l.setFont(QFont(self.attributes_font, self.attributes_font_size))

    @lru_cache(mem)
    def reload_stylesheet(self):
        self.mainStyleSheet = f""" background-color: {self.attributes_outside_color}; 
                                   color: {self.attributes_text_color};"""

        self.l.setStyleSheet(self.mainStyleSheet)

    def change_text(self, newText):           self.l.setText(newText)
    def change_text_color(self, newColor):    self.attributes_text_color    = newColor; self.reload_stylesheet()
    def change_outside_color(self, newColor): self.attributes_outside_color = newColor; self.reload_stylesheet()
    def change_font(self, newFont):           self.l.setFont(QFont(newFont, self.attributes_font_size))
    def change_font_size(self, newFontSize):  self.l.setFont(QFont(self.attributes_font, newFontSize))
