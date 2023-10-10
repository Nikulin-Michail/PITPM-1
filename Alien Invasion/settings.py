class Settings():
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3
        self.bullet_width = 2000
        self.bullet_height = 25
        self.bullet_color = 127, 255, 0
        self.bullets_allowed = 3
        self.fleet_drop_speed = 10
        self.boss_health = 5
        self.is_boss = False
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def boss_damage(self):
        self.boss_health -= 1

    def set_boss_image_size(self):
        self.is_boss = True

    def set_default_image_size(self):
        self.is_boss = False
