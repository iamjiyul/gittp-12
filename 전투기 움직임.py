# 전투기 움직이기

onGame = False
while not onGame:
    for event in pygame.event.get(): 
        if event.type in [pygame.QUIT]:     # 게임 프로그램 종료
            pygame.quit()
            sys.exit()

        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:    # 전투기 왼쪽으로 이동
                fighterX -= 5

            elif event.key == pygame.K_RIGHT:   # 전투기 오른쪽으로 이동
                fighterX += 5

        if event.type in [pygame.KEYUP]:     # 방향키를 떼면 전투기 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fighterX = 0

    drawObject(background, 0, 0)   # 배경 화면 그리기

    # 전투기 위치 재조정
    x +=fighterX
    if x < 0:
        x = 0
    elif x > padWidth - fighterWidth:
        x = padWidth - fighterWidth
