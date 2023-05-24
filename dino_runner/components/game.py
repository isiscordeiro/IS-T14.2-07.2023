import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        
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

    def update_score(self):
        self.score+=1
        self.save_progress()

    def update_speed(self):
        if self.score % 100 == 0:
            self.game_speed += 10
            self.save_progress()
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_clouds()
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_speed()
        self.obstacle_manager.draw(self.screen)
        
        pygame.display.flip()

    def display_menu(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render("Press any key to start", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)

        self.screen.blit(text, text_rect)
        print(self.death_count)

        self.menu_events_handler()
        pygame.display.flip()

    def menu_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

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
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20
    
    def save_progress(self):
        with open('saved_data.txt', 'w') as file:
            file.write(f'{self.game_speed}, {self.score}\n')