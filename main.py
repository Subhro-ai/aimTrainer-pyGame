import pygame as pg
white = (255,255,255)
HEIGHT = 720
WIDTH = 1280
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.font.init()
font = pg.font.Font("lemon_milk/LEMONMILK-Regular.otf", 42)
running = True
state = "menu"


def showMenu():
    #Title
    titleText = "Aim Trainer"
    title = font.render(titleText, True, white , None)
    textsize = pg.font.Font.size(font, titleText)[0]
    pos = (WIDTH/2 - (textsize / 2), 50)
    screen.blit(title, pos)

    #Buttons
    buttonRect = pg.Rect((WIDTH/2) - 100, 200, 200, 50)
    button = pg.draw.rect(screen,white, buttonRect)

while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("black")
    
    if running and state == "menu":
        showMenu()

    pg.display.flip()
    clock.tick(60)  # limits FPS to 60

pg.quit()