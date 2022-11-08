from contextlib import nullcontext
import pygame
import time
from drivers import AbstractCar, PlayerCar, ComputerCar
from utils import scale_image, blit_rotate_center, blit_text_center
pygame.font.init()
pygame.init()
x,y = 0,0
GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
LAPS = 10
TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
FINISH = pygame.image.load("imgs/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (130, 250)
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("F1 1999")
MAIN_FONT = pygame.font.SysFont("Arial", 30)
FPS = 60
PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]
class GameInfo:
    LEVELS = 10
    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0
    def next_level(self):
        self.level += 1
    def level(self):
        print(self.level)
    def reset(self):
        
        self.level = 1
        self.started = False
        self.level_start_time = 0
    def game_finished(self):
        return self.level > self.LEVELS
    def start_level(self):
        self.started = True
        self.level_start_time = time.time()
    def get_level_time(self):
        if not self.started:
            return 0
        return  round(time.time() - self.level_start_time,2)

def draw(win, images, player_car, computer_car, game_info):
    for img, pos in images:
        win.blit(img, pos)
    level_text = MAIN_FONT.render(
        f"Lap {game_info.level}", 1, (255, 255, 255))
    win.blit(level_text, (10, HEIGHT - level_text.get_height() - 70))
    time_text = MAIN_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
    win.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))
    vel_text = MAIN_FONT.render(
        f"ACC: {round(player_car.vel*25, 1)}%", 1, (255, 255, 255))
    win.blit(vel_text, (10, HEIGHT - vel_text.get_height() - 10))
    player_car.draw(win)
    computer_car.draw(win)
    pygame.display.update()
def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()
    if not moved:
        player_car.reduce_speed()
def handle_collision(player_car, computer_car, game_info):
    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()
    computer_finish_poi_collide = computer_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if computer_finish_poi_collide != None:
        time.sleep(5000)
        if game_info.next_level() == 10:
            blit_text_center(WIN, MAIN_FONT, "You lost!")
            pygame.display.update()
            game_info.reset()
            player_car.reset()
            computer_car.reset()
    player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            print("balls")
        else:
            game_info.next_level()
            player_car.reset()
            computer_car.next_level(game_info.level)

neutral_sound = pygame.mixer.Sound("f1neutral.mp3")
max_sound = pygame.mixer.Sound("f1max.mp3")
def neutral():
    pygame.mixer.Sound.play(neutral_sound)
def maxer():
    pygame.mixer.Sound.play(max_sound)
run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
          (FINISH, FINISH_POSITION), (TRACK_BORDER, (0, 0))]
player_car = PlayerCar(4, 4)
computer_car = ComputerCar(2, 4, PATH)
game_info = GameInfo()
while run:
    clock.tick(FPS)
    draw(WIN, images, player_car, computer_car, game_info)
    while not game_info.started:
        blit_text_center(
            WIN, MAIN_FONT, f"Press any key to start the Grand Prix!")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                game_info.start_level()
    if round(player_car.vel*25, 1) == 0:
        neutral()
    if round(player_car.vel*25, 1) >= 85:
        maxer()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    move_player(player_car)
    computer_car.move()
    handle_collision(player_car, computer_car, game_info)
    if game_info.game_finished():
        blit_text_center(WIN, MAIN_FONT, "You won the game!")
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()
        computer_car.reset()
pygame.quit()