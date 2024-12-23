


class Settings:

    def __init__(self):
        
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135,206,250)
        
        #ship settings
        self.ship_limit = 3
        
        #bullet settings
        self.bullet_width = 200
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #alien settings
        self.fleet_drop_speed = 3
        
        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        self.fleet_direction_y = 1

        #how quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 0.5
        self.alien_points = 50

        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)