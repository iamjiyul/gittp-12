#게임에 등장하는 객체를 드로잉 
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))

def initGame():
    global gamePad, clock, background
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting') #게임 이름 
    background = pygame.image.load('background.png') #배경 그림 
    clock = pygame.time.Clock()

def runGame():
    global gamepad, clock, background

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: #게임 프로그램 종료 
                pygame.quit()
                sys.exit()

                drawObject(background, 0, 0) #배경 화면 그리기

                pygame.display.update() #게임 화면을 다시 그
