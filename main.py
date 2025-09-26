import pygame
import sys
from player import Player
from bullet import Bullet
from enemy import Enemy
import random
from fruit import Fruit, BubbleFruit

class Game:
    def __init__(self, width:int=800, height:int=600):

        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("August 2025 Game")
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites,self.width//2, self.height - 50,self.screen,50,50)
        self.last_level_time = 0
        self.kills = 0

        ###bullets features
        self.bullets = 100
        self.bullet_speed = 5
        self.bullet_size = 10
        self.bullet_color = (255, 255, 0)
        self.bullet_strength = 1

        ###enemies
        self.custom_event = pygame.event.custom_type()
        self.spawn_time = 5000
        pygame.time.set_timer(self.custom_event, self.spawn_time)
        self.enemy_speed = 2
        self.enemy_size = 20
        self.enemy_color = (50,200,200)
        self.enemy_life = 3

        ###fruits
        self.fruit_speed = 5
        self.fruit_size = 10
        self.fruit_color = (255, 100, 100)
        self.last_fruit_spawn_time = -1
        self.fruit_taken = 0
        self.fruit_strength = 10

    def shoot(self,event:pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.bullets > 0:
            bullet = Bullet(self.all_sprites,
                            self.player.x + self.player.size // 2 - 5,
                            self.player.y, self.screen, self.bullet_size,self.bullet_speed,self.bullet_color,self.fruit_taken)
            self.bullets -= 1

    def enemy(self):
        self.enemy_x_spawn = random.randint(0, 750)
        self.new_enemy = Enemy(self.all_sprites,
                        self.enemy_x_spawn,
                        0, self.screen, self.enemy_size, self.enemy_speed,self.enemy_life, self.last_level_time)

    def fruit_spawn(self):
        self.fruit_x_spawn = random.randint(0, 750)
        self.new_fruit = Fruit(self.all_sprites,self.fruit_x_spawn,0,self.fruit_size,self.fruit_speed,self.fruit_color,self.last_level_time)

        if self.last_level_time > 0:
            self.bubble_x_spawn = random.randint(0, 750)
            self.bubble_fruit = BubbleFruit(self.all_sprites,self.bubble_x_spawn,0, self.fruit_size,self.fruit_speed,self.fruit_color,self.last_level_time)

    def enemy_groups(self):
        enemies_list = [sprite for sprite in self.all_sprites if hasattr(sprite, 'enemy')]
        return enemies_list

    def bullets_groups(self):
        bullet_group = [sprite for sprite in self.all_sprites if hasattr(sprite, 'bullet')]
        return bullet_group

    def fruits_groups(self):
        fruit_group = [sprite for sprite in self.all_sprites if hasattr(sprite,'fruit')]
        return fruit_group

    def collisions(self):
        enemies = pygame.sprite.Group(self.enemy_groups())
        bullets = pygame.sprite.Group(self.bullets_groups())

        for bullet in bullets:
            hit_enemy = pygame.sprite.spritecollideany(bullet, enemies)
            if hit_enemy:
                bullet.kill()
                hit_enemy.life -= self.bullet_strength
                if hit_enemy.life <= 0:
                    hit_enemy.kill()
                    self.kills += 1

        for enemy in enemies:
            if(hasattr(enemy,"additional_gear")):
                enemy.life += 1

    def player_damaged(self):
        enemies = self.enemy_groups()
        for enemy in enemies:
            if enemy.y > self.height:
                self.player.take_damage(1)
                self.fruit_taken = 0
                self.bullet_strength -= 1
            if self.bullet_strength <= 0:
                self.bullet_strength = 1

                break

    def display_captions(self):
        self.elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000

        self.caption = (f"\u2665 {self.player.life}     "
                        f"bullets: {self.bullets}     "
                        f"time passed: {self.elapsed_time}    "
                        f"enemy killed: {self.kills}    "
                        f"bullet strength: {self.bullet_strength}    "
                        f"level: {self.last_level_time}      "
                        f"fruits taken: {self.fruit_taken}"
                        )
        pygame.display.set_caption(self.caption)

    def fruit_handler(self):
        fruits_gr = pygame.sprite.Group(self.fruits_groups())

        if self.elapsed_time % 10 == 0 and self.elapsed_time != self.last_fruit_spawn_time:
            self.fruit_spawn()
            self.last_fruit_spawn_time = self.elapsed_time

        for fruit in fruits_gr:
            if fruit.rect.colliderect(self.player.rect):
                fruit.kill()
                self.fruit_speed += 1
                self.bullet_strength += self.fruit_strength + fruit.potency
                self.fruit_taken += 1

            if hasattr(fruit, 'bubble_fruit'):
                self.player.life += 1
                self.bullet_strength += 1

    def level_increase(self):
        current_level = self.elapsed_time // 20
        if current_level > self.last_level_time and self.elapsed_time > 0:
            self.enemy_life += 1
            self.enemy_speed += 1
            self.last_level_time = current_level

    def end_game(self):
        if self.player.life <= 0 or self.bullets == 0:
            font = pygame.font.Font(None, 74)
            game_over_text = font.render(f"GAME OVER, enemies killed {self.kills}", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(game_over_text, text_rect)
            pygame.display.flip()

            pygame.time.wait(5000)

            self.running = False
            pygame.quit()
            sys.exit()

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
            self.level_increase()
            self.fruit_handler()
            self.end_game()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()