from pathlib import Path
from PIL import Image
from .ImageDisplay import ImageDisplay
from .button import Button
from .Utility.hitbox import HitBox

class SpriteDisplay:
    def __init__(self,
                 master,
                 image: Image.Image | Path,
                 x,y,
                 width='auto',
                 height='auto',
                 display_hitbox_outline=False,
                 hitbox_outline_color='red',
                 hitbox_outline_size=3,
                 hitbox_outline_corner_radius=0):
        if isinstance(image, str): image = Image.open(image)
        if width == 'auto': width = image.width
        if height == 'auto': height = image.height
        self._display = ImageDisplay(master, image, width=width, height=height, x=x,y=y)

        self.attributes_master                       = master
        self.attributes_image                        = image
        self.attributes_width                        = width
        self.attributes_height                       = height
        self.attributes_display_hitbox_outline       = display_hitbox_outline
        self.attributes_hitbox_outline_color         = hitbox_outline_color
        self.attributes_hitbox_outline_size          = hitbox_outline_size
        self.attributes_hitbox_outline_corner_radius = hitbox_outline_corner_radius

        self._outline_display = Button(master, text='', hover_color='transparent', pressed_color='transparent', border_hover_color=hitbox_outline_color, width=width, height=height, x=x, y=y, button_color='transparent', border_width=hitbox_outline_size, border_color=hitbox_outline_color if display_hitbox_outline else 'transparent', corner_radius=hitbox_outline_corner_radius)

        self.hitbox = HitBox(x,y, width, height)
        self.hitbox = HitBox(x,y, width, height)
        self.place(x,y)

    def place(self, x,y):
        self._display.place(x,y)
        if self.attributes_display_hitbox_outline:
            self._outline_display.place(x, y)

    def configure(self,
                  image: Image.Image | Path,
                  width='auto',
                  height='auto',
                  display_hitbox_outline=False,
                  hitbox_outline_color='red',
                  hitbox_outline_size=1,
                  hitbox_outline_corner_radius=0):

            if width is not None:  self.attributes_width  = width
            else: self.attributes_width = 'auto'
            if height is not None: self.attributes_height = height
            else: self.attributes_width = 'auto'
            if image is not None:                        self.attributes_image = image
            if width is not None:                        self.attributes_width = width
            if height is not None:                       self.attributes_height = height
            if display_hitbox_outline is not None:       self.attributes_display_hitbox_outline = display_hitbox_outline
            if hitbox_outline_color is not None:         self.attributes_hitbox_outline_color = hitbox_outline_color
            if hitbox_outline_size is not None:          self.attributes_hitbox_outline_size = hitbox_outline_size
            if hitbox_outline_corner_radius is not None: self.attributes_hitbox_outline_corner_radius = hitbox_outline_corner_radius

            self.reload()
    def get(self, attribute_name):
        attributes = {'image':                        self.attributes_image,
                      'width':                        self.attributes_width,
                      'height':                       self.attributes_height,
                      'display_hitbox_outline':       self.attributes_display_hitbox_outline,
                      'hitbox_outline_color':         self.attributes_hitbox_outline_color,
                      'hitbox_outline_size':          self.attributes_hitbox_outline_size,
                      'hitbox_outline_corner_radius': self.attributes_hitbox_outline_corner_radius}
        return attributes.get(attribute_name)
    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'image':                  self.attributes_image                            = new_value
            case 'width':                  self.attributes_width                            = new_value
            case 'height':                 self.attributes_height                           = new_value
            case 'display_hitbox_outline': self.attributes_display_hitbox_outline           = new_value
            case 'hitbox_outline_color':   self.attributes_hitbox_outline_color             = new_value
            case 'x': self.place(new_value, self.info_y())
            case 'y': self.place(self.info_x(), new_value)
        self.reload()
    def info_x(self): return self._display.info_x()
    def info_y(self): return self._display.info_y()
    def reload(self):
        if isinstance(self.attributes_image, str): self.attributes_image = Image.open(self.attributes_image)
        if self.attributes_width == 'auto': self.attributes_width = self.attributes_image.width
        if self.attributes_height == 'auto': self.attributes_height = self.attributes_image.height

        disp_x = self._display.info_x()
        disp_y = self._display.info_y()

        self._display.configure(image=self.attributes_image, width=self.attributes_width, height=self.attributes_height)
        self.hitbox.set_xy(disp_x, disp_y)
        self.hitbox.set_width(self.attributes_width)
        self.hitbox.set_height(self.attributes_height)
        if self.attributes_display_hitbox_outline:
            self._outline_display.configure(border_hover_color=self.attributes_hitbox_outline_color, width=self.attributes_width, height=self.attributes_height, border_width=self.attributes_hitbox_outline_size, border_color=self.attributes_hitbox_outline_color, corner_radius=self.attributes_hitbox_outline_corner_radius)

        if self.attributes_display_hitbox_outline:
            self._outline_display.show()
        else: self._outline_display.hide()
    def hide(self):
        self._display.hide()
        self._outline_display.hide()
    def show(self):
        self._image.show()
        self._outline_display.show()
    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        self._display.connect(hover=hover,leave_hover=leave_hover,pressed=pressed,leave_pressed=leave_pressed,pressed_motion=pressed_motion,scroll=scroll)