import pygame


class Player:
    def __init__(self, x:int =100, y:int =100, size:int =50, life:int =100):
        self.x = x
        self.y = y
        self.size = size
        self.life = life
        self.max_life = life
        self.color = (0, 0, 255)
        self.rect = pygame.Rect(x, y, size, size)

    def update_position(self, x:int, y:int):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def take_damage(self, damage:int):
        self.life = max(0, self.life - damage)

    def heal(self, amount:int):
        self.life = min(self.max_life, self.life + amount)

    def is_alive(self):
        return self.life > 0

    def draw(self, screen:pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)

    def handle_input(self, screen_width):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_x = max(0, self.x - 5)
            self.update_position(new_x, self.y)
        elif keys[pygame.K_RIGHT]:
            new_x = min(screen_width - self.size, self.x + 5)
            self.update_position(new_x, self.y)