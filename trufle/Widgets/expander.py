from .Utility.animationhandler import Animation, AnimationGroup
from .frame import Frame
from .button import Button

class Expander:
    def __init__(self,
                 master,
                 x=None,y=None,
                 width = 200,
                 height = 300,
                 border_width=0,
                 border_color='white',
                 corner_radius=0,
                 expand_vertically=True,
                 expand_horizontally=False,
                 container_color='transparent',

                 button_icon_color='white',
                 button_icon_size = 9,
                 button_color = '#2d2d2d',
                 button_hover_color = '#424242',
                 button_pressed_color = '#282828',
                 button_icon_alignment='center',
                 button_corner_radius = 'round',
                 button_x=10,
                 button_y=10,
                 button_width=20,
                 button_height=20,

                 unexpanded_height = None,
                 expanded_height = None,
                 unexpanded_width = None,
                 expanded_width = None,

                 animation_duration = 300000,
                 animation_power = 300,
                 animation_extra_speed=0,
                 animation_curve = 'OutElastic',
                 mode = 'vertical',

                 starts_expanded = False,
                 placing_padding = None ):
        if unexpanded_height is None:  unexpanded_height = {'vertical': 40,    'horizontal': height, 'both': 40}    .get(mode)
        if unexpanded_width  is None:  unexpanded_width =  {'vertical': width, 'horizontal': 40,     'both': 40}    .get(mode)
        if expanded_height is None:    expanded_height =   {'vertical': 300,   'horizontal': height, 'both': height}.get(mode)
        if expanded_width  is None:    expanded_width =    {'vertical': width, 'horizontal': 300,    'both': width} .get(mode)

        if placing_padding is None: placing_padding = unexpanded_height
        self._commandsByMode = {'vertical': self.expandVertically,'horizontal': self.expandHorizontally,'both': self.expandBoth}

        self._expander = Frame(master, width={True: expanded_width, False: unexpanded_width}.get(starts_expanded), height={True: expanded_height, False: unexpanded_height}.get(starts_expanded), border_width=border_width, border_color=border_color, corner_radius=corner_radius)
        self._container = Frame(self._expander, corner_radius=0, frame_color=container_color, border_width=0, width=width, height=height - placing_padding)

        """ Info: Attributes """
        self.attributes_master = master
        self.attributes_x                          = x
        self.attributes_y                          = y
        self.attributes_width                      = width
        self.attributes_height                     = height
        self.attributes_border_width               = border_width
        self.attributes_border_color               = border_color
        self.attributes_corner_radius              = corner_radius
        self.attributes_expand_vertically          = expand_vertically
        self.attributes_expand_horizontally        = expand_horizontally
        self.attributes_container_color            = container_color
        self.attributes_button_icon_color          = button_icon_color
        self.attributes_button_icon_size           = button_icon_size
        self.attributes_button_color               = button_color
        self.attributes_button_hover_color         = button_hover_color
        self.attributes_button_pressed_color       = button_pressed_color
        self.attributes_button_icon_alignment      = button_icon_alignment
        self.attributes_button_corner_radius       = button_corner_radius
        self.attributes_button_x                   = button_x
        self.attributes_button_y                   = button_y
        self.attributes_button_width               = button_width
        self.attributes_button_height              = button_height
        self.attributes_unexpanded_height          = unexpanded_height
        self.attributes_expanded_height            = expanded_height
        self.attributes_unexpanded_width           = unexpanded_width
        self.attributes_expanded_width             = expanded_width
        self.attributes_animation_duration         = animation_duration
        self.attributes_animation_power            = animation_power
        self.attributes_animation_extra_speed      = animation_extra_speed
        self.attributes_animation_curve            = animation_curve
        self.attributes_mode                       = mode
        self.attributes_starts_expanded            = starts_expanded
        self.attributes_placing_padding            = placing_padding

        self._expandByMode = Button(self._expander, command=self._commandsByMode.get(mode), pressed_color=button_pressed_color, hover_color=button_hover_color, button_color=button_color, width=button_width, text_alignment=button_icon_alignment, height=button_height, text_color=button_icon_color, corner_radius=button_corner_radius, text='⮟', font_size=button_icon_size)
        self._expandByMode.place(button_x, button_y)

        self._animExpandVer = Animation(self._expander, 'height', unexpanded_height, expanded_height, extra_speed=animation_extra_speed, curve=animation_curve, duration=animation_duration, power=animation_duration)
        self._animExpandHor = Animation(self._expander, 'width',  unexpanded_width,  expanded_width,  extra_speed=animation_extra_speed, curve=animation_curve, duration=animation_duration, power=animation_duration)

        self._animGroupBoth = AnimationGroup(master, [self._animExpandVer, self._animExpandHor])
        if (x,y) != (None,None): self.place(x,y)
    def place(self, x,y):
        self._container.place(0,self.attributes_placing_padding)
        self._expander.place(x,y)
    def expandVertically(self):
        if self._expander.get('height') == self.attributes_expanded_height:
            self._animExpandVer.set_values(self.attributes_expanded_height, self.attributes_unexpanded_height)
        else: self._animExpandVer.set_values(self.attributes_unexpanded_height, self.attributes_expanded_height)

        if self._animExpandVer.is_stopped():
            self._animExpandVer.start()
    def expandHorizontally(self):
        if self._expander.get('width') == self.attributes_expanded_width:
            self._animExpandHor.set_values(self.attributes_expanded_width, self.attributes_unexpanded_width)
        else: self._animExpandHor.set_values(self.attributes_unexpanded_width, self.attributes_expanded_width)
        if self._animExpandHor.is_stopped():
            self._animExpandHor.start()
    def expandBoth(self):
        if self._expander.get('width') == self.attributes_expanded_width:
            self._animExpandHor.set_values(self.attributes_expanded_width, self.attributes_unexpanded_width)
            self._animExpandVer.set_values(self.attributes_expanded_height, self.attributes_unexpanded_height)
        else:
            self._animExpandHor.set_values(self.attributes_unexpanded_width,  self.attributes_expanded_width)
            self._animExpandVer.set_values(self.attributes_unexpanded_height, self.attributes_expanded_height)

        if  self._animExpandHor.is_stopped():

            self._animGroupBoth.reload_animations()
            self._animGroupBoth.start()
    def reload(self):
        if self.attributes_unexpanded_height is None: self.attributes_unexpanded_height = {'vertical': 40,    'horizontal': self.attributes_height, 'both': 40}                    .get(self.attributes_mode)
        if self.attributes_unexpanded_width  is None: self.attributes_unexpanded_width  = {'vertical': self.attributes_width, 'horizontal': 40,     'both': 40}                    .get(self.attributes_mode)
        if self.attributes_expanded_height   is None: self.attributes_expanded_height   = {'vertical': 300,   'horizontal': self.attributes_height, 'both': self.attributes_height}.get(self.attributes_mode)
        if self.attributes_expanded_width    is None: self.attributes_expanded_width    = {'vertical': self.attributes_width, 'horizontal': 300,    'both': self.attributes_width} .get(self.attributes_mode)

        if self.attributes_placing_padding is None: self.attributes_placing_padding = self.attributes_unexpanded_height
        self._commandsByMode = {'vertical': self.expandVertically,'horizontal': self.expandHorizontally,'both': self.expandBoth}

        self._expander.configure(width={True: self.attributes_expanded_width, False: self.attributes_unexpanded_width}.get(self.attributes_starts_expanded), height={True: self.attributes_expanded_height, False: self.attributes_unexpanded_height}.get(self.attributes_starts_expanded), border_width=self.attributes_border_width, border_color=self.attributes_border_color, corner_radius=self.attributes_corner_radius)
        self._container.configure(corner_radius=0, frame_color=self.attributes_container_color, border_width=0, width=self.attributes_width, height=self.attributes_height - self.attributes_placing_padding)
        self._expandByMode.configure(command=self._commandsByMode.get(self.attributes_mode), pressed_color=self.attributes_button_pressed_color, hover_color=self.attributes_button_hover_color, button_color=self.attributes_button_color, width=self.attributes_button_width, text_alignment=self.attributes_button_icon_alignment, height=self.attributes_button_height, text_color=self.attributes_button_icon_color, corner_radius=self.attributes_button_corner_radius, text='⮟', font_size=self.attributes_button_icon_size)
        self._expandByMode.place(self.attributes_button_x, self.attributes_button_y)

        self._animExpandVer.set_settings(extra_speed=self.attributes_animation_extra_speed, curve=self.attributes_animation_curve, duration=self.attributes_animation_duration, power=self.attributes_animation_duration)
        self._animExpandHor.set_settings(extra_speed=self.attributes_animation_extra_speed, curve=self.attributes_animation_curve, duration=self.attributes_animation_duration, power=self.attributes_animation_duration)
    def configure(self,
                  width                    = None,
                  height                   = None,
                  border_width             = None,
                  border_color             = None,
                  corner_radius            = None,
                  expand_vertically        = None,
                  expand_horizontally      = None,
                  container_color          = None,
                  button_icon_color        = None,
                  button_icon_size         = None,
                  button_color             = None,
                  button_hover_color       = None,
                  button_pressed_color     = None,
                  button_icon_alignment    = None,
                  button_corner_radius     = None,
                  button_x                 = None,
                  button_y                 = None,
                  button_width             = None,
                  button_height            = None,
                  unexpanded_height        = None,
                  expanded_height          = None,
                  unexpanded_width         = None,
                  expanded_width           = None,
                  animation_duration       = None,
                  animation_power          = None,
                  animation_extra_speed    = None,
                  animation_curve          = None,
                  mode                     = None,
                  starts_expanded          = None,
                  placing_padding          = None):
        if width is not None:                 self.attributes_width                 = width
        if height is not None:                self.attributes_height                = height
        if border_width is not None:          self.attributes_border_width          = border_width
        if border_color is not None:          self.attributes_border_color          = border_color
        if corner_radius is not None:         self.attributes_corner_radius         = corner_radius
        if expand_vertically is not None:     self.attributes_expand_vertically     = expand_vertically
        if expand_horizontally is not None:   self.attributes_expand_horizontally   = expand_horizontally
        if container_color is not None:       self.attributes_container_color       = container_color
        if button_icon_color is not None:     self.attributes_button_icon_color     = button_icon_color
        if button_icon_size is not None:      self.attributes_button_icon_size      = button_icon_size
        if button_color is not None:          self.attributes_button_color          = button_color
        if button_hover_color is not None:    self.attributes_button_hover_color    = button_hover_color
        if button_pressed_color is not None:  self.attributes_button_pressed_color  = button_pressed_color
        if button_icon_alignment is not None: self.attributes_button_icon_alignment = button_icon_alignment
        if button_corner_radius is not None:  self.attributes_button_corner_radius  = button_corner_radius
        if button_x is not None:              self.attributes_button_x              = button_x
        if button_y is not None:              self.attributes_button_y              = button_y
        if button_width is not None:          self.attributes_button_width          = button_width
        if button_height is not None:         self.attributes_button_height         = button_height
        if unexpanded_height is not None:     self.attributes_unexpanded_height     = unexpanded_height
        if expanded_height is not None:       self.attributes_expanded_height       = expanded_height
        if unexpanded_width is not None:      self.attributes_unexpanded_width      = unexpanded_width
        if expanded_width is not None:        self.attributes_expanded_width        = expanded_width
        if animation_duration is not None:    self.attributes_animation_duration    = animation_duration
        if animation_power is not None:       self.attributes_animation_power       = animation_power
        if animation_extra_speed is not None: self.attributes_animation_extra_speed = animation_extra_speed
        if animation_curve is not None:       self.attributes_animation_curve       = animation_curve
        if mode is not None:                  self.attributes_mode                  = mode
        if starts_expanded is not None:       self.attributes_starts_expanded       = starts_expanded
        if placing_padding is not None:       self.attributes_placing_padding       = placing_padding
        self.reload()
    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'width':                 self.attributes_width                 = new_value
            case 'height':                self.attributes_height                = new_value
            case 'border_width':          self.attributes_border_width          = new_value
            case 'border_color':          self.attributes_border_color          = new_value
            case 'corner_radius':         self.attributes_corner_radius         = new_value
            case 'expand_vertically':     self.attributes_expand_vertically     = new_value
            case 'expand_horizontally':   self.attributes_expand_horizontally   = new_value
            case 'container_color':       self.attributes_container_color       = new_value
            case 'button_icon_color':     self.attributes_button_icon_color     = new_value
            case 'button_icon_size':      self.attributes_button_icon_size      = new_value
            case 'button_color':          self.attributes_button_color          = new_value
            case 'button_hover_color':    self.attributes_button_hover_color    = new_value
            case 'button_pressed_color':  self.attributes_button_pressed_color  = new_value
            case 'button_icon_alignment': self.attributes_button_icon_alignment = new_value
            case 'button_corner_radius':  self.attributes_button_corner_radius  = new_value
            case 'button_x':              self.attributes_button_x              = new_value
            case 'button_y':              self.attributes_button_y              = new_value
            case 'button_width':          self.attributes_button_width          = new_value
            case 'button_height':         self.attributes_button_height         = new_value
            case 'unexpanded_height':     self.attributes_unexpanded_height     = new_value
            case 'expanded_height':       self.attributes_expanded_height       = new_value
            case 'unexpanded_width':      self.attributes_unexpanded_width      = new_value
            case 'expanded_width':        self.attributes_expanded_width        = new_value
            case 'animation_duration':    self.attributes_animation_duration    = new_value
            case 'animation_power':       self.attributes_animation_power       = new_value
            case 'animation_extra_speed': self.attributes_animation_extra_speed = new_value
            case 'animation_curve':       self.attributes_animation_curve       = new_value
            case 'mode':                  self.attributes_mode                  = new_value
            case 'starts_expanded':       self.attributes_starts_expanded       = new_value
            case 'placing_padding':       self.attributes_placing_padding       = new_value
            case 'x':                     self.place(new_value, self.info_y())
            case 'y':                     self.place(self.info_x(), new_value)
        self.reload()
    def _getM(self): return self._container._getM()
    def info_x(self): return self._expander.info_x()
    def info_y(self): return self._expander.info_y()

    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self._expander.enterEvent         = hover
        if leave_hover   is not None:  self._expander.leaveEvent         = leave_hover
        if pressed       is not None:  self._expander.mousePressEvent    = pressed
        if leave_pressed is not None:  self._expander.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self._expander.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self._expander.wheelEvent         = scroll