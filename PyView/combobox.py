from .button import Button
from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtGui import QFont
from .entry import Entry
from threading import Thread

class _combobox_:
    def __init__(self,
                 master,
                 width=100,
                 height=30,

                 entry_corner_radius=5,

                 button_corner_radius=5,
                 button_border_width=0,
                 button_border_color='#000000',
                 button_color='#FF0000',
                 button_indicator_color='#FFFFFF',
                 button_indicator_size=12,
                 button_width='auto',  # 'auto' = Automatic
                 _buttonEntryParts=4,

                 menu_width='auto',  # 'auto' = Automatic
                 menu_height='auto',  # 'auto' = Automatic
                 menu_color='#FFFFFF',

                 items_text_color='blue',
                 items_text_font='Century Gothic',
                 items_text_font_size=10,

                 items_hover_text_color='green',
                 items_hover_color='red',

                 items_press_text_color='green',
                 items_press_color='red',

                 menu_position_x='auto',
                 menu_position_y='auto'):

        if button_width == 'auto':
            self._buttonEntryParts = _buttonEntryParts

            if (width // self._buttonEntryParts) < 30:
                self._buttonEntryParts -= 1

            self.at_btn_width = width // self._buttonEntryParts
        else:
            self.at_btn_width = button_width

        self.at_entry_width = width
        self.at_entry_height = height

        self.menu = QMenu(master.w)

        self.menu.setStyleSheet(f'''
            QMenu {{
                color: {items_text_color};
                background-color: {menu_color};
            }}

            QMenu::item:selected {{ 
                background-color: {items_hover_color}; 
                color: {items_hover_text_color};
            }}

            QMenu::item:pressed {{ 
                background-color: {items_press_color}; 
                color: {items_press_text_color};
            }}
            ''')

        self.open_action = QAction("Open", master.w)
        self.menu.addAction(self.open_action)

        self.menu.setFont(QFont(items_text_font, items_text_font_size))

        self.menu.atwidth = 90
        self.menu.atheight = 80

        if menu_width != 'auto': self.menu.setFixedWidth(menu_width); self.menu.atheight = menu_height
        if menu_height != 'auto': self.menu.setFixedHeight(menu_height); self.menu.atwidth = menu_width

        # 100x80

        self.ent = Entry(master, corner_radius=entry_corner_radius, width=width, height=height)
        self.btn = Button(master,
                          text='▼',
                          text_color=button_indicator_color,
                          font_size=12,
                          border_width=button_border_width,
                          border_color=button_border_color,
                          height=height,
                          width=self.at_btn_width,
                          button_color=button_color,
                          corner_radius=button_corner_radius)

    def place(self, x, y):

        self.btn.posx = x
        self.btn.posy = y

        self.btn.change_command(lambda: self._DisplayMenu(addX=self.btn.posx + self.at_entry_width - self.menu.atwidth, addY=self.btn.posy + self.at_entry_height - 1))

        # (x + self.at_entry_width - self.at_btn_width)
        #

        self.ent.place(x, y)
        self.btn.place((x + self.at_entry_width - self.at_btn_width), y)


    def _DisplayMenu(self, subX=0, subY=0, addX=0, addY=0):
        menu = self.menu
        menu_button = self.btn
        try:
            position = menu_button.btn.parent().mapToGlobal(menu_button.btn.rect().topLeft())
            position.setY(position.y() - subY + addY)
            position.setX(position.x() - subX + addX)

            t = Thread( target=lambda: menu.exec_(position) )
            t.run()

        except AttributeError as ex:
            print('\033[31m' + "[Error]" + '\033[93m ' + f"Cannot display menu!\n{ex}" + '\033[31m')
