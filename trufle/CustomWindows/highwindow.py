from trufle import Window, Frame, Label, PositionGrip, ImageDisplay, Button
from os import path
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QGraphicsRectItem, QApplication
from PyQt5.QtCore import Qt, QPointF, QRectF, QTimer, QEvent
from PyQt5.QtGui import QColor
from PIL import Image
from pyautogui import size, position
from time import sleep

screenW, screenH = size()

default_icon_path = f'{path.dirname(path.abspath(__file__))}/window.png'

def setCursor(id_):
    cursor_dict = {'b': Qt.SizeVerCursor, 'r': Qt.SizeHorCursor, 'tl':Qt.SizeFDiagCursor, 'br': Qt.SizeFDiagCursor, 'bl': Qt.SizeBDiagCursor, 'normal': Qt.ArrowCursor}
    QApplication.setOverrideCursor(cursor_dict.get(id_))

class ThemeManager:
    def setUtilityFuncs(self, lighten, darken, hextorgb):
        self.funclightencolor = lighten
        self.funcdarkencolor = darken
        self.funchextorgb = hextorgb
    def setCoreValues(self, theme):
        self.theme = theme

        coreAttributes = {'Sleek': {
            'tb_color': '#2ECCFF',
            'tb_height': 30,
            'icon_x': 7 },
        'Realistic': {
                'tb_color': '#0078D7',
                'tb_height': 30,
                'icon_x': 7 }
        }
        self.tb_color = coreAttributes.get(theme).get('tb_color')
        self.tb_height = coreAttributes.get(theme).get('tb_height')
        self.icon_x = coreAttributes.get(theme).get('icon_x')

    def setSubValues(self):
        coreSubAttributes = {'Sleek': {
            'border_color': self.funclightencolor(self.tb_color, 0.3),
            'close_button_height': self.tb_height,
            'close_button_color': self.tb_color,
            'maximize_button_height': self.tb_height,
            'maximize_button_color': self.tb_color,
            'minimize_button_height': self.tb_height,
            'minimize_button_color': self.tb_color,
            'shadow_color': self.funchextorgb(self.tb_color),
            'border_color': self.funclightencolor(self.tb_color, 0.1),
            'title_x': self.icon_x,
        },
        'Realistic': {
            'border_color': self.funclightencolor(self.tb_color, 0.3),
            'close_button_height': self.tb_height,
            'close_button_color': self.tb_color,
            'maximize_button_height': self.tb_height,
            'maximize_button_color': self.tb_color,
            'minimize_button_height': self.tb_height,
            'minimize_button_color': self.tb_color,
            'shadow_color': (0,0,0,100),
            'border_color': self.funclightencolor(self.tb_color, 0.1),
            'title_x': 30,
            }
        }
        self.subattributes = coreSubAttributes[self.theme]
    def setThemedValues(self):
        theme_dict = {'Sleek': {
            'title': 'Trufle Sleek',
            'title_color': '#FFFFFF',
            'title_font': 'Segoe UI',
            'title_font_size': 14,
            'icon_x': 7,
            'icon_y': 100,
            'icon_width': 20,
            'icon_height': 20,
            'icon_title_padding': 0,
            'title_y': 2,
            'tb_height': 30,
            'border_width': 1,
            'border_color': self.subattributes['border_color'],
            'window_corner_radius': 5,
            'window_width': 600,
            'window_height': 400,
            'tb_color': '#2ECCFF',
            'dropShadowWidth': 10,
            'window_color': '#1e1e1e',
            'buttons_pad': 0,
            'icon': default_icon_path,

            'close_button_width': 46,
            'close_button_icon_color': '#FFFFFF',
            'close_button_icon_size': 17,
            'close_button_height': self.subattributes['close_button_height'],
            'close_button_color': self.subattributes['close_button_color'],
            'maximize_button_width': 46,
            'maximize_button_icon_color': '#FFFFFF',
            'maximize_button_icon_size': 17,
            'maximize_button_height': self.subattributes['maximize_button_height'],
            'maximize_button_color': self.subattributes['maximize_button_color'],
            'minimize_button_width': 46,
            'minimize_button_icon_color': '#FFFFFF',
            'minimize_button_icon_size': 15,
            'minimize_button_height': self.subattributes['minimize_button_height'],
            'minimize_button_color': self.subattributes['minimize_button_color'],
            'shadow_color': self.subattributes['shadow_color'],
            'window_x': 30,
            'window_y': 30,
            'border_color': self.subattributes['border_color'],
            'title_x': self.subattributes['title_x'],
        },
        'Realistic': {
            'title': 'Trufle Realistic',
            'title_color': '#FFFFFF',
            'title_font': 'Segoe UI',
            'title_font_size': 10,
            'icon_x': 7,
            'icon_y': 6,
            'icon_width': 20,
            'icon_height': 20,
            'icon_title_padding': 0,
            'title_y': 6,
            'tb_height': 30,
            'border_width': 1,
            'border_color': self.subattributes['border_color'],
            'window_corner_radius': 0,
            'window_width': 600,
            'window_height': 400,
            'tb_color': self.tb_color,
            'dropShadowWidth': 10,
            'window_color': '#1e1e1e',
            'buttons_pad': 1,
            'icon': default_icon_path,

            'close_button_width': 46,
            'close_button_icon_color': '#FFFFFF',
            'close_button_icon_size': 17,
            'close_button_height': self.subattributes['close_button_height'],
            'close_button_color': self.subattributes['close_button_color'],
            'maximize_button_width': 46,
            'maximize_button_icon_color': '#FFFFFF',
            'maximize_button_icon_size': 17,
            'maximize_button_height': self.subattributes['maximize_button_height'],
            'maximize_button_color': self.subattributes['maximize_button_color'],
            'minimize_button_width': 46,
            'minimize_button_icon_color': '#FFFFFF',
            'minimize_button_icon_size': 15,
            'minimize_button_height': self.subattributes['minimize_button_height'],
            'minimize_button_color': self.subattributes['minimize_button_color'],
            'shadow_color': self.subattributes['shadow_color'],
            'window_x': 30,
            'window_y': 30,
            'border_color': self.subattributes['border_color'],
            'title_x': self.subattributes['title_x'],
        }
        }
        self.theme_dictionary = theme_dict.get(self.theme)

    def get(self): return self.theme_dictionary


class HighWindow:
    def __init__(self,
        theme                      = 'Sleek',
        title                      = None,
        title_color                = None,
        title_font                 = None,
        title_font_size            = None,
        icon_x                     = None,
        icon_y                     = None,
        icon_width                 = None,
        icon_height                = None,
        icon_title_padding         = None,
        title_x                    = None,
        title_y                    = None,
        tb_height                  = None,
        border_width               = None,
        border_color               = None,
        window_corner_radius       = None,
        window_width               = None,
        window_height              = None,
        tb_color                   = None,
        dropShadowWidth            = None,
        window_color               = None,
        buttons_pad                = None,
        icon                       = None,
        close_button_width         = None,
        close_button_icon_color    = None,
        close_button_icon_size     = None,
        close_button_height        = None,
        close_button_color         = None,
        maximize_button_width      = None,
        maximize_button_icon_color = None,
        maximize_button_icon_size  = None,
        maximize_button_height     = None,
        maximize_button_color      = None,
        minimize_button_width      = None,
        minimize_button_icon_color = None,
        minimize_button_icon_size  = None,
        minimize_button_height     = None,
        minimize_button_color      = None,
        window_x                   = None,
        window_y                   = None,
        shadow_color               = None):

        themeManager = ThemeManager()
        themeManager.setUtilityFuncs(self._lightenHexColor, self._darkenHexColor, self.hex_to_rgba)
        themeManager.setCoreValues(theme)
        themeManager.setSubValues()
        themeManager.setThemedValues()
        Theme = themeManager.get()

        if title is None:                      title                      = Theme['title']
        if title_color is None:                title_color                = Theme['title_color']
        if title_font is None:                 title_font                 = Theme['title_font']
        if title_font_size is None:            title_font_size            = Theme['title_font_size']
        if icon_x is None:                     icon_x                     = Theme['icon_x']
        if icon_y is None:                     icon_y                     = Theme['icon_y']
        if icon_width is None:                 icon_width                 = Theme['icon_width']
        if icon_height is None:                icon_height                = Theme['icon_height']
        if icon_title_padding is None:         icon_title_padding         = Theme['icon_title_padding']
        if title_x is None:                    title_x                    = Theme['title_x']
        if title_y is None:                    title_y                    = Theme['title_y']
        if tb_height is None:                  tb_height                  = Theme['tb_height']
        if border_width is None:               border_width               = Theme['border_width']
        if border_color is None:               border_color               = Theme['border_color']
        if window_corner_radius is None:       window_corner_radius       = Theme['window_corner_radius']
        if window_width is None:               window_width               = Theme['window_width']
        if window_height is None:              window_height              = Theme['window_height']
        if tb_color is None:                   tb_color                   = Theme['tb_color']
        if dropShadowWidth is None:            dropShadowWidth            = Theme['dropShadowWidth']
        if window_color is None:               window_color               = Theme['window_color']
        if buttons_pad is None:                buttons_pad                = Theme['buttons_pad']
        if icon is None:                       icon                       = Theme['icon']
        if close_button_width is None:         close_button_width         = Theme['close_button_width']
        if close_button_icon_color is None:    close_button_icon_color    = Theme['close_button_icon_color']
        if close_button_icon_size is None:     close_button_icon_size     = Theme['close_button_icon_size']
        if close_button_height is None:        close_button_height        = Theme['close_button_height']
        if close_button_color is None:         close_button_color         = Theme['close_button_color']
        if maximize_button_width is None:      maximize_button_width      = Theme['maximize_button_width']
        if maximize_button_icon_color is None: maximize_button_icon_color = Theme['maximize_button_icon_color']
        if maximize_button_icon_size is None:  maximize_button_icon_size  = Theme['maximize_button_icon_size']
        if maximize_button_height is None:     maximize_button_height     = Theme['maximize_button_height']
        if maximize_button_color is None:      maximize_button_color      = Theme['maximize_button_color']
        if minimize_button_width is None:      minimize_button_width      = Theme['minimize_button_width']
        if minimize_button_icon_color is None: minimize_button_icon_color = Theme['minimize_button_icon_color']
        if minimize_button_icon_size is None:  minimize_button_icon_size  = Theme['minimize_button_icon_size']
        if minimize_button_height is None:     minimize_button_height     = Theme['minimize_button_height']
        if minimize_button_color is None:      minimize_button_color      = Theme['minimize_button_color']
        if window_x is None:                   window_x                   = Theme['window_x']
        if window_y is None:                   window_y                   = Theme['window_y']
        if shadow_color is None:               shadow_color               = Theme['shadow_color']

        self._mode = 'not max'
        self.__W = Window(transparent=True, width=window_width + (dropShadowWidth * 3) * 30, x=0,y=0, height = window_height + (dropShadowWidth * 3) * 30)
        self.__W._w.setWindowOpacity(0)

        self._HW_attributes_title = title
        self._HW_attributes_title_color = title_color
        self._HW_attributes_title_font = title_font
        self._HW_attributes_title_font_size = title_font_size
        self._HW_attributes_icon_x = icon_x
        self._HW_attributes_icon_y = icon_y
        self._HW_attributes_icon_width = icon_width
        self._HW_attributes_icon_height = icon_height
        self._HW_attributes_icon_title_padding = icon_title_padding
        self._HW_attributes_title_x = title_x
        self._HW_attributes_title_y = title_y
        self._HW_attributes_tb_height = tb_height
        self._HW_attributes_border_width = border_width
        self._HW_attributes_border_color = border_color
        self._HW_attributes_window_corner_radius = window_corner_radius
        self._HW_attributes_window_width = window_width
        self._HW_attributes_window_height = window_height
        self._HW_attributes_tb_color = tb_color
        self._HW_attributes_dropShadowWidth = dropShadowWidth
        self._HW_attributes_window_color = window_color
        self._HW_attributes_buttons_pad = buttons_pad
        self._HW_attributes_icon = icon
        self._HW_attributes_close_button_width = close_button_width
        self._HW_attributes_close_button_icon_color = close_button_icon_color
        self._HW_attributes_close_button_icon_size = close_button_icon_size
        self._HW_attributes_close_button_height = close_button_height
        self._HW_attributes_close_button_color = close_button_color
        self._HW_attributes_maximize_button_width = maximize_button_width
        self._HW_attributes_maximize_button_icon_color = maximize_button_icon_color
        self._HW_attributes_maximize_button_icon_size = maximize_button_icon_size
        self._HW_attributes_maximize_button_height = maximize_button_height
        self._HW_attributes_maximize_button_color = maximize_button_color
        self._HW_attributes_minimize_button_width      = minimize_button_width
        self._HW_attributes_minimize_button_icon_color = minimize_button_icon_color
        self._HW_attributes_minimize_button_icon_size  = minimize_button_icon_size
        self._HW_attributes_minimize_button_height     = minimize_button_height
        self._HW_attributes_minimize_button_color      = minimize_button_color
        self._HW_attributes_window_x = window_x
        self._HW_attributes_window_y = window_y
        self._HW_attributes_shadow_color = shadow_color

        # ///////////////

        # Maths
        dsw = dropShadowWidth
        tbhDiv = (tb_height // 2)
        wcr = (window_corner_radius)
        containerY = (tb_height - border_width)
        cbx = ((window_width - close_button_width)) - buttons_pad
        cby = dsw + buttons_pad
        containerHeight = ((window_height - tb_height) + border_width) - dsw
        cb_height = close_button_height - (buttons_pad*2)
        cb_width = close_button_width

        self.fullWindow = Frame(self.__W, width=window_width, frame_color='transparent', height=window_height, border_width=0,
                           corner_radius=[wcr, wcr, wcr, wcr])
        self.fullWindow.place(window_x, window_y)

        self.titleBar = Frame(self.fullWindow, frame_color=tb_color, width=window_width - dsw, height=tb_height,
                         border_width=border_width, border_color=border_color, corner_radius=[wcr, wcr, 0, 0])
        self.titleBar.place(dsw, dsw)

        self.titleLabel = Label(self.titleBar, text=title, width=window_width, text_color=title_color, font=title_font, font_size=title_font_size)
        self.titleLabel.place(title_x + icon_title_padding, title_y)

        self.iconDisplay = ImageDisplay(self.titleBar, image=Image.open(icon).resize((icon_width, icon_height)), width=icon_width + 2, height=icon_height )
        self.iconDisplay.place(icon_x, icon_y)

        self.sg = PositionGrip(self.fullWindow, move=self.fullWindow, position_grip_color='transparent', width=window_width)
        self.sg.place(dsw, dsw)

        self.container = Frame(self.fullWindow, frame_color=window_color, corner_radius=[0, 0, wcr, wcr], border_width=border_width,
                          border_color=border_color, height=containerHeight, width=window_width - dsw)
        self.container.place(dsw, containerY + dsw)

        self.close_button = Button(self.fullWindow, text_color=close_button_icon_color, corner_radius=[0,wcr,0,0], hover_color='#FF0000',
                              pressed_color='#AA0000', command=self.__W.close, text='×', font_size=close_button_icon_size, button_color=close_button_color,
                              width=cb_width, height=cb_height)
        self.close_button.place(cbx, cby)

        # Create maximize button.
        self.maximize_button = Button(self.fullWindow, text_alignment='top', text_color=close_button_icon_color, corner_radius=0, hover_color=self._lightenHexColor(tb_color, 0.3),
                              pressed_color=self._lightenHexColor(tb_color, 0.1), command=self._toggleMaximize, text='□', font='Arial', font_size=maximize_button_icon_size, button_color=close_button_color,
                              width=cb_width, height=cb_height)
        self.maximize_button.place(cbx - maximize_button_width - buttons_pad, dsw + buttons_pad)

        # Create minimize button.
        self.minimize_button = Button(self.fullWindow, text_alignment='top', text_color=close_button_icon_color, corner_radius=0, hover_color=self._lightenHexColor(tb_color, 0.3),
                              pressed_color=self._lightenHexColor(tb_color, 0.1), command=self.__W.minimize, text='–', font='Arial', font_size=minimize_button_icon_size, button_color=close_button_color,
                              width=cb_width, height=cb_height)
        self.minimize_button.place(cbx - maximize_button_width - minimize_button_width - buttons_pad, dsw + buttons_pad)

        self.sgHeight = 16
        self.sgWidth = 16
        self.dsw = dsw

        test = 'transparent'

        self._sizeGripBR = Frame(self.container, border_width=0, frame_color=test, width=self.sgWidth, height=self.sgHeight)
        self._sizeGripBR.place(window_width - (self.sgWidth) - dsw, window_height - (self.sgHeight*2) - (dsw*2) )
        self._sizeGripBR._w.mousePressEvent = self._sizeStart
        self._sizeGripBR._w.mouseMoveEvent = self._SizeChangedEventBR
        self._sizeGripBR._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripBR._w.enterEvent = lambda event: setCursor('br')
        self._sizeGripBR._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripB = Frame(self.container, border_width=0, frame_color=test, width=self._HW_attributes_window_width - (self.dsw) - (self.sgWidth*2), height=self.sgHeight)
        self._sizeGripB.place(self.sgWidth, window_height - (self.sgHeight*2) - (dsw*2) )
        self._sizeGripB._w.mousePressEvent = self._sizeStart
        self._sizeGripB._w.mouseMoveEvent = self._SizeChangedEventB
        self._sizeGripB._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripB._w.enterEvent = lambda event: setCursor('b')
        self._sizeGripB._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripR = Frame(self.container, border_width=0, width=self.sgWidth, frame_color=test, height=self._HW_attributes_window_height - (dsw*2) - (self.sgHeight*2))
        self._sizeGripR.place(window_width - (self.sgWidth//2) - (dsw*2), 0 )
        self._sizeGripR._w.mousePressEvent = self._sizeStart
        self._sizeGripR._w.mouseMoveEvent = self._SizeChangedEventR
        self._sizeGripR._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripR._w.enterEvent = lambda event: setCursor('r')
        self._sizeGripR._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripL = Frame(self.container, border_width=0, width=self.sgWidth, frame_color=test, height=self._HW_attributes_window_height - (dsw*2) - (self.sgHeight*2))
        self._sizeGripL.place((self.sgWidth//2) - dsw, 0)
        self._sizeGripL._w.mousePressEvent = self._sizeStart
        self._sizeGripL._w.mouseMoveEvent = self._SizeChangedEventL
        self._sizeGripL._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripL._w.enterEvent = lambda event: setCursor('r')
        self._sizeGripL._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripBL = Frame(self.container, border_width=0, frame_color=test, width=self.sgWidth, height=self.sgHeight)
        self._sizeGripBL.place(0, window_height - (self.sgHeight*2) - (self.dsw*2) )
        self._sizeGripBL._w.mousePressEvent = self._sizeStart
        self._sizeGripBL._w.mouseMoveEvent = self._SizeChangedEventBL
        self._sizeGripBL._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripBL._w.enterEvent = lambda event: setCursor('bl')
        self._sizeGripBL._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripTL = Frame(self.fullWindow, border_width=0, frame_color=test, width=self.sgWidth//2, height=self.sgHeight*2)
        self._sizeGripTL.place(self.dsw, self.dsw)
        self._sizeGripTL._w.mousePressEvent = self._sizeStart
        self._sizeGripTL._w.mouseMoveEvent = self._SizeChangedEventTL
        self._sizeGripTL._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripTL._w.enterEvent = lambda event: setCursor('tl')
        self._sizeGripTL._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripT = Frame(self.fullWindow, border_width=0, frame_color=test, corner_radius=0, width=window_width - (self.sgWidth*2) + dsw, height=int(self.sgHeight//1.5))
        self._sizeGripT.place(self.dsw + (self.sgWidth//2), self.dsw)
        self._sizeGripT._w.mousePressEvent = self._sizeStart
        self._sizeGripT._w.mouseMoveEvent = self._SizeChangedEventT
        self._sizeGripT._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripT._w.enterEvent = lambda event: setCursor('b')
        self._sizeGripT._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripTR = Frame(self.fullWindow, border_width=0, frame_color=test, corner_radius=0, width=window_width - (self.sgWidth*2) + dsw, height=self.sgHeight*2)
        self._sizeGripTR.place(self.dsw + self._HW_attributes_window_width - self.sgWidth, self.dsw)
        self._sizeGripTR._w.mousePressEvent = self._sizeStart
        self._sizeGripTR._w.mouseMoveEvent = self._SizeChangedEventTR
        self._sizeGripTR._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripTR._w.enterEvent = lambda event: setCursor('bl')
        self._sizeGripTR._w.leaveEvent = lambda event: setCursor('normal')
        # INFO : SIZE GRIPS

        # Create a QGraphicsDropShadowEffect
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(30)
        self.effect.setOffset(0)
        self.effect.setColor(QColor(shadow_color[0], shadow_color[1], shadow_color[2], shadow_color[3]))
        self.fullWindow._w.setGraphicsEffect(self.effect)

        self._previous = [window_width, window_height]

    def _toggleMaximize(self):
        if self._mode == 'max':
            self._mode = 'not max'
            try: self._setMn()
            except Exception as ex: print(ex)
        else:
            self._mode = 'max'
            self._setMx()
    def _sizeStart(self, event):
        self._previous = [position().x, position().y]
        self._mainXY = self.sg.get_xy()

    def _SizeChangedEventBR(self, event: QEvent):
        # X,Y
        self._HW_attributes_window_width += (position().x - self._previous[0])
        self._HW_attributes_window_height += (position().y - self._previous[1])

        if self._HW_attributes_window_height < self._HW_attributes_tb_height + 100:
            self._HW_attributes_window_height = self._HW_attributes_tb_height + 100
        if self._HW_attributes_window_width < 200:
            self._HW_attributes_window_width = 200

        # Update sizegrip x,y
        self._reloadEverything()
        self._UpdateSizeGrips()
    def _SizeChangedEventB(self, event: QEvent):
        # X,Y
        self._HW_attributes_window_height += (position().y - self._previous[1])

        if self._HW_attributes_window_height < self._HW_attributes_tb_height + 100:
            self._HW_attributes_window_height = self._HW_attributes_tb_height + 100

        # Update sizegrip x,y
        self._reloadEverything()
        self._UpdateSizeGrips()
    def _SizeChangedEventR(self, event: QEvent):
        # X,Y
        self._HW_attributes_window_width += (position().x - self._previous[0])

        if self._HW_attributes_window_width < 200:
            self._HW_attributes_window_width = 200

        # Update sizegrip x,y
        self._reloadEverything()
        self._UpdateSizeGrips()
    def _SizeChangedEventL(self, event: QEvent):
#        self._mainXY = self.sg.get_xy()
        delta = (position().x - self._previous[0])

        # X,Y
        self._HW_attributes_window_width -= delta

        if self._HW_attributes_window_width < 200:
            self._HW_attributes_window_width = 200

        # Update sizegrip x,y
        self._reloadEverything(xIncrease=delta)
        self._UpdateSizeGrips()
    def _SizeChangedEventBL(self, event: QEvent):
        #        self._mainXY = self.sg.get_xy()
        delta = (position().x - self._previous[0])
        deltaY = (position().y - self._previous[1])
        # X,Y
        self._HW_attributes_window_height += deltaY
        self._HW_attributes_window_width -= delta

        if self._HW_attributes_window_height < self._HW_attributes_tb_height + 100:
            self._HW_attributes_window_height = self._HW_attributes_tb_height + 100
        if self._HW_attributes_window_width < 200:
            self._HW_attributes_window_width = 200

        # Update sizegrip x,y
        self._reloadEverything(xIncrease=delta)
        self._UpdateSizeGrips()
    def _SizeChangedEventTL(self, event: QEvent):
        #        self._mainXY = self.sg.get_xy()
        delta = (position().x - self._previous[0])
        deltaY = (position().y - self._previous[1])
        # X,Y
        self._HW_attributes_window_height -= deltaY
        self._HW_attributes_window_width -= delta

        if self._HW_attributes_window_height < self._HW_attributes_tb_height + 100:
            self._HW_attributes_window_height = self._HW_attributes_tb_height + 100
        if self._HW_attributes_window_width < 200: self._HW_attributes_window_width = 200

        # Update and display window changes
        self._reloadEverything(xIncrease=delta, yIncrease=deltaY)
        self._UpdateSizeGrips()
    def _SizeChangedEventT(self, event: QEvent):
        deltaY = (position().y - self._previous[1])
        # X,Y
        self._HW_attributes_window_height -= deltaY

        if self._HW_attributes_window_height < self._HW_attributes_tb_height + 100:
            self._HW_attributes_window_height = self._HW_attributes_tb_height + 100

        # Update and display window changes
        self._reloadEverything(yIncrease=deltaY)
        self._UpdateSizeGrips()
    def _SizeChangedEventTR(self, event: QEvent):
        #        self._mainXY = self.sg.get_xy()
        delta = (position().x - self._previous[0])
        deltaY = (position().y - self._previous[1])
        # X,Y
        self._HW_attributes_window_height -= deltaY
        self._HW_attributes_window_width += delta

        if self._HW_attributes_window_height < self._HW_attributes_tb_height + 100:
            self._HW_attributes_window_height = self._HW_attributes_tb_height + 100
        if self._HW_attributes_window_width < 200: self._HW_attributes_window_width = 200

        # Update and display window changes
        self._reloadEverything(yIncrease=deltaY)
        self._UpdateSizeGrips()

    def _reloadEverything(self, xDecrease=0, yDecrease=0, xIncrease=0, yIncrease=0):
        winx = self.sg.get_xy()[0] - xDecrease + xIncrease
        winy = self.sg.get_xy()[1] - yDecrease + yIncrease
        self._previous = [position().x, position().y]
        self.fullWindow.place(winx, winy)
        self.sg.update_xy()
        self._setMn()

    def _UpdateSizeGrips(self):
        self._sizeGripB.place(self.sgWidth, self._HW_attributes_window_height - (self.sgHeight*2) - (self.dsw*2) )
        self._sizeGripBR.place(self._HW_attributes_window_width - (self.sgWidth//2) - (self.dsw*2), self._HW_attributes_window_height - (self.sgHeight*2) - (self.dsw*2) )
        self._sizeGripBL.place(0, self._HW_attributes_window_height - (self.sgHeight*2) - (self.dsw*2))
        self._sizeGripR.place(self._HW_attributes_window_width - (self.sgWidth//2) - (self.dsw*2), 0)
        self._sizeGripL.place((self.sgWidth//2) - self.dsw, 0)
        self._sizeGripTL.place(self.dsw, self.dsw)
        self._sizeGripT.place(self.dsw + (self.sgWidth//2), self.dsw)
        self._sizeGripTR.place(self.dsw + self._HW_attributes_window_width - self.sgWidth, self.dsw)

        self._sizeGripB.configure(width=self._HW_attributes_window_width - (self.dsw) - (self.sgWidth*2), height=self.sgHeight)
        self._sizeGripR.configure(height=self._HW_attributes_window_height - (self.dsw*2) - (self.sgHeight*2))
        self._sizeGripL.configure(width=self.sgWidth, height=self._HW_attributes_window_height - (self.dsw*2) - (self.sgHeight*2))
        self._sizeGripT.configure(width=self._HW_attributes_window_width - (self.sgWidth*2) + self.dsw, height=int(self.sgHeight//1.5))

    def _HideSizeGrips(self):
        self._sizeGripB.hide()
        self._sizeGripR.hide()
        self._sizeGripBR.hide()
    def _ShowSizeGrips(self):
        self._sizeGripB.show()
        self._sizeGripR.show()
        self._sizeGripBR.show()
    def _sizeRelease(self, event):
        self._previous = [position().x, position().y]

    # Set the getMaster method, Allowing for widgets to placed.
    def _getM(self):
        return self.container._w

    def _setMn(self):
        """                                      Info: MINIMIZE                                     """
        self._mode = 'not max'

        if self._HW_attributes_window_height < self._HW_attributes_tb_height:
            self._HW_attributes_window_height = self._HW_attributes_tb_height
        if self._HW_attributes_window_width < 200:
            self._HW_attributes_window_width = 200

        dsw = self._HW_attributes_dropShadowWidth
        tbhDiv = self._HW_attributes_tb_height // 2
        wcr = self._HW_attributes_window_corner_radius
        containerY = self._HW_attributes_tb_height - self._HW_attributes_border_width
        cbx = self._HW_attributes_window_width - self._HW_attributes_close_button_width - self._HW_attributes_buttons_pad
        cby = dsw + self._HW_attributes_buttons_pad
        containerHeight = ((self._HW_attributes_window_height - self._HW_attributes_tb_height) + self._HW_attributes_border_width) - dsw
        cb_height = self._HW_attributes_close_button_height - (self._HW_attributes_buttons_pad*2)
        cb_width = self._HW_attributes_close_button_width

        self.fullWindow.configure(width=self._HW_attributes_window_width, height=self._HW_attributes_window_height)
        self.fullWindow.place(self.sg.get_xy()[0], self.sg.get_xy()[1])

        self.titleBar.configure(frame_color=self._HW_attributes_tb_color, width=self._HW_attributes_window_width - dsw, height=self._HW_attributes_tb_height,
                         border_width=self._HW_attributes_border_width, border_color=self._HW_attributes_border_color, corner_radius=[wcr, wcr, 0, 0])
        self.titleBar.place(dsw, dsw)

        self.titleLabel.configure(text=self._HW_attributes_title, width=self._HW_attributes_window_width, text_color=self._HW_attributes_title_color, font=self._HW_attributes_title_font, font_size=self._HW_attributes_title_font_size)
        self.titleLabel.place(self._HW_attributes_title_x + self._HW_attributes_icon_title_padding, self._HW_attributes_title_y)

        self.iconDisplay.configure(image=Image.open(self._HW_attributes_icon).resize((self._HW_attributes_icon_width, self._HW_attributes_icon_height)), width=self._HW_attributes_icon_width + 2, height=self._HW_attributes_icon_height )
        self.iconDisplay.place(self._HW_attributes_icon_x, self._HW_attributes_icon_y)

        self.sg.configure(position_grip_color='transparent', width=self._HW_attributes_window_width)
        self.sg.place(dsw, dsw)

        self.container.configure(frame_color=self._HW_attributes_window_color, corner_radius=[0, 0, wcr, wcr], border_width=self._HW_attributes_border_width,
                          border_color=self._HW_attributes_border_color, height=containerHeight, width=self._HW_attributes_window_width - dsw)
        self.container.place(dsw, containerY + dsw)

        self.close_button.configure(corner_radius=[0,wcr,0,0], font_size=self._HW_attributes_close_button_icon_size - 2, button_color=self._HW_attributes_close_button_color,
                              width=cb_width, height=cb_height)
        self.close_button.place(cbx, cby)

        self.maximize_button.configure(width=cb_width, height=cb_height)
        self.maximize_button.place(cbx - self._HW_attributes_maximize_button_width - self._HW_attributes_buttons_pad, dsw + self._HW_attributes_buttons_pad)

        # Create minimize button.
        self.minimize_button.configure(width=self._HW_attributes_minimize_button_width, height=self._HW_attributes_minimize_button_height - (self._HW_attributes_buttons_pad*2))
        self.minimize_button.place(cbx - self._HW_attributes_maximize_button_width - self._HW_attributes_minimize_button_width - self._HW_attributes_buttons_pad, self.dsw + self._HW_attributes_buttons_pad)

        self.__W.size(size()[0], size()[1] - 1, 0, 0)
        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(30)
        self.effect.setOffset(0)
        self.effect.setColor(QColor(self._HW_attributes_shadow_color[0], self._HW_attributes_shadow_color[1], self._HW_attributes_shadow_color[2], self._HW_attributes_shadow_color[3]))
        self.fullWindow._w.setGraphicsEffect(self.effect)
        self._ShowSizeGrips()
        self.sg.show()
    def _setMx(self):
        self._mode = 'max'
        newTbHeight = self._HW_attributes_tb_height - 5
        #                                                 Info: FUUUUULLL SCREEEEEN

        self.fullWindow.configure(width=screenW, frame_color='transparent', height=screenH, corner_radius=0)
        self.fullWindow.place(0,0)

        self.titleBar.configure(width=screenW, height=newTbHeight, corner_radius=[0,0,0,0])
        self.titleBar.place(0,0)

        self.titleLabel.configure(text=self._HW_attributes_title, width=self._HW_attributes_window_width, text_color=self._HW_attributes_title_color, font=self._HW_attributes_title_font, font_size=self._HW_attributes_title_font_size)
        self.titleLabel.place(self._HW_attributes_title_x + 10 + self._HW_attributes_icon_title_padding, newTbHeight//5)
        self.iconDisplay.place(self._HW_attributes_icon_x, newTbHeight//6)

        self.sg.hide()

        self.container.configure(frame_color=self._HW_attributes_window_color, corner_radius=[0,0,0,0], border_width=0, height=screenH - newTbHeight, width=screenW)
        self.container.place(0,newTbHeight)

        self.close_button.configure(text_color=self._HW_attributes_close_button_icon_color, width=self._HW_attributes_close_button_width - self._HW_attributes_buttons_pad, corner_radius=[0,0,0,0], hover_color='#FF0000',
                              pressed_color='#AA0000', command=self.__W.close, text='×', height=newTbHeight - (self._HW_attributes_buttons_pad*2), font_size=self._HW_attributes_close_button_icon_size - 4, button_color=self._HW_attributes_close_button_color)
        self.close_button.place(screenW - self._HW_attributes_close_button_width, 0 + self._HW_attributes_buttons_pad)
        self.maximize_button.configure(width=self._HW_attributes_close_button_width - self._HW_attributes_buttons_pad,
                                    corner_radius=[0, 0, 0, 0], text='□',
                                    height=newTbHeight - (self._HW_attributes_buttons_pad * 2),
                                    font_size=self._HW_attributes_maximize_button_icon_size - 3)
        self.maximize_button.place(screenW - self._HW_attributes_close_button_width - self._HW_attributes_maximize_button_width, 0 + self._HW_attributes_buttons_pad)

        # Create minimize button.
        self.minimize_button.configure(text_color=self._HW_attributes_minimize_button_icon_color,
                command=self.__W.minimize, text='–', font_size=self._HW_attributes_minimize_button_icon_size, button_color=self._HW_attributes_minimize_button_color,
                width=self._HW_attributes_minimize_button_width, height=newTbHeight - (self._HW_attributes_buttons_pad*2))
        self.minimize_button.place(screenW - self._HW_attributes_close_button_width - self._HW_attributes_maximize_button_width - self._HW_attributes_minimize_button_width - self._HW_attributes_buttons_pad,
                                   self._HW_attributes_buttons_pad)

        self.__W.size(size()[0], size()[1], 0, 0)
        self.fullWindow._w.setGraphicsEffect(None)
        self._HideSizeGrips()

    def _lightenHexColor(self, hex_color, lighten_factor):
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

        lighten_factor = max(0, min(lighten_factor, 1))
        r += int((255 - r) * lighten_factor)
        g += int((255 - g) * lighten_factor)
        b += int((255 - b) * lighten_factor)

        return '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)
    def _darkenHexColor(self, hex_color, darken_factor):
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

        darken_factor = max(0, min(darken_factor, 1))
        r = int(r * (1 - darken_factor))
        g = int(g * (1 - darken_factor))
        b = int(b * (1 - darken_factor))

        return '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)

    def hex_to_rgba(self, hex_color):
        hex_color = hex_color.lstrip("#")
        red = int(hex_color[0:2], 16)
        green = int(hex_color[2:4], 16)
        blue = int(hex_color[4:6], 16)
        alpha = 100 if len(hex_color) == 6 else int(hex_color[6:8], 16)
        return (red, green, blue, alpha)

    def run(self) -> None:
        self.opacityVals = self._rangeFloat(0, 1, 2)
        self.opIndex = 0
        self.__W.size(size()[0],size()[1] - 1, 0,0)

        self.timer = QTimer(self.__W._w)
        self.timer.timeout.connect(self._updateOpacity)
        self.timer.start(1)

        self.__W._w.setWindowOpacity(0)
        self.__W.run()
    def close(self) -> None:
        self.opacityValsClose = self._rangeFloat(1, 0, 2)
        self.opIndexClose = 0

        self.timerClose = QTimer(self.__W._w)
        self.timerClose.timeout.connect(self._updateOpacityClose)
        self.timerClose.start(1)

        self.__W._w.setWindowOpacity(1)
        self.__W.close()
    def _updateOpacityClose(self) -> None:
        current_opacity = self.opacityValsClose[self.opIndexClose]
        self.__W._w.setWindowOpacity(current_opacity)
        self.opIndexClose += 1
        if self.opIndexClose > len(self.opacityValsClose) - 1:
            self.timerClose.stop()
            # Set it to min just to ensure opacity levels.
            self.__W._w.setWindowOpacity(0)
    def _updateOpacity(self) -> None:
        current_opacity = self.opacityVals[self.opIndex]
        self.__W._w.setWindowOpacity(current_opacity)
        self.opIndex += 1
        if self.opIndex > len(self.opacityVals) - 1:
            self.timer.stop()
            # Set it to max just to ensure opacity levels.
            self.__W._w.setWindowOpacity(1)
    def _rangeFloat(self, start, end, precision):
        result = []
        current = start
        while current <= end:
            result.append(round(current, precision))
            current += 1 / (10 ** precision)
        return result
