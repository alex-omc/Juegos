import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS
import Player as pl
'''
Objects
'''



'''
Setup
'''
worldx = 960
worldy = 720
fps   = 40  # frame rate
ani   = 4   # animation cycles
clock = pygame.time.Clock()
pygame.init()
world    = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load("Images/Background.png").convert()
backdropbox = world.get_rect()
player = pl.Player('hero')   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move
main = True
'''
Main Loop
'''

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
           
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
    player.update()