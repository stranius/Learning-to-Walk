import pymunk
import pymunk.pygame_util
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key
import Shapes
import Character

class Game:
    def set_ground(self):
        shape = pymunk.Segment(self.space.static_body, (0, 10), (1200, 10), 4)
        shape.friction = 1
        shape.collision_type = 3
        self.space.add(shape)

    def draw(self):
        self.window.clear()
        self.space.debug_draw(self.options)
        # self.label.draw()

    def update(self, dt):
        if(not self.running):
            return
        self.space.step(dt)  # Step the simulation one step forward
        self.draw()

    def createCharacter(self):
        self.characters.append(Character.Character(space = self.space))


    def __init__(self, window = None):
        self.objects = []
        self.characters = []
        self.genomes = []
        self.networks = []

        self.running = True
        self.window = window
        self.options = DrawOptions()

        self.space = pymunk.Space()
        self.space.gravity = (0, -1000)
        self.set_ground()

        self.createCharacter()
        self.createCharacter()
        # self.box = Shapes.Circle(space = self.space)

        @self.window.event
        def on_key_press(symbol, modifiers):
            # Symbolic names:
            return
            if symbol == key.RIGHT:
                self.char.moveFrontLegTop(rate = -1)
            if symbol == key.LEFT:
                self.char.moveFrontLegTop(rate = 1)

        @self.window.event
        def on_key_release(symbol, modifiers):
            return
            if symbol == key.RIGHT or symbol == key.LEFT:
                self.char.moveFrontLegTop()


        pyglet.clock.schedule_interval(self.update, 1.0 / 60)
        pyglet.app.run()