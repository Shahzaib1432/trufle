from .button import Button
from .frame import Frame

def Empty():pass

class ButtonGroup:
    def __init__(self,
                 master,
                 frame_color='#2D2D2D',
                 button_color='#242424',
                 values=['GroupButton', 'GroupButton', 'GroupButton'],
                 button_selected_color='#242424',
                 frame_corner_radius=5,
                 padding = 5,
                 width = 290,
                 height=40,
                 frame_border_width=0,
                 frame_border_color='#000000',
                 group_padding=5,
                 x=None,
                 y=None,
                 command = lambda:... ):
        self._frame = Frame(master, corner_radius=frame_corner_radius, frame_color=frame_color, height=height, width=width, border_width=frame_border_width, border_color=frame_border_color)

        self.attributes_frame_color           = frame_color
        self.attributes_button_color          = button_color
        self.attributes_values                = values
        self.attributes_button_selected_color = button_selected_color
        self.attributes_frame_corner_radius   = frame_corner_radius
        self.attributes_padding               = padding
        self.attributes_width                 = width
        self.attributes_height                = height
        self.attributes_frame_border_width    = frame_border_width
        self.attributes_frame_border_color    = frame_border_color
        self.attributes_group_padding         = group_padding
        self.attributes_command               = command

        self._globalId = 0
        self._btnAccessList = {}

        self._btnList = []
        self._mainWidth = 0
        for value in values:
            self.addValue(value)
        self._globalValue = Empty

        if x and y: self.place(x,y)

    def place(self, x, y):
        self._frame.place(x, y)

    def configure(self,
                  frame_color=None,
                  button_color=None,
                  values=None,
                  button_selected_color=None,
                  frame_corner_radius=None,
                  padding=None,
                  width=None,
                  height=None,
                  frame_border_width=None,
                  frame_border_color=None,
                  group_padding=None,
                  command=None):
        if frame_color is not None:           self.attributes_frame_color           = frame_color
        if button_color is not None:          self.attributes_button_color          = button_color
        if values is not None:                self.attributes_values                = values
        if button_selected_color is not None: self.attributes_button_selected_color = button_selected_color
        if frame_corner_radius is not None:   self.attributes_frame_corner_radius   = frame_corner_radius
        if padding is not None:               self.attributes_padding               = padding
        if width is not None:                 self.attributes_width                 = width
        if height is not None:                self.attributes_height                = height
        if frame_border_width is not None:    self.attributes_frame_border_width    = frame_border_width
        if frame_border_color is not None:    self.attributes_frame_border_color    = frame_border_color
        if group_padding is not None:         self.attributes_group_padding         = group_padding
        if command is not None:               self.attributes_command               = command
        self.reload()

    def reload(self):
        self._frame.configure(corner_radius=self.attributes_frame_corner_radius, frame_color=self.attributes_frame_color, height=self.attributes_height, width=self.attributes_width, border_width=self.attributes_frame_border_width, border_color=self.attributes_frame_border_color)

    def addValue(self, text = 'Button', key=Empty, button_color = 'auto', height = 'auto', width = 'auto',
                 text_color='#FFFFFF',
                 hover_color='#399c3d',
                 pressed_color='#328a36',
                 border_width=0,
                 border_color='#222222',
                 border_hover_color='#000000',
                 corner_radius=5,
                 font='HoloLens MDL2 Assets',
                 font_size=10,
                 state='enabled',
                 image=None,
                 image_width=50,
                 image_height=50,
                 command=lambda: ... ):
        if button_color == 'auto': button_color = self.attributes_button_color
        if height == 'auto': height = self.attributes_height - (self.attributes_padding*2)
        if width == 'auto': width = 100 - (self.attributes_padding*2)
        if key == Empty: key = self._getNewId()
        if key in self._btnAccessList: raise AttributeError('addValue Key already exists.')

        b = Button(self._frame, command=lambda: self._ExecCMDS(text, b, self.attributes_command, command) , corner_radius=corner_radius, font=font, font_size=font_size, state=state, image=image, image_width=image_width, image_height=image_height, text_color=text_color, hover_color=hover_color, pressed_color=pressed_color, border_width=border_width, border_color=border_color, border_hover_color=border_hover_color, button_color=button_color, height=height, width=width, text=text)
        b.place(self._mainWidth + self.attributes_padding, self.attributes_padding)

        self._mainWidth += width + self.attributes_group_padding
        self._btnList.append(b)

        self._btnAccessList[key] = b

    def delete_all_buttons(self):
        try:
            keys_to_delete = list(self._btnAccessList.keys())
            for key in keys_to_delete:
                self.delete_button(key)
        except Exception as ex:
            print(ex)

    def delete_button(self, button_key):
        b = self._btnAccessList[button_key]
        self._mainWidth -= b.attributes_width
        self._mainWidth -= self.attributes_padding
        if self._globalValue == b.attributes_text: self._globalValue = Empty
        b.delete()
        i = self._btnList.index(self._btnAccessList[button_key])
        del self._btnList[i]
        del self._btnAccessList[button_key]

    def get_button(self, id):
        """ Returns the button with the specified id
        :rtype Button if id exists
        :raises ValueError if id does not exist
        """
        btn = self._btnAccessList.get(id)
        if btn == None: raise ValueError('Button does not exist.')
        return btn

    def configure_button(self, button_key, text = 'Button', button_color = 'auto', height = 'auto', width = 'auto',
                 text_color='#FFFFFF',
                 hover_color='#399c3d',
                 pressed_color='#328a36',
                 border_width=0,
                 border_color='#222222',
                 border_hover_color='#000000',
                 corner_radius=5,
                 font='HoloLens MDL2 Assets',
                 font_size=10,
                 state='enabled',
                 image=None,
                 image_width=50,
                 image_height=50,
                 command=lambda: ...):
        btn = self._btnAccessList.get(button_key, Empty)
        if btn == Empty: raise ValueError('Key does not exist!')

        if button_color == 'auto': button_color = self.attributes_button_color
        if height == 'auto': height = self.attributes_height - (self.attributes_padding * 2)
        if width == 'auto': width = 100 - (self.attributes_padding * 2)

        btn.configure(command=lambda: self._ExecCMDS(text, btn, self.attributes_command, command),
                      corner_radius=corner_radius, font=font, font_size=font_size, state=state, image=image,
                      image_width=image_width, image_height=image_height, text_color=text_color,
                      hover_color=hover_color, pressed_color=pressed_color, border_width=border_width,
                      border_color=border_color, border_hover_color=border_hover_color, button_color=button_color,
                      height=height, width=width, text=text)

    def _getNewId(self):
        self._globalId += 1
        return self._globalId
    def _ExecCMDS(self, text, b, cmd2, cmd3):
        """ Internal Function.
            Calls _setGC and multiple other commands """
        self._setGC(text, b)
        cmd2()
        cmd3()
    def _setGC(self, val, b):
        """ Internal Function.
            Sets The global variable, And Switches the buttons colors. """
        self._globalValue = val
        for button in self._btnList:
            button.configure(button_color='#242424')
        b.configure(button_color='#3FAD44')
    def get_value(self):
        if self._globalValue == Empty:
            print('Any value has not been selected yet!\nStopping program...')
            raise ValueError('Any value has not been selected yet!')
        return self._globalValue

    def hide(self):
        self._frame.hide()
    def show(self):
        self._frame.show()

    def connect(self, widget='button', hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if widget == 'button':
            for btn in self._btnList:
                if hover is not None:          btn.enterEvent = hover
                if leave_hover is not None:    btn.leaveEvent = leave_hover
                if pressed is not None:        btn.mousePressEvent = pressed
                if leave_pressed is not None:  btn.mouseReleaseEvent = leave_pressed
                if pressed_motion is not None: btn.mouseMoveEvent = pressed_motion
                if scroll is not None:         btn.wheelEvent = scroll
        elif widget == 'frame':
            if hover is not None:          self._frame.enterEvent        = hover
            if leave_hover is not None:    self._frame.leaveEvent        = leave_hover
            if pressed is not None:        self._frame.mousePressEvent   = pressed
            if leave_pressed is not None:  self._frame.mouseReleaseEvent = leave_pressed
            if pressed_motion is not None: self._frame.mouseMoveEvent    = pressed_motion
            if scroll is not None:         self._frame.wheelEvent        = scroll
        else:
            """ Else, if the user uses self.get_button(), use it instead. """
            if hover is not None:          widget.enterEvent        = hover
            if leave_hover is not None:    widget.leaveEvent        = leave_hover
            if pressed is not None:        widget.mousePressEvent   = pressed
            if leave_pressed is not None:  widget.mouseReleaseEvent = leave_pressed
            if pressed_motion is not None: widget.mouseMoveEvent    = pressed_motion
            if scroll is not None:         widget.wheelEvent        = scroll