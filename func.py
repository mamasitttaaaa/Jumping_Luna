from parameters import *

def changes_in_hero_anim_counter():
    global hero_anim_counter
    if hero_anim_counter == 2:
        hero_anim_counter = 0
    else:
        hero_anim_counter += 1

def if_left():
    global bg_x, hero_x, screen, bg_control, hero_speed, scr_a, screen
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

def if_right():
    global hero_x, hero_speed, bg_x, bg_control, scr_a
    screen.blit(move_right[hero_anim_counter], (hero_x, hero_y))
    if hero_x < (scr_a - 150) or (bg_control > bg_max and hero_x < (scr_a-30)):
        hero_x += hero_speed
    else:
        if bg_x == 0 and bg_control <= bg_max:
            bg_control += 1
        if bg_x <= -scr_a:
            bg_x = 0
            bg_control += 1
        elif bg_control <= bg_max:
            bg_x -= hero_speed

def default_blit_hero():
    global hero_x, hero_y
    screen.blit(move_right[0], (hero_x, hero_y))

def if_quit():
    global running, bullets_stock, ghost_list, bullets
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

def give_me_true():
    global running
    return running

def portal_blit():
    global scr_a, portal_rect, bg_control, bg_x
    portal_rect = portal.get_rect(topleft=(scr_a - 200, 150))
    if bg_control > bg_max:
        screen.blit(portal, (scr_a - 100, 150))

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
            elem.x -= hero_speed - 3

            if elem.x < -10:
                ghost_list.pop(index)
            if hero_rect.colliderect(elem):
                gameplay = False

def what_happened():
    global gameplay
    return gameplay

def bullets_maker():
    global bullets, weap, screen, bullet, ghost_list, enemy
    if bullets:
        for (i, weap) in enumerate(bullets):
            screen.blit(bullet, (weap.x, weap.y))
            weap.x += 10
            if weap.x > 600:
                bullets.pop(i)

            if ghost_list:
                for (j, enemy) in enumerate(ghost_list):
                    if weap.colliderect(enemy):
                        ghost_list.pop(j)
                        bullets.pop(i)

def jump_checker():
    global is_jump, jump_count, hero_y
    if not is_jump:
        if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]:
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

def show_info_window():
    global hero_rect, portal_rect, screen, mouse, gameplay, hero_x, ghost_list, bullets, bullets_stock
    if hero_rect.colliderect(portal_rect):
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
            pygame.display.update()