# Nam Nguyen
# Fun python script that does physics calculations, mainly for kinematics, and fun!

from config import DELTA
from vector import Vector
from body import Body
from field import Field, GRAVITY_FIELD

from typing import List

# Big 4 Kinematic Equations

# d = (v_i * t) + (1/2)(a * t^2)
# d = [(v_i + v_f) / 2] * t
# v_f = v_i + a * t
# v_f^2 = v_i^2 + 2 * a * d

# Notes #
"""
We need to figure out how to restrain our bodies of mass.
Meaning, if we want to represent the ground as a horizontal line y = 0, we shouldn't allow bodies of mass to phase through.
The same goes for walls and ceilings.

For future plans, we also want to do collisions. So when we slam into walls, floors, ceilings, and other bodies, we want
to calculate the proper reaction.

For now lets cover the needs for our restraints:
For simplicity, they should be treated as infinite masses that absorb the entire force of a collision.
"""

def simulator(run_time: float, bodies: List[Body], fields: List[Field] = None, save_results: bool = False):
    print(f"Total bodies: {bodies}")
    body: Body

    # Prep all bodies with field effects.
    if fields:
        # [body.field_effect(fields) for body in bodies]
        print(f"Before: {bodies}")
        for idx,body in enumerate(bodies):
            bodies[idx].field_effect(fields)
        print(f"After field effects: {bodies}")

    # while run_time > 0:
    #     print(f"Time left: {run_time}")
    #     for body in bodies:
    #         body.tick()
    #         if save_results:
    #             with open(f"results/{body.name}.txt", "a") as file:
    #                 file.write(repr(body))
    #         print(body)
    #     run_time -= DELTA

body = Body(name="body", position=Vector(0, 200))
body2 = Body(name="body2", position=Vector(0, 200))
body3 = Body(name="body3", position=Vector(0, 200))
simulator(run_time = 5, bodies = [body, body2, body3], fields = [GRAVITY_FIELD])
