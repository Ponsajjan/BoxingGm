import pygame, sys
from pygame.math import Vector2
from pygame.locals import *
FPS = 4
pygame.init()
#this is ttriAL 1 CODE modified
screen_width = 1300
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boxing")
clock = pygame.time.Clock()``
game_font = pygame.font.Font('freesansbold.ttf', 32)
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()




























			
class spritesheet():
        def __init__(self, filename, cols, rows, player1_position, player1_rect):
            self.sheet = filename
                    
            self.cols = cols
            self.rows = rows
            self.totalCellCount = cols * rows
            self.player1_position = player1_position
                    
            self.rect = player1_rect
            w = self.cellWidth = int(self.rect.width / cols)
            h = self.cellHeight = int(self.rect.height / rows)
            hw, hh = self.cellCenter = (int(w / 2), int(h / 2))
                    
            self.cells = list([(index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)])
            self.handle = list([
                    (0, 0), (-hw, 0), (-w, 0),
                    (0, -hh), (-hw, -hh), (-w, -hh),
                    (0, -h), (-hw, -h), (-w, -h),])
                    
        def draw(self, surface, cellIndex, x, y, handle = 0):
            surface.blit(self.sheet, (self.rect), self.cells[cellIndex])

#player1
player1_play = pygame.image.load('player1.png').convert_alpha()
player1_player = player1_play
player1_angle = 0
player1_velocity = Vector2(0,-9)
player1_position = Vector2(screen_width, screen_height)
player1_rect = player1_player.get_rect(center = player1_position)







CENTER_HANDLE = 4

index = 0

# main loop
run = True
pause = False
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run=False
               
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player1_angle +=5
        player1_velocity.rotate_ip(-5)
        player1_player = pygame.transform.rotate(player1_player, player1_angle)
        player1_rect = player1_player.get_rect(center = player1_rect.center)
        player1_mask = pygame.mask.from_surface(player1_player)
                
        index +=1
        if index >= 8:
            index = 5
                    
    elif keys[pygame.K_UP]:
        player1_angle =-5
        player1_velocity.rotate_ip(5)
        player1_player = pygame.transform.rotate(player1_player, player1_angle)
        player1_rect = player1_player.get_rect(center = player1_rect.center)
        player1_mask = pygame.mask.from_surface(player1_player)

    index +=1
    if index >= 4:
        index = 2   
    player1_position += player1_velocity
    player1_rect.center = player1_position

    events()
    player1 = spritesheet(player1_player, 5, 2, player1_position, player1_rect)
    player1.draw(screen, index, screen_width/2, screen_height/2, CENTER_HANDLE)
    pygame.display.flip()
    #pygame.display.update()
    clock.tick(FPS)
    screen.fill((4, 44, 144))









