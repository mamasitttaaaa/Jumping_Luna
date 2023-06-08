import pygame

pygame.init()

from func import *

pygame.display.set_caption("Jumping_Luna")
pygame.display.set_icon(icon)

while running:  # запуск бесконечного цикла игры до нажатия кнопки закрыть окно

    pygame.display.update()
    for event in pygame.event.get():  # перебор всех событий в окне
        if event.type == pygame.QUIT:
            running = False

    window_switcher()


    clock.tick(20)  # задержка перед новой итерацией цикла (переключение анимаций персонажа и прокрутка фона)

