import pymunk

class PinJoint:
    def __init__(self, b, b2, a=(0, 0), a2=(0, 0), space = None):
        if(space == None):
            print("Joints.PivotJoint [ERROR] : parameter 'space' was not set")
            return
        joint = pymunk.constraint.PinJoint(b._body, b2._body, a, a2)
        space.add(joint)

# PIVIOT JOINT

# This joint acts as a simple pivot joint, "welding" two objects together with freedom
# for them to swing aroudn the joint with ease. 

# This is good for simple rope-like physics

class PivotJoint:
    def __init__(self, b, b2, a=(0, 0), a2=(0, 0), collide=True, space = None):
        if(space == None):
            print("Joints.PivotJoint [ERROR] : parameter 'space' was not set")
            return
        joint = pymunk.constraint.PinJoint(b._body, b2._body, a, a2)
        joint.collide_bodies = collide
        space.add(joint)




# ROTARY LIMIT JOINT

# This joint acts much like a pivot joint, but has limits for how far it can rotate around the central
# axis.

# This is good for human-body like joints

class RotaryLimitJoint:
    def __init__(self, b, b2, minimum, maximum, collide=True, space = None):
        if(space == None):
            print("Joints.RotaryLimitJoint [ERROR] : parameter 'space' was not set")
            return
        joint = pymunk.constraint.RotaryLimitJoint(b._body, b2._body, minimum, maximum)
        joint.collide_bodies = collide
        space.add(joint)


# DAMPENED ROTARY JOINT

class DampedRotarySpring:
    def __init__(self, b, b2, angle, stiffness, damping, space = None):
        if(space == None):
            print("Joints.DampedRotarySpring [ERROR] : parameter 'space' was not set")
            return
        joint = pymunk.constraint.DampedRotarySpring(b._body, b2._body, angle, stiffness, damping)
        space.add(joint)



class RatchetJoint:
    def __init__(self, b, b2, phase, ratchet, space = None):
        if(space == None):
            print("Joints.RatchetJoint [ERROR] : parameter 'space' was not set")
            return
        joint = pymunk.constraint.GearJoint(b._body, b2._body, phase, ratchet)
        space.add(joint)


class SimpleMotor:
    def __init__(self, b, b2, rate, space = None):
        if(space == None):
            print("Joints.SimpleMotor [ERROR] : parameter 'space' was not set")
            return
        joint = pymunk.constraint.SimpleMotor(b._body, b2._body, rate)
        space.add(joint)


class GearJoint:
    def __init__(self, b, b2, phase, ratio, space = None):
        if(space == None):
            print("Joints.GearJoint [ERROR] : parameter 'space' was not set")
            return
        joint = pymunk.constraint.GearJoint(b._body, b2._body, phase, ratio)
        space.add(joint)