from config import GRAVITY
from vector import Vector

class Field:
    """
    Fields are global entities that effect all bodies of mass in a simulation.

    For example, having a field representing gravity will result in masses to fall.

    Fields have two components that will be used to affect bodies in different ways:
    * Velocity - This field will cause all masses to move in a direction.
    * Acceleration - This field will cause all masses to move in a direction at a constant rate.
    """

    def __init__(self, velocity: Vector = None, acceleration: Vector = None):
        self.velocity = velocity if velocity else Vector()
        self.acceleration = acceleration if acceleration else Vector()

    def __repr__(self):
        return f"Velocity field {self.velocity}, Acceleration field: {self.acceleration}"

GRAVITY_FIELD = Field(acceleration=Vector(0, GRAVITY))