import pymunk
import Joints
from Shapes import *
from Joints import *

class Character :
    def moveFrontLegTop(self, rate = 0):
        self.frontLegTopMotor = SimpleMotor(b = self.body, b2 = self.frontLegTop, rate = rate, space = self.space)

    def moveFrontLegBottom(self, rate = 0):
        self.frontLegBottomMotor = SimpleMotor(b = self.body, b2 = self.frontLegBottom, rate = rate, space = self.space)

    def moveBackLegTop(self, rate = 0):
        self.backLegTopMotor = SimpleMotor(b = self.body, b2 = self.backLegTop, rate = rate, space = self.space)

    def moveBackLegBottom(self, rate = 0):
        self.backLegBottomMotor = SimpleMotor(b = self.body, b2 = self.backLegBottom, rate = rate, space = self.space)

    def __init__(self, space) :
        self.position = 200, 100
        self.space = space

        # Initialize the head
        # self.head = Circle(space = self.space, size = 15, pos = (100, 100))

        # Initialize the body
        self.body = Rect(space = self.space, size = (40, 40), pos = (100, 90))

        # Initialize the top legs
        legSize = (15, 30)
        xPos = self.body.position.x + self.body.width / 2 - legSize[0] / 2
        yPos = self.body.position.y - self.body.height / 2 - legSize[1] / 2
        self.frontLegTop = Rect(space = self.space, size = (legSize[0], legSize[1]), pos = (xPos, yPos))
        xPos = self.body.position.x - self.body.width / 2 + legSize[0] / 2
        self.backLegTop = Rect(space = self.space, size = (legSize[0], legSize[1]), pos = (xPos, yPos))

        # Initialize the bottom legs
        xPos = self.frontLegTop.position.x
        yPos = self.frontLegTop.position.y - self.frontLegTop.height
        self.frontLegBottom = Rect(space = self.space, size = (legSize[0], legSize[1]), pos = (xPos, yPos))
        xPos = self.backLegTop.position.x
        self.backLegBottom = Rect(space = self.space, size = (legSize[0], legSize[1]), pos = (xPos, yPos))

        # Handle all of the joints or "welds" within the character
        # self.headToBodyJoint = PinJoint(b = self.body, b2 = self.head, space = self.space, a = (0, 20), a2 = (0, -15))
        offsetX1 = self.body.width / 2 - self.frontLegTop.width / 2
        offsetY1 = -(self.body.height / 2)
        offsetX2 = 0
        offsetY2 = self.frontLegTop.height / 2

        # Joints for top legs
        self.frontLegTopJoint = PivotJoint(b = self.body, b2 = self.frontLegTop, space = self.space, a = (offsetX1, offsetY1), a2 = (offsetX2, offsetY2))
        self.backLegTopJoint = PivotJoint(b = self.body, b2 = self.backLegTop, space = self.space, a = (-offsetX1, offsetY1), a2 = (offsetX2, offsetY2))

        offsetX1 = 0
        offsetY1 = -(self.frontLegTop.height / 2)
        # Joints for bottom legs
        self.frontLegBottomJoint = PivotJoint(b = self.frontLegTop, b2 = self.frontLegBottom, space = self.space, a = (offsetX1, offsetY1), a2 = (offsetX2, offsetY2))
        self.backLegBottomJoint = PivotJoint(b = self.backLegTop, b2 = self.backLegBottom, space = self.space, a = (offsetX1, offsetY1), a2 = (offsetX2, offsetY2))

        # Now add in the motor joints to allow the characters legs to move
        self.frontLegTopMotor = SimpleMotor(b = self.body, b2 = self.frontLegTop, rate = 0, space = self.space)
        self.frontLegTopMotor.collide_bodies = False
        self.backLegTopMotor = SimpleMotor(b = self.body, b2 = self.backLegTop, rate = 0, space = self.space)


        # self.backLegToBodyMotor = SimpleMotor(b = self.body, b2 = self.backLeg, rate = 2, space = self.space)