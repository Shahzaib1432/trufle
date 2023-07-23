from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QColor, QPainterPath
from PyQt5.QtCore import Qt, QRectF
from random import choice
from string import ascii_letters, digits

def _NoneUnique():pass

class Canvas:
    def __init__(self,
                 master,
                 width=400,
                 height=300,
                 canvas_color='#1e1e1e',
                 border_width=2,
                 border_color='#ffffff',
                 corner_radius=5
                 ):
        corner_radius = self._bwCheck(corner_radius)

        self.attributes_width         = width
        self.attributes_height        = height
        self.attributes_canvas_color  = canvas_color
        self.attributes_border_width  = border_width
        self.attributes_border_color  = border_color
        self.attributes_corner_radius = corner_radius

        self._scene = QGraphicsScene(master._getM() )
        self._id_num = 0

        self._builtinColors = {
            'red':     '#FF0000',
            'green':   '#00FF00',
            'blue':    '#0000FF',
            'yellow':  '#FFFF00',
            'purple':  '#800080',
            'orange':  '#FFA500',
            'black':   '#000000',
            'white':   '#FFFFFF',
            'pink':    '#FFC0CB',
            'brown':   '#A52A2A',
            'gray':    '#808080',
            'teal':    '#008080',
            'navy':    '#000080',
            'magenta': '#FF00FF',
            'cyan':    '#00FFFF'}

        self._objectsList = {}

        self._view = QGraphicsView(self._scene, master._getM() )
        self._view.setStyleSheet(f'''
        QGraphicsView {{
            background-color: {canvas_color};
            border: {border_width}px solid {border_color};
            
             border-top-left-radius: {corner_radius[0]};
             border-top-right-radius: {corner_radius[1]};
             border-bottom-left-radius: {corner_radius[2]};
             border-bottom-right-radius: {corner_radius[3]}; 
        }} ''')

        self._view.hide()
        self._view.setFixedSize(width,height)
        self._view.setSceneRect(0,0, width, height)
        self._view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def _bwCheck(self, bw):
        if type(bw) == int:
            bw = [bw,bw,bw,bw]
        return bw

    def place(self, x, y):
        self._view.show()
        self._view.move(x,y)

    def reload(self):
        self.attributes_corner_radius = self._bwCheck(self.attributes_corner_radius)

        self._view.setStyleSheet(f'''
        QGraphicsView {{
             background-color: {self.attributes_canvas_color};
             border: {self.attributes_border_width}px solid {self.attributes_border_color};
            
             border-top-left-radius: {self.attributes_corner_radius[0]};
             border-top-right-radius: {self.attributes_corner_radius[1]};
             border-bottom-left-radius: {self.attributes_corner_radius[2]};
             border-bottom-right-radius: {self.attributes_corner_radius[3]}; 
        }}''')

        self._view.setFixedSize(self.attributes_width,self.attributes_height)
        self._view.setSceneRect(0,0, self.attributes_width, self.attributes_height)

    def configure(self,
                 width=None,
                 height=None,
                 canvas_color=None,
                 border_width=None,
                 border_color=None,
                 corner_radius=None):
        if width is not None: self.attributes_width = width
        if height is not None: self.attributes_height = height
        if canvas_color is not None: self.attributes_canvas_color = canvas_color
        if border_width is not None: self.attributes_border_width = border_width
        if border_color is not None: self.attributes_border_color = border_color
        if corner_radius is not None: self.attributes_corner_radius = corner_radius
        self.reload()

    """ Draw Methods """

    def create_oval(self, x1, y1, x2, y2, color='#FF0000', color_alpha=255, border_color_alpha=255, border_color='#000000', id=_NoneUnique):
        color = self._builtinColors.get(color, color)
        if id is _NoneUnique: id = self._getNewId()
        if id in self._objectsList: raise ValueError('[Errno 3] Id cannot already exist!')

        rc,gc,bc = self._hexToRgba(color)
        rb,gb,bb = self._hexToRgba(border_color)

        circle = self._scene.addEllipse(x1, y1, x1 + x2, y1 + y2,
                                        QColor(rc, gc, bc, border_color_alpha),
                                        QColor(rb, gb, bb, color_alpha) )
        self._objectsList[id] = circle

    def create_rect(self, x1, y1, x2, y2, color='#FF0000',
                    radius=0, color_alpha=255, border_color_alpha=255, border_color='#000000', id=_NoneUnique):
        color = self._builtinColors.get(color, color)
        if id is _NoneUnique: id = self._getNewId()
        if id in self._objectsList: raise ValueError('[Errno 3] Id cannot already exist!')

        rc, gc, bc = self._hexToRgba(color)
        rb, gb, bb = self._hexToRgba(border_color)

        path = QPainterPath()
        path.addRoundedRect(QRectF(x1, y1, x1 + x2, y1 + y2), radius, radius)
        rect = self._scene.addPath(path, QColor(rb, gb, bb, color_alpha),
                                         QColor(rc, gc, bc, border_color_alpha))

        self._objectsList[id] = rect

    def create_line(self,x1,y1,x2,y2, color='#666666', color_alpha=255, id=_NoneUnique):
        if id is _NoneUnique: id = self._getNewId()
        if id in self._objectsList: raise ValueError('[Errno 3] Id cannot already exist!')

        r,g,b = self._hexToRgba(color)
        line = self._scene.addLine(x1, y1, x1 + x2, y1 + y2, QColor(r, g, b, color_alpha))
        self._objectsList[id] = line

    def _hexToRgba(self, hex_code):
        hex_code = hex_code.strip("#")
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        return r, g, b

    def _getNewId(self):
        self._id_num += 1
        return self._id_num

    def hide(self):
        self._view.hide()
    def show(self):
        self._view.show()