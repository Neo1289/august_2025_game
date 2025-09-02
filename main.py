import pygame
import sys
from player import Player
from bullet import Bullet

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
        self.player = Player(self.all_sprites,self.width//2, self.height - 50,self.screen,50,100)

    def shoot(self,event:pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = Bullet(self.all_sprites,
                            self.player.x + self.player.size // 2 - 5,
                            self.player.y, self.screen, 10,5)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                self.shoot(event)

            self.screen.fill((0, 0, 0))
            self.clock.tick(60)
            self.all_sprites.draw(self.screen)
            self.all_sprites.update()
            pygame.display.flip()

        pygame.quit()
        sys.exit()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()