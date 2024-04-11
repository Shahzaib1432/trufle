from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Label:
    def __init__(self,
                master,
                x = None,
                y = None,
                width=400,
                height=50,
                text         ='Trufle Label',
                text_color   ='palegreen',
                outside_color='transparent',
                font         ='Century Gothic',
                font_size    =16,
                _alignment = 'top left'):
        self.l = QLabel(text, master._getM() )  # Create an instance of QLabel

        # StyleSheet
        self.mainStyleSheet = f"""
            QLabel {{
                background-color: {outside_color};
                color: {text_color};
                border: 0px solid transparent;
            }}
            """
        qt_alignments = {'top left': Qt.AlignLeft | Qt.AlignTop, 'center':Qt.AlignCenter}
        self.l.setAlignment(qt_alignments[_alignment])

        # params:
        self.l.setFixedSize(width, height)

        self.attributes_master        = master
        self.attributes_text          = text
        self.attributes_text_color    = text_color
        self.attributes_outside_color = outside_color
        self.attributes_font          = font
        self.attributes_font_size     = font_size
        self.attributes_width         = width
        self.attributes_height        = height
        # /StyleSheet
        self.l.setStyleSheet(self.mainStyleSheet)

        self.l.setFont(QFont(font, font_size))
        self.l.hide()

        if (x,y) != (None,None): self.place(x,y)

    def get(self, attribute_name):
        attributes = {'width':         self.attributes_width,
                      'height':        self.attributes_height,
                      'text':          self.attributes_text,
                      'text_color':    self.attributes_text_color,
                      'outside_color': self.attributes_outside_color,
                      'font':          self.attributes_font,
                      'font_size':     self.attributes_font_size}
        return attributes.get(attribute_name)

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
            if font is not None:          self.attributes_font          = font
            if font_size is not None:     self.attributes_font_size     = font_size
            self.reload()

    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'width':         self.attributes_width         = new_value
            case 'height':        self.attributes_height        = new_value
            case 'text':          self.attributes_text          = new_value
            case 'text_color':    self.attributes_text_color    = new_value
            case 'outside_color': self.attributes_outside_color = new_value
            case 'width':         self.attributes_hover_color   = new_value
            case 'height':        self.attributes_width         = new_value
            case 'font':          self.attributes_font          = new_value
            case 'font_size':     self.attributes_font_size     = new_value
            case 'x':             self.place(new_value, self.l.y())
            case 'y':             self.place(self.l.x(), new_value)
        self.reload()

    def reload(self):
        self.l.setFixedSize(self.attributes_width, self.attributes_height)
        self.l.setText(self.attributes_text)
        self.mainStyleSheet = f""" background-color: {self.attributes_outside_color};
                                   color: {self.attributes_text_color};
                                   border: 0px solid transparent; """

        self.l.setStyleSheet(self.mainStyleSheet)
        self.l.setFont(QFont(self.attributes_font, self.attributes_font_size))

    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self.l.enterEvent         = hover
        if leave_hover   is not None:  self.l.leaveEvent         = leave_hover
        if pressed       is not None:  self.l.mousePressEvent    = pressed
        if leave_pressed is not None:  self.l.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self.l.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self.l.wheelEvent         = scroll

    def info_x(self): return self.l.x()
    def info_y(self): return self.l.y()

    def hide(self):
        self.l.hide()
    def show(self):
        self.l.show()