'''Rectangle Inscribed inside of Circle'''

# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
from ApplicationController import ApplicationController
from InsideGeometricShape import InsideGeometricShape
from OutsideGeometricShape import OutsideGeometricShape
from ApplicationView import ApplicationView

# FUNCTIONS

def application():
    outside_model = OutsideGeometricShape(25, "black", "red")
    inside_model = InsideGeometricShape(10, 10, "black", "red")
    view = ApplicationView()
    controller = ApplicationController(outside_model, inside_model, view)

application()
