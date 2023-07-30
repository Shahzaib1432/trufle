from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image, ImageQt

def stateGetSize():pass

class ImageDisplay:
    def __init__(self,
                master,
                image: Image,
                width = stateGetSize,
                height = stateGetSize,
                x=None,y=None):
        self._image = QLabel('', master._getM() )  # Create an instance of QLabel

        pixmap = QPixmap.fromImage(ImageQt.ImageQt(image))
        self._image.setPixmap(pixmap)

        if width == stateGetSize: width = pixmap.width()
        if height == stateGetSize: height = pixmap.height()

        self.attributes_master = master
        self.attributes_image  = image
        self.attributes_width  = width
        self.attributes_height = height

        self._image.setStyleSheet(f'background-color: transparent; color: transparent; ' \
                                  f'border: 0px solid transparent;')

        self._image.setFixedSize(width, height)
        self._image.hide()

        if (x,y) != (None, None): self.place(x,y)

    def place(self, x, y):
        self._image.move(x, y)
        self._image.show()

    def configure(self,
                  image  = None,
                  width  = None,
                  height = None):

            if width is not None:  self.attributes_width  = width
            if height is not None: self.attributes_height = height
            if image is not None:  self.attributes_image  = image
            self.reload()

    def get(self, attribute_name):
        attributes = {'image':  self.attributes_image,
                      'width':  self.attributes_width,
                      'height': self.attributes_height}
        return attributes.get(attribute_name)

    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'image':  self.attributes_image  = new_value
            case 'width':  self.attributes_width  = new_value
            case 'height': self.attributes_height = new_value
            case 'x':      self.place(new_value, self.info_y())
            case 'y':      self.place(self.info_x(), new_value)
        self.reload()

    def info_x(self): return self._image.x()
    def info_y(self): return self._image.y()

    def reload(self):
        pixmap = QPixmap.fromImage(ImageQt.ImageQt(self.attributes_image))
        self._image.setPixmap(pixmap)

        if self.attributes_width == stateGetSize: self.attributes_width = pixmap.width()
        if self.attributes_height == stateGetSize: self.attributes_height = pixmap.height()

        self._image.setFixedSize(self.attributes_width, self.attributes_height)

    def hide(self):
        self._image.hide()
    def show(self):
        self._image.show()

    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self._image.enterEvent         = hover
        if leave_hover   is not None:  self._image.leaveEvent         = leave_hover
        if pressed       is not None:  self._image.mousePressEvent    = pressed
        if leave_pressed is not None:  self._image.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self._image.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self._image.wheelEvent         = scroll