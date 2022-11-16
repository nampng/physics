from typing import List

from config import DELTA
from vector import Vector
from field import Field

class Body:
    """
    The Body class represents a body of mass.

    Bodies of mass have four distinct components:
    * Mass (kg)
    * Position (m)
    * Velocity (m/s)
    * Acceleration (m/s/s)
    
    These components are used to calculate their movement and next position.
    """
    def __init__(self, name: str = "",
                mass: float = 0, 
                position: Vector = None, 
                velocity: Vector = None,
                acceleration: Vector = None):
        
        self.name = name
        self.mass = mass
        self.position = position if position else Vector()
        self.velocity = velocity if velocity else Vector()
        self.acceleration = acceleration if acceleration else Vector()

    def field_effect(self, fields: List[Field]):
        print(f"Applying these fields: {fields} to this body {self.name}")
        for field in fields:
            self.velocity += field.velocity
            self.acceleration += field.acceleration

    def tick(self, delta = DELTA):
        self.position += delta_distance(delta, self.velocity, self.acceleration)
        self.velocity += delta_velocity(delta, self.acceleration)

    def __repr__(self):
        return f"Name: {self.name}\nObject Mass: {self.mass} kg\nCurrent Position: {self.position} m\nCurrent Velocity: {self.velocity} m/s\nCurrent Acceleration: {self.acceleration} m/s/s\n"

# Delta functions
def delta_distance(time_elapsed: float = DELTA, velocity: Vector = None, acceleration: Vector = None):
    """
    Uses this kinematic equation to find the change in distance:
    d = (v_i * t) + (1/2)(a * t^2)
    """
    velocity = velocity if velocity else Vector()
    acceleration = acceleration if acceleration else Vector()

    v_x, v_y = velocity
    a_x, a_y = acceleration

    d_x = v_x * time_elapsed + (0.5 * a_x * time_elapsed**2)
    d_y = (v_y * time_elapsed) + (0.5 * a_y * time_elapsed**2)

    return Vector(d_x, d_y)

def delta_velocity(time_elapsed: float = DELTA, acceleration: Vector = None):
    """
    Uses this kinematic equation to find the change in velocity:
    v_f = v_i + a * t
    """
    acceleration = acceleration if acceleration else Vector()

    a_x, a_y = acceleration

    v_x = a_x * time_elapsed
    v_y = a_y * time_elapsed

    return Vector(v_x, v_y)