from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image, ImageQt

def stateGetSize():pass

class ImageDisplay:
    def __init__(self,
                master,
                image: Image,
                width=stateGetSize,
                height=stateGetSize):
        self._image = QLabel('', master._getM() )  # Create an instance of QLabel
        self._image.setStyleSheet('background-color: transparent; color: transparent; border: 0px solid transparent;')

        pixmap = QPixmap.fromImage(ImageQt.ImageQt(image))
        self._image.setPixmap(pixmap)

        if width == stateGetSize: width = pixmap.width()
        if height == stateGetSize: height = pixmap.height()

        self._image.setFixedSize(width, height)

        self.attributes_image  = image
        self.attributes_width  = width
        self.attributes_height = height

        self._image.hide()

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