from .gradientgen import GenerateGradient
from .timer import CurveTimer, CurveTimerGroup

class Animation:
    def __init__(self, widget, attribute,
                 start_value=None, end_value=None,
                 curve = 'Linear', duration = 10000,
                 power = 700):
        self.curve, self.attribute = curve, attribute
        self._widget, self.duration = widget, duration
        self.power = power

        self._activeInstantly = True

        if start_value is not None: self.start_value = start_value
        if end_value   is not None: self.end_value   = end_value

        self._master = self._widget.attributes_master
        self._index = 0

        self._stateTicking = False
        self._calledStarted = False

    def set_start_value(self, value):
        self.start_value = value
    def set_end_value(self, value):
        self.end_value = value

    def start(self):
        self._handleWidget()

        self._stateTicking = True
        self.values = self._getListedValues()

    def restart(self):
        self.stop()
        self.start()

    def stop(self):
        try:
            self._t.stop()
            self._index = 0
            self._widget.config(self.attribute, self.end_value)
            self._stateTicking = False
        except: pass

    def _handleWidget(self):
        self.values = self._getListedValues()
        self.function_dict = {'button_color': lambda: self._update(self.values, 'button_color'),
                              'text_color':   lambda: self._update(self.values, 'text_color  '),
                              'border_color': lambda: self._update(self.values, 'border_color'),
                              'width':        lambda: self._update(self.values, 'width_color '),
                              'height':       lambda: self._update(self.values, 'height_color')}

        self._t = CurveTimer(self._master, duration=self.duration, power=self.power, curve=self.curve, on_tick=self.function_dict.get(self.attribute) )
        if self._activeInstantly: self._t.start()

    def _start_curveTimer(self): self._t.start()
    def _reload_curveTimer(self):
        self.values = self._getListedValues()
        self.function_dict = {'button_color':  lambda: self._update(self.values, 'button_color'),
                              'text_color':    lambda: self._update(self.values, 'text_color  '),
                              'border_color':  lambda: self._update(self.values, 'border_color'),
                              'width':         lambda: self._update(self.values, 'width_color '),
                              'height':        lambda: self._update(self.values, 'height_color'),
                              'font_size':     lambda: self._update(self.values, 'height_color'),
                              'corner_radius': lambda: self._update(self.values, 'height_color'),
                              'border_width':  lambda: self._update(self.values, 'border_width')
                              }
        self._t.configure(on_tick=self.function_dict.get(self.attribute))

    def _getListedValues(self):
        if self.attribute in ['button_color','text_color','border_color']:
            return GenerateGradient(colours=[self.start_value, self.end_value])
        if self.attribute in ['width', 'height', 'x','y']:
            return self._generate_steps(self.start_value, self.end_value)
        elif self.attribute in ['corner_radius','border_width','font_size']:
            return self._generate_steps(self.start_value, self.end_value, 1)

    def _update(self, values, type):
        self._indexCheck(values)
        if self._index < len(values) - 1:
            self._widget.config(type, values[self._index])

        else: self.stop()

    def _generate_steps(self, start, end, precision = None):
        if precision is None:
            if start <= end:
                return list(range(start, end + 1))
            else: return list(range(start, end - 1, -1))
        else:
            numbers = []
            current_number = start

            while current_number <= end:
                numbers.append(round(current_number, precision))
                current_number += 10 ** (-precision)

            return numbers

    def _indexCheck(self, mainList):
        self._index += self._t.amount_increased()

        if self._index > len(mainList) - 1:
            self._t.stop()
            self._stateTicking = False
    def is_stopped(self): return not self._stateTicking
    def is_ticking(self): return self._stateTicking
    def pause(self):      self._t.pause()
    def unpause(self):    self._t.unpause()



class AnimationGroup:
    def __init__(self,
                 master,
                 animations: list[Animation]):
        self._cgroup = CurveTimerGroup(master)

        self._animationsList = []

        for animation in animations:
            animation._activeInstantly = False
            animation.start()
            self._cgroup.add_timer(animation._t)
            self._animationsList.append(animation)

    def start(self):
        for animation in self._animationsList:
            animation._start_curveTimer()

    def restart(self):
        for animation in self._animationsList:
            animation._reload_curveTimer()
            animation._start_curveTimer()
            animation._start_curveTimer()
