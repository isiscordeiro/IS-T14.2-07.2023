import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, GAME_OVER, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, DIE_SOUND

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            if random.random() < 0.5:
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0, 2)]))
            elif random.random() < 0.8:
                self.obstacles.append(Bird(BIRD))
            else:
                cactus = Cactus(LARGE_CACTUS[random.randint(0,2)])
                cactus.rect.y = 305 # mudando a posição do cactus largo
                self.obstacles.append(cactus)
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    self.game_over(game.screen)
                    game.playing = False
                    game.death_count += 1
                    self.reset_obstacles()
                else:
                    self.obstacles.remove(obstacle)
            
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()

    def game_over(self, screen):
        game_over_x = (SCREEN_WIDTH - GAME_OVER.get_width()) // 2
        game_over_y = (SCREEN_HEIGHT - GAME_OVER.get_height()) // 2 - 45
        screen.blit(GAME_OVER, (game_over_x, game_over_y))

        restart_x = (SCREEN_WIDTH - RESET.get_width()) // 2
        restart_y = (SCREEN_HEIGHT - RESET.get_height()) // 2 + 45
        screen.blit(RESET, (restart_x, restart_y))

        DIE_SOUND.play()

        pygame.display.update()
        pygame.time.delay(1500)