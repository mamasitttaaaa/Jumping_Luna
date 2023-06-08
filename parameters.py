import pygame
clock = pygame.time.Clock()

scr_a = 600
scr_b = 300

screen = pygame.display.set_mode((scr_a, scr_b))  # размеры экрана через кортеж (ширина,высота)
icon = pygame.image.load('images/icon.png').convert_alpha()

bg = pygame.image.load('images/background1.jpg').convert_alpha()
portal = pygame.image.load('images/gates.png').convert_alpha()

move_left = [
    pygame.image.load('images/left_moves/left_move1.png'),
    pygame.image.load('images/left_moves/left_move2.png'),
    pygame.image.load('images/left_moves/left_move3.png')
]
move_right = [
    pygame.image.load('images/right_moves/right_move1.png'),
    pygame.image.load('images/right_moves/right_move2.png'),
    pygame.image.load('images/right_moves/right_move3.png')
]

ground = pygame.image.load('images/platform.png')
ground_y = 250
ground_x = 0
collidir_with_ground_tracker = False
check_fall = False

hero_anim_counter = 0  # счетчик анимаций для цикла, чтобы показывать все картинки из списка беспрерывно
bg_x = 0  # для смещения фона (две одинаковых картинки идут друг за другом)
# параметры положения игрока и его движения
hero_speed = 10
hero_x = 30
hero_y = 190
bg_control = 0
bg_max = 6  #максимальное колличество итераций фона на уровне
bg_x2 = - scr_a

bonfire = pygame.image.load('images/fire1.png')
bonfire_x = 0
bonfire_rect: None

ghost = pygame.image.load('images/enemy_ghost.png')
ghost_x = 0
delete_ghost1 = False
delete_ghost2 = False
ghost1_exist = False
ghost2_exist = False
ghost1_y = 250 - 52 #198 #if 198>150: - elif 198 < 250: +
ghost2_y = 130 - 52 #78
ghost_police1 = True
ghost_police2 = True

boss = pygame.image.load('images/boss.png')
boss_x = scr_a - 50
boss_speed = 3
boss_life = 3
boss_delete = False
boss_rect = boss.get_rect(topleft=(-1000, -1000))

bullet = pygame.image.load('images/weapon.png')
bullet_speed_norm = 16 # скорость пули, если фон стабилен
bullet_speed_in_moving_bg = bullet_speed_norm - hero_speed # скорость пули, если фон двигается
move_bg_check = False
# bullets_list = []
press = False
bullet_x: None
bullet_y: None
remember_x: None
bullet_rect: None
delete_item = False
bullet_stock = 6

is_jump = False
jump_y = 8
jump_count = jump_y
stop_jump = False
check_stop = False

bg_sound = pygame.mixer.Sound('sounds/background.mp3')
losing_sound = pygame.mixer.Sound('sounds/sound_for_losing.mp3')
winning_sound = pygame.mixer.Sound('sounds/sound_for_winning.mp3')

label = pygame.font.Font('fonts/beer-money12.ttf', 50)
labelforwin = pygame.font.Font('fonts/gogoia-deco.ttf', 50)
lose_label = label.render('GAME OVER!!!', False, (255, 43, 43))
win_label = labelforwin.render('CONGRATS, WINNER!!!', False, (239, 0, 151))
restart_label = label.render('Revive', False, (245, 245, 245))
restart_rect = restart_label.get_rect(topleft=(100, 100))


gameplay = True

running = True

