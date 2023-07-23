from trufle import Window, Frame, Label, PositionGrip, ImageDisplay, Button
from os import path
from PyQt5.QtWidgets import QSizeGrip, QGraphicsDropShadowEffect, QGraphicsRectItem, QApplication
from PyQt5.QtCore import Qt, QPointF, QRectF, QTimer, QEvent
from PyQt5.QtGui import QColor
from PIL import Image
from pyautogui import size, position
from time import sleep

screenW, screenH = size()

default_icon_path = f'{path.dirname(path.abspath(__file__))}/window.png'

def setCursor(id_):
    cursor_dict = {'b': Qt.SizeVerCursor, 'r': Qt.SizeHorCursor, 'br': Qt.SizeFDiagCursor, 'normal': Qt.ArrowCursor}
    QApplication.setOverrideCursor(cursor_dict.get(id_))

class HighWindow:
    def __init__(self,
        title = 'Trufle',
        title_color = '#FFFFFF',
        title_font = 'Segoe UI',
        title_font_size = 9,
        icon_x = 7,
        icon_y = 6,
        icon_width=20,
        icon_height=20,
        icon_title_padding = 7,

        title_x=None,
        title_y=8,
        tb_height = 30,
        border_width = 1,
        border_color = None,
        window_corner_radius = 0,
        window_width = 600,
        window_height = 400,
        tb_color = '#4C4A48',
        dropShadowWidth = 10,
        window_color = '#1e1e1e',
        buttons_pad = 1,

        icon=default_icon_path,

        close_button_width = 46,
        close_button_icon_color='#FFFFFF',
        close_button_icon_size=17,
        close_button_height = None,
        close_button_color = None,

        maximize_button_width=46,
        maximize_button_icon_color='#FFFFFF',
        maximize_button_icon_size=13,
        maximize_button_height=None,
        maximize_button_color=None,

        minimize_button_width=46,
        minimize_button_icon_color='#FFFFFF',
        minimize_button_icon_size=10,
        minimize_button_height=None,
        minimize_button_color=None):

        self._mode = 'not max'

        self.__W = Window(transparent=True, width=window_width + (dropShadowWidth * 3), height = window_height + (dropShadowWidth * 3))
        if close_button_height is None: close_button_height = tb_height
        if close_button_color is None: close_button_color = tb_color
        if minimize_button_height is None: minimize_button_height = tb_height
        if minimize_button_color is None: minimize_button_color = tb_color
        if maximize_button_height is None: tb_height
        if maximize_button_color is None: maximize_button_color = tb_color

        if border_color is None: border_color = self._lightenHexColor(tb_color, 0.1)
        if title_x is None: title_x = 7 + icon_x

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
        self.fullWindow.place(dsw, dsw)

        self.titleBar = Frame(self.fullWindow, frame_color=tb_color, width=window_width - dsw, height=tb_height,
                         border_width=border_width, border_color=border_color, corner_radius=[wcr, wcr, 0, 0])
        self.titleBar.place(dsw, dsw)

        self.titleLabel = Label(self.titleBar, text=title, width=window_width, text_color=title_color, font=title_font, font_size=title_font_size)
        self.titleLabel.place(title_x + 10 + icon_title_padding, title_y)

        self.iconDisplay = ImageDisplay(self.titleBar, image=Image.open(icon).resize((icon_width, icon_height)), width=icon_width + 2, height=icon_height )
        self.iconDisplay.place(icon_x, icon_y)

        self.sg = PositionGrip(self.fullWindow, move=self.__W, position_grip_color='transparent', width=window_width)
        self.sg.place(dsw, dsw)
        self.sg.event_move = self.sg.get_xy

        self.container = Frame(self.fullWindow, frame_color=window_color, corner_radius=[0, 0, wcr, wcr], border_width=border_width,
                          border_color=border_color, height=containerHeight, width=window_width - dsw)
        self.container.place(dsw, containerY + dsw)

        self.close_button = Button(self.fullWindow, text_color=close_button_icon_color, corner_radius=[0,wcr,0,0], hover_color='#FF0000',
                              pressed_color='#AA0000', command=self.__W.close, text='×', font_size=close_button_icon_size, button_color=close_button_color,
                              width=cb_width, height=cb_height)
        self.close_button.place(cbx, cby)

        # Create maximize button.
        self.maximize_button = Button(self.fullWindow, text_alignment='top', text_color=close_button_icon_color, corner_radius=0, hover_color=self._lightenHexColor(tb_color, 0.3),
                              pressed_color=self._lightenHexColor(tb_color, 0.1), command=self._toggleMaximize, text='□', font='Arial', font_size=close_button_icon_size, button_color=close_button_color,
                              width=cb_width, height=cb_height)
        self.maximize_button.place(cbx - maximize_button_width - buttons_pad, dsw + buttons_pad)

        # Create minimize button.
        self.minimize_button = Button(self.fullWindow, text_alignment='top', text_color=close_button_icon_color, corner_radius=0, hover_color=self._lightenHexColor(tb_color, 0.3),
                              pressed_color=self._lightenHexColor(tb_color, 0.1), command=self.__W.minimize, text='–', font='Arial', font_size=close_button_icon_size, button_color=close_button_color,
                              width=cb_width, height=cb_height)
        self.minimize_button.place(cbx - maximize_button_width - minimize_button_width - buttons_pad, dsw + buttons_pad)

        self.sgHeight = 20
        self.sgWidth = 20
        self.dsw = dsw

        self._sizeGripBR = Frame(self.container, frame_color='transparent', border_width=0, width=self.sgWidth, height=self.sgHeight)
        self._sizeGripBR.place(window_width - (self.sgWidth//2) - dsw, window_height - (self.sgHeight*2) - dsw )
        self._sizeGripBR._w.mousePressEvent = self._sizeStart
        self._sizeGripBR._w.mouseMoveEvent = self._SizeChangedEventBR
        self._sizeGripBR._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripBR._w.enterEvent = lambda event: setCursor('br')
        self._sizeGripBR._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripB = Frame(self.container, frame_color='transparent', border_width=0, width=self._HW_attributes_window_width - self.dsw - (self.sgWidth//2), height=self.sgHeight)
        self._sizeGripB.place(0, window_height - (self.sgHeight*2) - dsw )
        self._sizeGripB._w.mousePressEvent = self._sizeStart
        self._sizeGripB._w.mouseMoveEvent = self._SizeChangedEventB
        self._sizeGripB._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripB._w.enterEvent = lambda event: setCursor('b')
        self._sizeGripB._w.leaveEvent = lambda event: setCursor('normal')

        self._sizeGripR = Frame(self.container, frame_color='transparent', border_width=0, width=self.sgWidth, height=self._HW_attributes_window_height - dsw - (self.sgHeight*2))
        self._sizeGripR.place(window_width - (self.sgWidth//2) - dsw, 0 )
        self._sizeGripR._w.mousePressEvent = self._sizeStart
        self._sizeGripR._w.mouseMoveEvent = self._SizeChangedEventR
        self._sizeGripR._w.mouseReleaseEvent = self._sizeRelease

        self._sizeGripR._w.enterEvent = lambda event: setCursor('r')
        self._sizeGripR._w.leaveEvent = lambda event: setCursor('normal')

        # Create a QGraphicsDropShadowEffect
        effect = QGraphicsDropShadowEffect()
        shadowWidth = 10
        shadowHeight = 10
        sourceItem = QGraphicsRectItem(QRectF(-shadowWidth / 2, -shadowHeight / 2, shadowWidth, shadowHeight))
        effect.setBlurRadius(30)
        effect.setOffset(0)
        effect.setColor(QColor(0, 0, 0, 170))
        self.fullWindow._w.setGraphicsEffect(effect)

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

        # Set the previous position
        self._previous = [position().x, position().y]

        try:
            # Update window size
            self._mainXY = self.sg.get_xy()

            self._setMn()
            self.__W.size(self._HW_attributes_window_width + self._HW_attributes_dropShadowWidth + 20,
                          self._HW_attributes_window_height + self._HW_attributes_dropShadowWidth + 20, self._mainXY[0],
                          self._mainXY[1])
        except Exception as ex:
            print(ex)

        # Update sizegrip x,y
        self._UpdateSizeGrips()
    def _SizeChangedEventB(self, event: QEvent):
        # X,Y
        self._HW_attributes_window_height += (position().y - self._previous[1])

        if self._HW_attributes_window_height < self._HW_attributes_tb_height + 100:
            self._HW_attributes_window_height = self._HW_attributes_tb_height + 100

        # Set the previous position
        self._previous = [position().x, position().y]

        try:
            # Update window size
            self._mainXY = self.sg.get_xy()

            self._setMn()
            self.__W.size(self._HW_attributes_window_width + self._HW_attributes_dropShadowWidth + 20,
                          self._HW_attributes_window_height + self._HW_attributes_dropShadowWidth + 20, self._mainXY[0],
                          self._mainXY[1])
        except Exception as ex:
            print(ex)

        # Update sizegrip x,y
        self._UpdateSizeGrips()
    def _SizeChangedEventR(self, event: QEvent):
        # X,Y
        self._HW_attributes_window_width += (position().x - self._previous[0])

        if self._HW_attributes_window_width < 200:
            self._HW_attributes_window_width = 200

        # Set the previous position
        self._previous = [position().x, position().y]

        try:
            # Update window size
            self._mainXY = self.sg.get_xy()

            self._setMn()
            self.__W.size(self._HW_attributes_window_width + self._HW_attributes_dropShadowWidth + 20,
                          self._HW_attributes_window_height + self._HW_attributes_dropShadowWidth + 20, self._mainXY[0],
                          self._mainXY[1])
        except Exception as ex:
            print(ex)

        # Update sizegrip x,y
        self._UpdateSizeGrips()

    def _UpdateSizeGrips(self):
        self._sizeGripB.place(0, self._HW_attributes_window_height - (self.sgHeight*2) - self.dsw )
        self._sizeGripBR.place(self._HW_attributes_window_width - (self.sgWidth//2) - self.dsw, self._HW_attributes_window_height - (self.sgHeight*2) - self.dsw )
        self._sizeGripR.place(self._HW_attributes_window_width - (self.sgWidth//2) - self.dsw, 0)

        self._sizeGripB.configure(width=self._HW_attributes_window_width - self.dsw - (self.sgWidth//2))
        self._sizeGripR.configure(height=self._HW_attributes_window_height - self.dsw - (self.sgHeight*2))

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

    # Set the getMaster function, Allowing for widgets to placed.
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

        self.fullWindow.configure(width=self._HW_attributes_window_width, frame_color='transparent', height=self._HW_attributes_window_height, border_width=0,
                           corner_radius=[wcr, wcr, wcr, wcr])
        self.fullWindow.place(dsw, dsw)

        self.titleBar.configure(frame_color=self._HW_attributes_tb_color, width=self._HW_attributes_window_width - dsw, height=self._HW_attributes_tb_height,
                         border_width=self._HW_attributes_border_width, border_color=self._HW_attributes_border_color, corner_radius=[wcr, wcr, 0, 0])
        self.titleBar.place(dsw, dsw)

        self.titleLabel.configure(text=self._HW_attributes_title, width=self._HW_attributes_window_width, text_color=self._HW_attributes_title_color, font=self._HW_attributes_title_font, font_size=self._HW_attributes_title_font_size)
        self.titleLabel.place(self._HW_attributes_title_x + 10 + self._HW_attributes_icon_title_padding, self._HW_attributes_title_y)

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

        # Create a QGraphicsDropShadowEffect
        effect = QGraphicsDropShadowEffect()
        shadowWidth = 10
        shadowHeight = 10
        sourceItem = QGraphicsRectItem(QRectF(-shadowWidth / 2, -shadowHeight / 2, shadowWidth, shadowHeight))
        effect.setBlurRadius(30)
        effect.setOffset(0)
        effect.setColor(QColor(0, 0, 0, 170))
        self.fullWindow._w.setGraphicsEffect(effect)
        self._ShowSizeGrips()
        self.__W._w.showNormal()
        self.sg.show()

    def _setMx(self):
        self._mode = 'max'
        newTbHeight = self._HW_attributes_tb_height - 5
        #      Info: FUUUUULLL SCREEEEEN

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
                                    font_size=self._HW_attributes_maximize_button_icon_size)
        self.maximize_button.place(screenW - self._HW_attributes_close_button_width - self._HW_attributes_maximize_button_width, 0 + self._HW_attributes_buttons_pad)

        # Create minimize button.
        self.minimize_button.configure(text_color=self._HW_attributes_minimize_button_icon_color,
                command=self.__W.minimize, text='–', font_size=self._HW_attributes_minimize_button_icon_size, button_color=self._HW_attributes_minimize_button_color,
                width=self._HW_attributes_minimize_button_width, height=newTbHeight - (self._HW_attributes_buttons_pad*2))
        self.minimize_button.place(screenW - self._HW_attributes_close_button_width - self._HW_attributes_maximize_button_width - self._HW_attributes_minimize_button_width - self._HW_attributes_buttons_pad,
                                   self._HW_attributes_buttons_pad)

        self._HideSizeGrips()
        self.__W._w.showMaximized()

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

    def run(self):
        self.opacityVals = self._rangeFloat(0, 1, 2)
        self.opIndex = 0

        self.timer = QTimer(self.__W._w)
        self.timer.timeout.connect(self._updateOpacity)
        self.timer.start(1)

        self.__W._w.setWindowOpacity(0)
        self.__W.run()

    def close(self):
        self.opacityValsClose = self._rangeFloat(1, 0, 2)
        self.opIndexClose = 0

        self.timerClose = QTimer(self.__W._w)
        self.timerClose.timeout.connect(self._updateOpacityClose)
        self.timerClose.start(1)

        self.__W._w.setWindowOpacity(1)
        self.__W.close()

    def _updateOpacityClose(self):
        current_opacity = self.opacityValsClose[self.opIndexClose]
        self.__W._w.setWindowOpacity(current_opacity)
        self.opIndexClose += 1
        if self.opIndexClose > len(self.opacityValsClose) - 1:
            self.timerClose.stop()
            # Set it to min just to ensure opacity levels.
            self.__W._w.setWindowOpacity(0)

    def _updateOpacity(self):
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
