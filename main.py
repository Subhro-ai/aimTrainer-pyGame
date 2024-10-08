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
#Time difference, Time On, Size, distance
easySetting = [3, 5, 15, 100]
state = "menu"
timer =0


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

def game(settings):
    timeDifference = settings[0]
    timeOn = settings[1]
    size = settings[2]
    distance = settings[3]
    global timer
    currentTime = int(timer/60)
    print("1")
    while state == "easy" or "med" or "hard":
        print("2")
        while (timer / 60) - currentTime < 3:
            print("3")
            screen.fill("black")
            timer += 1
            count = font.render(str(int((timer / 60) - currentTime) + 1), True, white, None)
            container = pg.Rect((WIDTH/2) - 200, HEIGHT / 2 - 100, 400, 100)
            textRect = count.get_rect(center = container.center)
            screen.blit(count, textRect)
            pg.display.flip()
            clock.tick(60) 
        return "menu"
    
    

    
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
    elif (running and state == "easy"):
        state = game(easySetting)
        print("SDF")
    
    timer +=1
    secs = int(timer/60)
    # print(secs)
    pg.display.flip()
    clock.tick(60)  # limits FPS to 60

pg.quit()