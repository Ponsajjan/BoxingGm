import pygame, sys
from pygame.math import Vector2
from pygame.locals import *
FPS = 1
pygame.init()
screen_width = 650
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Boxing")
clock = pygame.time.Clock()
game_font = pygame.font.Font('freesansbold.ttf', 32)
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
class spritesheet():
        def __init__(self, filename, cols, rows):
            self.sheet = pygame.image.load(filename).convert_alpha()
                    
            self.cols = cols
            self.rows = rows
            self.totalCellCount = cols * rows
                    
            self.rect = self.sheet.get_rect()
            w = self.cellWidth = int(self.rect.width / cols)
            h = self.cellHeight = int(self.rect.height / rows)
            hw, hh = self.cellCenter = (int(w / 2), int(h / 2))
                    
            self.cells = list([(index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)])
            self.handle = list([
                    (0, 0), (-hw, 0), (-w, 0),
                    (0, -hh), (-hw, -hh), (-w, -hh),
                    (0, -h), (-hw, -h), (-w, -h),])
                    
        def draw(self, surface, cellIndex, x, y, handle = 0):
            surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

#player1
player1 = spritesheet("player1.png", 5, 2)
player1_player = player1.sheet
player1_angle = 0
player1_velocity = Vector2(-3,0)
player1_position = Vector2(screen_width/2+300, screen_height/2-50)
player1_rect = player1.rect
player1_mask = pygame.mask.from_surface(player1_player)
player1_score = 0
play1_stext = game_font.render("player1 ", False, (200, 200, 200))

#player2
player2 = spritesheet("player2.png", 5, 2)
player2_player = player2.sheet
player2_angle = 0
player2_velocity = Vector2(3,0)
player2_position = Vector2(screen_width/2-300, screen_height/2+50)
player2_rect = player2.rect
player2_mask = pygame.mask.from_surface(player2_player)
player2_score = 0
play2_stext = game_font.render("player2 ", False, (200, 200, 200))

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
               
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_angle =5
                player1_velocity.rotate_ip(-5)
                player1_player = pygame.transform.rotate(player1_player, player1_angle)
                player1_rect = player1_player.get_rect(center = player1_rect.center)
                player1_mask = pygame.mask.from_surface(player1_player)
            if event.key == pygame.K_UP:
                player1_angle =-5
                player1_velocity.rotate_ip(5)
                player1_player = pygame.transform.rotate(player1_player, player1_angle)
                player1_rect = player1_player.get_rect(center = player1_rect.center)
                player1_mask = pygame.mask.from_surface(player1_player)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_UP:
                pass


    player1_position += player1_velocity
    player1_rect.center = player1_position
    player2_position += player2_velocity
    player2_rect.center = player2_position
                 
    events()
    player1.draw(screen, index % player1.totalCellCount, screen_width/2, screen_height/2, CENTER_HANDLE)

    player2.draw(screen, index % player2.totalCellCount, screen_width/2, screen_height/2, CENTER_HANDLE)

    index += 1
	
    pygame.display.update()
    clock.tick(FPS)
    screen.fill((144, 44, 4))

'''

background = pygame.image.load('BG_IMG.png').convert()
player1_idle = [pygame.image.load('player1_1.png'), pygame.image.load('player1_2.png')]
player1_walk = [pygame.image.load('player1_3.png'), pygame.image.load('player1_4.png')]
player1_attack = [pygame.image.load('player1_5.png'), pygame.image.load('player1_6.png')]
player1_attacked1 = [pygame.image.load('player1_7.png')]
player1_attacked2 = [pygame.image.load('player1_8.png')]
player1_attacked3 = [pygame.image.load('player1_9.png')]
'''







