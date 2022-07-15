from settings import *


class Car(pygame.sprite.Sprite):

    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image = pygame.image.load("images/car.png")
        self.sprite = self.image
        self.rect = self.image.get_rect()
        self.rect.center = WINDOW.get_rect().center
        self.pos = pygame.Vector2(self.rect.center)
        self.spd = pygame.Vector2(0,0)
        self.angle = 0.0
        self.inst_thrust = pygame.Vector2(0,0)
    def draw(self):
        WINDOW.blit(self.sprite, self.rect)

    def update(self):

        self.spd += self.inst_thrust
        self.spd -= MUE_K*self.spd
        self.pos += self.spd
        self.rect.center = self.pos
        self.angle = self.spd.angle_to(pygame.Vector2(1,0))

        self.sprite = pygame.transform.rotate(self.image, self.angle-90)

        self.loop()
        self.draw()

    def loop(self):


        if self.pos.x > WIDTH+30:
            self.pos.x = -30
        elif self.pos.x < -30:
            self.pos.x = WIDTH+30
        if self.pos.y > HEIGHT+30:
            self.pos.y = -30
        elif self.pos.y < -30:
            self.pos.y = HEIGHT+30
    