# 미사일 발사하기

def initGame():
    global gamePad, clock, background, fighter, missile
    pygame.init()
    gamePad = pygame.display.set_mode((padwidth, padHeight))
    pygame.display.set_caption('PyShooting')            # 게임 이름
    background = pygame.image.load('background.png')    # 배경 그림
    fighter = pygame.image.load('fighter.png')          # 전투기 그림
    missile = pygame.image.load('missile.png')          # 미사일 그림
    clock = pygame.time.Clock()


def runGame():
    global gamepad, clock, background, fighter, missile


    # 무기 좌표 리스트
    missileXY = []


onGame = False
while not onGame:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT]:     # 게임 프로그램 종료
            pygame.quit()
            sys.exit()

        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:      # 전투기 왼쪽으로 이동
                fighterX -= 5

             elif event.key == pygame.K_RIGHT:   # 전투기 오른쪽으로 이동
                fighterX += 5

            elif event.key == pygame.K_SPACE:   # 미사일 발사
                missileX = x + fighterWidth/2
                missileY = y - fighterHeight
                missileXY.append([missileX, missileY])

drawObject(fighter, x, y)       # 비행기를 게임 화면의 (x,y) 좌표에 그림

# 미사일 발사 화면에 그리기
if len(missileXY) !=0:
    for i, bxy in enumerate(missileXY):  # 미사일 요소에 대해 반복함
        bxy[1] -= 10     #총알의 y좌표 -10 (위로 이동)
        missileXY[i][1] = bxy[1]

        if bxy[1] <= 0:  # 미사일이 화면 밖을 벗어나면
            try:
                missileXY.remove(bxy)   #미사일 제거
            except:
                pass

if len(missileXY) != 0:
    for bx, by in missileXY:
        drawObject(missile, bx, by)

pygame.display.update()  # 게임화면을 다시그림
