"""
With this library, you can calculate movements such as vertical shot
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
        if(y <= 0):
            print('Y must be grater than 0')
        else:
            self.y = y
    def add_launch_speed(self,launch_speed_x):
        if(launch_speed_x > 0):
            self.launch_speed_x = launch_speed_x
        else:
            print('Launch Speed must be greater than 0')
            
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
    
    def find_max_velocity(self):
        return self.find_end_time() * self.environment.gravity_magnitude
    def find_end_time(self):
        end_time = (self.launcher.y * 2 / self.environment.gravity_magnitude)**(1/2)
        return end_time
 

