from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from functools import lru_cache
from .memhand import getMaxMemory

mem = getMaxMemory()


class Button:
    def __init__(self,
                 master,
                 text='Button',
                 text_color='#FFFFFF',
                 button_color='#1A37F3',
                 hover_color='#0b25cc',
                 width=130,
                 height=40,
                 border_width=0,
                 border_color='#000000',
                 corner_radius=5,
                 font='Century Gothic',
                 font_size=10,
                 state='enabled',
                 command=lambda: ...):

        self.btn = QPushButton(text, master.w)  # Create an instance of QPushButton

        # StyleSheet
        self.mainStyleSheet = f"""
            QPushButton {{
                background-color: {button_color};
                color: {text_color};
                
                border-radius: {corner_radius};
                
                border: {border_width}px solid {border_color};
            }}

            QPushButton:hover{{background-color: {hover_color};}}}}
            """

        # params:
        self.attributes_text = text
        self.attributes_text_color = text_color
        self.attributes_button_color = button_color
        self.attributes_hover_color = hover_color
        self.attributes_width = width
        self.attributes_height = height
        self.attributes_border_width = border_width
        self.attributes_border_color = border_color
        self.attributes_corner_radius = corner_radius
        self.attributes_font = font
        self.attributes_font_size = font_size
        self.attributes_command = command
        self.attributes_state = state

        # /StyleSheet
        self.btn.setFixedSize(width, height)
        self.btn.setStyleSheet(self.mainStyleSheet)

        self.btn.clicked.connect(command)  # Connect clicked signal to function
        self.btn.setFont(QFont(font, font_size))

        self.btn.hide()

    def place(self, x, y):
        self.btn.move(x, y)
        self.btn.show()

    @lru_cache(mem)
    def configure(self,
                  text         = None,
                  text_color   = None,
                  button_color = None,
                  hover_color  = None,
                  width        = None,
                  height       = None,
                  border_width = None,
                  border_color = None,
                  corner_radius= None,
                  font         = None,
                  font_size    = None,
                  state        = None,
                  command      = None):

        if text is not None:          self.attributes_text          = text
        if text_color is not None:    self.attributes_text_color    = text_color
        if button_color is not None:  self.attributes_button_color  = button_color
        if hover_color is not None:   self.attributes_hover_color   = hover_color
        if width is not None:         self.attributes_width         = width
        if height is not None:        self.attributes_height        = height
        if border_width is not None:  self.attributes_border_width  = border_width
        if border_color is not None:  self.attributes_border_color  = border_color
        if corner_radius is not None: self.attributes_corner_radius = corner_radius
        if font is not None:          self.attributes_font          = font
        if font_size is not None:     self.attributes_font_size     = font_size
        if state is not None:         self.attributes_state         = state
        if command is not None:       self.attributes_command       = command
        self.reload()

    @lru_cache(mem)
    def reload(self):
        self.btn.setText(self.attributes_text)
        self.mainStyleSheet = f"""
            QPushButton {{
                background-color: {self.attributes_button_color};
                color: {self.attributes_text_color};
                
                top-left-border-radius: {self.attributes_corner_radius[0]}px;
                top-right-border-radius: {self.attributes_corner_radius[1]}px;
                bottom-left-border-radius: {self.attributes_corner_radius[2]}px;
                bottom-right-border-radius: {self.attributes_corner_radius[3]}px;

                border: {self.attributes_border_width}px solid {self.attributes_border_color};

            QPushButton:hover{{background-color: {self.attributes_hover_color};}}"""

        self.btn.setStyleSheet(self.mainStyleSheet)
        self.btn.setFixedSize(self.attributes_width, self.attributes_height)
        self.btn.setFont(QFont(self.attributes_font, self.attributes_font_size))

        if self.attributes_state == 'enabled':    self.btn.setEnabled(True)
        elif self.attributes_state == 'disabled': self.btn.setEnabled(False)

        self.btn.clicked.disconnect()
        self.btn.clicked.connect(self.attributes_command)

    @lru_cache(mem)
    def reload_stylesheet(self):

        self.mainStyleSheet = f"""
            QPushButton {{
                background-color: {self.attributes_button_color};
                color: {self.attributes_text_color};

                top-left-border-radius: {self.attributes_corner_radius[0]}px;
                top-right-border-radius: {self.attributes_corner_radius[1]}px;
                bottom-left-border-radius: {self.attributes_corner_radius[2]}px;
                bottom-right-border-radius: {self.attributes_corner_radius[3]}px;

                border: {self.attributes_border_width}px solid {self.attributes_border_color};

            QPushButton:hover {{
                background-color: {self.attributes_hover_color}; }}"""

        self.btn.setStyleSheet(self.mainStyleSheet)


    def change_text(self, newText):                  self.btn.setText(newText)
    def change_text_color(self, newColor):           self.attributes_text_color = newColor;           self.reload_stylesheet()
    def change_button_color(self, newColor):         self.attributes_button_color = newColor;         self.reload_stylesheet()
    def change_hover_color(self, newColor):          self.attributes_hover_color = newColor;          self.reload_stylesheet()
    def change_width(self, newWidth):                self.btn.setFixedWidth(newWidth)
    def change_height(self, newHeight):              self.btn.setFixedHeight(newHeight)
    def change_border_width(self, newWidth):         self.attributes_border_width = newWidth;         self.reload_stylesheet()
    def change_border_color(self, newColor):         self.attributes_border_color = newColor;         self.reload_stylesheet()
    def change_corner_radius(self, newCornerRadius): self.attributes_corner_radius = newCornerRadius; self.reload_stylesheet()
    def change_font(self, newFont):                  self.btn.setFont(QFont(newFont, self.attributes_font_size))
    def change_font_size(self, newFontSize):         self.btn.setFont(QFont(self.attributes_font, newFontSize))
    def change_state(self, newState):                self.btn.setEnabled(True) if newState == 'enabled' else self.btn.setEnabled(False)
    def change_command(self, newCommand):            self.btn.clicked.disconnect(); self.btn.clicked.connect(newCommand)
