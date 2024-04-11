from difflib import get_close_matches

import attrs.filters

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

                 # x,y
                 x=None, y=None):
        event = self._getValidEvents(direction)
        self._sg = Frame(master, border_color=border_color, border_width=border_width, frame_color=frame_color, corner_radius=corner_radius, width=width, height=height)
        self._sg.connect(pressed = self._SizeChangeStart, pressed_motion = event, leave_pressed = self._SizeChangeStart,
                         hover = lambda event: setCursor(master, cursor.replace('-',' ')), leave_hover = lambda event: setCursor(master, 'default'))
        self._rs = resize

        attributes = {'master':master,'resize':resize,'direction':direction,'cursor':cursor,'width':width,'height':height,'frame_color':frame_color,'corner_radius':corner_radius,'border_width':border_width,'border_color':border_color}
        for attrName, value in attributes.items(): setattr(self, f'attributes_{attrName}', value)

        if (x,y) != (None,None): self.place(x,y)

    # config methods
    def config(self, attribute_name, new_value):
        setattr(self, f'attribute_{attribute_name}', new_value)

    def configure(self,
                  direction     = None,
                  cursor        = None,
                  width         = None,
                  height        = None,
                  frame_color   = None,
                  corner_radius = None,
                  border_width  = None,
                  border_color  = None):
        attributes_dict = {'direction':direction,'cursor':cursor,'width':width,'height':height,'frame_color':frame_color,
                           'corner_radius':corner_radius,'border_width':border_width,'border_color':border_color}

        for attrName, value in attributes_dict.items():
            if value is not None:
                setattr(self, f'attributes_{attrName}', value)
        self.reload()

    # other methods
    def reload(self):
        event = self._getValidEvents(self.attributes_direction)
        self._sg.configure(border_color=self.attributes_border_color, border_width=self.attributes_border_width, frame_color=self.attributes_frame_color,
                         corner_radius=self.attributes_corner_radius, width=self.attributes_width, height=self.attributes_height)
        self._sg.connect(pressed=self._SizeChangeStart, pressed_motion=event, leave_pressed=self._SizeChangeStart,
                         hover=lambda event: setCursor(self.attributes_master, self.attributes_cursor.replace('-', ' ')),
                         leave_hover=lambda event: setCursor(self.attributes_master, 'default'))

    def place(self, x,y): self._sg.place(x,y)
    def _getValidEvents(self, direction):
        return lambda event: self._SizeChanged(direction.split('-'))
    def _SizeChangeStart(self, event):
        self._previous = [position().x, position().y]
        self._winXY = [self._rs.info_x()+1, self._rs.info_y()+31]
        self._winWH = [self._rs.info_width(),self._rs.info_height()]
    def _SizeChanged(self, directions):
        deltaX = (position().x - self._previous[0])
        deltaY = (position().y - self._previous[1])

        self._previous = [position().x, position().y]

        for direction in directions:
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

        self._evResized()
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
    def _evResized(self):pass

    def connect(self, resized=None, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if resized is not None: self._evResized = resized
        self._sg.connect(hover=hover,leave_hover=leave_hover,pressed=pressed,leave_pressed=leave_pressed, pressed_motion=pressed_motion,scroll=scroll)







class SizeGripFrame:
    def __init__(self,
                 # SizeGrip
                 master,
                 resize,
                 # Frame
                 width=300,
                 height=300,
                 frame_color='#2D2D2D',
                 corner_radius=10,
                 border_width=0,
                 border_color='white',

                 # Pos Grip attrs.
                 sizegrips_size = 40,
                 sizegrips_color='transparent',
                 sizegrips_corner_radius=0,
                 sizegrips_border_width=0,
                 sizegrips_border_color='white',

                 x=None,y=None):
        self._frame = Frame(master,width=width,height=height,frame_color=frame_color,corner_radius=corner_radius,border_width=border_width,border_color=border_color)

        # Info: Define attributes. (Dynamic to make it concise)
        atts = {'master'      :   master,       'resize'       : resize,        'width'       : width,        'height'       : height,
                'frame_color' :   frame_color,  'corner_radius': corner_radius, 'border_width': border_width, 'border_color' : border_color,
                'sizegrips_size': sizegrips_size, 'sizegrips_color':sizegrips_color, 'sizegrips_corner_radius':sizegrips_corner_radius,'sizegrips_border_width':sizegrips_border_width,'sizegrips_border_color':sizegrips_border_color}
        for attr, value in atts.items():
            setattr(self, f'attributes_{attr}', value)

        # Info: Define sizegrips.
        directions = ['top-left','top-right','bottom-left','bottom-right',
                      'top','bottom','left','right']
        for i in range(8):
            self._defineSizeGrip(directions[i])

        if (x,y) != (None,None): self.place(x,y)

    def _defineSizeGrip(self, direction):
        width_dictionary = {'top':self.attributes_width - (self.attributes_sizegrips_size*2), 'bottom':(self.attributes_width - self.attributes_sizegrips_size*2)}
        height_dictionary = {'left':self.attributes_height - (self.attributes_sizegrips_size*2), 'right':(self.attributes_height - self.attributes_sizegrips_size*2)}

        sizegrip = SizeGrip(self.attributes_master,self.attributes_resize, border_width=self.attributes_sizegrips_border_width, border_color=self.attributes_sizegrips_border_color, cursor=direction, frame_color=self.attributes_sizegrips_color, corner_radius=self.attributes_sizegrips_corner_radius,
                            direction=direction, width=width_dictionary.get(direction, self.attributes_sizegrips_size),
                            height=height_dictionary.get(direction, self.attributes_sizegrips_size))
        sizegrip.place(self._calculateDirection(direction)[0],self._calculateDirection(direction)[1])
        setattr(self, f'_sg_{direction.replace("-","")}', sizegrip)
    def _calculateDirection(self, direction):
        match direction:
            case 'top':          return self.attributes_sizegrips_size,0
            case 'bottom':       return self.attributes_sizegrips_size,self.attributes_height - self.attributes_sizegrips_size
            case 'right':        return self.attributes_width - self.attributes_sizegrips_size,self.attributes_sizegrips_size
            case 'left':         return 0,self.attributes_sizegrips_size,
            case 'top-left':     return 0,0
            case 'top-right':    return self.attributes_width - self.attributes_sizegrips_size, 0
            case 'bottom-left':  return 0,self.attributes_height - self.attributes_sizegrips_size
            case 'bottom-right': return self.attributes_width - self.attributes_sizegrips_size,self.attributes_height - self.attributes_sizegrips_size
    def connect(self, resized=None, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if resized is not None:
            for grip in [self._sg_topleft,self._sg_topright, self._sg_bottomleft, self._sg_bottomright, self._sg_top, self._sg_left, self._sg_right, self._sg_bottom]:
                grip.connect(resized=resized)
        self._sg.connect(hover=hover, leave_hover=leave_hover, pressed=pressed, leave_pressed=leave_pressed,
                         pressed_motion=pressed_motion, scroll=scroll)

    def place(self, x,y): self._frame.place(x,y)
    def configure(self,
                  width         = None,
                  height        = None,
                  frame_color   = None,
                  corner_radius = None,
                  border_width  = None,
                  border_color  = None,
                  sizegrips_size= None):
        attributes_dictionary = {'width':width,'height':height,'frame_color':frame_color,'corner_radius':corner_radius,'border_width':border_width,'border_color':border_color,'sizegrips_size':sizegrips_size}
        for attribute_name, value in attributes_dictionary.items():
            if value is not None:
                setattr(self, f'attributes_{attribute_name}', value)
        self.reload()
    def reload(self):
        self._frame.configure(width=self.attributes_width,height=self.attributes_height,frame_color=self.attributes_frame_color,corner_radius=self.attributes_corner_radius,border_width=self.attributes_border_width,border_color=self.attributes_border_color)
        atts = {'master'      :   self.attributes_master,       'resize'       : self.attributes_resize,        'width'       : self.attributes_width,        'height'       : self.attributes_height,
                'frame_color' :   self.attributes_frame_color,  'corner_radius': self.attributes_corner_radius, 'border_width': self.attributes_border_width, 'border_color' : self.attributes_border_color,
                'sizegrips_size': self.attributes_sizegrips_size}

        for attr, value in atts.items():
            setattr(self, f'attributes_{attr}', value)

        directions = ['top-left','top-right','bottom-left','bottom-right',
                      'top','bottom','left','right']

        for i in range(8):
            self._reloadSizeGrip(directions[i])
    def _reloadSizeGrip(self, direction):
        colors_dictionary = {'top-left':'red','top-right':'green','bottom-left':'yellow','bottom-right':'black', 'top':'purple','bottom':'lightblue','left':'orange','right':'pink'}
        width_dictionary = {'top':self.attributes_width - (self.attributes_sizegrips_size*2), 'bottom':(self.attributes_width - self.attributes_sizegrips_size*2)}
        height_dictionary = {'left':self.attributes_height - (self.attributes_sizegrips_size*2), 'right':(self.attributes_height - self.attributes_sizegrips_size*2)}

        sizegrip = getattr(self, f'_sg_{direction.replace("-","")}')
        sizegrip.configure(border_width=self.attributes_sizegrips_border_width, border_color=self.attributes_sizegrips_border_color, cursor=direction, frame_color=self.attributes_sizegrips_color, corner_radius=self.attributes_sizegrips_corner_radius,
                            direction=direction, width=width_dictionary.get(direction, self.attributes_sizegrips_size),
                            height=height_dictionary.get(direction, self.attributes_sizegrips_size))
        sizegrip.place(self._calculateDirection(direction)[0],self._calculateDirection(direction)[1])

    def get(self, attribute_name):
        attributes_dict = {
                width                   : self.attributes_width,
                height                  : self.attributes_height,
                frame_color             : self.attributes_frame_color,
                corner_radius           : self.attributes_corner_radius,
                border_width            : self.attributes_border_width,
                border_color            : self.attributes_border_color,
                sizegrips_size          : self.attributes_sizegrips_size,
                sizegrips_color         : self.attributes_sizegrips_color,
                sizegrips_corner_radius : self.attributes_sizegrips_corner_radius,
                sizegrips_border_width  : self.attributes_sizegrips_border_width,
                sizegrips_border_color  : self.attributes_sizegrips_border_color}
        return attributes_dict.get(attribute_name)

    def info_x(self): return self._frame.info_x()
    def info_y(self): return self._frame.info_y()