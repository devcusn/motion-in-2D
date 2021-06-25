"""
With this library, you can calculate movements such as oblique shot
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
        
    def add_launch_speed(self,launch_speed_x,launch_speed_y):-
            self.launch_speed_x = launch_speed_x
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
    
    def find_max_height(self):
        return self.launcher.launch_speed_y * (self.find_end_time()/2) - 1/2 * self.environment.gravity_magnitude * self.find_end_time()**2
    
    def find_end_time(self):
        end_time = ((self.launcher.launch_speed_y * 2 / self.environment.gravity_magnitude)*2)**(1/2)
        return end_time
 


