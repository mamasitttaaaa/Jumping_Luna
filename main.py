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

        hero_rect: None

        collidir_with_portal_check()

        ghosts_tracker()

        # переменная, содержащая действия пользователя
        keys = pygame.key.get_pressed()

        changes_in_hero_anim_counter()  # чередование анимации

        # отслживание действий пользователя, чтобы изменять положение героя и фона
        # если герой подходит к краю картинки, то фон сдвигается при нажатии кнопоки управления движением в соответствующую сторону
        # ограничениями является начало первой картинки, а концом - конец последней, так что движение будет заблокировано
        if keys[pygame.K_LEFT]:
            if_left()
            anim_control = True

        elif keys[pygame.K_RIGHT]:
            if_right()
            anim_control = False

        elif not anim_control:
            hero_blit(move_right)

        elif anim_control:
            hero_blit(move_left)

        # если не прыжок проверяем на нажатие пользователем клавши "пробел" или "вверх"
        jump_checker()

        bullets_maker()

    else:
        bg_sound.stop()
        show_info_window()

    gameplay = what_happened()
    running = give_me_true()


    clock.tick(20)  # задержка перед новой итерацией цикла (переключение анимаций персонажа и прокрутка фона)
