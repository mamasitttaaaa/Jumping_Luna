import pygame

clock = pygame.time.Clock()

scr_a = 600
scr_b = 300

pygame.init()
screen = pygame.display.set_mode((scr_a, scr_b))  # размеры экрана через кортеж (ширина,высота)
pygame.display.set_caption("Jumping_Luna")
icon = pygame.image.load('images/icon.png').convert_alpha()
platform = pygame.image.load('images/ground.png').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('images/background1.jpg').convert_alpha()

#define var

# tile_size = 100
# def draw_grid():
#     for line in range (0, 4):
#         pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (scr_a, line * tile_size))
#     for line in range(0, 7):
#         pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, scr_b))
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
bg_max = 5  #максимальное колличество итераций фона на уровне

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('sounds/background.mp3')
# bg_sound.play()
losing_sound = pygame.mixer.Sound('sounds/sound_for_losing.mp3')

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 5000)

label = pygame.font.Font('fonts/beer-money12.ttf', 50)
lose_label = label.render('GAME OVER!!!', False, (255, 43, 43))
restart_label = label.render('Revive', False, (245, 245, 245))
restart_rect = restart_label.get_rect(topleft=(100, 100))

bullets_stock = 6  # запас выстрелов на уровень

gameplay = True

running = True
while running:  # запуск бесконечного цикла игры до нажатия кнопки закрыть окно

    pygame.display.update()
    # bg_sound.play()
    for event in pygame.event.get():  # перебор всех событий в окне
        if event.type == pygame.QUIT:
            running = False
            # выводит ошибку display Surface quit
            # pygame.quit()
            # безошибочный вариант
        if event.type == ghost_timer:
            ghost_list.append(ghost.get_rect(topleft = (630, 200)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_c:
            if bullets_stock > 0:
                bullets.append(bullet.get_rect(topleft=(hero_x + 25, hero_y + 25)))
                bullets_stock -= 1
                break

    screen.blit(bg, (bg_x - scr_a, 0))
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + scr_a, 0))

    #draw_grid()

    if gameplay:
        # screen.blit(platform, (70, 200))
        bg_sound.play()
        hero_rect = move_left[0].get_rect(topleft = (hero_x, hero_y))
        #ghost_rect = ghost.get_rect(topleft=(ghost_x, 200))
        if ghost_list:
            for (index, elem) in enumerate(ghost_list):
                screen.blit(ghost, elem)
                elem.x -= 6

                if elem.x < -10:
                    ghost_list.pop(index)
                if hero_rect.colliderect(elem):
                    gameplay = False


        # переменная, содержащая действия пользователя
        keys = pygame.key.get_pressed()

        screen.blit(move_right[0], (hero_x, hero_y))

        if hero_anim_counter == 2:
            hero_anim_counter = 0
        else:
            hero_anim_counter += 1


        # отслживание действий пользователя, чтобы изменять положение героя и фона
        # если герой подходит к краю картинки, то фон сдвигается при нажатии кнопоки управления движением в соответствующую сторону
        # ограничениями является начало первой картинки, а концом - конец последней, так что движение будет заблокировано
        if keys[pygame.K_LEFT]:
            print(bg_x)
            screen.blit(move_left[hero_anim_counter], (hero_x, hero_y))
            if hero_x > 30:
                hero_x -= hero_speed
            else:
                if bg_x == 0 and bg_control > 0:
                    bg_control -= 1
                if bg_x >= scr_a:
                    bg_x = 0
                    bg_control -= 1
                elif bg_control > 0:
                    bg_x += hero_speed

        elif keys[pygame.K_RIGHT]:
            screen.blit(move_right[hero_anim_counter], (hero_x, hero_y))
            if hero_x < (scr_a - 70):
                hero_x += hero_speed
            else:
                if bg_x == 0 and bg_control <= bg_max:
                    bg_control += 1
                if bg_x <= -scr_a:
                    bg_x = 0
                    bg_control += 1
                elif bg_control <= bg_max:
                    bg_x -= hero_speed

        # если не прыжок проверяем на нажатие пользователем клавши "пробел"
        if not is_jump:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    hero_y -= (jump_count ** 2) / 2
                else:
                    hero_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 7

        # if keys[pygame.K_c]:
        #     bullets.append(bullet.get_rect(topleft=(hero_x + 25, hero_y + 25)))

        if bullets:
            for (i, weap) in enumerate (bullets):
                screen.blit(bullet, (weap.x, weap.y))
                weap.x += 10
                if weap.x > 600:
                    bullets.pop(i)

                if ghost_list:
                    for (j, enemy) in enumerate (ghost_list):
                        if weap.colliderect(enemy):
                            ghost_list.pop(j)
                            bullets.pop(i)

    else:
        screen.fill((0, 191, 255))
        screen.blit(lose_label, (300, 150))
        screen.blit(restart_label, restart_rect)
        bg_sound.stop()
        losing_sound.play()

        mouse = pygame.mouse.get_pos()
        if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            hero_x = 30
            ghost_list.clear()
            bullets.clear()
            bullets_stock = 6
            # bg_sound.play()
            #pygame.display.update()


    clock.tick(20)  # задержка перед новой итерацией цикла (переключение анимаций персонажа и прокрутка фона)
