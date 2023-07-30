from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor, QKeySequence
from PyQt5.QtCore import QPropertyAnimation, Qt, QSize
from PIL import Image, ImageQt

class Button:
    def __init__(self,
                 master,
                 text               = 'Button',
                 text_color         = '#FFFFFF',
                 button_color       = '#3FAD44',
                 hover_color        = '#399c3d',
                 pressed_color      = '#328a36',
                 width              = 130,
                 height             = 40,
                 border_width       = 0,
                 border_color       = '#399c3d',
                 border_hover_color = '#399c3d',
                 corner_radius      = 5,
                 font               = 'HoloLens MDL2 Assets',
                 font_size          = 10,
                 state              = 'enabled',
                 image              = None,
                 image_width        = 50,
                 image_height       = 50,
                 command            = lambda: ...,
                 x                  = None,
                 y                  = None,
                 shortcut           = None,
                 text_alignment     = 'center',
                 can_hover          = True):
        corner_radius = self._bwCheck(corner_radius)
        self.btn = QPushButton(text, master._getM() )  # Create an instance of QPushButton
        if shortcut is not None: self.btn.setShortcut(QKeySequence(shortcut))

        # params:
        self.attributes_text_alignment     = text_alignment
        self.attributes_shortcut           = shortcut
        self.attributes_text               = text
        self.attributes_text_color         = text_color
        self.attributes_pressed_color      = pressed_color
        self.attributes_button_color       = button_color
        self.attributes_hover_color        = hover_color
        self.attributes_width              = width
        self.attributes_height             = height
        self.attributes_border_width       = border_width
        self.attributes_border_color       = border_color
        self.attributes_border_hover_color = hover_color
        self.attributes_corner_radius      = corner_radius
        self.attributes_font               = font
        self.attributes_font_size          = font_size
        self.attributes_command            = command
        self.attributes_state              = state
        self.attributes_image              = image
        self.attributes_image_width        = image_width
        self.attributes_image_height       = image_height
        self.attributes_can_hover          = can_hover
        self.attributes_master             = master

        # StyleSheet
        self.mainStyleSheet = f"""
            QPushButton {{
                background-color: {button_color};
                color: {text_color};
                
                text-align: {text_alignment};
                
                {self._getCornerRadius(corner_radius)}
                
                border: {border_width}px solid {border_color};
            }}

            {self._getCanHover(border_hover_color, hover_color, can_hover)}
            
            QPushButton:pressed {{
                background-color: {pressed_color};
            }}
            """

        # /StyleSheet
        if image == '!empty': self.btn.setIcon(QIcon())
        if image is not None:
            self.btn.setIcon(self._pilToQIcon(image) )
            self.btn.setIconSize(QSize(image_width, image_height))

        self.btn.setFixedSize(width, height)
        self.btn.setStyleSheet(self.mainStyleSheet)

        self.btn.clicked.connect(command)  # Connect clicked signal to function
        self.btn.setFont(QFont(font, font_size))

        self.btn.hide()

        if [x, y] != [None, None]:
            self.place(x, y)
    def _getCanHover(self, bh, h, ch):
        if ch:
            return f'''QPushButton:hover {{ background-color: {h}; border: {self.attributes_border_width}px solid {bh}; }}'''
        else: return ''
    def _getCornerRadius(self, cw):
        if type(cw) == list:
            return f'border-top-left-radius: {cw[0]};' \
                   f'border-top-right-radius: {cw[1]}; ' \
                   f'border-bottom-left-radius: {cw[2]}; ' \
                   f'border-bottom-right-radius: {cw[3]};'

        elif cw == 'round':
            return f'border-radius: {self.attributes_width//2};'
    def _bwCheck(self, bw):
        if type(bw) == int:
            bw = [bw,bw,bw,bw]
        return bw
    def _pilToQIcon(self, pilImage):
        image = pilImage.convert("RGBA")
        pixmap = QPixmap.fromImage(ImageQt.ImageQt(image))
        return QIcon(pixmap)
    def place(self, x, y):
        self.btn.move(x, y)
        self.btn.show()
    def config(self, attribute, new_value):
        match attribute:
            case 'shortcut':           self.attributes_shortcut = new_value
            case 'pressed_color':      self.attributes_pressed_color = new_value
            case 'text':               self.attributes_text = new_value
            case 'text_color':         self.attributes_text_color = new_value
            case 'button_color':       self.attributes_button_color = new_value
            case 'hover_color':        self.attributes_hover_color = new_value
            case 'width':              self.attributes_width = new_value
            case 'height':             self.attributes_height = new_value
            case 'border_width':       self.attributes_border_width = new_value
            case 'border_color':       self.attributes_border_color = new_value
            case 'corner_radius':      self.attributes_corner_radius = new_value
            case 'font':               self.attributes_font = new_value
            case 'font_size':          self.attributes_font_size = new_value
            case 'state':              self.attributes_state = new_value
            case 'command':            self.attributes_command = new_value
            case 'image':              self.attributes_image = new_value
            case 'image_width':        self.attributes_image_width = new_value
            case 'image_height':       self.attributes_image_height = new_value
            case 'border_hover_color': self.attributes_border_hover_color = new_value
            case 'text_alignment':     self.attributes_text_alignment = new_value
            case 'x':                  self.place(new_value, self.btn.y())
            case 'y':                  self.place(self.btn.x(), new_value)
        self.reload()
    def get(self, attribute_name):
        attributes = {'shortcut': self.attributes_shortcut,
                      'pressed_color':      self.attributes_pressed_color,
                      'text':               self.attributes_text,
                      'text_color':         self.attributes_text_color,
                      'button_color':       self.attributes_button_color,
                      'hover_color':        self.attributes_hover_color,
                      'width':              self.attributes_width,
                      'height':             self.attributes_height,
                      'border_width':       self.attributes_border_width,
                      'border_color':       self.attributes_border_color,
                      'corner_radius':      self.attributes_corner_radius,
                      'font':               self.attributes_font,
                      'font_size':          self.attributes_font_size,
                      'state':              self.attributes_state,
                      'command':            self.attributes_command,
                      'image':              self.attributes_image,
                      'image_width':        self.attributes_image_width,
                      'image_height':       self.attributes_image_height,
                      'border_hover_color': self.attributes_border_hover_color,
                      'text_alignment':     self.attributes_text_alignment,
                      'x':                  self.btn.x(),
                      'y':                  self.btn.y()}
        return attributes.get(attribute_name)
    def configure(self,
                  can_hover          = None,
                  shortcut           = None,
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
                  image              = None,
                  image_width        = None,
                  image_height       = None,
                  pressed_color      = None,
                  text_alignment     = None):

        if shortcut is not None:           self.attributes_shortcut           = shortcut
        if pressed_color is not None:      self.attributes_pressed_color      = pressed_color
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
        if image_width is not None:        self.attributes_image_width        = image_width
        if image_height is not None:       self.attributes_image_height       = image_height
        if border_hover_color is not None: self.attributes_border_hover_color = border_hover_color
        if text_alignment is not None:     self.attributes_text_alignment     = text_alignment
        if can_hover is not None:          self.attributes_can_hover          = can_hover
        self.reload()
    def reload(self):
        self.attributes_corner_radius = self._bwCheck(self.attributes_corner_radius)
        self.btn.setText(self.attributes_text)

        if self.attributes_shortcut is not None: self.btn.setShortcut(QKeySequence(self.attributes_shortcut))
        else: self.btn.setShortcut(QKeySequence())

        self.mainStyleSheet = f"""
            QPushButton {{
                background-color: {self.attributes_button_color};
                color: {self.attributes_text_color};
                
                {self._getCornerRadius(self.attributes_corner_radius)}
                
                border: {self.attributes_border_width}px solid {self.attributes_border_color};
                text-align: {self.attributes_text_alignment};
            }}

            {self._getCanHover(self.attributes_border_hover_color, self.attributes_hover_color, self.attributes_can_hover)}
            
            QPushButton:pressed {{
                background-color: {self.attributes_pressed_color};
            }}
            """

        self.btn.setStyleSheet(self.mainStyleSheet)
        self.btn.setFixedSize(self.attributes_width, self.attributes_height)
        self.btn.setFont(QFont(self.attributes_font, self.attributes_font_size))

        if self.attributes_state == 'enabled':
            self.btn.setEnabled(True)
        elif self.attributes_state == 'disabled':
            self.btn.setEnabled(False)

        if self.attributes_image == "!empty": self.btn.setIcon(QIcon())
        if self.attributes_image is not None:
            self.btn.setIcon(self._pilToQIcon(self.attributes_image))
            self.btn.setIconSize(QSize(self.attributes_image_width, self.attributes_image_height))

        self.btn.clicked.disconnect()
        self.btn.clicked.connect(self.attributes_command)
    def delete(self):
        self.btn.hide()
        del self.btn
    def hide(self):
        self.btn.hide()
    def show(self):
        self.btn.show()
    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self.btn.enterEvent         = hover
        if leave_hover   is not None:  self.btn.leaveEvent         = leave_hover
        if pressed       is not None:  self.btn.mousePressEvent    = pressed
        if leave_pressed is not None:  self.btn.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self.btn.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self.btn.wheelEvent         = scroll
    def info_x(self): return self.btn.x()
    def info_y(self): return self.btn.y()
