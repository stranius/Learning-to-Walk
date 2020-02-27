import pymunk

class Object:
    def __init__(self, pos = (400, 50), space = None, static = False):
        if(space == None):
            print("Shapes.Object [ERROR] : parameter 'space' was not set")
            return
        if(static) :
            self._body = space.static_body
        else :
            self._body = pymunk.Body(1, 100)
        self._body.position = pos
        self.position = Vec2(pos[0], pos[1])
        self.space = space
        space.add(self._body)
        
    # def draw(self):
    #     angle = self.body.angle
    #     img = pygame.transform.rotate(self.img, math.degrees(angle))
        
    #     pos = to_pygame(self.body.position, screen)
    #     rect = img.get_rect()
    #     rect.center = to_pygame(self.body.position, screen)
    #     screen.blit(img, rect)

class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


class Circle(Object):
    def __init__(self, pos = (400, 50), space = None, size = 10, static = False):
        if(space == None):
            print("Shapes.Circle [ERROR] : parameter 'space' was not set")
            return
        super().__init__(pos, space = space)
        shape = pymunk.Circle(self._body, size)
        shape.elasticity = 0.5
        shape.friction = .5
        shape.collision_type = 0
        self._shape = shape
        self.space.add(shape)

class Rect(Object):
    def __init__(self, pos = (400, 50), space = None, size = (100, 20), static = False):
        if(space == None):
            print("Shapes.Rectangle [ERROR] : parameter 'space' was not set")
            return
        super().__init__(pos, space = space)
        shape = pymunk.Poly.create_box(self._body, size)
        shape.elasticity = 0
        shape.friction = .5
        self._shape = shape
        self.width = size[0]
        self.height = size[1]
        self.space.add(shape)