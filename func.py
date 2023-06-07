from parameters import *

def window_switcher():  #approved
    if gameplay:
        bg_sound.play()

        screen_blit()

        ground_blit()

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

        # если не прыжок проверяем на нажатие пользователем клавши "пробел" или "вверх"
        jump_checker()

        falling()

    else:
        bg_sound.stop()
        show_info_window()

def falling():
    global hero_y, collidir_with_ground_tracker, gameplay
    if collidir_with_ground_tracker and not is_jump:
        hero_y += 10

    if hero_y > scr_b:
        gameplay = False

    collidir_with_ground_tracker = False

def ground_blit():
    global collidir_with_ground_tracker, should_i_update, stop_jump, check_stop, jump_count
    gr_y = ground_y

    for i in range(0, 6):
        if i > 0 and i < 3:
            gr_y -= 60
        elif i >= 4 and i < 5:
            gr_y += 60

        screen.blit(ground, (ground_x + 100 * i + bg_x + scr_a, gr_y))

        if (i != 4 and i != 2) or (bg_control >= bg_max - 1 and bg_x < - scr_a) or (bg_control > bg_max - 1 and bg_x > - scr_a):
            screen.blit(ground, (ground_x + 100 * i + bg_x2 + scr_a, ground_y))
        elif hero_x + 20 > ground_x + 100 * i + bg_x2 + scr_a and hero_x + 20 < ground_x + 100 * i + bg_x2 + scr_a + 90:
            collidir_with_ground_tracker = True

        if ((hero_y + 51 > gr_y and hero_x > ground_x + 100 * i + bg_x + scr_a and hero_x < ground_x + 100 * i + bg_x + scr_a + 100) or (hero_y + 51 > ground_y and hero_x > ground_x + 100 * i + bg_x2 + scr_a and hero_x < ground_x + 100 * i + bg_x2 + scr_a + 100)):
            collidir_with_ground_tracker = True

        if ((hero_y + 61 < gr_y and hero_x > ground_x + 100 * i + bg_x + scr_a and hero_x < ground_x + 100 * i + bg_x + scr_a + 100) or (hero_y + 61 < ground_y and hero_x > ground_x + 100 * i + bg_x2 + scr_a and hero_x < ground_x + 100 * i + bg_x2 + scr_a + 100)):
            collidir_with_ground_tracker = True

    if not check_stop:
        if (hero_x > ground_x + 100 + bg_x + scr_a and hero_x < ground_x + 100 + bg_x + scr_a + 100 and hero_y + 61 >= 194.5) or\
                (hero_x > ground_x + 100 * 2 + bg_x + scr_a and hero_x < ground_x + 100 * 2 + bg_x + scr_a + 100 * 2 and hero_y + 61 >= 130) or\
                (hero_x > ground_x + 100 * 4 + bg_x + scr_a and hero_x < ground_x + 100 * 4 + bg_x + scr_a + 100 and hero_y + 61 >= 194.5):
            stop_jump = True
            check_stop = True
        else:
            stop_jump = False
    else:
        stop_jump = False
        jump_count = jump_y

def changes_in_hero_anim_counter():  #approved
    global hero_anim_counter
    if hero_anim_counter == 2:
        hero_anim_counter = 0
    else:
        hero_anim_counter += 1

def if_right():  #approved
    global hero_x, bg_x, bg_control, bg_x2, hero_y, collidir_with_ground_tracker
    screen.blit(move_right[hero_anim_counter], (hero_x, hero_y))
    if hero_x < (scr_a // 2) or (bg_control > bg_max and hero_x < (scr_a - 30)):
        hero_x += hero_speed
    else:
        if bg_x == 0 and bg_control <= bg_max:
            bg_control += 1
        if bg_x2 <= - 2 * scr_a:
            bg_x2 = 0
        if bg_x <= - 2 * scr_a:
            bg_control += 1
            bg_x = 0
        elif bg_control <= bg_max:
            bg_x -= hero_speed
            bg_x2 -= hero_speed

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
    global hero_rect, portal_rect, screen, mouse, gameplay, hero_x, bg_control, bg_x, hero_anim_counter, jump_count, bg_x2, collidir_with_ground_tracker, should_i_update, hero_y
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
            hero_x = 30
            hero_y = 190
            hero_anim_counter = 0
            bg_x = 0
            bg_x2 = - scr_a
            hero_x = 30
            bg_control = 0
            jump_count = jump_y
            collidir_with_ground_tracker = False
            should_i_update = True
            pygame.display.update()






def light_bonfire():
    # global bonfire_x1, bonfire_x2, bonfire_x3, bonfire1_rect, bonfire2_rect, bonfire3_rect
    # screen.blit(bonfire, (bonfire_x1, 200))
    # screen.blit(bonfire, (bonfire_x2, 200))
    # screen.blit(bonfire, (bonfire_x3, 200))
    # bonfire1_rect = bonfire.get_rect(topleft=(bonfire_x1, 200))
    # bonfire2_rect = bonfire.get_rect(topleft=(bonfire_x2, 200))
    # bonfire3_rect = bonfire.get_rect(topleft=(bonfire_x3, 200))
    global bonfire1_rect, bonfire2_rect, bonfire3_rect, bonfire4_rect, bonfire_x
    # screen.blit(bonfire, (bonfire_x - scr_a - 60, 200))
    screen.blit(bonfire, (bonfire_x - 60, 200))
    # screen.blit(bonfire, (bonfire_x + scr_a + 60, 200))
    screen.blit(bonfire, (bonfire_x + scr_a + 300, 200))
    # bonfire1_rect = bonfire.get_rect(topleft=(bg_x - 580, 200))
    # bonfire2_rect = bonfire.get_rect(topleft=(bg_x + 360, 200))
    # bonfire3_rect = bonfire.get_rect(topleft=(bg_x + scr_a + 180, 200))
    # bonfire4_rect = bonfire.get_rect(topleft=(bg_x + scr_a + 490, 200))

# костер появляется за пределами кадра, когда выходит за пределы создается новый за кадром
# если перепрыгнули, то костер гаснет
def calc_new_place_for_bonfire_if_possible():
    global bonfire_x1, bonfire_x2, bonfire_x3, last_bonfire_list
    if (bonfire_x1 <= - 50 or bonfire_x1 + 70 < hero_x) and bg_control < bg_max - 1:
        last_bonfire_list.append(("1", bg_x, bg_control))
        bonfire_x1 = scr_a + bon1 + bg_control * 90
    elif bonfire_x1 + 70 < hero_x:
        bonfire_x1 = scr_a * 3
    elif (bonfire_x2 <= - 50 or bonfire_x2 + 70 < hero_x) and bg_control < bg_max - 2:
        bonfire_x2 = scr_a * 3 + bon2 - bg_control * 90
        last_bonfire_list.append(("2", bg_x, bg_control))
    elif bonfire_x2 + 70 < hero_x:
        bonfire_x2 = scr_a * 3
    elif (bonfire_x3 <= - 50 or bonfire_x3 + 70 < hero_x) and bg_control < bg_max - 3:
        bonfire_x3 = scr_a * 3 + bon3 + bg_control *24
        last_bonfire_list.append(("3", bg_x, bg_control))
    elif bonfire_x3 + 70 < hero_x:
        bonfire_x3 = scr_a * 3

def calc_previous_bonfire_place():
    global last_bonfire_list, bonfire_x1, bonfire_x2, bonfire_x3
    counter = len(last_bonfire_list)-1
    print("in", bg_x, bg_control)
    while counter > len(last_bonfire_list) - 4 and counter >= 0:
        my_tuple = last_bonfire_list[counter]
        print("tuple", my_tuple)
        if my_tuple[0] == "1" and (scr_a - abs(my_tuple[1]) == abs(bg_x) or my_tuple[1] == bg_x) and my_tuple[2] == bg_control:
            print("first")
            bonfire_x1 = -50
            last_bonfire_list.pop(counter)
            print("new list", last_bonfire_list)
        elif my_tuple[0] == "2" and (scr_a - abs(my_tuple[1]) == abs(bg_x) or my_tuple[1] == bg_x) and my_tuple[2] == bg_control:
            print("second")
            bonfire_x2 = -50
            last_bonfire_list.pop(counter)
            print("new list", last_bonfire_list)
        elif my_tuple[0] == "3" and (scr_a - abs(my_tuple[1]) == abs(bg_x) or my_tuple[1] == bg_x) and my_tuple[2] == bg_control:
            print("third")
            bonfire_x3 = -50
            last_bonfire_list.pop(counter)
            print("new list", last_bonfire_list)
        counter -= 1

def collidir_with_bonfire():
    global hero_rect, bonfire1_rect, gameplay, bonfire2_rect, bonfire3_rect
    hero_rect = move_left[0].get_rect(topleft=(hero_x, hero_y))

    if bonfire1_rect.colliderect(hero_rect) or bonfire2_rect.colliderect(hero_rect) or bonfire3_rect.colliderect(hero_rect):
        gameplay = False