import sys
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QColor, QFont, QKeyEvent

class Entry:
    def __init__(self,
                 master,
                 text          = '',
                 default_text  = '',
                 text_color    = '#000000',
                 entry_color   = '#3FAD44',
                 width         = 130,
                 height        = 30,
                 border_width  = 2,
                 border_color  = '#FFFFFF',
                 corner_radius = 3,
                 font          = 'Calibri',
                 font_size     = 15,
                 state         = 'enabled',
                 x = None,
                 y = None):
        corner_radius = self._bwCheck(corner_radius)

        self.ent = QLineEdit(master._getM() )

        self.mainStyleSheet = f""" 
             color: {text_color};
             background-color: {entry_color};
             border: {border_width}px solid {border_color};
             
             border-top-left-radius: {corner_radius[0]};
             border-top-right-radius: {corner_radius[1]};
             border-bottom-left-radius: {corner_radius[2]};
             border-bottom-right-radius: {corner_radius[3]}; """

        # # params: # #
        self.attributes_master =        master
        self.attributes_text =          text
        self.attributes_default_text =  default_text
        self.attributes_text_color =    text_color
        self.attributes_entry_color =   entry_color
        self.attributes_width =         width
        self.attributes_height =        height
        self.attributes_border_width =  border_width
        self.attributes_border_color =  border_color
        self.attributes_corner_radius = corner_radius
        self.attributes_font =          font
        self.attributes_font_size =     font_size
        self.attributes_state =         state

        # set settings

        self.ent.setFont(QFont(font, font_size))
        self.ent.setEnabled(True) if state == 'enabled' else self.ent.setDisabled(True)
        self.ent.setPlaceholderText(default_text)
        self.ent.setStyleSheet(self.mainStyleSheet)
        self.ent.setFixedSize(width, height)
        self.ent.setText(text)
        self.ent.hide()

        if [x,y] != [None, None]:
            self.place(x, y)

    def info_x(self): return self.ent.x()
    def info_y(self): return self.ent.y()

    def _bwCheck(self, bw):
        if type(bw) == int:
            bw = [bw,bw,bw,bw]
        return bw

    def place(self, x, y):
        self.ent.move(x, y)
        self.ent.show()

    def configure(self,
                  text         = None,
                  default_text = None,
                  text_color   = None,
                  entry_color  = None,
                  width        = None,
                  height       = None,
                  border_width = None,
                  border_color = None,
                  corner_radius= None,
                  font         = None,
                  font_size    = None,
                  state        = None):

        if text is not None:          self.attributes_text          = text
        if default_text is not None:  self.attributes_default_text  = default_text
        if text_color is not None:    self.attributes_text_color    = text_color
        if entry_color is not None:   self.attributes_entry_color   = entry_color
        if width is not None:         self.attributes_width         = width
        if height is not None:        self.attributes_height        = height
        if border_width is not None:  self.attributes_border_width  = border_width
        if border_color is not None:  self.attributes_border_color  = border_color
        if corner_radius is not None: self.attributes_corner_radius = corner_radius
        if font is not None:          self.attributes_font          = font
        if font_size is not None:     self.attributes_font_size     = font_size
        if state is not None:         self.attributes_state         = state
        self.reload()

    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'text':          self.attributes_text = new_value
            case 'default_text':  self.attributes_default_text = new_value
            case 'text_color':    self.attributes_text_color = new_value
            case 'entry_color':   self.attributes_entry_color = new_value
            case 'width':         self.attributes_width = new_value
            case 'height':        self.attributes_height = new_value
            case 'border_width':  self.attributes_border_width = new_value
            case 'border_color':  self.attributes_border_color = new_value
            case 'corner_radius': self.attributes_corner_radius = new_value
            case 'font':          self.attributes_font = new_value
            case 'font_size':     self.attributes_font_size = new_value
            case 'state':         self.attributes_state = new_value
            case 'x':             self.place(new_value, self.info_y())
            case 'y':             self.place(self.info_x(), new_value)
        self.reload()

    def get(self, attribute_name):
        attributes = {'text': self.attributes_text,
                      'default_text': self.attributes_default_text,
                      'text_color': self.attributes_text_color,
                      'entry_color': self.attributes_entry_color,
                      'width': self.attributes_width,
                      'height': self.attributes_height,
                      'border_width': self.attributes_border_width,
                      'border_color': self.attributes_border_color,
                      'corner_radius': self.attributes_corner_radius,
                      'font': self.attributes_font,
                      'font_size': self.attributes_font_size,
                      'state': self.attributes_state}
        return attributes.get(attribute_name)

    def set_text(self, new_text): self.ent.setText(new_text)

    def reload(self, updateText=False):
        self.attributes_corner_radius = self._bwCheck(self.attributes_corner_radius)

        self.mainStyleSheet = f""" 
             color: {self.attributes_text_color};
             background-color: {self.attributes_entry_color};

             border-top-left-radius: {self.attributes_corner_radius[0]};
             border-top-right-radius: {self.attributes_corner_radius[1]};
             border-bottom-left-radius: {self.attributes_corner_radius[2]};
             border-bottom-right-radius: {self.attributes_corner_radius[3]}; """

        self.ent.setStyleSheet(self.mainStyleSheet)

        if self.attributes_state == 'enabled': self.ent.setEnabled(True)
        elif self.attributes_state == 'disabled': self.ent.setEnabled(False)

        self.ent.setFixedSize(self.attributes_width, self.attributes_height)
        self.ent.setFont(QFont(self.attributes_font, self.attributes_font_size))

    def get_text(self): return self.ent.text()
    def hide(self):     self.ent.hide()
    def show(self):     self.ent.show()

    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self.ent.enterEvent         = hover
        if leave_hover   is not None:  self.ent.leaveEvent         = leave_hover
        if pressed       is not None:  self.ent.mousePressEvent    = pressed
        if leave_pressed is not None:  self.ent.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self.ent.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self.ent.wheelEvent         = scroll