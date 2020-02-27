import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
import Character
import Shapes
import Joints
import Game

# poly = pymunk.Poly.create_box(base, size=(window.width, 10))
# space.add(base, poly)


# from here, the rest of the code is the render loop

# addBall()
# char = Character.Character(space = space)

window = pyglet.window.Window(800, 600, "Learning to Walk")

game = Game.Game(window = window)