from settings import *



while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    WINDOW.fill(BG)
    pygame.display.update()
    CLOCK.tick(FPS)
