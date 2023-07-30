from .gradientgen import GenerateGradient
from .timer import CurveTimer, CurveTimerGroup
from numpy import minimum as np_minimum

class Animation:
    def __init__(self, widget, attribute,
                 start_value=None, end_value=None,
                 curve = 'Linear', duration = 3000,
                 power = 255, extra_speed = 0):
        self.curve, self.attribute = curve, attribute
        self._widget, self.duration = widget, duration
        self.power = power
        self.extra_speed = extra_speed

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
    def set_values(self, start_value, end_value):
        self.start_value = start_value
        self.end_value = end_value
    def set_settings(self, duration=None,power=None,extra_speed=None,curve=None):
        if duration    is not None: self.duration    = duration
        if power       is not None: self.power       = power
        if extra_speed is not None: self.extra_speed = extra_speed
        if curve       is not None: self.curve       = curve
        self._reload_curveTimer()
    def start(self):
        self._handleWidget()
        self._stateTicking = True
    def restart(self):
        self.stop()
        self.start()
    def stop(self):
        try:
            self._index = 0
            self._t.stop()
            self._widget.config(self.attribute, self.end_value)
            self._stateTicking = False
            self.event_timeout()
        except: pass
    def _handleWidget(self):
        self.values = self._getListedValues()

        self._t = CurveTimer(self._master, duration=self.duration, power=self.power, curve=self.curve, on_tick=lambda: self._update(self.values, self.attribute))
        if self._activeInstantly: self._t.start()
    def _contains(self, value, contains):
        for string in contains:
            if string in value:
                return True
        return False
    def _define_curveTimer(self):
        self.values = self._getListedValues()
        self._t = CurveTimer(self._master, duration=self.duration, power=self.power, curve=self.curve, on_tick=lambda: self._update(self.values, self.attribute))
    def _start_curveTimer(self): self._t.start(); self._stateTicking = True
    def _reload_curveTimer(self):
        self.values = self._getListedValues()
        self._t.configure(on_tick=lambda: self._update(self.values, self.attribute) )
    def _getListedValues(self):
        if 'color' in self.attribute:
            return GenerateGradient(colours=[self.start_value, self.end_value])
        elif self._contains(self.attribute, ['width', 'height', 'x','y', 'font_size']):
            return self._generate_steps(self.start_value, self.end_value)
        elif self.attribute == 'corner_radius':
            return self._getGradualBw(self.start_value, self.end_value)
    def _getHighestNum(self, *lists):
        return max([num for sublist in lists for num in sublist])
    def _combine_lists(self, list1, list2, list3, list4):
        output = []
        for i in range(self._getHighestNum(list1,list2,list3,list4)):
            num1 = list1[i] if i < len(list1) else list1[len(list1) - 1]
            num2 = list2[i] if i < len(list2) else list2[len(list2) - 1]
            num3 = list3[i] if i < len(list3) else list3[len(list3) - 1]
            num4 = list4[i] if i < len(list4) else list4[len(list4) - 1]
            newList = [num1, num2, num3, num4]
            output.append(newList)
        return output
    def _getGradualBw(self, bw1, bw2):
        if type(bw1) == int: bw1 = [bw1,bw1,bw1,bw1]
        if type(bw2) == int: bw2 = [bw2,bw2,bw2,bw2]

        result = []
        for i, fromCorner in enumerate(bw1):
            toCorner = bw2[i]
            listedCorners = self._generate_steps(fromCorner, toCorner)
            result.append(listedCorners)
        combined = self._combine_lists(result[0], result[1], result[2], result[3])
        return combined
    def _update(self, values, type):
        self._indexCheck(values)
        if self._index < len(values) - 1:
            self._widget.config(type, values[self._index])
        else:
            self.stop()
    def _generate_steps(self, start, end):
        if start <= end:
            return list(range(start, end + 1))
        else: return list(range(start, end - 1, -1))
    def _indexCheck(self, mainList):
        self._index += self._t.amount_increased() + self.extra_speed

        if self._index > len(mainList) - 1:
            self._t.stop()
            self.event_timeout()
            self._stateTicking = False
    def is_stopped(self): return not self._stateTicking
    def is_ticking(self): return self._stateTicking
    def pause(self):      self._t.pause()
    def unpause(self):    self._t.unpause()
    def event_timeout(self): pass

class AnimationGroup:
    def __init__(self,
                 master,
                 animations: list[Animation]):
        self.animations = animations
        self._cgroup = CurveTimerGroup(master)
        self.master = master

        self._animationsList = []

        for animation in animations:
            try: animation._define_curveTimer()
            except AttributeError:
                raise ValueError('All animations must have their start and end values defined before an making animation group.\n')

            self._cgroup.add_timer(animation._t)
            self._animationsList.append(animation)

        self._ranOnce = False
    def start(self):
        for animation in self._animationsList:
            animation._t.start()
        self._ranOnce = True
    def autostart(self):
        if self._ranOnce:
            self.restart()
        else: self.start()
    def restart(self):
        for animation in self._animationsList:
            animation._reload_curveTimer()
            animation._start_curveTimer()
            animation._start_curveTimer()
    def change_animations(self, new_animations):
        self.animations = new_animations
        self._cgroup = CurveTimerGroup(self.master)

        self._animationsList = []

        for animation in new_animations:
            animation._activeInstantly = False

            try: animation.start()
            except AttributeError:
                raise ValueError('All animations must have their start and end values defined before an reloading animation group.\n')

            self._cgroup.add_timer(animation._t)
            self._animationsList.append(animation)
    def reload_animations(self):
        self._cgroup = CurveTimerGroup(self.master)

        self._animationsList = []

        for animation in self.animations:
            animation._activeInstantly = False

            try: animation.start()
            except AttributeError:
                raise ValueError('All animations must have their start and end values defined before an updating animation group.\n')

            self._cgroup.add_timer(animation._t)
            self._animationsList.append(animation)
    def is_animations_stopped(self):
        is_stopped = []
        for anim in self.animations:
            is_stopped.append(anim.is_stopped())
        return all(is_stopped)