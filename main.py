import pygame
import sys
from player import Player
from bullet import Bullet
from enemy import Enemy
import random

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
        self.player = Player(self.all_sprites,self.width//2, self.height - 50,self.screen,50,10)

        ###bullets features
        self.bullets = 100
        self.bullet_speed = 5
        self.bullet_size = 10
        self.bullet_color = (255, 255, 0)

        ###enemies
        self.custom_event = pygame.event.custom_type()
        self.spawn_time = 5000
        pygame.time.set_timer(self.custom_event, self.spawn_time)
        self.enemy_speed = 2
        self.enemy_size = 20
        self.enemy_color = (200,200,200)

    def shoot(self,event:pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.bullets > 0:
            bullet = Bullet(self.all_sprites,
                            self.player.x + self.player.size // 2 - 5,
                            self.player.y, self.screen, self.bullet_size,self.bullet_speed,self.bullet_color)
            self.bullets -= 1

    def enemy(self):
        self.enemy_x_spawn = random.randint(0, 750)
        Enemy(self.all_sprites,
                        self.enemy_x_spawn,
                        0, self.screen, self.enemy_size, self.enemy_speed, self.enemy_color,3)

    def enemy_groups(self):
        enemies_list = [sprite for sprite in self.all_sprites if hasattr(sprite, 'enemy')]
        return enemies_list

    def bullets_groups(self):
        bullet_group = [sprite for sprite in self.all_sprites if hasattr(sprite, 'bullet')]
        return bullet_group

    def collisions(self):
        enemies = pygame.sprite.Group(self.enemy_groups())
        bullets = pygame.sprite.Group(self.bullets_groups())

        for bullet in bullets:
            hit_enemy = pygame.sprite.spritecollideany(bullet, enemies)
            if hit_enemy:
                bullet.kill()
                hit_enemy.life -= 1
                if hit_enemy.life <= 0:
                    hit_enemy.kill()

    def player_damaged(self):
        enemies = self.enemy_groups()
        for enemy in enemies:
            if enemy.y > self.height:
                self.player.take_damage(1)
                break

    def display_captions(self):
        self.caption = (f"\u2665 {self.player.life}     "
                        f"Bullets: {self.bullets}")
        pygame.display.set_caption(self.caption)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                elif event.type == self.custom_event:
                    self.enemy()

                self.shoot(event)

            self.screen.fill((0, 0, 0))
            self.clock.tick(60)
            self.all_sprites.draw(self.screen)
            self.all_sprites.update()
            self.collisions()
            self.player_damaged()
            self.display_captions()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()