# 게임 메시지 출력
def writeMessage(text):
    global gamePad
    textfont=pygame.font.Font('NanumGothic.ttf',80)
    text=textfont.render(text,True,(255,0,0))
    textpos=text.get_rect()
    textpos.center=(padWidth/2,padHeight/2)
    gamePad.blit(text,textpos)
    pygame.display.update()
    sleep(2)
    runGame()

# 전투기가 운석과 충돌
def crash():
    global gamePad
    writeMessage('전투기 파괴!')

# 게임 오버 메시지 보이기
def gameOver():
    global gamePad
    writeMessage('게임 오버!')
# 전투기 위치 재조정
    x+=fighterX
    if x<0:
        x=0
    elif x>padWidth-fighterWidth:
        x=padWidth-fighterWidth
# 전투기가 운석과 충돌했는지 체크
    if y<rockY+rockHeight:
        if(rockX> x and rockX< x + fighterWidth) or (rockX+rockWidth>x and rockX + rockWidth <  x + fighterWidth)
            crash()

    drawObject(fighter,x,y) # 비행기를 게임 화면의 (x,y) 좌표에 그림

    if rockPassed==3: #운석 3개 놓치면 게임오버
        gameOver()
    #놓친 운석 수 표시
    writePassed(rockPassed)
