from trufle import Window, Button, Frame, PositionGrip
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

class MacWindow:
    def __init__(self,
                 window_corner_radius          = 5,
                 background                    = '#DDDDDD',
                 title_bar_color               = '#000000',
                 drop_shadow_width             = 30,
                 border_color                  = '#FFFFFF',
                 window_border_width           = 0,
                 title_bar_border_width        = 0,
                 window_border_color           = '#000000',
                 title_bar_border_color        = '#000000',
                 width                         = 300,
                 height                        = 150,
                 title_bar_height              = 30,
                 close_button_color            = '#F45963',
                 close_button_hover_color      = '#F45963',
                 close_button_press_color      = '#f67a82',
                 close_button_icon_color       = '#F45963',
                 close_button_hover_icon_color = '#FFFFFF',
                 close_button_icon_size        = 7):

        self._dsw = drop_shadow_width
        self.__W = Window(transparent=True, height=height+ title_bar_height + (self._dsw*2), width=width + (self._dsw*2))

        self._fullwindow = Frame(self.__W, border_color='transparent', border_width=0, frame_color='transparent', width=width, height=height + title_bar_height + self._dsw)
        self._fullwindow.place(self._dsw,self._dsw)

        wcr = window_corner_radius

        self.title_bar = Frame(self._fullwindow, frame_color=title_bar_color, border_color=title_bar_border_color, corner_radius=[wcr,wcr, 0,0], border_width=title_bar_border_width, width=width, height=title_bar_height)
        self.title_bar.place(0,0)
        self.container = Frame(self._fullwindow, frame_color=background, border_color=window_border_color, corner_radius=[0,0,wcr,wcr], border_width=window_border_width, height=height)
        self.container.place(0,title_bar_height)

        self._pg = PositionGrip(self.title_bar, move=self.__W, position_grip_color='transparent', height=title_bar_height, width=width)
        self._pg.place(0,0)

        # Close Button

        self.close_button = Button(self.title_bar, command=self.__W.close, hover_color=close_button_hover_color, pressed_color=close_button_press_color,
                                   button_color=close_button_color, width=17, height=17, text_color=close_button_icon_color, text='×',
                                   font_size=close_button_icon_size, corner_radius='round')
        self.close_button.connect(hover=lambda event: self.close_button.configure(text_color=close_button_hover_icon_color),
                                  leave_hover=lambda event: self.close_button.configure(text_color=close_button_icon_color) )
        self.close_button.place(10,title_bar_height//5)

        # Create a QGraphicsDropShadowEffect
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(30)
        effect.setOffset(0)
        effect.setColor(QColor(0, 0, 0, 170))
        self._fullwindow._w.setGraphicsEffect(effect)

    def run(self):
        self.__W.run()