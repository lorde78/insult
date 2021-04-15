import pygame, sys

from pygame.locals import *

pygame.init()
FPS = pygame.time.Clock()

window = pygame.display.set_mode((375, 812))

#Display le titre du jeu en haut
pygame.display.set_caption("10'Quetes")

jaune = (255, 220, 128)
violet_claire = (225, 48, 108)
violet_sombre = (131, 58, 180)
orange = (247, 119, 55)

def gradientLin(window, first_colour, second_colour, third_colour, forth_colour, target_window):
    colour_rect = pygame.Surface( ( 4, 4 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, first_colour,  ( 0,2 ), ( 1,2 ) )            # left colour line
    pygame.draw.line( colour_rect, second_colour, ( 1,2 ), ( 2,2 ) )            # right colour line
    pygame.draw.line( colour_rect, third_colour,  ( 2,2 ), ( 3,2 ) )            # left colour line
    pygame.draw.line( colour_rect, forth_colour,  ( 3,2 ), ( 4,2 ) )            # left colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_window.width, target_window.height ) )  # stretch!
    window.blit( colour_rect, target_window )                                  # paint it

window.fill( ( 0,0,0 ) )
gradientLin( window, (violet_sombre), (violet_claire),(orange), (jaune), pygame.Rect( 0,0, 375, 812 ) )
#gradientLin( window, (violet_sombre), (orange), pygame.Rect( 100,200, 128, 64 ) )
pygame.display.flip()

#window.fill(jaune)
#pygame.display.flip()

running = True

while running :
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
    FPS.tick(60)
    

window.blit(window, (0,0))





