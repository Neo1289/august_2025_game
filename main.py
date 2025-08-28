import pygame
import sys
from player import Player

class Game:
    def __init__(self, width:int=800, height:int=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("August 2025 Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites,x=self.screen.get_width()/2, y=self.height-50)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

            self.player.shooting(event)

    def update(self):
        self.player.handle_input(self.screen.get_width())

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()