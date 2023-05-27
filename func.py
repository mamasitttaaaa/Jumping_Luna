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
    if bg_control > bg_max:
        screen.blit(portal, (scr_a - 100, 150))
        portal_rect = portal.get_rect(topleft=(scr_a - 200, 150))

def screen_blit():
    global screen, bg, bg_x, scr_a
    screen.blit(bg, (bg_x - scr_a, 0))
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + scr_a, 0))

def collidir_check():
    global hero_rect, ghost_rect, gameplay, elem, ghost_list, portal_rect
    hero_rect = move_left[0].get_rect(topleft=(hero_x, hero_y))
    # hero_area()

    if bg_control > bg_max and portal_rect.colliderect(hero_rect):
        gameplay = False
    if ghost_list:
        for (index, elem) in enumerate(ghost_list):
            screen.blit(ghost, elem)
            elem.x -= 6

            if elem.x < -10:
                ghost_list.pop(index)
            if hero_rect.colliderect(elem):
                gameplay = False

def what_happened():
    global gameplay
    return gameplay