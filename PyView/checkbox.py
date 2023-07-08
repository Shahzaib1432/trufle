from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QFont
from functools import lru_cache
from .memhand import getMaxMemory

mem = getMaxMemory()

"""
Warning, Due to the checkboxes of pyqt5 
not being customizable, 
i did not make a working widget. 
Therefore just dont use this. 
"""

class CheckBox: # just dont use this, its very bad. like VERY bad.
    def __init__(self,
                 master,
                 text            = 'CheckBox',
                 text_color      = '#FFFFFF',
                 # check_box_color = '#1A37F3',
                 # width           = 10,
                 # height          = 10,
                 border_width    = 0,
                 border_color    = '#000000',
                 # corner_radius   = 10,
                 font            = 'Century Gothic',
                 font_size       = 10,
                 state           = 'enabled',
                 command         = lambda: ...):
        self.cb = QCheckBox(text, master.w)  # Create an instance of QCheckBox

        # StyleSheet
        self.mainStyleSheet = f"""
            QCheckBox {{
                background-color: transparent;
                color: {text_color};
                border: {border_width}px solid {border_color};
            }}
            """

        # params:
        self.attributes_text            = text
        self.attributes_text_color      = text_color
        self.attributes_check_box_color = check_box_color
        self.attributes_width           = width
        self.attributes_height          = height
        self.attributes_border_width    = border_width
        self.attributes_border_color    = border_color
        self.attributes_corner_radius   = corner_radius
        self.attributes_font            = font
        self.attributes_font_size       = font_size
        self.attributes_state           = state
        self.attributes_command         = command

        # /StyleSheet
        self.cb.setText(text)
        self.cb.setStyleSheet(self.mainStyleSheet)

        if state == 'enabled': self.cb.setEnabled(True)
        elif state == 'disabled': self.cb.setEnabled(False)

        self.cb.clicked.connect(command)  # Connect clicked signal to function
        self.cb.setFont(QFont(font, font_size))

        self.cb.hide()

    def place(self, x, y):
        self.cb.move(x, y)
        self.cb.show()

    @lru_cache(mem)
    def configure(self,
                  text         = self.attributes_text          ,
                  text_color   = self.attributes_text_color    ,
                  button_color = self.attributes_button_color  ,
                  hover_color  = self.attributes_hover_color   ,
                  width        = self.attributes_width         ,
                  height       = self.attributes_height        ,
                  border_width = self.attributes_border_width  ,
                  border_color = self.attributes_border_color  ,
                  corner_radius= self.attributes_corner_radius ,
                  font         = self.attributes_font          ,
                  font_size    = self.attributes_font_size     ,
                  state        = self.attributes_state         ,
                  command      = self.attributes_command       ):
        self.cb.setText(newText)
        self.attributes_text_color    = text_color
        self.attributes_button_color  = button_color
        self.attributes_hover_color   = hover_color
        self.cb.setFixedWidth(newWidth)
        self.cb.setFixedHeight(newHeight)
        self.attributes_border_width  = newWidth
        self.attributes_border_color  = newColor
        self.attributes_corner_radius = newCornerRadius
        self.cb.setFont(QFont(newFont, self.attributes_font_size))
        self.cb.setFont(QFont(self.attributes_font, newFontSize))
        self.cb.setEnabled(True) if newState == 'enabled' else self.cb.setEnabled(False)
        self.cb.clicked.disconnect(); self.cb.clicked.connect(newCommand)
        self.reload_stylesheet()

    @lru_cache(mem)
    def reload(self):
        self.cb.setText(self.attributes_text)
        self.mainStyleSheet = f"""
            QCheckBox {{
                background-color: transparent;
                color: {self.attributes_text_color};
            }}

            QCheckBox::indicator {{
                width: {self.attributes_width}px;
                height: {self.attributes_height}px;
                border-radius: {self.attributes_corner_radius}px; }}
            """

        self.cb.setStyleSheet(self.mainStyleSheet)
        self.cb.setFixedSize(self.attributes_width, self.attributes_height)
        self.cb.setFont(QFont(self.attributes_font, self.attributes_font_size))

        if self.attributes_state == 'enabled':
            self.cb.setEnabled(True)
        elif self.attributes_state == 'disabled':
            self.cb.setEnabled(False)

        self.cb.clicked.disconnect()
        self.cb.clicked.connect(self.attributes_command)

    @lru_cache(mem)
    def reload_stylesheet(self):
        self.mainStyleSheet = f"""
            QCheckBox {{
                background-color: transparent;
                color: {self.attributes_text_color};
            }}

            QCheckBox::indicator {{
                width: {self.attributes_width}px;
                height: {self.attributes_height}px;
                border-radius: {self.attributes_corner_radius}px; }}
            """

        self.cb.setStyleSheet(self.mainStyleSheet)


    def change_text(self, newText):                  self.cb.setText(newText)
    def change_text_color(self, newColor):           self.attributes_text_color = newColor;           self.reload_stylesheet()
    def change_button_color(self, newColor):         self.attributes_button_color = newColor;         self.reload_stylesheet()
    def change_hover_color(self, newColor):          self.attributes_hover_color = newColor;          self.reload_stylesheet()
    def change_width(self, newWidth):                self.cb.setFixedWidth(newWidth)
    def change_height(self, newHeight):              self.cb.setFixedHeight(newHeight)
    def change_border_width(self, newWidth):         self.attributes_border_width = newWidth;         self.reload_stylesheet()
    def change_border_color(self, newColor):         self.attributes_border_color = newColor;         self.reload_stylesheet()
    def change_corner_radius(self, newCornerRadius): self.attributes_corner_radius = newCornerRadius; self.reload_stylesheet()
    def change_font(self, newFont):                  self.cb.setFont(QFont(newFont, self.attributes_font_size))
    def change_font_size(self, newFontSize):         self.cb.setFont(QFont(self.attributes_font, newFontSize))
    def change_state(self, newState):                self.cb.setEnabled(True) if newState == 'enabled' else self.cb.setEnabled(False)
    def change_command(self, newCommand):            self.cb.clicked.disconnect(); self.cb.clicked.connect(newCommand)
