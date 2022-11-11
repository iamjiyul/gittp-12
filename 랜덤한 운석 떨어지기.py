#import pygame
#import sys
import random
#from time import sleep

padWidth=480    #게임화면의 가로크기
padHeight=640   #게임화면의 세로크기
rockImage=['rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
            'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
            'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
            'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
            'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
            'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png'  ]


missileXY=[]    #무기 좌표 리스트

rock=pygame.image.load(random.choice(rockImage))    #운석 랜덤 생성
rockSize=rock.get_rect().size   #운석 크기
rockWidth=rockSize[0]
rockHeight=rockSize[1]

#운석 초기 위치 설정
rockX=random.randrange(0,padWidth-rockWidth)
rockY=0
rockSpeed=2

if len(missileXY) != 0:
    for bx, by in missileXY:
        drawObject(missile, bx, by)

rockY+=rockSpeed #운석 아래로 움직임

#운석이 지구로 떨어진 경우
if rocky > padHeight:
    #새로운 운석 (랜덤)
    rock = pygame.image.load(random.choice(rockImage))
    rockSize=rock.get_rect().size
    rockWidth=rockSize[0]
    rockHeight=rockSize[1]
    rockX=random,randrange(0,padWidth-rockWidth)
    rockY=0

drawObject(rock,rockX,rockY)    #운석 그리기

pygame.display.update() #게임 화면을 다시 그림
