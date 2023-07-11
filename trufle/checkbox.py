from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont
from functools import lru_cache
from .memhand import getMaxMemory
from .button import Button
from .label import Label

mem = getMaxMemory()

class CheckBox:
    def __init__(self,
                 master,

                 button_width=90,
                 button_height=30,
                 button_tick_size=10,

                 label_text='PyView CheckBox',

                 padding=10,

                 trials='one'):

        self._attributes_trials = {'one': ['✘','✓'], 'two': ['✕','✔'], 'three': ['■','❌','✔'],
                                       'four': ['', '✕', '✔'], 'five':['✕','','✔'], 'six':['','■', '✕','✔']}.get(trials)
        self._attributes_button_text = self._attributes_trials[0]


        self._btn = Button(master,
                           width=button_width,
                           height=button_height,
                           text=self._attributes_button_text,
                           font_size=button_tick_size,
                           command=self._switch)

        # Attributes
        self.attributes_padding = padding
        self.attributes_button_width = button_width
        self.attributes_button_height = button_height
        # /End Attributes

        self._lbl = Label(master,
                          text=label_text)

    def place(self, x, y):
        self._btn.place(x, y)
        self._lbl.place(x+self.attributes_button_width + self.attributes_padding, y)

    def _switch(self):
        self._attributes_button_text = self._var_switch( self._attributes_button_text, self._attributes_trials )
        self._btn.configure(text=self._attributes_button_text)

    def _var_switch(self, val: any, lst: list):
        index = lst.index(val)
        if index >= len(lst) - 1:
            index = 0
        else:
            index += 1

        return lst[index]