def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf',20)
    text = font.render('파괴한 운석 수: + str(count),True(255,255,255))
    gamePad.blit(text,(10.0))



def writePassed(count):
    global gamePad
    font= pygame.font.Font('NanumGothic.ttf',20)
    text = font.render('놓친 운석:' + str(count),True,(255.0.0))
    gamePad.blit(text, (360.0))




writeScore(shotCount)
rockY += rockSpeed

if rockY > padHeight:

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0,padWidth - rockWidth)
    rockY = 0
    rockPassed +=1

    writePassed(rockPassed)
