import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        
        self.playing = False
        self.executing = False

        self.game_speed = 20
        self.score = 0
        self.death_count = 0

        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.x_pos_cloud = 200
        self.y_pos_cloud = 100

    def execute(self):
        self.executing = True
        while self.executing:

            if not self.playing:
                self.display_menu()

        pygame.quit()   

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
                
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.update_speed()
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def update_score(self):
        self.score+=1
    
    def update_speed(self):
        if self.score % 100 == 0:
            self.game_speed += 10
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_clouds()
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_speed()
        self.draw_power_up_time()
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000,2)

            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up Time: {time_to_show}s", True, (255,0,0))

                text_rect = text.get_rect()
                text_rect.center = (SCREEN_WIDTH // 2, 50)

                self.screen.blit(text, text_rect)

            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def display_menu(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2

        font = pygame.font.Font(FONT_STYLE, 22)
        text1 = font.render("Press 'S' to start", True, (0,0,0))
        text2 = font.render("Press 'C' to continue the game", True, (0, 0, 0))
        text3 = font.render("Press 'R' to restart the game", True, (0, 0, 0))

        text_rect1 = text1.get_rect()
        text_rect1.center = (x_text_pos, y_text_pos - 30)
        text_rect2 = text2.get_rect()
        text_rect2.center = (x_text_pos, y_text_pos)
        text_rect3 = text3.get_rect()
        text_rect3.center = (x_text_pos, y_text_pos + 30)

        self.screen.blit(text1, text_rect1)
        self.screen.blit(text2, text_rect2)
        self.screen.blit(text3, text_rect3)
        #print(self.death_count)

        self.menu_events_handler()
        pygame.display.flip()

    def menu_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.run()
                elif event.key == pygame.K_c:
                    self.continue_game()
                elif event.key == pygame.K_r:
                    self.restart_game()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        score_text = font.render("Score: " + str(self.score), True, (0, 0, 0))
        self.screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))

    def draw_speed(self):
        speed_km_per_h = self.game_speed * (10 * FPS) / 1000 # converter a velocidade de pixels por quadro para km/h

        font = pygame.font.Font(FONT_STYLE, 22)
        speed_text = font.render("Speed: " + str(speed_km_per_h) + " km/h", True, (0, 0, 0))
        self.screen.blit(speed_text, (10, 10))

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_clouds(self):
        image_width = CLOUD.get_width()
        if self.x_pos_cloud + image_width <= 0:
            self.x_pos_cloud = SCREEN_WIDTH
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.x_pos_cloud -= 1

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20

    def restart_game(self):
        self.playing = True
        self.reset_game()
        self.run()

    def continue_game(self):
        self.playing = True

        while self.playing:
                self.events()
                self.update()
                self.draw()