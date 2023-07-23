import sys
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QColor, QFont

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
                 cursor_limit  = 'max',
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
        self.attributes_cursor_limit =  cursor_limit

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
                  state        = None,
                  cursor_limit = None):

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
        if cursor_limit is not None:  self.attributes_cursor_limit  = cursor_limit
        self.reload()

    def reload(self):
        self.attributes_corner_radius = self._bwCheck(self.attributes_corner_radius)

        self.ent.setText(self.attributes_text)
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
        self.ent.setFont(pv_QFont(self.attributes_font, self.attributes_font_size))

    def get_text(self):
        return self.ent.text()

    def hide(self):
        self.ent.hide()
    def show(self):
        self.ent.show()