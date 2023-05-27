import pygame


pygame.init()

from func import *

pygame.display.set_caption("Jumping_Luna")
pygame.display.set_icon(icon)

pygame.time.set_timer(ghost_timer, 5000)


while running:  # запуск бесконечного цикла игры до нажатия кнопки закрыть окно

    pygame.display.update()
    if_quit()

    screen_blit()


    portal_rect: None
    portal_blit()


    if gameplay:
        bg_sound.play()

        # ghost_rect: None
        hero_rect: None

        collidir_check()

        # hero_rect = move_left[0].get_rect(topleft = (0,0))
        # hero_area()
        #
        # if portal_rect.colliderect(hero_rect):
        #     gameplay = False
        # ghost_rect = ghost.get_rect(topleft=(ghost_x, 200))
        # if ghost_list:
        #     for (index, elem) in enumerate(ghost_list):
        #         screen.blit(ghost, elem)
        #         elem.x -= 6
        #
        #         if elem.x < -10:
        #             ghost_list.pop(index)
        #         if hero_rect.colliderect(elem):
        #             gameplay = False


        # переменная, содержащая действия пользователя
        keys = pygame.key.get_pressed()

        default_blit_hero()

        changes_in_hero_anim_counter()  # чередование анимации

        # отслживание действий пользователя, чтобы изменять положение героя и фона
        # если герой подходит к краю картинки, то фон сдвигается при нажатии кнопоки управления движением в соответствующую сторону
        # ограничениями является начало первой картинки, а концом - конец последней, так что движение будет заблокировано
        if keys[pygame.K_LEFT]:
            if_left()

        elif keys[pygame.K_RIGHT]:
            if_right()


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


        gameplay = what_happened()

    else:
        bg_sound.stop()
        if hero_rect.colliderect(portal_rect):
                screen.fill((230, 168, 215))
                screen.blit(win_label, (50, 150))
                winning_sound.play()
        else:
            screen.fill((0, 191, 255))
            screen.blit(lose_label, (300, 150))
            screen.blit(restart_label, restart_rect)
            # bg_sound.stop()
            losing_sound.play()

            mouse = pygame.mouse.get_pos()
            if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                hero_x = 30
                ghost_list.clear()
                bullets.clear()
                bullets_stock = 6
                # bg_sound.play()
                pygame.display.update()
    running = give_me_true()


    clock.tick(20)  # задержка перед новой итерацией цикла (переключение анимаций персонажа и прокрутка фона)
