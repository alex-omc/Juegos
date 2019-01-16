import pygame
import sys
import os

class Player(pygame.sprite.Sprite):

    def __init__(self, player_id):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.frameL = 0

        self.player_id = player_id
        self.images = [] #moving to the right
        self.throw = []  # player throws object - arm movement only
        self.player_dies = [] #player dies

        self.image = None
        self.rect = None

        self.wfq = 5 # frames walking
        self.twq = 1 # frames throwing
        self.dwq = 1 # frames dying
        self.ani = 4

        self.set_animation()


    def set_animation(self):
        ALPHA = (255, 255, 255)
        for i in range(1, self.wfq):
            img = pygame.image.load(os.path.join('images', str(self.player_id) + str(i) + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha


    def control(self, x, y):
        '''
        #control player movement
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        Update sprite position
        '''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 4:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // -1], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.images[(self.frame)]

    def detenido(self):
        self.image = self.images[0]


