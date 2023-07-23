from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import QSize
from os import path

p = path.dirname(path.abspath(__file__))
class CheckBox:
    def __init__(self,
                 master,

                 button_width             = 30,
                 button_height            = 30,
                 button_symbol_width      = 14,
                 button_symbol_height     = 14,
                 button_color             = '#3FAD44',
                 button_hover_color       = '#399c3d',
                 button_border_width      = 3,
                 button_border_color      = '#399c3d',
                 button_border_hover_color= '#399c3d',
                 button_corner_radius     = 5,

                 button_on_image=f'{p}/Assets or Icons/tick.png',
                 button_off_image=f'{p}/Assets or Icons/cross.png',
                 button_unknown_image=f'{p}/Assets or Icons/unknown.png',

                 label_text='Trufle CheckBox',
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
        button_corner_radius = self._bwCheck(button_corner_radius)

        self.value_dict = {'✘':off_value,
                      '': off_value,
                      '■':unknown_value,
                      '✓':on_value}

        self.attributes_button_on_image      = button_on_image
        self.attributes_button_off_image     = button_off_image
        self.attributes_button_unknown_image = button_unknown_image

        self._attributes_trials_dict = {1: ['','✓'], 2: ['✘','✓'], 3: ['■','✘','✓'],
                                   4: ['', '✘', '✓'], 5:['✘','','✓'], 6:['','■', '✘','✓'],
                                   7:['✓', '■']}

        self._attributes_button_text = self._attributes_trials_dict.get(trials)[0]

        self._btn = QPushButton('', master._getM())
        self._btn.setIcon(QIcon(self._getImage(self._attributes_button_text)))
        self._btn.setIconSize(QSize(button_symbol_width, button_symbol_height))
        self._btn.setFixedSize(button_width, button_height)
        self._btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {button_color};
                border: {button_border_width}px solid {button_border_color};
                
                border-top-left-radius: {button_corner_radius[0]};
                border-top-right-radius: {button_corner_radius[1]};
                border-bottom-left-radius: {button_corner_radius[2]};
                border-bottom-right-radius: {button_corner_radius[3]}; 
            }}

            QPushButton:hover {{
                background-color: {button_hover_color};
                border: {button_border_width}px solid {button_border_hover_color};
            }}
            """)
        self._btn.clicked.connect(self._switch)
        self._btn.hide()
        # Attributes
        self.attributes_button_width = button_width
        self.attributes_button_height = button_height
        self.attributes_button_symbol_width = button_symbol_width
        self.attributes_button_symbol_height = button_symbol_height
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

        self._lbl = QLabel(label_text, master._getM())
        self._lbl.setStyleSheet(f"""
            QLabel {{
                background-color: {label_outside_color};
                color: {label_text_color};
            }} """)
        self._lbl.setFixedSize(label_width, label_height)
        self._lbl.setFont(QFont(label_font, label_font_size))

    def _bwCheck(self, bw):
        if type(bw) == int:
            bw = [bw,bw,bw,bw]
        return bw

    def place(self, x, y):
        self._btn.move(x, y)
        self._lbl.move(x+self.attributes_button_width + self.attributes_padding, y)
        self._btn.show()
        self._lbl.show()

    def reload(self):
        self.attributes_button_corner_radius = self._bwCheck(self.attributes_button_corner_radius)

        self.attributes_button_off_image     = self._switchImageColor(self.attributes_button_off_image, self.attributes_button_symbol_color)
        self.attributes_button_unknown_image = self._switchImageColor(self.attributes_button_unknown_image, self.attributes_button_symbol_color)
        self.attributes_button_on_image      = self._switchImageColor(self.attributes_button_on_image, self.attributes_button_symbol_color)
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
                border: {self._attributes_button_border_width}px solid {self._attributes_button_border_color};

                border-top-left-radius: {self.attributes_button_corner_radius[0]};
                border-top-right-radius: {self.attributes_button_corner_radius[1]};
                border-bottom-left-radius: {self.attributes_button_corner_radius[2]};
                border-bottom-right-radius: {self.attributes_button_corner_radius[3]}; 
            }}

            QPushButton:hover {{
                background-color: {self._attributes_button_hover_color};
                border: {self._attributes_button_border_width}px solid {self._attributes_button_border_hover_color};
            }}
            """)
        self._btn.setIconSize(QSize(self.attributes_button_symbol_width, self.attributes_button_symbol_height))
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
                 button_symbol_width       = None,
                 button_symbol_height      = None,
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
                 unknown_value             = None,
                 button_on_image           = None,
                 button_off_image          = None,
                 button_unknown_image      = None):

        if button_width is not None:              self.attributes_button_width              = button_width
        if button_height is not None:             self.attributes_button_height             = button_height
        if button_symbol_width is not None:       self.attributes_button_symbol_width       = button_symbol_width
        if button_symbol_height is not None:      self.attributes_button_symbol_height      = button_symbol_height
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
        if button_on_image is not None:           self.attributes_button_on_image = button_on_image
        if button_off_image is not None:          self.attributes_button_off_image = button_off_image
        if button_unknown_image is not None:      self.attributes_button_unknown_image = button_unknown_image
        self.reload()

    def get_value(self):
        return self.value_dict.get( self._attributes_button_text )

    def _switch(self):
        self._attributes_button_text = self._var_switch(self._attributes_button_text,
                                                        self._attributes_trials_dict.get(self.attributes_trials))
        self._btn.setIcon(QIcon(self._getImage(self._attributes_button_text)))

    def _getImage(self, text):
        imagePath = {'✘': self.attributes_button_off_image,
                     '✓': self.attributes_button_on_image,
                     '■': self.attributes_button_unknown_image}.get(text)

        return imagePath

    def _var_switch(self, val: any, lst: list):
        try:    return lst[ lst.index(val) + 1]
        except: return lst[0]

    def _switchImageColor(self, image, new_color_hex, iName):
        new_color_hex = new_color_hex.removeprefix('#')
        image = Image.open(image)
        image = image.convert("RGBA")

        new_color_rgb = tuple(int(new_color_hex[i:i + 2], 16) for i in (0, 2, 4))
        color_image = Image.new("RGBA", image.size, new_color_rgb)
        blended_image = Image.alpha_composite(color_image, image)

        final_image = blended_image.convert("RGB")
        final_image.save(f'{p}/Assets or Icons/{iName}')
        return final_image

    def hide(self):
        self._btn.hide()
        self._lbl.hide()
    def show(self):
        self._btn.show()
        self._lbl.show()