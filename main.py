import pygame

pygame.init()

from func import *

pygame.display.set_caption("Jumping_Luna")
pygame.display.set_icon(icon)

while running:  # запуск бесконечного цикла игры до нажатия кнопки закрыть окно

    pygame.display.update()
    # if_quit()
    for event in pygame.event.get():  # перебор всех событий в окне
        if event.type == pygame.QUIT:
            running = False

    # screen_blit()
    #
    # portal_rect: None
    # portal_blit()

    # if gameplay:
    #     bg_sound.play()
    #
    #     screen_blit()
    #
    #     portal_rect: None
    #     portal_blit()
    #
    #     hero_rect: None
    #
    #     collidir_with_portal_check()
    #
    #     # переменная, содержащая действия пользователя
    #     keys = pygame.key.get_pressed()
    #
    #     changes_in_hero_anim_counter()  # чередование анимации
    #
    #     # отслживание действий пользователя, чтобы изменять положение героя и фона
    #     # если герой подходит к краю картинки, то фон сдвигается при нажатии кнопоки управления движением в соответствующую сторону
    #     # ограничениями является начало первой картинки, а концом - конец последней, так что движение будет заблокировано
    #     if keys[pygame.K_RIGHT]:
    #         if_right()
    #         anim_control = False
    #
    #     else:
    #         hero_blit(move_right)
    #
    #     # если не прыжок проверяем на нажатие пользователем клавши "пробел" или "вверх"
    #     jump_checker()
    #
    # else:
    #     bg_sound.stop()
    #     show_info_window()
    #
    # gameplay = what_happened()
    # running = give_me_true()
    window_switcher()


    clock.tick(20)  # задержка перед новой итерацией цикла (переключение анимаций персонажа и прокрутка фона)

