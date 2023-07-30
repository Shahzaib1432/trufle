from .frame import Frame
from .button import Button
from PyQt5.QtGui import QWheelEvent

class ScrollableFrame:
    def __init__(self,
                 master,
                 # Functionality
                 width = 300,
                 height = 300,
                 scrollbar_width = 10,
                 scrollbar_height = None,
                 scrollbar_alignment='right',
                 content_height_limit = 700,
                 padding = 10,
                 scroll_speed=10, # The higher the value, the slower the wheel moves

                 # Styling Frame
                 frame_border_width=2,
                 frame_border_color='white',
                 frame_color='#2d2d2d',
                 frame_corner_radius=3,
                 # Styling Button
                 scrollbar_color='#E43F3F',
                 scrollbar_hover_color='#e02525',
                 scrollbar_pressed_color='#cc1d1d',
                 scrollbar_border_width=0,
                 scrollbar_border_color='white',
                 scrollbar_corner_radius=5,
                 scrollbar_state='enabled',
                 scrollbar_can_hover=True
                 ):

        self._frame = Frame(master, corner_radius=frame_corner_radius, border_width=frame_border_width, frame_color=frame_color, width=width, height=height)
        self._content = Frame(self._frame, width=width, height=content_height_limit, border_width=0, frame_color='transparent')
        self._moveButton = Button(self._frame, can_hover=scrollbar_can_hover, border_width=scrollbar_border_width, border_color=scrollbar_border_color, corner_radius=scrollbar_corner_radius, state=scrollbar_state, button_color=scrollbar_color, hover_color=scrollbar_hover_color, pressed_color=scrollbar_pressed_color, text='', width=scrollbar_width, height={None:height - (padding*2)}.get(scrollbar_height,scrollbar_height))
        self._moveButton.connect(pressed=self._dragPressEvent, pressed_motion=self._dragEvent, leave_pressed=self._setButtonColorBack)
        self._content.connect(scroll=self._scrollEvent)

        # Define a dictionary to store attribute names and values
        atts = {
            'master': master, 'width': width, 'height': height, 'scrollbar_width': scrollbar_width, 'scrollbar_height': scrollbar_height, 'scrollbar_alignment': scrollbar_alignment, 'content_height_limit': content_height_limit, 'padding': padding, 'scroll_speed': scroll_speed, 'frame_border_width': frame_border_width, 'frame_border_color': frame_border_color, 'frame_color': frame_color, 'frame_corner_radius': frame_corner_radius, 'scrollbar_color': scrollbar_color, 'scrollbar_hover_color': scrollbar_hover_color, 'scrollbar_pressed_color': scrollbar_pressed_color, 'scrollbar_border_width': scrollbar_border_width, 'scrollbar_border_color': scrollbar_border_color, 'scrollbar_corner_radius': scrollbar_corner_radius, 'scrollbar_state': scrollbar_state, 'scrollbar_can_hover': scrollbar_can_hover}
        for attr, value in atts.items():
            setattr(self, f'attributes_{attr}', value)

    def place(self, x,y):
        self._content.place(0,0)
        self._moveButton.place({'right':self.attributes_width - self.attributes_scrollbar_width - self.attributes_padding}.get(self.attributes_scrollbar_alignment),  self.attributes_padding)
        self._frame.place(x,y)
    def _scrollEvent(self, event: QWheelEvent):
        deltaY = -(event.angleDelta().y()//self.attributes_scroll_speed)
        self._scroll(deltaY)
    def _dragPressEvent(self, event):
        self._moveButton.configure(hover_color=self.attributes_scrollbar_pressed_color)
        self._oldPos = (event.x(), event.y())
    def _setButtonColorBack(self, event): self._moveButton.configure(hover_color=self.attributes_scrollbar_hover_color)
    def _dragEvent(self, event):
        deltaY = event.y() - self._oldPos[1]
        self._scroll(deltaY)
    def _scroll(self, amount_to_scroll):
        newButtonY = self._moveButton.info_y() + amount_to_scroll
        newY = self._content.info_y() - amount_to_scroll

        limit = self.attributes_content_height_limit - self.attributes_height

        if not newButtonY > self.attributes_padding:
            newButtonY = self._moveButton.info_y()
            newY = self._content.info_y() if self._content.info_y() > 0 else 0

        if newY < -limit:
            newButtonY = self._moveButton.info_y()
            newY = -limit

        self._content.place(self._content.info_x(), newY)
        self._moveButton.place(self._moveButton.info_x(), newButtonY)
    def _getM(self):
        return self._content._getM()
    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self._frame.enterEvent         = hover
        if leave_hover   is not None:  self._frame.leaveEvent         = leave_hover
        if pressed       is not None:  self._frame.mousePressEvent    = pressed
        if leave_pressed is not None:  self._frame.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self._frame.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self._frame.wheelEvent         = scroll
    def info_x(self): return self._frame.info_x()
    def info_y(self): return self._frame.info_y()
    def config(self, attribute_name, new_value): setattr(self, f'attributes_{attribute_name}', new_value); self.reload()

    def reload(self):
        self._frame.configure(corner_radius=self.attributes_frame_corner_radius, border_width=self.attributes_frame_border_width, frame_color=self.attributes_frame_color, width=self.attributes_width, height=self.attributes_height)
        self._content.configure(width=self.attributes_width, height=self.attributes_content_height_limit, border_width=0, frame_color='transparent')
        self._moveButton.configure(can_hover=self.attributes_scrollbar_can_hover, border_width=self.attributes_scrollbar_border_width, border_color=self.attributes_scrollbar_border_color, corner_radius=self.attributes_scrollbar_corner_radius, state=self.attributes_scrollbar_state, button_color=self.attributes_scrollbar_color, hover_color=self.attributes_scrollbar_hover_color, pressed_color=self.attributes_scrollbar_pressed_color, text='', width=self.attributes_scrollbar_width, height={None:self.attributes_height - (self.attributes_padding*2)}.get(self.attributes_scrollbar_height,self.attributes_scrollbar_height))

    def configure(self,
                  width = None,
                  height = None,
                  scrollbar_width = None,
                  scrollbar_height = None,
                  scrollbar_alignment = None,
                  content_height_limit = None,
                  padding = None,
                  scroll_speed = None,
                  frame_border_width = None,
                  frame_border_color = None,
                  frame_color = None,
                  frame_corner_radius = None,
                  scrollbar_color = None,
                  scrollbar_hover_color = None,
                  scrollbar_pressed_color = None,
                  scrollbar_border_width = None,
                  scrollbar_border_color = None,
                  scrollbar_corner_radius = None,
                  scrollbar_state = None,
                  scrollbar_can_hover = None):
        if width is not None:                   self.attributes_width                   = width
        if height is not None:                  self.attributes_height                  = height
        if scrollbar_width is not None:         self.attributes_scrollbar_width         = scrollbar_width
        if scrollbar_height is not None:        self.attributes_scrollbar_height        = scrollbar_height
        if scrollbar_alignment is not None:     self.attributes_scrollbar_alignment     = scrollbar_alignment
        if content_height_limit is not None:    self.attributes_content_height_limit    = content_height_limit
        if padding is not None:                 self.attributes_padding                 = padding
        if scroll_speed is not None:            self.attributes_scroll_speed            = scroll_speed
        if frame_border_width is not None:      self.attributes_frame_border_width      = frame_border_width
        if frame_border_color is not None:      self.attributes_frame_border_color      = frame_border_color
        if frame_color is not None:             self.attributes_frame_color             = frame_color
        if frame_corner_radius is not None:     self.attributes_frame_corner_radius     = frame_corner_radius
        if scrollbar_color is not None:         self.attributes_scrollbar_color         = scrollbar_color
        if scrollbar_hover_color is not None:   self.attributes_scrollbar_hover_color   = scrollbar_hover_color
        if scrollbar_pressed_color is not None: self.attributes_scrollbar_pressed_color = scrollbar_pressed_color
        if scrollbar_border_width is not None:  self.attributes_scrollbar_border_width  = scrollbar_border_width
        if scrollbar_border_color is not None:  self.attributes_scrollbar_border_color  = scrollbar_border_color
        if scrollbar_corner_radius is not None: self.attributes_scrollbar_corner_radius = scrollbar_corner_radius
        if scrollbar_state is not None:         self.attributes_scrollbar_state         = scrollbar_state
        if scrollbar_can_hover is not None:     self.attributes_scrollbar_can_hover     = scrollbar_can_hover
        self.reload()

    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'width':                   self.attributes_width                    = width
            case 'height':                  self.attributes_height                   = height
            case 'scrollbar_width':         self.attributes_scrollbar_width          = scrollbar_width
            case 'scrollbar_height':        self.attributes_scrollbar_height         = scrollbar_height
            case 'scrollbar_alignment':     self.attributes_scrollbar_alignment      = scrollbar_alignment
            case 'content_height_limit':    self.attributes_content_height_limit     = content_height_limit
            case 'padding':                 self.attributes_padding                  = padding
            case 'scroll_speed':            self.attributes_scroll_speed             = scroll_speed
            case 'frame_border_width':      self.attributes_frame_border_width       = frame_border_width
            case 'frame_border_color':      self.attributes_frame_border_color       = frame_border_color
            case 'frame_color':             self.attributes_frame_color              = frame_color
            case 'frame_corner_radius':     self.attributes_frame_corner_radius      = frame_corner_radius
            case 'scrollbar_color':         self.attributes_scrollbar_color          = scrollbar_color
            case 'scrollbar_hover_color':   self.attributes_scrollbar_hover_color    = scrollbar_hover_color
            case 'scrollbar_pressed_color': self.attributes_scrollbar_pressed_color  = scrollbar_pressed_color
            case 'scrollbar_border_width':  self.attributes_scrollbar_border_width   = scrollbar_border_width
            case 'scrollbar_border_color':  self.attributes_scrollbar_border_color   = scrollbar_border_color
            case 'scrollbar_corner_radius': self.attributes_scrollbar_corner_radius  = scrollbar_corner_radius
            case 'scrollbar_state':         self.attributes_scrollbar_state          = scrollbar_state
            case 'scrollbar_can_hover':     self.attributes_scrollbar_can_hover      = scrollbar_can_hover
            case 'x':                       self.place(new_value, self.info_y())
            case 'y':                       self.place(self.info_x(), new_value)
        self.reload()
