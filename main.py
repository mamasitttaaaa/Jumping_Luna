import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 300))  # размеры экрана через кортеж (ширина,высота)
pygame.display.set_caption("Jumping_Luna")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/background1.jpg')

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
hero_anim_counter = 0  # счетчик анимаций для цикла, чтобы показывать все картинки из списка беспрерывно
bg_x = 0  # для смещения фона (две одинаковых картинки идут друг за другом)
# параметры положения игрока и его движения
hero_speed = 5
hero_x = 0
hero_y = 200
bg_control = 0
bg_max = 4 #максимальное колличество итераций фона на уровне

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('sounds/background.mp3')
bg_sound.play()

running = True
while running:  # запуск бесконечного цикла игры до нажатия кнопки закрыть окно

    pygame.display.update()

    for event in pygame.event.get():  # перебор всех событий в окне
        if event.type == pygame.QUIT:
            running = False
            # выводит ошибку display Surface quit
            # pygame.quit()
            # безошибочный вариант
            break

    # screen.blit(bg, (bg_x - 600, 0))
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 600, 0))

    # переменная, содержащая действия пользователя
    keys = pygame.key.get_pressed()

    screen.blit(move_right[0], (hero_x, hero_y))

    if hero_anim_counter == 2:
        hero_anim_counter = 0
    else:
        hero_anim_counter += 1

    # отслживание действий пользователя, чтобы изменять положение героя и фона
    # если герой подходит к краю картинки, то фон сдвигается при нажатии кнопоки управления движением в соответствующую сторону
    # ограничениями является начало первой картинки, а концом - конец последней, так что движение будет заблокировано
    if keys[pygame.K_LEFT]:
        screen.blit(move_left[hero_anim_counter], (hero_x, hero_y))
        if hero_x > 10:
            hero_x -= hero_speed
        else:
            if bg_x == 0:
                bg_control -= 1
            if bg_x >= 600:
                bg_x = 0
                bg_control -= 1
            elif bg_control > 0:
                bg_x += hero_speed

    elif keys[pygame.K_RIGHT]:
        screen.blit(move_right[hero_anim_counter], (hero_x, hero_y))
        if hero_x < 560:
            hero_x += hero_speed
        else:
            if bg_x == 0:
                bg_control += 1
            if bg_x <= -600:
                bg_x = 0
                bg_control += 1
            elif bg_control <= bg_max:
                bg_x -= hero_speed

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

    clock.tick(10)  # задержка перед новой итерацией цикла (медленное переключение анимаций персонажа и медленная прокрутка фона)
