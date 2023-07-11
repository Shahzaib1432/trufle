from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont, QIcon
from .memhand import getMaxMemory

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
                 border_color='#222222',
                 border_hover_color='#000000',
                 corner_radius=5,
                 font='Century Gothic',
                 font_size=10,
                 state='enabled',
                 image=None,
                 command=lambda: ...):

        self.btn = QPushButton(text, master._w)  # Create an instance of QPushButton

        # StyleSheet
        self.mainStyleSheet = f"""
            QPushButton {{
                background-color: {button_color};
                color: {text_color};
                
                border-radius: {corner_radius};
                border: {border_width}px solid {border_color};
            }}

            QPushButton:hover {{
                background-color: {hover_color};
                border: {border_width}px solid {border_hover_color};
            }}
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
        self.attributes_border_hover_color = hover_color
        self.attributes_corner_radius = corner_radius
        self.attributes_font = font
        self.attributes_font_size = font_size
        self.attributes_command = command
        self.attributes_state = state
        self.attributes_image = image

        # /StyleSheet
        if image is not None:
            self.btn.setIcon(QIcon(image) )

        self.btn.setFixedSize(width, height)
        self.btn.setStyleSheet(self.mainStyleSheet)

        self.btn.clicked.connect(command)  # Connect clicked signal to function
        self.btn.setFont(QFont(font, font_size))

        self.btn.hide()

    def place(self, x, y):
        self.btn.move(x, y)
        self.btn.show()

    def configure(self,
                  text               = None,
                  text_color         = None,
                  button_color       = None,
                  hover_color        = None,
                  width              = None,
                  height             = None,
                  border_width       = None,
                  border_color       = None,
                  border_hover_color = None,
                  corner_radius      = None,
                  font               = None,
                  font_size          = None,
                  state              = None,
                  command            = None,
                  image              = None):

        if text is not None:               self.attributes_text               = text
        if text_color is not None:         self.attributes_text_color         = text_color
        if button_color is not None:       self.attributes_button_color       = button_color
        if hover_color is not None:        self.attributes_hover_color        = hover_color
        if width is not None:              self.attributes_width              = width
        if height is not None:             self.attributes_height             = height
        if border_width is not None:       self.attributes_border_width       = border_width
        if border_color is not None:       self.attributes_border_color       = border_color
        if corner_radius is not None:      self.attributes_corner_radius      = corner_radius
        if font is not None:               self.attributes_font               = font
        if font_size is not None:          self.attributes_font_size          = font_size
        if state is not None:              self.attributes_state              = state
        if command is not None:            self.attributes_command            = command
        if image is not None:              self.attributes_image              = image
        if border_hover_color is not None: self.attributes_border_hover_color = border_hover_color
        self.reload()

    def reload(self):
        self.btn.setText(self.attributes_text)
        self.mainStyleSheet = f"""
            QPushButton {{
                background-color: {self.attributes_button_color};
                color: {self.attributes_text_color};
                
                border-radius: {self.attributes_corner_radius};
                border: {self.attributes_border_width}px solid {self.attributes_border_color};
            }}

            QPushButton:hover {{
                background-color: {self.attributes_hover_color};
                border: {self.attributes_border_width}px solid {self.attributes_border_hover_color};
            }}
            """

        self.btn.setStyleSheet(self.mainStyleSheet)
        self.btn.setFixedSize(self.attributes_width, self.attributes_height)
        self.btn.setFont(QFont(self.attributes_font, self.attributes_font_size))

        if self.attributes_state == 'enabled':
            self.btn.setEnabled(True)
        elif self.attributes_state == 'disabled':
            self.btn.setEnabled(False)

        if self.attributes_image is not None:
            self.btn.setIcon(QIcon(self.attributes_image))

        self.btn.clicked.disconnect()
        self.btn.clicked.connect(self.attributes_command)