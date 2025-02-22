import pygame

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Платформер")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Игрок
player = pygame.Rect(375, 500, 50, 50)
player_speed = 5

# Гравитация и прыжки
player_velocity_y = 0
gravity = 1
jump_power = -15
on_ground = False

# Переменная для игрового цикла
running = True  

while running:
    pygame.time.delay(30)  # Задержка для плавности

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление движением
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed
    if keys[pygame.K_SPACE] and on_ground:  # Прыжок, если персонаж на земле
        player_velocity_y = jump_power
        on_ground = False

    # Обновление вертикального движения (гравитация)
    player_velocity_y += gravity
    player.y += player_velocity_y

    # Проверка: стоит ли персонаж на платформе
    if player.y >= 500:  # 500 — уровень платформы
        player.y = 500
        player_velocity_y = 0
        on_ground = True

    # Отрисовка экрана
    screen.fill(WHITE)  
    pygame.draw.rect(screen, BLUE, (50, 500, 100, 20))  # Платформа
    pygame.draw.rect(screen, RED, player)  # Игрок

    pygame.display.update()

pygame.quit()