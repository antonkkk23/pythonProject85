import sys
import pygame as pg

W = 1280
H = 720
FPS = 1000
clock = pg.time.Clock()

pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Ping Pong | ') # создаем экран игры разрешением 1280х720px

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()