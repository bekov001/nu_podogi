from random import randint

from src.origin.classes.chicken import Chicken
from src.origin.classes.egg import Egg
from src.origin.classes.left_chicken import LeftChicken
from src.origin.classes.stick import Stick


def level():
    # eggs = [Egg(50, 50),
    sticks = [Stick(10, 130), Stick(700, 130),
              Stick(10, 280), Stick(700, 280),]
    chicken = [Chicken(0, 50, randint(10, 1000)), LeftChicken(910, 50, randint(10, 1000)),
               Chicken(0, 200, randint(10, 1000)), LeftChicken(910, 200, randint(10, 1000))]


def level2():
    # eggs = [Egg(50, 50),
    sticks = [Stick(10, 130), Stick(700, 130),
              Stick(10, 280), Stick(700, 280),
              Stick(10, 430), Stick(700, 430),
              ]
    chicken = [Chicken(0, 50, randint(10, 1000)), LeftChicken(910, 50, randint(10, 1000)),
               Chicken(0, 200, randint(10, 1000)), LeftChicken(910, 200, randint(10, 1000)),
               Chicken(0, 350, randint(10, 1000)),
               LeftChicken(910, 350, randint(10, 1000))
               ]


def level3():
    # eggs = [Egg(50, 50),
    sticks = [Stick(10, 130), Stick(700, 130),
              Stick(10, 280), Stick(700, 280),
              Stick(10, 430), Stick(700, 430),
              ]
    chicken = [Chicken(0, 50, randint(0, 100)), LeftChicken(910, 50, randint(0, 100)),
               Chicken(0, 200, randint(0, 100)), LeftChicken(910, 200, randint(0, 100)),
               Chicken(0, 350, randint(0, 100)),
               LeftChicken(910, 350, randint(0, 100))
               ]
