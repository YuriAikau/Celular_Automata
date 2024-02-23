import pygame as pg
from matrix import Matrix

ROWS_HEIGHT = 30
COLUMNS_WIDTH = 30

pg.init()
screen = pg.display.set_mode((300,300))
clock = pg.time.Clock()
running = True

mat = Matrix()

for i in range(mat.n_columns):
    mat.set_element(i,i,1)

print(mat)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    for i in range(mat.n_rows):
        for j in range(mat.n_columns):
            rect = (i*ROWS_HEIGHT,j*COLUMNS_WIDTH, (i+1)*ROWS_HEIGHT, (j+1)*COLUMNS_WIDTH)
            if mat.get_element(i,j):
                color = "blue"
            else:
                color = "white"
            pg.draw.rect(screen,color,rect)

    pg.display.flip()
    clock.tick(60)
pg.quit()
