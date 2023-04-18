import pygame

pygame.init()
screen = pygame.display.set_mode((600,300)) #размеры экрана через кортеж (ширина,высота)
pygame.display.set_caption("Jumping_Luna")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

running = True
while running: #запуск бесконечного цикла игры до нажатия кнопки закрыть окно

    pygame.display.update()

    for event in pygame.event.get(): #перебор всех событий в окне
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

