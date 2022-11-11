if isShot:
    drawObject(explosion, rockX, rockY)

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    isShot = False

    rockSpeed += 0.02
    if rockSpeed >= 10:
        rockSpeed = 10
