from trufle.gradientgen import GenerateGradient
from trufle import Button, Timer

class Transition:
    def __init__(self, master,
                 widget, attribute,
                 start_value=None, end_value=None,
                 tick_speed = 5):
        self.attribute = attribute
        self._widget = widget
        self.tick_speed = tick_speed
        if start_value is not None: self.start_value = start_value
        if end_value   is not None: self.end_value   = end_value
        self._master = master
        self._index = 0

    def setStartValue(self, value):
        self.start_value = value
    def setEndValue(self, value):
        self.end_value = value

    def start(self):
        match self._widget:
            case Button:
                self._handleButton()

    def _handleButton(self):
        match self.attribute:
            case 'button_color':
                colorsList = GenerateGradient(colours=[self.start_value, self.end_value])
                self._t = Timer(self._master, wait_time=self.tick_speed, on_tick=lambda: self._updateColor(colorsList) )
                self._t.start()

    def _updateColorButton(self, colors):
        self._widget.configure(button_color=colors[self._index])
        self._indexCheck()
    def _updateColorButton(self, colors):
        self._widget.configure(button_color=colors[self._index])
        self._indexCheck()

    def _indexCheck(self):
        self._index += 1
        if self._index > len(colors) - 1:
            self._t.stop()
