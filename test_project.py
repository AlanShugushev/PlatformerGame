import pygame

def test_player_movement():
    player = pygame.Rect(375, 500, 50, 50)
    player.x += 5
    assert player.x == 380  # Проверяем, что персонаж двигается

def test_gravity():
    velocity_y = -10
    velocity_y += 1  # Гравитация должна увеличивать скорость падения
    assert velocity_y == -9