padWidth=480
padHeight=640
rockImage=['rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
           'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
           'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
           'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
           'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
           'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png',]
explosionSound=['explosion01.wav','explosion02.wav','explosion03.wav','explosion04.wav',]

def initGame():
        global gamePad,clock,background,fighter,missile,explosion,missileSound,gameOverSound
        pygame.init()
        gamePad=pygame.display.set_mode((padWidth,padHeight))
        pygame.display.set_caption('PYShooting')            #게임이름
        background=pygame.image.load('backgrounde.png')     #배경그림
        fighter=pygame.image.load('fighter.png')            #전투기그림
        missle=pygame.image.load('missile.png')             #미사일그림
        explosion=pygame.image.load('explosion.png')        #폭발그림
        pygame.mixer.music.load('music.wav')                #배경음악
        pygame.mixer.music.play(-1)                         #배경음악재생
        missileSound=pygame.mixer.Sound('missle.wav')       #미사일사운드
        gameOverSound=pygame.mixer.Sound('gameover.wav')    #게임오버사운
        clock=pygame.time.Clock()

def runGame():
    global gamepad,clock,background,fighter,missile,explosion,missileSound

            elif event.key==pygame.K_SPACE: #미사일 발사
                missileSound.play()         #미사일 사운드 재생
                missileX=x+fighterWidth/2
                missileY=y-fighterHeight
                missile.append([missileX,missileY])

#게임 메시지 출력
def writeMessage(text):
    global gamePad,gameOverSound
    textfont=pygame.font.Font('NanumGothic.ttf',80)
    text=textfont.render(text,True,(255,0,0))
    textpos=text.get_rect()
    textpos.center=(padWidth/2,padHeight/2)
    gamePad.blit(text,textpos)
    pygame.display.update()
    pygame.mixer.music.stop()       #배경음악정지
    gameoverSound.play()            #게임오버사운드재생
    sleep(2)
    pygame.mixer.music.play(-1)     #배경음악재생
    runGame()

    rock=pygame.image.load(random.choice(rockImage))
    rockSize=rock.get_rect().size
    rockWidth=rockSize[0]
    rockHeight=rockSize[1]
    destroySound=pygame.mixer.Sound(random.choice(exposionSound))

    if isShot:
        drawObject(explosion,rockX,rockY)
        destroySound.play()

        rock=pygame.image.load(random.choice(rockImage))
        rockSize=rock.get_rect().size
        rockWidth=rockSize[0]
        rockHeight=rockSize[1]
        rockX=random.randrange(0,padWidth-rockWidth)
        rockY=0
        destroySound=pygame.mixer.Sound(random.choice(exposionSound))
        isShot=False



    
