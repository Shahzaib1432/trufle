import sys
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QColor, QFont
from functools import lru_cache
from .memhand import getMaxMemory

mem = getMaxMemory()


class Entry:
    @lru_cache(mem)
    def __init__(self,
                 master,
                 text          = '',
                 default_text  = '',
                 text_color    = '#000000',
                 entry_color   = '#1A37F3',
                 width         = 130,
                 height        = 30,
                 border_width  = 1,
                 border_color  = '#FFFFFF',
                 corner_radius = 5,
                 font          = 'Calibri',
                 font_size     = 15,
                 state         = 'enabled',
                 cursor_limit  = 'max'):
        self.ent = QLineEdit(master.w)

        self.mainStyleSheet = f""" 
             color: {text_color};
             background-color: {entry_color};
             border: {border_width}px solid {border_color};
             
             border-radius: {corner_radius}px; """

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

        if self.attributes_cursor_limit == 'max': self.attributes_cursor_limit = len(self.ent.text())

        self.ent.setFont(QFont(font, font_size))
        self.ent.setEnabled(True) if state == 'enabled' else self.ent.setDisabled(True)
        self.ent.setPlaceholderText(default_text)
        self.ent.setStyleSheet(self.mainStyleSheet)
        self.ent.setFixedSize(width, height)
        self.ent.setText(text)
        self.ent.hide()

    @lru_cache(mem)
    def place(self, x, y):
        self.ent.move(x, y)
        self.ent.show()

    @lru_cache(mem)
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


    @lru_cache(mem)
    def reload(self):
        if self.attributes_cursor_limit == 'max': self.attributes_cursor_limit = len(self.ent.text())

        self.ent.setText(self.attributes_text)
        self.mainStyleSheet = f""" 
             color: {self.attributes_text_color};
             background-color: {self.attributes_entry_color};
             border: {self.attributes_border_width}px solid {self.attributes_border_color};
             border-radius: {self.attributes_corner_radius}px; """

        self.ent.setStyleSheet(self.mainStyleSheet)

        if self.attributes_state == 'enabled': self.ent.setEnabled(True)
        elif self.attributes_state == 'disabled': self.ent.setEnabled(False)

        self.ent.setFixedSize(self.attributes_width, self.attributes_height)
        self.ent.setFont(pv_QFont(self.attributes_font, self.attributes_font_size))
        self.ent.keyPressEvent = self._keyPressEvent

    @lru_cache(mem)
    def get_text(self):
        return self.text()

    @lru_cache(mem)
    def reload_cursor_limit(self):
        if self.attributes_cursor_limit == 'max': self.attributes_cursor_limit = len(self.ent.text())

    def _keyPressEvent(self, event):
        self.reload_cursor_limit()
        if (event.key() == Qt.Key_Right) and (self.cursorPosition() == self.attributes_cursor_limit):
            return  # Ignore right key press at the end of the text

        super().keyPressEvent(event)
