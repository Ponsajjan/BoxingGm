import pygame, sys
from pygame.math import Vector2
from pygame.locals import *
FPS = 10
pygame.init()
screen_width = 1300
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boxing")
clock = pygame.time.Clock()
game_font = pygame.font.Font('freesansbold.ttf', 32)

#player1
player1 = list([pygame.image.load('player1_{0}.png'.format(i)).convert_alpha() for i in range(1, 9)])
player1_angle = 0
player1_velocity = Vector2(-25,0)
player1_position = Vector2(screen_width/2+300, screen_height/2-50)
player1_mask = pygame.mask.from_surface(player1[0])

player1_turn = 2  
player1_idle = [0, 1]
player1_walk = [2, 3]
player1_attack = [4, 5]
player1_attacked1 = 6
player1_attacked2 = 7
player1_attacked3 = 8
index = 0
    
run = True
while run == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run=False
                 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1_position += player1_velocity
        index = [2, 3]

    elif keys[pygame.K_LEFT]:
        player1_angle +=25
        player1_velocity.rotate_ip(-25)
        index = [2, 3]
  
    elif keys[pygame.K_RIGHT]:
        player1_angle -=25
        player1_velocity.rotate_ip(25)
        index = [2, 3]

    elif keys[pygame.K_SPACE]:
        index = [1, 2, 3, 4, 5]

    else:
        index = [1, 2]

    for frame in index:
        screen.fill((4, 44, 48))
        player = pygame.transform.rotate(player1[frame], player1_angle)
        player1_rect = player.get_rect(center = player1_position)
        screen.blit(player, player1_rect)   
        pygame.display.flip()
        clock.tick(FPS)

