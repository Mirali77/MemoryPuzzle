import pygame
from card import Card
from text import Text
import random

WIDTH = 600  # ширина игрового окна
HEIGHT = 550  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (50, 255, 255)
GREY = (75, 75, 75)

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

# Подключение картинок
images = [pygame.image.load('elprimo.png').convert_alpha(), pygame.image.load('colt.png').convert_alpha(),
          pygame.image.load('shelly.png').convert_alpha(), pygame.image.load('edgar.png').convert_alpha(),
          pygame.image.load('ruffs.png').convert_alpha(), pygame.image.load('poco.png').convert_alpha(),
          pygame.image.load('barley.png').convert_alpha(), pygame.image.load('crow.png').convert_alpha()]

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

# Буфер выбранных карточек
chosen_cards = []


def is_rectangle_clicked(pos, rect: pygame.rect):
    x1 = rect.x
    x2 = rect.x + rect.width
    y1 = rect.y
    y2 = rect.y + rect.height
    if x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2:
        return True
    else:
        return False


def check_for_finish(_all_cards):
    for idx1 in range(4):
        for idx2 in range(4):
            if not _all_cards[idx1][idx2].is_out():
                return False
    return True


game_status = True
attempts = 0
gio_message = Text(54, (WIDTH / 2, HEIGHT / 2 - 30), "GAME IS OVER", BLACK)
pa_message = Text(36, (WIDTH / 2, HEIGHT / 2 + 10), "Play again?", BLACK)
yes_message = Text(36, (WIDTH / 2 - 40, HEIGHT / 2 + 50), "YES", BLACK)
no_message = Text(36, (WIDTH / 2 + 40, HEIGHT / 2 + 50), "NO", BLACK)
attempts_message = Text(36, (WIDTH / 2, HEIGHT - 60), "ATTEMPTS: " + str(attempts), BLACK)
