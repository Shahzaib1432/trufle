from PyQt5.QtWidgets import QMenu, QAction, QLineEdit, QPushButton
from PyQt5.QtGui import QFont

class ComboBox:
    def __init__(self,
                 master,
                 width=100,
                 height=30,
                 items=['Items'],

                 entry_text='',
                 entry_default_text='',
                 entry_text_color='#ffffff',
                 entry_color='#3FAD44',
                 entry_border_width=1,
                 entry_border_color='#ffffff',
                 entry_corner_radius=5,
                 entry_font='HoloLens MDL2 Assets',
                 entry_font_size=10,

                 button_corner_radius=[0,4,0,4],
                 button_border_width=0,
                 button_border_color='#FFFFFF',
                 button_color='#54c159',
                 button_hover_color='#43b748',
                 button_indicator_color='#FFFFFF',
                 button_indicator_size=10,
                 button_width='auto',  # 'auto' = Automatic
                 _buttonEntryParts=4,  # Used if button_width is auto

                 menu_width='auto',    # 'auto' = Automatic
                 menu_height='auto',   # 'auto' = Automatic
                 menu_color='#3FAD44',
                 menu_border_width=3,
                 menu_border_color='#399c3d',
                 menu_position_x='auto',
                 menu_position_y='auto',
                 menu_items_padding=0,

                 items_text_color       = '#FFFFFF',
                 items_text_font        = 'Century Gothic',
                 items_text_font_size   = 10,
                 items_hover_text_color = '#FFFFFF',
                 items_hover_color      = '#3ca441',
                 items_press_text_color ='#FFFFFF',
                 items_press_color      ='#36933a'
                 ):

        # Attributes ====
        self.attributes_width =                  width
        self.attributes_height =                 height
        self.attributes_items =                  items
        self.attributes_entry_text =             entry_text
        self.attributes_entry_default_text =     entry_default_text
        self.attributes_entry_text_color =       entry_text_color
        self.attributes_entry_color =            entry_color
        self.attributes_entry_border_width =     entry_border_width
        self.attributes_entry_border_color =     entry_border_color
        self.attributes_entry_corner_radius =    entry_corner_radius
        self.attributes_entry_font =             entry_font
        self.attributes_entry_font_size =        entry_font_size
        self.attributes_button_corner_radius =   button_corner_radius
        self.attributes_button_border_width =    button_border_width
        self.attributes_button_border_color =    button_border_color
        self.attributes_button_color =           button_color
        self.attributes_button_hover_color =     button_hover_color
        self.attributes_button_indicator_color = button_indicator_color
        self.attributes_button_indicator_size =  button_indicator_size
        self.attributes_button_width =           button_width
        self.attributes_buttonEntryParts =       _buttonEntryParts
        self.attributes_menu_width =             menu_width
        self.attributes_menu_height =            menu_height
        self.attributes_menu_color =             menu_color
        self.attributes_menu_border_width =      menu_border_width
        self.attributes_menu_border_color =      menu_border_color
        self.attributes_menu_position_x =        menu_position_x
        self.attributes_menu_position_y =        menu_position_y
        self.attributes_menu_items_padding =     menu_items_padding
        self.attributes_items_text_color =       items_text_color
        self.attributes_items_text_font =        items_text_font
        self.attributes_items_text_font_size =   items_text_font_size
        self.attributes_items_hover_text_color = items_hover_text_color
        self.attributes_items_hover_color =      items_hover_color
        self.attributes_items_press_text_color = items_press_text_color
        self.attributes_items_press_color =      items_press_color

        # ===============

        if button_width == 'auto':
            self._buttonEntryParts = _buttonEntryParts
            if (width // self._buttonEntryParts) < 30:
                self._buttonEntryParts -= 1
            self.at_btn_width = width // self._buttonEntryParts
        else:self.at_btn_width = button_width

        self.master = master

        self.at_entry_width = width
        self.at_entry_height = height

        self.menu = QMenu(master._getM() )

        self.menu.setStyleSheet(f'''
                QMenu {{
                    color: {items_text_color};
                    background-color: {menu_color};
                    border: {menu_border_width}px solid {menu_border_color};
                    padding: {menu_items_padding};
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

        entry_corner_radius = self._bwCheck(entry_corner_radius)
        button_corner_radius = self._bwCheck(button_corner_radius)

        self.menu.setFont(QFont(items_text_font, items_text_font_size))

        self.at_items = []

        self.menu.atwidth = 90
        self.menu.atheight = 80

        if menu_width != 'auto': self.menu.setFixedWidth(menu_width); self.menu.atheight = menu_height
        if menu_height != 'auto': self.menu.setFixedHeight(menu_height); self.menu.atwidth = menu_width

        # 100x80

        # Make Core Entry

        self.ent = QLineEdit(parent=master._getM() )
        self.ent.setStyleSheet(f'''
            QLineEdit {{
                color: {entry_text_color};
                background-color: {entry_color};
                
                border-top-left-radius: {entry_corner_radius[0]};
                border-top-right-radius: {entry_corner_radius[1]};
                border-bottom-left-radius: {entry_corner_radius[2]};
                border-bottom-right-radius: {entry_corner_radius[3]};
                
                border: {entry_border_width}px solid {entry_border_color};
            }} ''')

        self.ent.setText(entry_text)

        _width = button_width
        if _width == 'auto': _width = 30

        self.ent.setFixedSize(width - _width + 5, height)
        self.ent.setPlaceholderText(entry_default_text)
        self.ent.setFont(QFont(entry_font, entry_font_size))

        # Make core Button
        self.btn = QPushButton('▼', master._getM() )
        self.btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {button_color};
                color: {button_indicator_color};
                
                border-top-left-radius: {button_corner_radius[0]};
                border-top-right-radius: {button_corner_radius[1]};
                border-bottom-left-radius: {button_corner_radius[2]};
                border-bottom-right-radius: {button_corner_radius[3]};
                
                border: {button_border_width}px solid {button_border_color};
            }}
            
            QPushButton:hover{{ background-color: {button_hover_color}; }}
            """)
        self.btn.setFont(QFont( 'Century Gothic', button_indicator_size) )
        self.btn.setFixedSize(self.at_btn_width, height)

        self.setItems(items)

        # Hide!
        self.btn.hide()
        self.ent.hide()

    def _bwCheck(self, bw):
        if type(bw) == int:
            bw = [bw,bw,bw,bw]
        return bw

    def place(self, x, y):
        self.btn.posx = x
        self.btn.posy = y

        self.btn.clicked.connect(lambda: self.showMenu())

        self.ent.move(x, y)
        self.btn.move((x + self.at_entry_width - self.at_btn_width), y)
        self.ent.show()
        self.btn.show()

    def showMenu(self, subX=0, subY=0, addX=None, addY=None):
        menu = self.menu
        menu_button = self.btn
        if addX is None: addX = self.btn.posx
        if addY is None: addY = self.btn.posy + self.at_entry_height - 1

        try:
            position = menu_button.parent().mapToGlobal(menu_button.rect().topLeft())
            position.setY(position.y() - subY + addY)
            position.setX(position.x() - subX + addX)

            menu.exec_(position)

        except AttributeError as ex:
            print('\033[31m' + "[Error]" + '\033[93m ' + f"Cannot display menu!\n{ex}" + '\033[31m')

    def addItem(self, name):
        action = QAction(name, self.master._getM() )
        self.menu.addAction(action)
        action.triggered.connect(lambda: self.ent.setText(name) )
        self.at_items.append(action)

    def setItems(self, newList):
        self.deleteItems()
        for action in newList:
            self.addItem(action)

    def deleteItems(self):
        for action in self.at_items:
            self.menu.removeAction(action)

    def reload(self):
        self.attributes_entry_corner_radius = self._bwCheck(self.attributes_entry_corner_radius)
        self.attributes_button_corner_radius = self._bwCheck(self.attributes_button_corner_radius)

        if self.attributes_button_width == 'auto':
            # If it's too low, Decrement it.
            if (self.attributes_width // self.attributes_buttonEntryParts) < 30:
                self.attributes_buttonEntryParts -= 1
            # Calculate the Auto-Button-Width
            self.at_btn_width = self.attributes_width // self.attributes_buttonEntryParts
        else:
            # Use the button width provided instead if it isn't 'auto'
            self.at_btn_width = self.attributes_button_width

        self.at_entry_width = self.attributes_width
        self.at_entry_height = self.attributes_height

        self.menu.setStyleSheet(f'''
                QMenu {{
                    color: {self.attributes_items_text_color};
                    background-color: {self.attributes_menu_color};
                    border: {self.attributes_menu_border_width}px solid {self.attributes_entry_border_color};
                    padding: {self.attributes_menu_items_padding};
                }}

                QMenu::item:selected {{ 
                    background-color: {self.attributes_items_hover_color}; 
                    color: {self.attributes_items_hover_text_color};
                }}

                QMenu::item:pressed {{ 
                    background-color: {self.attributes_items_press_color}; 
                    color: {self.attributes_items_press_text_color};
                }}
                ''')

        self.menu.setFont(QFont(self.attributes_items_text_font, self.attributes_items_text_font_size))

        self.at_items = []

        self.menu.atwidth = 90
        self.menu.atheight = 80

        if self.attributes_menu_width != 'auto':
            self.menu.setFixedWidth(self.attributes_menu_width)
            self.menu.atheight = self.attributes_menu_height
        if self.attributes_menu_height != 'auto':
            self.menu.setFixedHeight(self.attributes_menu_height)
            self.menu.atwidth = self.attributes_menu_height

        self.ent.setStyleSheet(f'''
            QLineEdit {{
                color: {self.attributes_entry_text_color};
                background-color: {self.attributes_entry_color};
                
                border-top-left-radius: {self.attributes_entry_corner_radius[0]};
                border-top-right-radius: {self.attributes_entry_corner_radius[1]};
                border-bottom-left-radius: {self.attributes_entry_corner_radius[2]};
                border-bottom-right-radius: {self.attributes_entry_corner_radius[3]};
                
                border: {self.attributes_entry_border_width}px solid {self.attributes_entry_border_color};
            }} ''')

        self.ent.setText(self.attributes_entry_text)
        self.ent.setFixedSize(self.attributes_width - 20, self.attributes_height)
        self.ent.setPlaceholderText(self.attributes_entry_default_text)
        self.ent.setFont(QFont(self.attributes_entry_font, self.attributes_entry_font_size))

        # Make core Button
        self.btn.setText('▼')
        self.btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.attributes_button_color};
                color: {self.attributes_button_indicator_color};

                border-top-left-radius: {self.attributes_button_corner_radius[0]};
                border-top-right-radius: {self.attributes_button_corner_radius[1]};
                border-bottom-left-radius: {self.attributes_button_corner_radius[2]};
                border-bottom-right-radius: {self.attributes_button_corner_radius[3]};
                border: {self.attributes_button_border_width}px solid {self.attributes_button_border_color};
            }}

            QPushButton:hover{{ background-color: {self.attributes_button_hover_color}; }}
            """)
        self.btn.setFont(QFont('Century Gothic', self.attributes_button_indicator_size))
        self.btn.setFixedSize(self.at_btn_width, self.attributes_height)

        self.setItems(self.attributes_items)

    def configure(self,
                  width                 =None,
                  height                =None,
                  items                 =None,
                  entry_text            =None,
                  entry_default_text    =None,
                  entry_text_color      =None,
                  entry_color           =None,
                  entry_border_width    =None,
                  entry_border_color    =None,
                  entry_corner_radius   =None,
                  entry_font            =None,
                  entry_font_size       =None,
                  button_corner_radius  =None,
                  button_border_width   =None,
                  button_border_color   =None,
                  button_color          =None,
                  button_hover_color    =None,
                  button_indicator_color=None,
                  button_indicator_size =None,
                  button_width          =None,
                  _buttonEntryParts     =None,
                  menu_width            =None,
                  menu_height           =None,
                  menu_color            =None,
                  menu_border_width     =None,
                  menu_border_color     =None,
                  menu_position_x       =None,
                  menu_position_y       =None,
                  menu_items_padding    =None,
                  items_text_color      =None,
                  items_text_font       =None,
                  items_text_font_size  =None,
                  items_hover_text_color=None,
                  items_hover_color     =None,
                  items_press_text_color=None,
                  items_press_color     =None):
        if width is not None: self.attributes_width =                                   width
        if height is not None: self.attributes_height =                                 height
        if items is not None: self.attributes_items =                                   items
        if entry_text is not None: self.attributes_entry_text =                         entry_text
        if entry_default_text is not None: self.attributes_entry_default_text =         entry_default_text
        if entry_text_color is not None: self.attributes_entry_text_color =             entry_text_color
        if entry_color is not None: self.attributes_entry_color =                       entry_color
        if entry_border_width is not None: self.attributes_entry_border_width =         entry_border_width
        if entry_border_color is not None: self.attributes_entry_border_color =         entry_border_color
        if entry_corner_radius is not None: self.attributes_entry_corner_radius =       entry_corner_radius
        if entry_font is not None: self.attributes_entry_font =                         entry_font
        if entry_font_size is not None: self.attributes_entry_font_size =               entry_font_size
        if button_corner_radius is not None: self.attributes_button_corner_radius =     button_corner_radius
        if button_border_width is not None: self.attributes_button_border_width =       button_border_width
        if button_border_color is not None: self.attributes_button_border_color =       button_border_color
        if button_color is not None: self.attributes_button_color =                     button_color
        if button_hover_color is not None: self.attributes_button_hover_color =         button_hover_color
        if button_indicator_color is not None: self.attributes_button_indicator_color = button_indicator_color
        if button_indicator_size is not None: self.attributes_button_indicator_size =   button_indicator_size
        if button_width is not None: self.attributes_button_width =                     button_width
        if _buttonEntryParts is not None: self.attributes_buttonEntryParts =            _buttonEntryParts
        if menu_width is not None: self.attributes_menu_width =                         menu_width
        if menu_height is not None: self.attributes_menu_height =                       menu_height
        if menu_color is not None: self.attributes_menu_color =                         menu_color
        if menu_border_width is not None: self.attributes_menu_border_width =           menu_border_width
        if menu_border_color is not None: self.attributes_menu_border_color =           menu_border_color
        if menu_position_x is not None: self.attributes_menu_position_x =               menu_position_x
        if menu_position_y is not None: self.attributes_menu_position_y =               menu_position_y
        if menu_items_padding is not None: self.attributes_menu_items_padding =         menu_items_padding
        if items_text_color is not None: self.attributes_items_text_color =             items_text_color
        if items_text_font is not None: self.attributes_items_text_font =               items_text_font
        if items_text_font_size is not None: self.attributes_items_text_font_size =     items_text_font_size
        if items_hover_text_color is not None: self.attributes_items_hover_text_color = items_hover_text_color
        if items_hover_color is not None: self.attributes_items_hover_color =           items_hover_color
        if items_press_text_color is not None: self.attributes_items_press_text_color = items_press_text_color
        if items_press_color is not None: self.attributes_items_press_color =           items_press_color
        self.reload()

    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'width':                  self.attributes_width                  = width
            case 'height':                 self.attributes_height                 = height
            case 'items':                  self.attributes_items                  = items
            case 'entry_text':             self.attributes_entry_text             = entry_text
            case 'entry_default_text':     self.attributes_entry_default_text     = entry_default_text
            case 'entry_text_color':       self.attributes_entry_text_color       = entry_text_color
            case 'entry_color':            self.attributes_entry_color            = entry_color
            case 'entry_border_width':     self.attributes_entry_border_width     = entry_border_width
            case 'entry_border_color':     self.attributes_entry_border_color     = entry_border_color
            case 'entry_corner_radius':    self.attributes_entry_corner_radius    = entry_corner_radius
            case 'entry_font':             self.attributes_entry_font             = entry_font
            case 'entry_font_size':        self.attributes_entry_font_size        = entry_font_size
            case 'button_corner_radius':   self.attributes_button_corner_radius   = button_corner_radius
            case 'button_border_width':    self.attributes_button_border_width    = button_border_width
            case 'button_border_color':    self.attributes_button_border_color    = button_border_color
            case 'button_color':           self.attributes_button_color           = button_color
            case 'button_hover_color':     self.attributes_button_hover_color     = button_hover_color
            case 'button_indicator_color': self.attributes_button_indicator_color = button_indicator_color
            case 'button_indicator_size':  self.attributes_button_indicator_size  = button_indicator_size
            case 'button_width':           self.attributes_button_width           = button_width
            case '_buttonEntryParts':      self.attributes_buttonEntryParts       = _buttonEntryParts
            case 'menu_width':             self.attributes_menu_width             = menu_width
            case 'menu_height':            self.attributes_menu_height            = menu_height
            case 'menu_color':             self.attributes_menu_color             = menu_color
            case 'menu_border_width':      self.attributes_menu_border_width      = menu_border_width
            case 'menu_border_color':      self.attributes_menu_border_color      = menu_border_color
            case 'menu_position_x':        self.attributes_menu_position_x        = menu_position_x
            case 'menu_position_y':        self.attributes_menu_position_y        = menu_position_y
            case 'menu_items_padding':     self.attributes_menu_items_padding     = menu_items_padding
            case 'items_text_color':       self.attributes_items_text_color       = items_text_color
            case 'items_text_font':        self.attributes_items_text_font        = items_text_font
            case 'items_text_font_size':   self.attributes_items_text_font_size   = items_text_font_size
            case 'items_hover_text_color': self.attributes_items_hover_text_color = items_hover_text_color
            case 'items_hover_color':      self.attributes_items_hover_color      = items_hover_color
            case 'items_press_text_color': self.attributes_items_press_text_color = items_press_text_color
            case 'items_press_color':      self.attributes_items_press_color      = items_press_color
            case 'x':                      self.place(new_value, self.info_y())
            case 'y':                      self.place(self.info_x(), new_value)
        self.reload()

    def info_x(self): return self.btn.x()
    def info_y(self): return self.btn.y()

    def hide(self):
        self.ent.hide()
        self.btn.hide()
        self.menu.hide()

    def show(self):
        self.ent.show()
        self.btn.show()
        self.menu.show()

    def connect(self, widget='entry', hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        match widget:
            case 'entry':
                if hover         is not None:  self.ent.enterEvent         = hover
                if leave_hover   is not None:  self.ent.leaveEvent         = leave_hover
                if pressed       is not None:  self.ent.mousePressEvent    = pressed
                if leave_pressed is not None:  self.ent.mouseReleaseEvent  = leave_pressed
                if pressed_motion is not None: self.ent.mouseMoveEvent     = pressed_motion
                if scroll         is not None: self.ent.wheelEvent         = scroll
            case 'button':
                if hover         is not None:  self.btn.enterEvent         = hover
                if leave_hover   is not None:  self.btn.leaveEvent         = leave_hover
                if pressed       is not None:  self.btn.mousePressEvent    = pressed
                if leave_pressed is not None:  self.btn.mouseReleaseEvent  = leave_pressed
                if pressed_motion is not None: self.btn.mouseMoveEvent     = pressed_motion
                if scroll         is not None: self.btn.wheelEvent         = scroll
            case 'menu':
                if hover         is not None:  self.menu.enterEvent         = hover
                if leave_hover   is not None:  self.menu.leaveEvent         = leave_hover
                if pressed       is not None:  self.menu.mousePressEvent    = pressed
                if leave_pressed is not None:  self.menu.mouseReleaseEvent  = leave_pressed
                if pressed_motion is not None: self.menu.mouseMoveEvent     = pressed_motion
                if scroll         is not None: self.menu.wheelEvent         = scroll