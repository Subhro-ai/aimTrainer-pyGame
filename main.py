import pygame as pg
white = (255,255,255)
black = (0,0,0)
HEIGHT = 720
WIDTH = 1280
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.font.init()
font = pg.font.Font("lemon_milk/LEMONMILK-Regular.otf", 42)
running = True

state = "menu"


def showMenu(click, state):
    #Title
    titleText = "Aim Trainer"
    title = font.render(titleText, True, white , None)
    textsize = pg.font.Font.size(font, titleText)[0]
    pos = (WIDTH/2 - (textsize / 2), 50)
    screen.blit(title, pos)

    #Buttons
    easyButtonRect = pg.Rect((WIDTH/2) - 200, 200, 400, 50)
    medButtonRect = pg.Rect((WIDTH/2) - 200, 200 + 100, 400, 50)
    hardButtonRect = pg.Rect((WIDTH/2) - 200, 200 + 200, 400, 50)
    if easyButtonRect.collidepoint(mouse):
        easyButtonRect = pg.Rect((WIDTH/2) - 200 -10, 200 - 10, 400, 50)
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        if click:
            state = "easy"
            

    elif medButtonRect.collidepoint(mouse):
        medButtonRect = pg.Rect((WIDTH/2) - 200 -10, 200 + 100 -10, 400, 50)
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        if click:
            state = "med"
            

    elif hardButtonRect.collidepoint(mouse):
        hardButtonRect = pg.Rect((WIDTH/2) - 200 - 10, 200 + 200 -10, 400, 50)
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        if click:
            state = "hard"

    else:
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
    

    easyText = font.render("EASY", True, black , None)
    medText = font.render("MEDIUM", True, black , None)
    hardText = font.render("HARD", True, black , None)

    easyButton = pg.draw.rect(screen,white, easyButtonRect)
    easyRect = easyText.get_rect(center = easyButtonRect.center)
    screen.blit(easyText, easyRect)

    medButton = pg.draw.rect(screen, white, medButtonRect)
    medRect = medText.get_rect(center = medButtonRect.center)
    screen.blit(medText, medRect)

    hardButton = pg.draw.rect(screen, white, hardButtonRect)
    hardRect = hardText.get_rect(center = hardButtonRect.center)
    screen.blit(hardText, hardRect)
    return state


    
click = False


while running:
    mouse = pg.mouse.get_pos()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            click = True
        else: click = False
    screen.fill("black")
    if (running and state == "menu"):
        state = showMenu(click, state)
    else: break
    print(state)
    pg.display.flip()
    clock.tick(60)  # limits FPS to 60

pg.quit()