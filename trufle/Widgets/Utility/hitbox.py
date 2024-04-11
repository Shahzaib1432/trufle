from functools import lru_cache

class HitBox:
    def __init__(self, x,y,width,height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def set_x(self, new_val): self.x = new_val
    def set_y(self, new_val): self.y = new_val
    def set_width(self, new_val): self.width = new_val
    def set_height(self, new_val): self.height = new_val
    def set_xy(self, x,y):
        self.x = x
        self.y = y

    def collides_with(self, other_hit_box, shrink_amount=0, increase_amount=0):
        x1, y1, width1, height1 = self._get_properties(shrink_amount, increase_amount)
        x2, y2, width2, height2 = other_hit_box._get_properties(shrink_amount, increase_amount)

        return x1 < x2 + width2 and x1 + width1 > x2 and y1 < y2 + height2 and y1 + height1 > y2
    def collides_with_any(self, other_hit_boxes: list, shrink_amount=0, increase_amount=0):
        return any(self.collides_with(hitbox, shrink_amount, increase_amount) for hitbox in other_hit_boxes)
    def collides_with_all(self, other_hit_boxes: list, shrink_amount=0):
        return all(self.collides_with(hitbox, shrink_amount) for hitbox in other_hit_boxes)

    def collides_on_side(self, other_hit_box, side='down', shrink_amount=0, increase_amount=0):
        x1, y1, width1, height1 = self._get_properties(shrink_amount, increase_amount)
        x2, y2, width2, height2 = other_hit_box._get_properties(shrink_amount, increase_amount)

        if side == 'down':
            y2 = height2 - 1
            height2 = 1
        elif side == 'up':
            height2 = 1
        elif side == 'left':
            width2 = 1
        elif side == 'right':
            x2 = width2 - 1
            width2 = 1
        return x1 < x2 + width2 and x1 + width1 > x2 and y1 < y2 + height2 and y1 + height1 > y2
    def collides_on_any_side(self, other_hit_box, sides=['down', 'up'], shrink_amount=0, increase_amount=0):
        return any(self.collides_on_side(other_hit_box, side, shrink_amount, increase_amount) for side in sides)

    @property
    def x(self): return self._x
    @property
    def y(self): return self._y
    @property
    def width(self): return self._width
    @property
    def height(self): return self._height
    @x.setter
    def x(self, new_value): self._x = new_value
    @y.setter
    def y(self, new_value): self._y = new_value
    @width.setter
    def width(self, new_value): self._width = new_value
    @height.setter
    def height(self, new_value): self._height = new_value

    # Multi-properties, access-only properties.
    @property
    def xy(self): return self._x, self._y
    @property
    def width_height(self): return self._width, self._height
    @property
    def xy_width_height(self): return self._x,self._y, self._width,self._height

    def _get_properties(self, shrink_amount, increase_amount):
        return (self.x + shrink_amount) - increase_amount, (self.y + shrink_amount) - increase_amount, (self.width - (shrink_amount*2)) + (increase_amount*2), (self.height - (shrink_amount*2)) + (increase_amount*2)
