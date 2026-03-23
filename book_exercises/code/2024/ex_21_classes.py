# Examples of objects and classes

class Animals:

    def __init__(self, fam):
        self.family = fam

    def number_of_legs(self):
        if self.family == "insects":
            print("6 legs")
        elif self.family == "mammals":
            print("2 or 4 legs")


mammal = Animals("mammals")
#mammal.number_of_legs()

fly = Animals("insects")
#fly.number_of_legs()
import numpy as np

class SpaceShip:

    def __init__(self, pos, vel, acc, image, R):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.image = image
        self.R = R

    def check_collision(self, other_pos, other_R):
        return np.sum((self.pos - other_pos) ** 2) < (self.R + other_R) ** 2


ship1 = SpaceShip(pos=np.array([0, 0]),
                  vel=np.array([0, 0]),
                  acc=np.array([0, 0]),
                  image=None,
                  R=2)

ship2 = SpaceShip(pos=np.array([5, 3]),
                  vel=np.array([0, 0]),
                  acc=np.array([0, 0]),
                  image=None,
                  R=2)

test = ship1.check_collision(other_pos=ship2.pos, other_R=ship2.R)
print(test)
