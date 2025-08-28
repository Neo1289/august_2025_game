import pygame

class Projectile:
    def __init__(self, x, y, speed=7, radius=5):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = (255, 255, 0)  # Yellow circle
        self.active = True

    def update(self):
        self.y -= self.speed
        if self.y < -self.radius:
            self.active = False

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
