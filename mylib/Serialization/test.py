from person import *
from Objector import *


ojt = Objector("dave.smith")
p = Person("Dave","Smith")

#ojt.toBin(p)

dave = ojt.toObj()
dave.show("hi")
