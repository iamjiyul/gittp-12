def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad=pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')        #게임 이름
    background=pygame.image.load('background.png')  #배경 그림
    fighter=pygame.image.load('fighter.png')        #전투기 그림
    missile=pygame.image.load('missile.png')        #미사일 그림
    explosion=pygame.image.load('explosion.png')    #폭발 그림
    clock=pygame.time.Clock()

def runGame():
    global gamepad, clock, background, fighter, missile, explosion

#전투기 미사일에 운석이 맞았을 경우 True
isShot=False
shotCount=0
rockPassed=0

onGame=False
while not onGame:
    #미사일 발사 화면에 그리기
    if len(missileXY) != 0:
        for i, bxy in enumerate(missileXY): #미사일 요소에 대해 반복함
            bxy[1] -= 10    #총알의 y좌표 -10 (위로 이동)
            missileXY[i][1]=bxy[1]

            #미사일이 운석을 맞추었을 경우
            if bxy[1] <rockY:
                if bxy[0]<rockX and bxy[0]<rockX+rockWidth:
                    missileXY.remove(bxy)
                    isShot=True
                    shotCount +=1

            if bxy[1]<=0:   #미사일이 화면 밖을 벗어나면
                try:
                    missileXY.remove(bxy)   #미사일 제거
                except:
                    pass

            #운석을 맞춘 경우        
            if isShot:
                #운석 폭발
                drawObject(explosion, rockX, rockY) #운석 폭발 그리기

                #새로운 운석 (랜덤)
                rock=pygame.image.load(random.choice(rockImage))
                rockSize=rock.get_rect().size
                rockWidth=rockSize[0]
                rockHeight=rockSize[1]
                rockX=random.randrange(0,padWidth-rockWidth)
                rockY=0
                isShot=False
            
            drawObject(rock,rockX, rockY)     #운석 그리기


