# Pygame шаблон - скелет для нового проекта Pygame
from init import *


# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    # Название окна
    pygame.display.set_caption('MemoryPuzzle')

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    screen.fill(CYAN)

    # Визуализация (сборка)
    pygame.display.flip()

pygame.quit()
