def initGame():
    global gamePad, clock, background, fighter
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting') # 게임 이름
    background = pygame.image.load('background.png') #배경 그림
    fighter = pygame.image.load('fighter.png') #전투기 그림 
    clock = pygame.time.Clock()

def runGame():
    global gamepad, clock, background, fighter

    #전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    #전투기 초기 위치 (x,y)
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0
