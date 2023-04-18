import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 625)) #размеры экрана через кортеж (ширина,высота)
pygame.display.set_caption("Jumping_Luna")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/background.jpg')
player = pygame.image.load('images/left_moves/left_move1.png')
move_left = [
    pygame.image.load('images/left_moves/left_move1.png'),
    pygame.image.load('images/left_moves/left_move2.png'),
    pygame.image.load('images/left_moves/left_move3.png')
]
move_right = [
    pygame.image.load('images/right_moves/right_move1.png'),
    pygame.image.load('images/right_moves/right_move2.png'),
    pygame.image.load('images/right_moves/right_move3.png')
]
player_anim_counter = 0
bg_x = 0

running = True
while running: #запуск бесконечного цикла игры до нажатия кнопки закрыть окно


    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x + 1000, 0))
    screen.blit(move_left[player_anim_counter], (300, 250))

    if player_anim_counter == 2:
        player_anim_counter = 0
    else:
        player_anim_counter += 1


    bg_x -= 2
    if bg_x == -618:
        bg_x = 0
    pygame.display.update()

    for event in pygame.event.get(): #перебор всех событий в окне
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(10)


