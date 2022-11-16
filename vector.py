from dataclasses import dataclass

@dataclass
class Vector:
    """
    Vectors represent vectors in a physics sense. 

    A collection of components that, when combined, result in a magnitude and direction.
    """
    x: float = 0.0
    y: float = 0.0

    def __iter__(self):
        return iter((self.x, self.y))

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Vector(self.x, self.y)