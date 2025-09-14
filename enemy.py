import pygame


class ColorChange:
    def __init__(self):
        self.rgb_dict = {
            1: (45, 125, 255),
            2: (255, 99, 71),
            3: (60, 179, 113),
            4: (255, 206, 84),
            5: (153, 102, 204),
        }

    def get_color(self, number:int):
        return self.rgb_dict.get(number, (255, 255, 255))

class ShootMissiles(pygame.sprite.Sprite):
    def __init__(self, groups, x:int, y:int, speed:int, size:int, level:int):
        super().__init__(groups)
        self.image = pygame.Surface((size, size))
        self.rect = pygame.Rect(x, y, size, size)
        self.x = x
        self.y = y
        self.speed = speed + 1
        self.image.fill((25, 255, 255))
        self.level = level

    def update_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.y += self.speed
        self.update_position(self.x, self.y)

        if self.y > 603:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups: pygame.sprite.Sprite, x: int, y: int, screen: pygame.display, size: int, speed: int, life: int, level: int):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size
        self.enemy = True
        self.image = pygame.Surface((size, size))
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed
        self.life = life
        self.level = level
        self.groups = groups

        # Timer for shooting
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 1000  # Shoot every 1 second

        ####first class
        self.color_generator = ColorChange()
        self.image.fill(self.color_generator.get_color(self.level))

    def update_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.y += self.speed
        self.update_position(self.x, self.y)

        # Create missiles periodically if level > 1
        if self.level > 1:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot > self.shoot_delay:
                # Create missile at bottom center of enemy
                missile_x = self.x + self.size // 2 - 5  # Center horizontally, offset by half missile width
                missile_y = self.y + self.size           # Bottom of enemy
                ShootMissiles(self.groups, missile_x, missile_y, self.speed, 10, self.level)
                self.last_shot = current_time

        if self.y > 603:
            self.kill()
