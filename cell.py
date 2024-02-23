import pygame as pg
from matrix import Matrix

(WIDTH,HEIGHT) = (300,300)
ROWS_HEIGHT = 10
COLUMNS_WIDTH = 10
WAIT_TIME = 200
TITLE = "Cellular Automata"


pg.init()
screen: pg.Surface = pg.display.set_mode((WIDTH,HEIGHT))
clock: pg.time.Clock = pg.time.Clock()
pg.display.set_caption(TITLE)
last_tick: int = -1000
running: bool = True
paused: bool = True

mat: Matrix = Matrix(WIDTH//COLUMNS_WIDTH,HEIGHT//ROWS_HEIGHT)
mat.set_element(4,5,1)
mat.set_element(5,6,1)
mat.set_element(6,4,1)
mat.set_element(6,5,1)
mat.set_element(6,6,1)


def draw_screen(screen: pg.Surface, mat: Matrix) -> None:
    for i in range(mat.n_rows):                
        hline_start: tuple[int,int] = (0,i*ROWS_HEIGHT)
        hline_end: tuple[int,int] = (WIDTH,i*ROWS_HEIGHT)
        for j in range(mat.n_columns):
            rect = (j*ROWS_HEIGHT,i*COLUMNS_WIDTH, ROWS_HEIGHT, COLUMNS_WIDTH)
            vline_start: tuple[int,int] = (j*COLUMNS_WIDTH, 0)
            vline_end: tuple[int,int] = (j*COLUMNS_WIDTH,HEIGHT)

            if mat.get_element(i,j):
                color = "black"
            else:
                color = "white"
            pg.draw.rect(screen,color,rect)

            pg.draw.line(screen,"gray",hline_start,hline_end)
            pg.draw.line(screen,"gray",vline_start,vline_end)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                paused = not paused
                if paused:
                    pg.display.set_caption("Paused")
                else:
                    pg.display.set_caption(TITLE)
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
            mat.toggle_element(y//ROWS_HEIGHT, x//COLUMNS_WIDTH)
            draw_screen(screen, mat)
            pg.display.flip()

    curr_tick: int = pg.time.get_ticks()
    if (curr_tick - last_tick >= WAIT_TIME) and (not paused):
        last_tick = curr_tick
        draw_screen(screen,mat)
        pg.display.flip()
        mat.cell_automata()
    clock.tick(60)
pg.quit()
