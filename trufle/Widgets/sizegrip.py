from difflib import get_close_matches
from .frame import Frame
from pyautogui import position

def setCursor(master, cursor_id):
    cursor = f'resize {cursor_id}' if cursor_id != 'default' else 'default'
    master.set_cursor(cursor)

class SizeGrip:
    def __init__(self,
                 # Grip attrs
                 master,
                 resize, # Which window to resize on drag.
                 direction='bottom-right',
                 cursor='top-right',
                 # Frame attrs
                 width=50,
                 height=50,
                 frame_color='#5D5D5D',
                 corner_radius=[0,5,5,0],
                 border_width=0,
                 border_color='white',
                 x=None, y=None):
        event = self._getValidEvents(direction)
        self._sg = Frame(master, border_color=border_color, border_width=border_width, frame_color=frame_color, corner_radius=corner_radius, width=width, height=height)
        self._sg.connect(pressed = self._SizeChangeStart, pressed_motion = event, leave_pressed = self._SizeChangeStart,
                         hover = lambda event: setCursor(master, cursor.replace('-',' ')), leave_hover = lambda event: setCursor(master, 'default'))

        self._rs = resize

        if (x,y) != (None,None): self.place(x,y)

    def place(self, x,y): self._sg.place(x,y)
    def _getValidEvents(self, direction):
        return lambda event: self._SizeChanged(direction.split('-'))
    def _SizeChangeStart(self, event):
        self._previous = [position().x, position().y]
        self._winXY = [self._rs.info_x()+1, self._rs.info_y()+31]
        self._winWH = [self._rs.info_width(),self._rs.info_height()]

        print(self._winXY[0], self._winXY[1], self._winWH[0], self._winWH[1])
    def _SizeChanged(self, directions):
        deltaX = (position().x - self._previous[0])
        deltaY = (position().y - self._previous[1])

        self._previous = [position().x, position().y]

        for direction in directions:
            # Static.
            if direction == 'right':
                self._winWH[0] += deltaX
            elif direction == 'left':
                self._winXY[0] += deltaX
                self._winWH[0] -= deltaX
            elif direction == 'bottom':
                self._winWH[1] += deltaY
            elif direction == 'top':
                self._winXY[1] += deltaY
                self._winWH[1] -= deltaY

        self._reloadWindow()
    def _reloadWindow(self):
        winW = max(self._winWH[0], 102)
        winH = max(self._winWH[1], 102)
        winX = max(self._winXY[0], 102)
        winY = max(self._winXY[1], 102)

        self._rs.size(winW,winH,winX,winY)
    def _getMatchEvent(self, direction):
        return lambda: self._SizeChanged(direction.split("-") )
    def _findMatch(self, input_str):
        match_ = get_close_matches(input_str, self._get_valid_directions(), n=1)
        if match_ == [] or match_ is None:
            raise EnvironmentError('Invalid direction!')
        return match_[0]
    def _get_valid_directions(self):
        return ['left','right','up','down',
                'top-left', 'top-right',
                'bottom-left', 'bottom-right']







class SizeGripFrame:
    def __init__(self,
                 # SizeGrip
                 master,
                 resize,
                 # Frame
                 width=300,
                 height=300,
                 frame_color='#2D2D2D',
                 corner_radius=0,
                 border_width=0,
                 border_color='white',
                 x=None,y=None,
                 sizegrips_size = 40):
        self._frame = Frame(master,width=width,height=height,frame_color=frame_color,corner_radius=corner_radius,border_width=border_width,border_color=border_color)

        # Info: Define attributes. (Dynamic to make it concise)
        atts = {'master'      : master,       'resize'       : resize,        'width'       : width,        'height'       : height,
                'frame_color' : frame_color,  'corner_radius': corner_radius, 'border_width': border_width, 'border_color' : border_color}
        for attr, value in atts.items():
            setattr(self, f'attributes_{attr}', value)

        if (x,y) != (None,None): self.place(x,y)

    def _defineSizeGrip(self, direction):
        sizegrip = SizeGrip(self.attributes_master,self.attributes_master,
                            direction=direction)
        sizegrip.place()

    def _calculateDirection(self, direction):
        if direction == 'top':
            pass

    def place(self, x,y): self._frame.place(x,y)