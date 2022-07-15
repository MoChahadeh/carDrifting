from settings import *
from car import *


car = Car()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_RIGHT:
                car.inst_thrust.x = THRUST
            elif event.key == pygame.K_LEFT:
                car.inst_thrust.x = -THRUST
            elif event.key == pygame.K_UP:
                car.inst_thrust.y = -THRUST
            elif event.key == pygame.K_DOWN:
                car.inst_thrust.y = THRUST
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car.inst_thrust.x = 0
            elif event.key == pygame.K_LEFT:
                car.inst_thrust.x = 0
            elif event.key == pygame.K_UP:
                car.inst_thrust.y = 0
            elif event.key == pygame.K_DOWN:
                car.inst_thrust.y = 0

    WINDOW.fill(BG)
    car.update()
    pygame.display.update()
    CLOCK.tick(FPS)
