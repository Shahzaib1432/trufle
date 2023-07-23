from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Label:
    def __init__(self,
                master,
                x = None,
                y = None,
                width=100,
                height=50,
                text         ='PyView Label',
                text_color   ='#FFFFFF',
                outside_color='transparent',
                font         ='Century Gothic',
                font_size    =10):
        self.l = QLabel(text, master._getM() )  # Create an instance of QLabel

        # StyleSheet
        self.mainStyleSheet = f"""
            QLabel {{
                background-color: {outside_color};
                color: {text_color};
                border: 0px solid transparent;
            }}
            """
        self.l.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # params:
        self.l.setFixedSize(width, height)

        self.attributes_master = master
        self.attributes_text = text
        self.attributes_text_color = text_color
        self.attributes_outside_color = outside_color
        self.attributes_font = font
        self.attributes_font_size = font_size
        self.attributes_width = width
        self.attributes_height = height
        # /StyleSheet
        self.l.setStyleSheet(self.mainStyleSheet)

        self.l.setFont(QFont(font, font_size))
        self.l.hide()

        if (x,y) != (None,None): self.place(x,y)

    def place(self, x, y):
        self.l.move(x, y)
        self.l.show()

    def configure(self,
                text         = None,
                text_color   = None,
                outside_color= None,
                width        = None,
                height       = None,
                font         = None,
                font_size    = None):

            if width is not None:         self.attributes_width         = width
            if height is not None:        self.attributes_height        = height
            if text is not None:          self.attributes_text          = text
            if text_color is not None:    self.attributes_text_color    = text_color
            if outside_color is not None: self.attributes_outside_color = outside_color
            if width is not None:         self.attributes_hover_color   = width
            if height is not None:        self.attributes_width         = height
            if font is not None:          self.attributes_font          = font
            if font_size is not None:     self.attributes_border_width  = font_size
            self.reload()

    def reload(self):
        self.l.setFixedSize(self.attributes_width, self.attributes_height)
        self.l.setText(self.attributes_text)
        self.mainStyleSheet = f""" background-color: {self.attributes_outside_color};
                                   color: {self.attributes_text_color};
                                   border: 0px solid transparent; """

        self.l.setStyleSheet(self.mainStyleSheet)
        self.l.setFont(QFont(self.attributes_font, self.attributes_font_size))

    def connect(self,
                hover = None, leave_hover = None,
                pressed = None, leave_pressed = None):
        if hover         is not None: self.l.enterEvent        = hover
        if leave_hover   is not None: self.l.leaveEvent        = leave_hover
        if pressed       is not None: self.l.mousePressEvent   = pressed
        if leave_pressed is not None: self.l.mouseReleaseEvent = leave_pressed

    def _setTextColor(self, newCol): self.configure(text_color=newCol)