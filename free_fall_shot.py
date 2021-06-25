"""
With this library, you can calculate movements such as free fall
"""

class Rock():
    def __init__(self):
        self.name = 'rock'
        
    class sphere_rock:
        def __init__(self):
            self.name = 'sphere'
        def create_sphere(self,radius,density):
            self.radius = radius
            self.density = density
            
    class cube_rock():
        def __init__(self):
            self.name = 'rock'
        
        def create_cube(self,sideLength,density):
            self.sideLength = sideLength
            self.density = density
            
class Launcher():

    def __init__(self):
        name = 'Launcher'
        
    def coordinate_y(self,y):
            self.y = y
            
    def add_launch_speed(self,launch_speed_y):
            self.launch_speed_y = launch_speed_y
    
            
class Environment():
    
    def __init__(self):
        self.name = 'environment'

    def add_gravity(self,magnitude):
        self.gravity_magnitude = magnitude
        
    def add_wind(self,wind,direction):
        self.magnitude_wind = wind
        self.direction = direction

    def add_air_friction(self,friction):
        self.air_friction = friction

class Computation():
    
    def __init__(self,environment,launcher,rock):
        self.environment = environment
        self.launcher = launcher
        self.rock = rock
    
    def find_end_time(self):
        end_time = self.launch.
        return (self.launch.y * 2 / self.environment)**(1/2)
 
