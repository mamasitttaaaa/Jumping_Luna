# Platformer
## Jumping Luna 

Статус: в разработке.

### О чем

Главная героиня нашей игры – Луна. Она жила в спокойной деревне, где каждый житель знал друг друга. Луна была разносторонней девушкой со знанием множества ремесел, самым любимым из которых было собирать ягоды в волшебном лесу.

Однажды, отправившись за ягодами, Луна узнала, что темные силы планируют напасть на её деревню. Она быстро вернулась и попросила помощи у своих соседей, однако ее слова были проигнорированы, так как они не верили в ее предчувствия. 

Луна решила действовать самостоятельно. Она отправилась к вершине самой высокой горы - в храм богов, - чтобы попросить их помощи. 

Игроку предстоит преодолеть длинный и полный приключений путь вместе с героиней. Вы столкнётесь с опасными существами и ловушками - пройдёте через многое, чтобы спасти деревню и победить тёмные силы! Также по мере прохождения уровней Вы сможете собирать различные бонусы, которые будут помогать Луне в её пути.

### Библиотеки и модули 

Используется библиотека pygame, необходимая для написания мультимедийных приложений с графическим интерфейсом на языке Python. 

Основные модули библиотеки, использующиеся на данный момент:
| Модуль         | Назначение                                       |
| -------------- | ------------------------------------------------ |
| pygame.display | Доступ к дисплею                                 |
| pygame.event   | Управление внешними событиями                    |
| pygame.image	 | Загружает и сохраняет изображение                |
| pygame.mixer	 | Загружает и воспроизводит мелодии                |
| pygame.time	   | Управляет временем и частотой кадров             |
| pygame.font    | Использует системные шрифты                      |
| pygame.key     | Считывает нажатия клавиш с клавиатуры            |
| pygame.mouse   | Управляет мышью                                  |
| pygame.rect    | Управляет прямоугольными областями               |
| pygame.surface | Управляет изображениями и экраном                |


### Сборка проекта

Чтобы собрать проект игры на Pygame с репозитория Github, следуйте следующим шагам:

Склонируйте репозиторий на ваш локальный компьютер, используя команду git clone URL, где URL - ссылка на репозиторий.
Установите модуль pygame при помощи команды pip install pygame, введенной в терминале.
Задайте конфигурацию запуска, где в качестве запускаемого файла установите main.py, интерпретатор установите Python 3.10.

### Взаимодействие с приложением 

При запуске проекта игра сразу же начинается. Для управления героиней используются клавиши K_UP или K_SPACE (для прыжка), K_RIGHT (для продвижения). В игре присутствуют препятствия в виде костров, а также враги, среди которых множество приведений и финальый босс, охраняющий ворота. Всех врагов можно убить выстрелами, которые производятся с помощью нажатия клавиши K_c (срабатывает при выборе английской раскладки), однако приведения убиваются с одного выстрела, а босс - с трёх. Запас выстрелов ограничен - 6 выстрелов на уровень. Чтобы сберечь выстрелы, приведений можно перепрыгивать, при это не сталкиваясь с ними. Босса же, из-за размера и характера передвижения нельзя победить никак, кроме выстрелов. При проигрыше на экране появляются надписи Game Over и Revive. Надпись Revive является кнопкой для перепрохождения игры. При выигрыше пройти заново возможно только при закрытии окна и запуске игры заново, а на экране остаётся только надпись Congrats,Winner.

### Условная архитектура проекта

![Рис. 1 - Условная архитектура игры](./for%20readme/scheme_for_platformer.png)  
