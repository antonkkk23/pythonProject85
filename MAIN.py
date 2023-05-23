import sys
import pygame as pg

W = 1280
H = 720
FPS = 1000
clock = pg.time.Clock()

GREY = (230, 230,230)
WHITE = (255,255,255)
VIOLET = (230,61,245)



player = pg.Rect(W - 20, H //2,10,150)
opponent = pg.Rect(10, H //2,10,150)
ball = pg.Rect(W // -15, H // -15,30,30)
pg.init()  # инициализируем pygame
screen = pg.display.set_mode((W, H))
pg.display.set_caption('Ping Pong | ') # создаем экран игры разрешением 1280х720px

while True:  # цикл игры
    for event in pg.event.get():  # обработчик событий pygame
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fiil(GREY)
    pg.draw.rect(screen, VIOLET, player)
    pg.draw.rect(screen, VIOLET, opponent)
    pg.draw.aaline(screen, WHITE, [W // 2, 0], [W // 2, H])
    pg.draw.ellipse(screen, VIOLET, ball)
    pg.display.update()