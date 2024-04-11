from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QColor, QPainterPath
from PyQt5.QtCore import Qt, QRectF
from uuid import uuid4
from .Utility.advancedconvertor import color_to_rgb

def _NoneUnique():pass

class Canvas:
    def __init__(self,
                 master,
                 width=400,
                 height=300,
                 canvas_color='#1e1e1e',
                 border_width=2,
                 border_color='#ffffff',
                 corner_radius=5,
                 x=None,y=None):
        corner_radius = self._bwCheck(corner_radius)

        self.attributes_width         = width
        self.attributes_height        = height
        self.attributes_canvas_color  = canvas_color
        self.attributes_border_width  = border_width
        self.attributes_border_color  = border_color
        self.attributes_corner_radius = corner_radius

        self._scene = QGraphicsScene(master._getM() )
        self._id_num = 0

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

        if (x,y) != (None,None): self.place(x,y)

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
    def config(self, attribute_name, new_value):
        match attribute_name:
            case 'width':         self.attributes_width         = width
            case 'height':        self.attributes_height        = height
            case 'canvas_color':  self.attributes_canvas_color  = canvas_color
            case 'border_width':  self.attributes_border_width  = border_width
            case 'border_color':  self.attributes_border_color  = border_color
            case 'corner_radius': self.attributes_corner_radius = corner_radius
            case 'x':             self.place(new_value, self.info_y())
            case 'y':             self.place(self.info_x(), new_value)
        self.reload()

    def info_x(self): return self._view.x()
    def info_y(self): return self._view.y()

    """ Info: Draw Methods """

    def create_oval(self, x1, y1, x2, y2, oval_color='#FF0000', border_color='#000000', key=_NoneUnique):
        if key == _NoneUnique: key = self._getNewId()
        if key in self._objectsList: raise ValueError('[Errno 3] key cannot already exist!')

        rc,gc,bc,ac = color_to_rgb(oval_color)
        rb,gb,bb,ab = color_to_rgb(border_color)

        circle = self._scene.addEllipse(x1, y1, x1 + x2, y1 + y2,
                                        QColor(rc, gc, bc, ac),
                                        QColor(rb, gb, bb, ab) )
        self._objectsList[key] = circle
    def create_rect(self, x1, y1, x2, y2, rect_color='#FF0000', radius=0, border_color='#000000', key=_NoneUnique):
        if key == _NoneUnique: key = self._getNewId()
        if key in self._objectsList: raise ValueError('[Errno 3] key cannot already exist!')

        rc, gc, bc, ac = color_to_rgb(rect_color)
        rb, gb, bb, ab = color_to_rgb(border_color)

        path = QPainterPath()
        path.addRoundedRect(QRectF(x1, y1, x1 + x2, y1 + y2), radius, radius)
        rect = self._scene.addPath(path, QColor(rb, gb, bb, ab),
                                         QColor(rc, gc, bc, ac))

        self._objectsList[key] = rect
    def create_line(self,x1,y1,x2,y2, line_color='#666666', key=_NoneUnique):
        if key == _NoneUnique: key = self._getNewId()
        if key in self._objectsList: raise ValueError('[Errno 3] key cannot already exist!')

        r,g,b,a = color_to_rgb(line_color)
        line = self._scene.addLine(x1, y1, x1 + x2, y1 + y2, QColor(r,g,b,a))
        self._objectsList[key] = line

    # Size Based
    def draw_oval(self, x,y, width, height, oval_color='#FF0000', border_color='#000000', key=_NoneUnique):
        if key == _NoneUnique: key = self._getNewId()
        if key in self._objectsList: raise ValueError('[Errno 3] Id cannot already exist!')

        rc,gc,bc,ac = color_to_rgb(oval_color)
        rb,gb,bb,ab = color_to_rgb(border_color)

        circle = self._scene.addEllipse(x,y,width,height,
                                        QColor(rc, gc, bc, ac),
                                        QColor(rb, gb, bb, ab) )
        self._objectsList[key] = circle
    def draw_rect(self, x,y, width, height, rect_color='#FF0000', border_color='#000000', radius=0, key=_NoneUnique):
        if key == _NoneUnique: key = self._getNewId()
        if key in self._objectsList: raise ValueError('[Errno 3] key cannot already exist!')

        rc, gc, bc, ac = color_to_rgb(rect_color)
        rb, gb, bb, ab = color_to_rgb(border_color)

        path = QPainterPath()
        path.addRoundedRect(QRectF(x,y,width,height), radius, radius)
        rect = self._scene.addPath(path, QColor(rb, gb, bb, ab),
                                         QColor(rc, gc, bc, ac))

        self._objectsList[key] = rect

    def _getNewId(self):
        return uuid4()
    def hide(self):
        self._view.hide()
    def show(self):
        self._view.show()
    def connect(self, hover=None, leave_hover=None, pressed=None, leave_pressed=None,
                pressed_motion = None, scroll = None):
        if hover         is not None:  self._view.enterEvent         = hover
        if leave_hover   is not None:  self._view.leaveEvent         = leave_hover
        if pressed       is not None:  self._view.mousePressEvent    = pressed
        if leave_pressed is not None:  self._view.mouseReleaseEvent  = leave_pressed
        if pressed_motion is not None: self._view.mouseMoveEvent     = pressed_motion
        if scroll         is not None: self._view.wheelEvent         = scroll


    # Changing item methods
    def delete_item(self, key):
        assert key in self._objectsList, 'Key does not exist, Therefore cannot delete canvas item.'
        obj = self._objectsList.get(key)
        self._scene.removeItem(obj)

    def reposition_item(self, key, x1,y1,x2,y2):
        assert key in self._objectsList, 'Key does not exist, Therefore cannot change/configure canvas item.'
        obj = self._objectsList.get(key)

        try:
            obj.setX(x1)
            obj.setY(y1)
            obj_rect = obj.boundingRect()
            obj_rect.setWidth(x1 + x2)
            obj_rect.setHeight(y1 + y2)
        except AttributeError:
            obj.setX1(x1)
            obj.setY1(y1)
            obj.setX2(x2)
            obj.setY2(y2)

    def move_item(self, key, x,y,width,height):
        assert key in self._objectsList, 'Key does not exist, Therefore cannot change/configure canvas item.'
        obj = self._objectsList.get(key)

        obj.setX(x)
        obj.setY(y)
        try:
            obj_rect = obj.boundingRect()
            obj_rect.setWidth(width)
            obj_rect.setHeight(height)
        except AttributeError:
            raise ValueError('A item of type ("line") cannot have a width or height! Use "item.reposition(x1,y1,x2,y2)" to reposition a line.')

    def get_item_attribute(self, key, attr_name):
        assert key in self._objectsList, 'Key does not exist. Therefore cannot get item attribute.'

        obj = self._objectsList[key]
        obj_rect = obj.boundingRect()
        attrs_dictionary = {'x': obj.x(), 'y': obj.y(), 'width': obj_rect.width(), 'height': obj_rect.height(),
                            'x1': obj.x(), 'y1': obj.y(), 'x2': obj.x() + obj_rect.width(), 'y2': obj.y() + obj_rect.height(),
                            'x1 y1 x2 y2': (obj.x(),obj.y(),obj.x() + obj_rect.width(), obj.y() + obj_rect.height()),
                            'x y width height': (obj.x(), obj.y(), obj_rect.width(), obj_rect.height())}
        attribute = attrs_dictionary.get(attr_name)

        assert attribute is not None, f'Invalid attribute: "{attr_name}"'
        return attribute

