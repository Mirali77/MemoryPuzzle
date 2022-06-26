# Pygame шаблон - скелет для нового проекта Pygame
from init import *
import time

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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_status:
            for idx1 in range(4):
                for idx2 in range(4):
                    card = all_cards[idx1][idx2]
                    flag1 = card.is_out()
                    flag2 = card.is_shown()
                    flag3 = is_rectangle_clicked(event.pos, card.rect)
                    if not flag1 and flag3 and not flag2:
                        card.switch()
                        chosen_cards.append((idx1, idx2))
                        break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_status:
            if is_rectangle_clicked(event.pos, yes_message.rect):
                game_status = True
                attempts = 0
                # Разброс карточек
                all_cards = []
                for idx1 in range(4):
                    four_cards = []
                    for idx2 in range(2):
                        four_cards.append(Card(idx1 * 2 + idx2, all_sprites))
                        four_cards.append(Card(idx1 * 2 + idx2, all_sprites))
                    all_cards.append(four_cards)
                for times in range(2):
                    for idx1 in range(4):
                        for idx2 in range(4):
                            pos1 = random.randint(0, 3)
                            pos2 = random.randint(0, 3)
                            all_cards[idx1][idx2], all_cards[pos1][pos2] = all_cards[pos1][pos2], all_cards[idx1][idx2]
                # Установка расположения карточек
                for idx1 in range(4):
                    for idx2 in range(4):
                        all_cards[idx1][idx2].set_place((120 * (idx1 + 1), 90 * (idx2 + 1)))
            elif is_rectangle_clicked(event.pos, no_message.rect):
                running = False
    # Обновление
    if not game_status:
        if len(all_cards) > 0:
            for idx1 in range(4):
                for idx2 in range(4):
                    all_cards[idx1][idx2].kill()
            all_cards.clear()
    all_sprites.update()
    screen.fill(CYAN)
    all_sprites.draw(screen)
    if game_status:
        attempts_message.draw()
    else:
        gio_message.draw()
        pa_message.draw()
        yes_message.draw()
        no_message.draw()

    # Визуализация (сборка)
    pygame.display.flip()

    # Обработка после визуализации
    if game_status:
        if len(chosen_cards) == 2:
            time.sleep(1)
            if all_cards[chosen_cards[0][0]][chosen_cards[0][1]].key == all_cards[chosen_cards[1][0]][chosen_cards[1][1]].key:
                all_cards[chosen_cards[0][0]][chosen_cards[0][1]].make_out()
                all_cards[chosen_cards[1][0]][chosen_cards[1][1]].make_out()
            else:
                all_cards[chosen_cards[0][0]][chosen_cards[0][1]].switch()
                all_cards[chosen_cards[1][0]][chosen_cards[1][1]].switch()
            attempts += 1
            attempts_message.set_message("ATTEMPTS: " + str(attempts))
            chosen_cards.clear()

        # Проверка на конец игры
        game_status = not check_for_finish(all_cards)

pygame.quit()
