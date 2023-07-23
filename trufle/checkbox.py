from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont

class CheckBox:
    def __init__(self,
                 master,

                 button_width=30,
                 button_height=30,
                 button_symbol_size=10,
                 button_symbol_color='#FFFFFF',
                 button_color='#0000FF',
                 button_hover_color='#0000EE',
                 button_border_width=0,
                 button_border_color='#000000',
                 button_border_hover_color='#000000',
                 button_corner_radius=5,

                 label_text='PyView CheckBox',
                 label_text_color='#FFFFFF',
                 label_font='Century Gothic',
                 label_font_size=10,
                 label_width=100,
                 label_height=30,
                 label_outside_color='transparent',

                 padding=10,
                 trials=1,

                 on_value='on',
                 unknown_value='unknown',
                 off_value='off'):

        self.value_dict = {'✘':self.attributes_off_value,
                      '': self.attributes_off_value,
                      '■':self.attributes_unknown_value,
                      '✓':self.attributes_on_value}


        self._attributes_trials_dict = {1: ['','✓'], 2: ['✘','✓'], 3: ['■','✘','✓'],
                                   4: ['', '✘', '✓'], 5:['✘','','✓'], 6:['','■', '✘','✓'],
                                   7:['✓', '■']}

        self._attributes_button_text = self._attributes_trials_dict.get(trials)[0]

        self._btn = QPushButton(self._attributes_button_text, master._w)
        self._btn.setFixedSize(button_width, button_height)
        self._btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {button_color};
                color: {button_symbol_color};
                
                border-radius: {button_corner_radius};
                border: {button_border_width}px solid {button_border_color};
            }}

            QPushButton:hover {{
                background-color: {button_hover_color};
                border: {button_border_width}px solid {button_border_hover_color};
            }}
            """)
        self._btn.setFont(QFont('Century Gothic', button_symbol_size))
        self._btn.clicked.connect(self._switch)
        self._btn.hide()
        # Attributes
        self.attributes_button_width = button_width
        self.attributes_button_height = button_height
        self.attributes_button_symbol_size = button_symbol_size
        self.attributes_button_symbol_color = button_symbol_color
        self.attributes_button_color = button_color
        self.attributes_button_hover_color = button_hover_color
        self.attributes_button_border_width = button_border_width
        self.attributes_button_border_color = button_border_color
        self.attributes_button_border_hover_color = button_border_hover_color
        self.attributes_button_corner_radius = button_corner_radius

        self.attributes_unknown_value = unknown_value
        self.attributes_off_value = off_value
        self.attributes_on_value = on_value

        self.attributes_label_text = label_text
        self.attributes_label_text_color = label_text_color
        self.attributes_label_font = label_font
        self.attributes_label_font_size = label_font_size
        self.attributes_label_outside_color = label_outside_color
        self.attributes_label_width = label_width
        self.attributes_label_height = label_height

        self.attributes_padding = padding
        self.attributes_trials = trials
        # /End Attributes

        self._lbl = QLabel(label_text, master._w)
        self._lbl.setStyleSheet(f"""
            QLabel {{
                background-color: {label_outside_color};
                color: {label_text_color};
            }} """)
        self._lbl.setFixedSize(label_width, label_height)
        self._lbl.setFont(QFont(label_font, label_font_size))

    def place(self, x, y):
        self._btn.move(x, y)
        self._lbl.move(x+self.attributes_button_width + self.attributes_padding, y)
        self._btn.show()
        self._lbl.show()

    def reload(self):
        self._lbl.setFixedSize(self.attributes_label_width, self.attributes_label_height)
        self._attributes_trials_dict = {1: ['', '✓'], 2: ['✘', '✓'], 3: ['■', '✘', '✓'],
                                   4: ['', '✘', '✓'], 5: ['✘', '', '✓'], 6: ['', '■', '✘', '✓'],
                                   7: ['✓', '■']}.get(self.attributes_trials)
        self._attributes_button_text = self._attributes_trials[0]

        self._btn.setText(self._attributes_button_text)
        self._btn.setFixedSize(self._attributes_button_width, self._attributes_button_height)
        self._btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self._attributes_button_color};
                color: {self._attributes_button_symbol_color};

                border-radius: {self._attributes_button_corner_radius};
                border: {self._attributes_button_border_width}px solid {self._attributes_button_border_color};
            }}

            QPushButton:hover {{
                background-color: {self._attributes_button_hover_color};
                border: {self._attributes_button_border_width}px solid {self._attributes_button_border_hover_color};
            }}
            """)
        self._btn.setFont(QFont('Century Gothic', self._attributes_button_symbol_size))
        self._btn.clicked.connect(self._switch)
        self._btn.hide()

        # Attributes
        self.attributes_padding = padding
        self.attributes_button_width = button_width
        self.attributes_button_height = button_height
        # /End Attributes

        self._lbl.setText(self._attributes_label_text)
        self._lbl.setStyleSheet(f"""
            QLabel {{
                background-color: {self._attributes_label_outside_color};
                color: {self._attributes_label_text_color};
            }} """)

        self._lbl.setFont(QFont(self._attributes_label_font, self._attributes_label_font_size))

    def configure(self,
                 button_width              = None,
                 button_height             = None,
                 button_symbol_size        = None,
                 button_symbol_color       = None,
                 button_color              = None,
                 button_hover_color        = None,
                 button_border_width       = None,
                 button_border_color       = None,
                 button_border_hover_color = None,
                 button_corner_radius      = None,
                 label_text                = None,
                 label_text_color          = None,
                 label_font                = None,
                 label_font_size           = None,
                 label_outside_color       = None,
                 label_width               = None,
                 label_height              = None,
                 padding                   = None,
                 trials                    = None,
                 on_value                  = None,
                 off_value                 = None,
                 unknown_value             = None):

        if button_width is not None:              self.attributes_button_width              = button_width
        if button_height is not None:             self.attributes_button_height             = button_height
        if button_symbol_size is not None:        self.attributes_button_symbol_size        = button_symbol_size
        if button_symbol_color is not None:       self.attributes_button_symbol_color       = button_symbol_color
        if button_color is not None:              self.attributes_button_color              = button_color
        if button_hover_color is not None:        self.attributes_button_hover_color        = button_hover_color
        if button_border_width is not None:       self.attributes_button_border_width       = button_border_width
        if button_border_color is not None:       self.attributes_button_border_color       = button_border_color
        if button_border_hover_color is not None: self.attributes_button_border_hover_color = button_border_hover_color
        if button_corner_radius is not None:      self.attributes_button_corner_radius      = button_corner_radius
        if label_text is not None:                self.attributes_label_text                = label_text
        if label_text_color is not None:          self.attributes_label_text_color          = label_text_color
        if label_font is not None:                self.attributes_label_font                = label_font
        if label_font_size is not None:           self.attributes_label_font_size           = label_font_size
        if label_outside_color is not None:       self.attributes_label_outside_color       = label_outside_color
        if label_width is not None:               self.attributes_label_width               = label_width
        if label_height is not None:              self.attributes_label_height              = label_height
        if padding is not None:                   self.attributes_padding                   = padding
        if trials is not None:                    self.attributes_trials                    = trials
        if on_value is not None:                  self.attributes_on_value                  = on_value
        if off_value is not None:                 self.attributes_off_value                 = off_value
        if unknown_value is not None:             self.attributes_unknown_value             = unknown_value
        self.reload()

    def get_value(self):
        return self.value_dict.get( self._attributes_button_text )

    def _switch(self):
        self._attributes_button_text = self._var_switch(self._attributes_button_text, self._attributes_trials_dict.get(self.attributes_trials))
        self._btn.setText(self._attributes_button_text)

    def _var_switch(self, val: any, lst: list):
        try:    return lst[ lst.index(val) + 1]
        except: return lst[0]