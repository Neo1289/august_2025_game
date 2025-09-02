import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,groups: pygame.sprite.Sprite, x:int, y:int,screen:pygame.display, size:int, life:int):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.size = size
        self.life = life
        self.max_life = life
        self.color = (0, 0, 255)
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(x, y, size, size)
        self.screen_width = screen.get_width()

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

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_x = max(0, self.x - 5)
            self.update_position(new_x, self.y)
        elif keys[pygame.K_RIGHT]:
            new_x = min(self.screen_width - self.size, self.x + 5)
            self.update_position(new_x, self.y)

    def update(self):
        self.handle_input()



