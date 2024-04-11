from .frame import Frame
from .button import Button

class ProgressBar:
    def __init__(self,
                 master,
                 width=200,
                 value_range=(0,100),
                 start_value=100,
                 height=30,
                 border_width=1,
                 corner_radius=2,
                 border_color='white',
                 progressbar_color='white',

                 progress_padding=1,
                 progress_height=None,
                 progress_corner_radius=None,
                 progress_color='#3FAD44',
                 progress_hover_color   =None,
                 progress_pressed_color =None,

                 x=None,y=None):
        if progress_hover_color is None: progress_hover_color = progress_color
        if progress_pressed_color is None: progress_pressed_color = progress_color
        if progress_height is None: progress_height = height
        if progress_corner_radius is None:
            progress_corner_radius = [corner_radius,0,corner_radius,0] if start_value < value_range[1] else [corner_radius,corner_radius,corner_radius,corner_radius]

        self.attributes_master                 = master
        self.attributes_width                  = width
        self.attributes_value_range            = value_range
        self.attributes_start_value            = start_value
        self.attributes_height                 = height
        self.attributes_border_width           = border_width
        self.attributes_corner_radius          = corner_radius
        self.attributes_border_color           = border_color
        self.attributes_progressbar_color      = progressbar_color
        self.attributes_progress_padding       = progress_padding
        self.attributes_progress_height        = progress_height
        self.attributes_progress_corner_radius = progress_corner_radius
        self.attributes_progress_color         = progress_color

        self._current_value = start_value

        self._frame = Frame(master, width=width,height=height,border_width=border_width,frame_color=progressbar_color,border_color=border_color,corner_radius=corner_radius)
        self._progress = Button(master, hover_color=progress_hover_color, pressed_color=progress_pressed_color, button_color=progress_color, text='',width=self._get_button_width(value_range,start_value,width),
                                height=progress_height - (progress_padding*2), corner_radius=progress_corner_radius)

        if (x,y) != (None,None): self.place(x,y)

    def place(self, x,y):
        self._progress.place(x+self.attributes_progress_padding,y+self.attributes_progress_padding)
        self._frame.place(x,y)

    def set_value(self, new_value):
        self._current_value = new_value
        self._progress.configure(width=self._get_button_width(self.attributes_value_range,new_value,self.attributes_width))

    def get_value(self):
        return self._current_value

    def _get_button_width(self, ranges, start_value, progressbar_width):
        assert not start_value > self.attributes_value_range[1], 'starting value or current progress cannot be higher than value limit.'
        completion_percentage = (start_value - ranges[0]) / (ranges[1] - ranges[0])
        result = int(progressbar_width * completion_percentage) - (self.attributes_progress_padding*2)
        return result

    def reload(self):
        if self.attributes_progress_hover_color is None:   self.attributes_progress_hover_color   = self.attributes_progress_color
        if self.attributes_progress_pressed_color is None: self.attributes_progress_pressed_color = self.attributes_progress_color
        if self.attributes_progress_height is None:        self.attributes_progress_height = self.attributes_height
        if self.attributes_progress_corner_radius is None: self.attributes_progress_corner_radius = [self.attributes_corner_radius,0,self.attributes_corner_radius,0] if self.attributes_start_value < self.attributes_value_range[1] else [self.attributes_corner_radius,self.attributes_corner_radius,self.attributes_corner_radius,self.attributes_corner_radius]

        self._frame.configure(width=self.attributes_width,height=self.attributes_height,border_width=self.attributes_border_width,frame_color=self.attributes_progressbar_color,border_color=self.attributes_border_color,corner_radius=self.attributes_corner_radius)
        self._progress.configure(button_color=self.attributes_progress_color, text='',width=self._get_button_width(self.attributes_value_range,self.attributes_start_value,self.attributes_width),
                                height=self.attributes_progress_height - (self.attributes_progress_padding*2), corner_radius=self.attributes_progress_corner_radius)

    def configure(self,
                 width                  = None,
                 value_range            = None,
                 start_value            = None,
                 height                 = None,
                 border_width           = None,
                 corner_radius          = None,
                 border_color           = None,
                 progressbar_color      = None,

                 progress_padding       = None,
                 progress_height        = None,
                 progress_corner_radius = None,
                 progress_color         = None):
        if width is not None:                  self.attributes_width                  = width
        if value_range is not None:            self.attributes_value_range            = value_range
        if start_value is not None:            self.attributes_start_value            = start_value
        if height is not None:                 self.attributes_height                 = height
        if border_width is not None:           self.attributes_border_width           = border_width
        if corner_radius is not None:          self.attributes_corner_radius          = corner_radius
        if border_color is not None:           self.attributes_border_color           = border_color
        if progressbar_color is not None:      self.attributes_progressbar_color      = progressbar_color
        if progress_padding is not None:       self.attributes_progress_padding       = progress_padding
        if progress_height is not None:        self.attributes_progress_height        = progress_height
        if progress_corner_radius is not None: self.attributes_progress_corner_radius = progress_corner_radius
        if progress_color is not None:         self.attributes_progress_color         = progress_color
        self.reload()

    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'width':                  self.attributes_width                  = new_value
            case 'value_range':            self.attributes_value_range            = new_value
            case 'start_value':            self.attributes_start_value            = new_value
            case 'height':                 self.attributes_height                 = new_value
            case 'border_width':           self.attributes_border_width           = new_value
            case 'corner_radius':          self.attributes_corner_radius          = new_value
            case 'border_color':           self.attributes_border_color           = new_value
            case 'progressbar_color':      self.attributes_progressbar_color      = new_value
            case 'progress_padding':       self.attributes_progress_padding       = new_value
            case 'progress_height':        self.attributes_progress_height        = new_value
            case 'progress_corner_radius': self.attributes_progress_corner_radius = new_value
            case 'progress_color':         self.attributes_progress_color         = new_value
            case 'x': self.place(new_value, self.info_y())
            case 'y': self.place(self.info_x(), new_value)
        self.reload()

    def info_x(self): return self._frame.info_x()
    def info_y(self): return self._frame.info_y()

    def get(self, attribute_name):
        attributes_dict = {
                          'width':                  self.attributes_width,
                          'value_range':            self.attributes_value_range,
                          'start_value':            self.attributes_start_value,
                          'height':                 self.attributes_height,
                          'border_width':           self.attributes_border_width,
                          'corner_radius':          self.attributes_corner_radius,
                          'border_color':           self.attributes_border_color,
                          'progressbar_color':      self.attributes_progressbar_color,
                          'progress_padding':       self.attributes_progress_padding,
                          'progress_height':        self.attributes_progress_height,
                          'progress_corner_radius': self.attributes_progress_corner_radius,
                          'progress_color':         self.attributes_progress_color}
        return attributes_dict.get(attribute_name)
