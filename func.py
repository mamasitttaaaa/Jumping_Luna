from parameters import *

def changes_in_hero_anim_counter():
    global hero_anim_counter
    if hero_anim_counter == 2:
        hero_anim_counter = 0
    else:
        hero_anim_counter += 1

def if_left():
    global bg_x, hero_x, screen, bg_control, hero_speed, scr_a, screen, anim_control, bonfire_x1, bonfire_x2, bonfire_x3, to_control_bg
    # calc_previous_bonfire_place()
    screen.blit(move_left[hero_anim_counter], (hero_x, hero_y))
    if to_control_bg == True:
        to_control_bg = False
        bg_control += 1
    if hero_x > 30:
        hero_x -= hero_speed
    else:
        if bg_x == 0 and bg_control > 0:
            bg_control -= 1
        if bg_x >= scr_a:
            bg_control -= 1
            bg_x = 0
        elif bg_control > 1:
            bg_x += hero_speed
            bonfire_x1 += hero_speed
            bonfire_x2 += hero_speed
            bonfire_x3 += hero_speed

def if_right():
    global hero_x, hero_speed, bg_x, bg_control, scr_a, anim_control, bonfire_x1, bonfire_x2, bonfire_x3, to_control_bg
    calc_new_place_for_bonfire_if_possible()
    screen.blit(move_right[hero_anim_counter], (hero_x, hero_y))
    if hero_x < (scr_a - 250) or (bg_control > bg_max and hero_x < (scr_a-30)):
        hero_x += hero_speed
    else:
        if bg_x == 0 and bg_control <= bg_max:
            bg_control += 1
        if bg_x <= -scr_a:
            bg_control += 1
            bg_x = 0
        elif bg_control <= bg_max:
            bg_x -= hero_speed
            bonfire_x1 -= hero_speed
            bonfire_x2 -= hero_speed
            bonfire_x3 -= hero_speed
    to_control_bg = True

def hero_blit(move: list):
    global hero_x, hero_y
    screen.blit(move[0], (hero_x, hero_y))

def if_quit():
    global running, bullets_stock, ghost_list, boss_list, boss_stock
    for event in pygame.event.get():  # перебор всех событий в окне
        if event.type == pygame.QUIT:
            running = False

        if event.type == ghost_timer:
            ghost_list.append(ghost.get_rect(topleft=(630, 200)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_c:
            if bullets_stock > 0:
                bullets.append(bullet.get_rect(topleft=(hero_x + 25, hero_y + 25)))
                bullets_stock -= 1
                break

        if gameplay:
            if boss_stock > 0:
                screen.blit(boss, (scr_a, 110))
                boss_list.append(boss.get_rect(topleft=(scr_a, 110)))
                boss_stock -= 1
            # if boss_stock > 0:
            #     if bg_x >= bg_max-1:
            #         screen.blit(boss, (scr_a, 110))
            #         boss_list.append(boss.get_rect(topleft=(scr_a, 110)))
            #         boss_stock -= 1

def give_me_true():
    global running
    return running

def portal_blit():
    global scr_a, portal_rect, bg_control, bg_x
    if bg_control > bg_max:
        screen.blit(portal, (scr_a - 100, 150))
        portal_rect = portal.get_rect(topleft=(scr_a - 100, 150))

def screen_blit():
    global screen, bg, bg_x, scr_a
    screen.blit(bg, (bg_x - scr_a, 0))
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + scr_a, 0))

def collidir_with_portal_check():
    global hero_rect, ghost_rect, gameplay, elem, ghost_list, portal_rect
    hero_rect = move_left[0].get_rect(topleft=(hero_x, hero_y))

    if bg_control > bg_max and portal_rect.colliderect(hero_rect):
        gameplay = False

def ghosts_tracker():
    global hero_rect, ghost_rect, gameplay, elem, ghost_list, portal_rect

    if ghost_list:
        for (index, elem) in enumerate(ghost_list):
            screen.blit(ghost, elem)
            if hero_x < (scr_a - 250):
                elem.x -= hero_speed - 9
            else:
                elem.x -= hero_speed + hero_speed - 8

            if elem.x < -10:
                ghost_list.pop(index)
            if hero_rect.colliderect(elem):
                gameplay = False

def what_happened():
    global gameplay
    return gameplay

def bullets_maker():
    global bullets, weap, screen, bullet, ghost_list, enemy, boss_rect, boss_death, boss_list, k
    if bullets:
        for (i, weap) in enumerate(bullets):
            screen.blit(bullet, (weap.x, weap.y))
            weap.x += 50
            if weap.x > hero_x + 450:
                bullets.pop(i)

            if ghost_list:
                for (j, enemy) in enumerate(ghost_list):
                    if weap.colliderect(enemy):
                        ghost_list.pop(j)
                        bullets.pop(i)

            if boss_list:
                for (j, monster) in enumerate(boss_list):
                    if weap.colliderect(monster):
                        k += 1
                        bullets.pop(i)
                    if weap.colliderect(monster) and (k == 3):
                        boss_list.pop(j)


def jump_checker():
    global is_jump, jump_count, hero_y
    if not is_jump:
        if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]:
            is_jump = True
    else:
        if jump_count >= -jump_y:
            if jump_count > 0:
                hero_y -= (jump_count ** 2) / 2
            else:
                hero_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = jump_y

def show_info_window():
    global hero_rect, portal_rect, screen, mouse, gameplay, hero_x, ghost_list, bullets, bullets_stock, bg_control, bonfire_x1, bonfire_x2, bonfire_x3, boss_x, boss_death, boss_stock, k
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
            ghost_list.clear()
            bullets.clear()
            bullets_stock = 6
            bg_control = 0
            bonfire_x1 = bon1
            bonfire_x2 = bon2
            bonfire_x3 = bon3
            boss_stock = 1
            k = 0
            pygame.time.set_timer(ghost_timer, 8000)
            # last_bonfire_list = []
            for (index, elem) in enumerate(boss_list):
                elem.x = scr_a
            pygame.display.update()

def light_bonfire():
    global bonfire_x1, bonfire_x2, bonfire_x3, bonfire1_rect, bonfire2_rect, bonfire3_rect
    screen.blit(bonfire, (bonfire_x1, 220))
    screen.blit(bonfire, (bonfire_x2, 220))
    screen.blit(bonfire, (bonfire_x3, 220))
    bonfire1_rect = bonfire.get_rect(topleft=(bonfire_x1, 220))
    bonfire2_rect = bonfire.get_rect(topleft=(bonfire_x2, 220))
    bonfire3_rect = bonfire.get_rect(topleft=(bonfire_x3, 220))

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
        bonfire_x2 = scr_a * 2 + bon2 - bg_control * 90
        last_bonfire_list.append(("2", bg_x, bg_control))
    elif bonfire_x2 + 70 < hero_x:
        bonfire_x2 = scr_a * 3
    elif (bonfire_x3 <= - 50 or bonfire_x3 + 70 < hero_x) and bg_control < bg_max - 3:
        bonfire_x3 = scr_a * 3 + bon3 + bg_control
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

def boss_blit():
    global boss_list, gameplay
    if boss_list:
        for (index, elem) in enumerate(boss_list):
            screen.blit(boss, elem)
            elem.x -= 4
            if elem.x < -10:
                boss_list.pop(index)
            if hero_rect.colliderect(elem):
                gameplay = False
