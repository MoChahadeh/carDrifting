import pygame


WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()
FPS = 60

BG = (100,100,100)

pygame.display.set_caption("Car Drifter")

THRUST = 2
MUE_K = 0.05