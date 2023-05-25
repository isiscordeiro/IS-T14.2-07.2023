import random
import pygame
import sys

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

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
                    game.draw_game_over()

                    pygame.display.flip() # atualizar a tela

                    pygame.time.delay(500)
                    
                    restart_pressed = False
                    while not restart_pressed: # aguardar até que uma tecla seja pressionado
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                restart_pressed = True
                            if event.type == pygame.QUIT: # se o jogador fechar a janela
                                pygame.quit() # encerrar o módulo pygame
                                sys.exit() # finalizar o programa
                        
                        if restart_pressed:
                            game.death_count += 1
                            self.obstacles.clear()
                            game.reset_game()
                            break
                else:
                    self.obstacles.remove(obstacle)

                self.obstacles.clear()
                break
            
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()