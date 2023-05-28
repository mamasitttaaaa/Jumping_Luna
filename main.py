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

    # portal_rect = portal.get_rect(topleft=(scr_a - 200, 150))
    portal_rect: None
    portal_blit()


    if gameplay:
        bg_sound.play()

        hero_rect: None

        collidir_with_portal_check()

        ghosts_tracker()

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

        # если не прыжок проверяем на нажатие пользователем клавши "пробел" или "вверх"
        jump_checker()

        bullets_maker()

        # gameplay = what_happened()

    else:
        bg_sound.stop()
        show_info_window()
        # if hero_rect.colliderect(portal_rect):
        #         screen.fill((230, 168, 215))
        #         screen.blit(win_label, (50, 150))
        #         winning_sound.play()
        # else:
        #     screen.fill((0, 191, 255))
        #     screen.blit(lose_label, (300, 150))
        #     screen.blit(restart_label, restart_rect)
        #     # bg_sound.stop()
        #     losing_sound.play()
        #
        #     mouse = pygame.mouse.get_pos()
        #     if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        #         gameplay = True
        #         hero_x = 30
        #         ghost_list.clear()
        #         bullets.clear()
        #         bullets_stock = 6
        #         # bg_sound.play()
        #         pygame.display.update()

    gameplay = what_happened()
    running = give_me_true()


    clock.tick(20)  # задержка перед новой итерацией цикла (переключение анимаций персонажа и прокрутка фона)
