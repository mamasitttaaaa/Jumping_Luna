import pygame

from parameters import *

def window_switcher():  #approved
    if gameplay:
        bg_sound.play()

        screen_blit()

        ground_blit()

        ghost1_rect: None
        ghost2_rect: None
        ghost_blit()

        portal_rect: None
        portal_blit()

        hero_rect: None
        collidir_with_portal_check()

        # переменная, содержащая действия пользователя
        keys = pygame.key.get_pressed()

        changes_in_hero_anim_counter()  # чередование анимации

        # отслживание действий пользователя, чтобы изменять положение героя и фона
        # если герой подходит к краю картинки, то фон сдвигается при нажатии кнопоки управления движением в соответствующую сторону
        # ограничениями является начало первой картинки, а концом - конец последней, так что движение будет заблокировано
        if keys[pygame.K_RIGHT]:
            if_right()

        else:
            hero_blit(move_right)

        collidir_with_ghost()

        bullet_rect: None
        bullet_blit()

        boss_blit()
        collidir_with_boss()

        collidir_with_bullets()

        bonfire_blit()
        collidir_with_bonfire()

        # если не прыжок проверяем на нажатие пользователем клавши "пробел" или "вверх"
        jump_checker()

        falling()

    else:
        bg_sound.stop()
        show_info_window()

def falling():
    global hero_y, collidir_with_ground_tracker, gameplay, check_fall
    if collidir_with_ground_tracker and not is_jump:
        if hero_y + 10 + 60 >= ground_y and check_fall:
            hero_y = ground_y - 60  # костыль для решения проблемы понижения положения героя относительно уровня нижней платформы после поднятия и спуска по другим уроням
        else:
            hero_y += 10


    if hero_y > scr_b:
        gameplay = False

    collidir_with_ground_tracker = False
    check_fall = False

def ground_blit():
    global collidir_with_ground_tracker, stop_jump, check_stop, jump_count, check_fall
    gr_y = ground_y

    for i in range(0, 6):
        if i > 0 and i < 3:
            gr_y -= 60
        elif i >= 4 and i < 5:
            gr_y += 60

        screen.blit(ground, (ground_x + 100 * i + bg_x + scr_a, gr_y))

        if (i != 4 and i != 2) or (bg_control >= bg_max - 1 and bg_x < - scr_a) or (bg_control > bg_max - 1 and bg_x > - scr_a):
            screen.blit(ground, (ground_x + 100 * i + bg_x2 + scr_a, ground_y))
        # если платформы нет под ногами на нечетном фрейме, то герой падает
        elif hero_x + 20 > ground_x + 100 * i + bg_x2 + scr_a and hero_x - 20 < ground_x + 100 * i + bg_x2 + scr_a + 90:
            collidir_with_ground_tracker = True

        # отвечает за падение при изменении уровней платформ
        if ((hero_y + 61 > gr_y + 10 and hero_x > ground_x + 100 * i + bg_x + scr_a and hero_x - 10 < ground_x + 100 * i + bg_x + scr_a + 100) or (hero_y + 51 > ground_y and hero_x > ground_x + 100 * i + bg_x2 + scr_a and hero_x - 30 < ground_x + 100 * i + bg_x2 + scr_a + 100)):
            collidir_with_ground_tracker = True

    # останавливает прыжок, если приземлиление произошло на платформу
    if not check_stop:
        if (hero_x + 40 > ground_x + 100 + bg_x + scr_a and hero_x - 20 <= ground_x + 100 + bg_x + scr_a + 100 and hero_y + 61 >= 190) or\
                (hero_x + 40 > ground_x + 100 * 2 + bg_x + scr_a and hero_x - 20 <= ground_x + 100 * 2 + bg_x + scr_a + 100 * 2 and hero_y + 61 >= 130) or\
                (hero_x + 40 > ground_x + 100 * 4 + bg_x + scr_a and hero_x - 20 <= ground_x + 100 * 4 + bg_x + scr_a + 100 and hero_y + 61 >= 190):
            stop_jump = True
            check_stop = True # следит, чтобы второй раз не произошла остановка прыжка
        else:
            stop_jump = False
    else:
        stop_jump = False
        jump_count = jump_y

    if hero_x + 40 > ground_x + 100 * 4 + bg_x + scr_a and hero_x < ground_x + 100 * 4 + bg_x + scr_a + 100 and hero_y + 61 < 190 or\
        hero_x + 40 > ground_x + 100 * 6 + bg_x + scr_a and hero_x < ground_x + 100 * 6 + bg_x + scr_a + 100 and hero_y + 61 < 250:
        collidir_with_ground_tracker = True
        check_fall = True

def ghost_blit():
    global ghost1_rect, ghost2_rect, ghost1_exist, ghost2_exist, ghost1_y, ghost2_y, ghost_police1, ghost_police2

    if ghost2_y >= 10 and ghost_police2:
        ghost2_y -= 2
    elif ghost2_y <= 90:
        ghost_police2 = False
        ghost2_y += 2
    else:
        ghost_police2 = True

    if ghost1_y >= 120 and ghost_police1:
        ghost1_y -= 2
    elif ghost1_y <= 210:
        ghost_police1 = False
        ghost1_y += 2
    else:
        ghost_police1 = True

    if bg_control > 2 and not delete_ghost1:
        screen.blit(ghost, (ghost_x + bg_x + scr_a + 100 / 2 - 20, ghost1_y))
        ghost1_rect = ghost.get_rect(topleft=(ghost_x + bg_x + scr_a + 100 / 2 - 20, ghost1_y))
        ghost1_exist = True
    else:
        ghost1_exist = False

    if not delete_ghost2:
        screen.blit(ghost, (ghost_x + 100 * 3 + bg_x + scr_a + 100 / 2 - 20, ghost2_y))
        ghost2_rect = ghost.get_rect(topleft=(ghost_x + 100 * 3 + bg_x + scr_a + 100 / 2 - 20, ghost2_y))
        ghost2_exist = True
    else:
        ghost2_exist = False

def collidir_with_ghost():
    global gameplay

    if (ghost2_exist and hero_rect.colliderect(ghost2_rect) and not delete_ghost2) or (ghost1_exist and bg_control > 2 and not delete_ghost1 and hero_rect.colliderect(ghost1_rect)):
        gameplay = False

# def bullet_blit():
#     global bullets_list, press
#
#     if pygame.key.get_pressed()[pygame.K_c] or pygame.key.get_pressed()[pygame.K_DOWN] and not press:
#         bullets_list.append([hero_x + 40, hero_y + 15, hero_x + 40, None])
#         press = True
#         print("bullet")
#     else:
#         press = False
#
#     delete_list = []
#     for i in range(0, len(bullets_list)):
#         if not move_bg_check:
#             bullets_list[i][0] += bullet_speed_norm
#         else:
#             bullets_list[i][0] += bullet_speed_in_moving_bg
#
#         if bullets_list[i][0] < bullets_list[i][2] + 250:
#             screen.blit(bullet, (bullets_list[i][0], bullets_list[i][1]))
#             bullets_list[i][3] = bullet.get_rect(topleft=(bullets_list[i][0], bullets_list[i][1]))
#         else:
#             delete_list.append(i)
#
#     delete_bullet(delete_list)

def bullet_blit():
    global bullet_x, bullet_y, remember_x, bullet_rect, press, delete_item, bullet_stock

    if bullet_stock > 0:
        if not press and (pygame.key.get_pressed()[pygame.K_c] or pygame.key.get_pressed()[pygame.K_DOWN]):
            bullet_x = hero_x + 40
            bullet_y = hero_y + 25
            remember_x = hero_x + 40
            press = True
            delete_item = False
            bullet_stock -= 1

        if press:
            if not move_bg_check:
                bullet_x += bullet_speed_norm
            else:
                bullet_x += bullet_speed_in_moving_bg

            if bullet_x < remember_x + 250 and not delete_item:
                screen.blit(bullet, (bullet_x, bullet_y))
                bullet_rect = bullet.get_rect(topleft=(bullet_x, bullet_y))
            else:
                press = False

def collidir_with_bullets():
    global delete_item, delete_ghost2, delete_ghost1, boss_life, boss_delete

    if press:
        if ghost2_exist and ghost2_rect.colliderect(bullet_rect):
            delete_item = True
            delete_ghost2 = True
        elif ghost1_exist and bg_control > 2 and ghost1_rect.colliderect(bullet_rect):
            delete_item = True
            delete_ghost1 = True
        if boss_rect.colliderect(bullet_rect) and boss_life > 0:
            boss_life -= 1
            delete_item = True
        elif boss_life == 0:
            boss_delete = True

def boss_blit():
    global boss_rect, boss_x

    if bg_control >= bg_max - 1 and bg_x < - scr_a - 500 and not boss_delete:
        screen.blit(boss, (boss_x, 250 - 156))
        boss_rect = boss.get_rect(topleft=(boss_x, 250 - 156))
        if boss_x > 200:
            boss_x -= boss_speed

def collidir_with_boss():
    global gameplay, boss_delete

    if bg_control >= bg_max - 1 and bg_x < - scr_a - 500 and hero_rect.colliderect(boss_rect):
        boss_delete = True
        gameplay = False

# def collidir_with_bullets():
#     global gameplay, bullets_list, delete_ghost1, delete_ghost2
#
#     delete_list = []
#     for i in range(0, len(bullets_list)):
#         if ghost2_exist and ghost2_rect.colliderect(bullets_list[i][3]):
#             print("1")
#             delete_list.append(i)
#             delete_ghost2 = True
#         elif ghost1_exist and bg_control > 2 and ghost1_rect.colliderect(bullets_list[i][3]):
#             print("2")
#             delete_list.append(i)
#             delete_ghost1 = True
#
#     if len(delete_list) > 0:
#         print(delete_list)
#     delete_bullet(delete_list)

# def delete_bullet(delete_list):
#     global bullets_list
#
#     for i in range(0, len(delete_list)):
#         print("delete")
#         bullets_list.pop(delete_list[i])

def bonfire_blit():
    global bonfire_rect

    if bg_control < 2:
        screen.blit(bonfire, (bonfire_x + 100 + bg_x2 + scr_a, 250 - 47))
        bonfire_rect = bonfire.get_rect(topleft=(bonfire_x + 100 + bg_x2 + scr_a, 250 - 47))
    else:
        screen.blit(bonfire, (bonfire_x + 100 * 5 + bg_x + scr_a + 10, 190 - 47))
        bonfire_rect = bonfire.get_rect(topleft=(bonfire_x + bg_x + 100 * 5 + scr_a + 10, 190 - 47))


def collidir_with_bonfire():
    global gameplay

    if hero_rect.colliderect(bonfire_rect):
        gameplay = False


def changes_in_hero_anim_counter():  #approved
    global hero_anim_counter
    if hero_anim_counter == 2:
        hero_anim_counter = 0
    else:
        hero_anim_counter += 1

def if_right():  #approved
    global hero_x, bg_x, bg_control, bg_x2, hero_y, collidir_with_ground_tracker, move_bg_check, delete_ghost2, delete_ghost1
    screen.blit(move_right[hero_anim_counter], (hero_x, hero_y))
    if hero_x < (scr_a // 2) or (bg_control > bg_max and hero_x < (scr_a - 30)):
        hero_x += hero_speed
        move_bg_check = False
    else:
        if bg_x == 0 and bg_control <= bg_max:
            bg_control += 1
        if bg_x2 <= - 2 * scr_a:
            bg_x2 = 0
        if bg_x <= - 2 * scr_a:
            bg_control += 1
            bg_x = 0
            delete_ghost1 = False
            delete_ghost2 = False
        elif bg_control <= bg_max:
            bg_x -= hero_speed
            bg_x2 -= hero_speed
            move_bg_check = True

def hero_blit(move: list):  #approved
    global hero_x, hero_y
    screen.blit(move[0], (hero_x, hero_y))

def portal_blit():  #approved
    global scr_a, portal_rect, bg_control, bg_x
    if bg_control > bg_max:
        screen.blit(portal, (scr_a - 100, 150))
        portal_rect = portal.get_rect(topleft=(scr_a - 100, 150))

def screen_blit():  #approved
    global screen, bg, bg_x, scr_a
    screen.blit(bg, (bg_x + 2 * scr_a, 0))
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + scr_a, 0))

def collidir_with_portal_check():  #approved
    global hero_rect, gameplay, portal_rect
    hero_rect = move_left[0].get_rect(topleft=(hero_x, hero_y))

    if bg_control > bg_max and portal_rect.colliderect(hero_rect):
        gameplay = False

def jump_checker():  #approved
    global is_jump, jump_count, hero_y, gr_y, stop_jump, check_stop
    if not stop_jump:
        if not is_jump:
            if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]:
                is_jump = True
        else:
            check_stop = False
            if jump_count >= -jump_y:
                if jump_count > 0:
                    hero_y -= (jump_count ** 2) / 2
                else:
                    hero_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = jump_y
    else:
        is_jump = False
    stop_jump = False

def show_info_window():  #approved
    global hero_rect, portal_rect, screen, mouse, gameplay, hero_x, bg_control, bg_x, hero_anim_counter, jump_count, bg_x2, collidir_with_ground_tracker, should_i_update, hero_y,\
    ground_x, ground_y, check_fall, bonfire_x, ghost_x, delete_ghost1, delete_ghost2, ghost1_exist, ghost2_exist, ghost1_y, ghost2_y, ghost_police1, ghost_police2,\
    boss_x, boss_life, boss_delete, boss_rect, move_bg_check, press, delete_item, bullet_stock, is_jump, stop_jump, check_stop
    if bg_control > bg_max and hero_rect.colliderect(portal_rect):
        screen.fill((230, 168, 215))
        screen.blit(win_label, (50, 150))
        winning_sound.play()
    else:
        screen.fill((0, 191, 255))
        screen.blit(lose_label, (300, 150))
        screen.blit(restart_label, restart_rect)
        losing_sound.play()

        mouse = pygame.mouse.get_pos()
        if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            ground_y = 250
            ground_x = 0
            collidir_with_ground_tracker = False
            check_fall = False

            hero_anim_counter = 0  # счетчик анимаций для цикла, чтобы показывать все картинки из списка беспрерывно
            bg_x = 0  # для смещения фона (две одинаковых картинки идут друг за другом)
            # параметры положения игрока и его движения
            hero_x = 30
            hero_y = 190
            bg_control = 0
            bg_x2 = - scr_a

            bonfire_x = 0
            bonfire_rect: None

            ghost_x = 0
            delete_ghost1 = False
            delete_ghost2 = False
            ghost1_exist = False
            ghost2_exist = False
            ghost1_y = 250 - 52
            ghost2_y = 130 - 52
            ghost_police1 = True
            ghost_police2 = True

            boss_x = scr_a
            boss_life = 3
            boss_delete = False
            boss_rect = boss.get_rect(topleft=(-1000, -1000))

            move_bg_check = False
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

            pygame.display.update()






# def light_bonfire():
#     # global bonfire_x1, bonfire_x2, bonfire_x3, bonfire1_rect, bonfire2_rect, bonfire3_rect
#     # screen.blit(bonfire, (bonfire_x1, 200))
#     # screen.blit(bonfire, (bonfire_x2, 200))
#     # screen.blit(bonfire, (bonfire_x3, 200))
#     # bonfire1_rect = bonfire.get_rect(topleft=(bonfire_x1, 200))
#     # bonfire2_rect = bonfire.get_rect(topleft=(bonfire_x2, 200))
#     # bonfire3_rect = bonfire.get_rect(topleft=(bonfire_x3, 200))
#     global bonfire1_rect, bonfire2_rect, bonfire3_rect, bonfire4_rect, bonfire_x
#     # screen.blit(bonfire, (bonfire_x - scr_a - 60, 200))
#     screen.blit(bonfire, (bonfire_x - 60, 200))
#     # screen.blit(bonfire, (bonfire_x + scr_a + 60, 200))
#     screen.blit(bonfire, (bonfire_x + scr_a + 300, 200))
#     # bonfire1_rect = bonfire.get_rect(topleft=(bg_x - 580, 200))
#     # bonfire2_rect = bonfire.get_rect(topleft=(bg_x + 360, 200))
#     # bonfire3_rect = bonfire.get_rect(topleft=(bg_x + scr_a + 180, 200))
#     # bonfire4_rect = bonfire.get_rect(topleft=(bg_x + scr_a + 490, 200))

# костер появляется за пределами кадра, когда выходит за пределы создается новый за кадром
# если перепрыгнули, то костер гаснет
# def calc_new_place_for_bonfire_if_possible():
#     global bonfire_x1, bonfire_x2, bonfire_x3, last_bonfire_list
#     if (bonfire_x1 <= - 50 or bonfire_x1 + 70 < hero_x) and bg_control < bg_max - 1:
#         last_bonfire_list.append(("1", bg_x, bg_control))
#         bonfire_x1 = scr_a + bon1 + bg_control * 90
#     elif bonfire_x1 + 70 < hero_x:
#         bonfire_x1 = scr_a * 3
#     elif (bonfire_x2 <= - 50 or bonfire_x2 + 70 < hero_x) and bg_control < bg_max - 2:
#         bonfire_x2 = scr_a * 3 + bon2 - bg_control * 90
#         last_bonfire_list.append(("2", bg_x, bg_control))
#     elif bonfire_x2 + 70 < hero_x:
#         bonfire_x2 = scr_a * 3
#     elif (bonfire_x3 <= - 50 or bonfire_x3 + 70 < hero_x) and bg_control < bg_max - 3:
#         bonfire_x3 = scr_a * 3 + bon3 + bg_control *24
#         last_bonfire_list.append(("3", bg_x, bg_control))
#     elif bonfire_x3 + 70 < hero_x:
#         bonfire_x3 = scr_a * 3

# def calc_previous_bonfire_place():
#     global last_bonfire_list, bonfire_x1, bonfire_x2, bonfire_x3
#     counter = len(last_bonfire_list)-1
#     print("in", bg_x, bg_control)
#     while counter > len(last_bonfire_list) - 4 and counter >= 0:
#         my_tuple = last_bonfire_list[counter]
#         print("tuple", my_tuple)
#         if my_tuple[0] == "1" and (scr_a - abs(my_tuple[1]) == abs(bg_x) or my_tuple[1] == bg_x) and my_tuple[2] == bg_control:
#             print("first")
#             bonfire_x1 = -50
#             last_bonfire_list.pop(counter)
#             print("new list", last_bonfire_list)
#         elif my_tuple[0] == "2" and (scr_a - abs(my_tuple[1]) == abs(bg_x) or my_tuple[1] == bg_x) and my_tuple[2] == bg_control:
#             print("second")
#             bonfire_x2 = -50
#             last_bonfire_list.pop(counter)
#             print("new list", last_bonfire_list)
#         elif my_tuple[0] == "3" and (scr_a - abs(my_tuple[1]) == abs(bg_x) or my_tuple[1] == bg_x) and my_tuple[2] == bg_control:
#             print("third")
#             bonfire_x3 = -50
#             last_bonfire_list.pop(counter)
#             print("new list", last_bonfire_list)
#         counter -= 1

# def collidir_with_bonfire():
#     global hero_rect, bonfire1_rect, gameplay, bonfire2_rect, bonfire3_rect
#     hero_rect = move_left[0].get_rect(topleft=(hero_x, hero_y))
#
#     if bonfire1_rect.colliderect(hero_rect) or bonfire2_rect.colliderect(hero_rect) or bonfire3_rect.colliderect(hero_rect):
#         gameplay = False