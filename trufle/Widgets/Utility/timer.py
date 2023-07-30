from PyQt5.QtCore import QTimer, QVariantAnimation, QEasingCurve, QPoint
from PyQt5.QtWidgets import QLabel

class Timer:
    def __init__(self,
                 master,
                 wait_time = 250,
                 on_tick      = lambda: ...):
        self._timer = QTimer(master._getM())
        self._timer.setInterval(wait_time)
        self._timer.timeout.connect(on_tick)

    def start(self, lasts_for = None):
        self._timer.start()
        if lasts_for is not None: self._timer.singleShot(lasts_for, self._timer.stop)

    def stop(self):
        self._timer.stop()

    def is_ticking(self):
        return self._timer.isActive()

    def is_stopped(self):
        return not self._timer.isActive()

curveDict = {
    'Linear': QEasingCurve.Linear,
    'InQuad': QEasingCurve.InQuad,
    'OutQuad': QEasingCurve.OutQuad,
    'InOutQuad': QEasingCurve.InOutQuad,
    'OutInQuad': QEasingCurve.OutInQuad,
    'InCubic': QEasingCurve.InCubic,
    'OutCubic': QEasingCurve.OutCubic,
    'InOutCubic': QEasingCurve.InOutCubic,
    'OutInCubic': QEasingCurve.OutInCubic,
    'InQuart': QEasingCurve.InQuart,
    'OutQuart': QEasingCurve.OutQuart,
    'InOutQuart': QEasingCurve.InOutQuart,
    'OutInQuart': QEasingCurve.OutInQuart,
    'InQuint': QEasingCurve.InQuint,
    'OutQuint': QEasingCurve.OutQuint,
    'InOutQuint': QEasingCurve.InOutQuint,
    'OutInQuint': QEasingCurve.OutInQuint,
    'InSine': QEasingCurve.InSine,
    'OutSine': QEasingCurve.OutSine,
    'InOutSine': QEasingCurve.InOutSine,
    'OutInSine': QEasingCurve.OutInSine,
    'InExpo': QEasingCurve.InExpo,
    'OutExpo': QEasingCurve.OutExpo,
    'InOutExpo': QEasingCurve.InOutExpo,
    'OutInExpo': QEasingCurve.OutInExpo,
    'InCirc': QEasingCurve.InCirc,
    'OutCirc': QEasingCurve.OutCirc,
    'InOutCirc': QEasingCurve.InOutCirc,
    'OutInCirc': QEasingCurve.OutInCirc,
    'InElastic': QEasingCurve.InElastic,
    'OutElastic': QEasingCurve.OutElastic,
    'InOutElastic': QEasingCurve.InOutElastic,
    'OutInElastic': QEasingCurve.OutInElastic,
    'InBack': QEasingCurve.InBack,
    'OutBack': QEasingCurve.OutBack,
    'InOutBack': QEasingCurve.InOutBack,
    'OutInBack': QEasingCurve.OutInBack,
    'InBounce': QEasingCurve.InBounce,
    'OutBounce': QEasingCurve.OutBounce,
    'InOutBounce': QEasingCurve.InOutBounce,
    'OutInBounce': QEasingCurve.OutInBounce }


class CurveTimer:
    def __init__(self, master,
                 curve = 'Linear',
                 speed = 100,
                 power = 600,
                 duration = 800,
                 on_tick = lambda:...):
        easing_curve = QEasingCurve(curveDict.get(curve, 'Nothing found.'))
        if easing_curve == 'Nothing found.': raise ValueError(f'Invalid Curve "{curve}"!')

        self.animation = QVariantAnimation()
        self.animation.setStartValue(0)
        self.animation.setEndValue(power)
        self.animation.setDuration(duration)
        self.animation.valueChanged.connect(lambda: self._callTick(on_tick) )
        self.animation.setEasingCurve(easing_curve)
        self._oldValue = self.animation.currentValue()
        self._mode = 'up'

    def configure(self,
                  curve = None,
                  speed = None,
                  power = None,
                  duration = None,
                  on_tick = None):
        self.animation.setStartValue(0)
        if power is not None:    self.animation.setEndValue(power)
        if duration is not None: self.animation.setDuration(duration)
        if on_tick is not None:  self.animation.valueChanged = lambda: self._callTick(on_tick)
        if curve is not None:
            easing_curve = QEasingCurve(curveDict.get(curve, 'Nothing found.'))
            if easing_curve == 'Nothing found.': raise ValueError(f'Invalid Curve "{curve}"!')
            self.animation.setEasingCurve(easing_curve)

    def _callTick(self, func):
        func()
        if self._oldValue < self.animation.currentValue():
            self._mode = 'up'
            self._oldValue = self.animation.currentValue()
        else:
            self._mode = 'down'
            self._oldValue = self.animation.currentValue()

    def amount_increased(self): return self.animation.currentValue() - self._oldValue
    def is_going_down(self):    return True if self._mode == 'down' else False
    def is_going_up(self):      return True if self._mode == 'up' else False
    def direction(self):        return self._mode
    def start(self):            self.animation.start()
    def stop(self):             self.animation.stop()
    def finish(self):           self.animation.stop(); del self.animation
    def value(self):            return self.animation.currentValue()
    def is_ticking(self):       return bool(self.animation.state())
    def is_stopped(self):       return not bool(self.animation.state())
    def pause(self):            self.animation.setPaused(True)
    def unpause(self):          self.animation.setPaused(False)


from PyQt5.QtCore import QParallelAnimationGroup

class CurveTimerGroup:
    def __init__(self,
                 master,
                 timers = []):
        self._parallel = QParallelAnimationGroup(master._getM() )
        self._timers = timers

    def add_timer(self, timer): self._timers.append(timer)

    def start(self):
        for timer in self._timers:
            self._parallel.addAnimation(timer.animation)
        self._parallel.start()

    def stop(self):
        self._parallel.stop()