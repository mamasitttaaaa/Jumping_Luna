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

ghost = pygame.image.load('images/enemy_ghost.png').convert_alpha()
ghost_list = []
bullet = pygame.image.load('images/weapon.png').convert_alpha()
bullets = []

hero_anim_counter = 0  # счетчик анимаций для цикла, чтобы показывать все картинки из списка беспрерывно
bg_x = 0  # для смещения фона (две одинаковых картинки идут друг за другом)
# параметры положения игрока и его движения
hero_speed = 10
hero_x = 30
hero_y = 200
bg_control = 0
bg_max = 15  #максимальное колличество итераций фона на уровне
anim_control = True
to_control_bg = True

bonfire = pygame.image.load('images/bonfire/fire1.png')
bon1 = 300
bon2 = scr_a + 20
bon3 = scr_a * 2 + 200
bonfire_x1 = bon1
bonfire_x2 = bon2
bonfire_x3 = bon3
last_bonfire_list = []

is_jump = False
jump_y = 8
jump_count = jump_y

bg_sound = pygame.mixer.Sound('sounds/background.mp3')
losing_sound = pygame.mixer.Sound('sounds/sound_for_losing.mp3')
winning_sound = pygame.mixer.Sound('sounds/sound_for_winning.mp3')

ghost_timer = pygame.USEREVENT + 1

label = pygame.font.Font('fonts/beer-money12.ttf', 50)
labelforwin = pygame.font.Font('fonts/gogoia-deco.ttf', 50)
lose_label = label.render('GAME OVER!!!', False, (255, 43, 43))
win_label = labelforwin.render('CONGRATS, WINNER!!!', False, (239, 0, 151))
restart_label = label.render('Revive', False, (245, 245, 245))
restart_rect = restart_label.get_rect(topleft=(100, 100))

bullets_stock = 6  # запас выстрелов на уровень

gameplay = True

running = True

