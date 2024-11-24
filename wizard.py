from projectile import Projectile
import random
import pygame
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Wizard(pygame.sprite.Sprite):
    projExists = False

    def __init__(self, x, y, WINDOW_WIDTH, WINDOW_HEIGHT):
        super().__init__()
        # Create a simple rectangle for the player
        wizardsurf = pygame.image.load(os.path.join('static', 'img', 'wizardfire' , 'frame_0.gif'))
        self.fireframe = 0
        self.image = wizardsurf
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.WINDOW_WIDTH= WINDOW_WIDTH 


        # Movement speed
        self.speed = 25
        
    def sendBasicProj(self, projectiles):
        self.projExists = True
        direction = 0#random.random() * 6 - 3 
   
        fireballDelay = 15
        fireball_x = -260
        fireball_y = -80
        fireball_tail = Projectile(self.WINDOW_WIDTH//2+fireball_x,self.WINDOW_HEIGHT//2+fireball_y,"fireball_tail", direction)
        fireball_head = Projectile(self.WINDOW_WIDTH//2+fireball_x+fireballDelay,self.WINDOW_HEIGHT//2+fireball_y,"fireball_head", direction)
        projectiles.add(fireball_head)
        projectiles.add(fireball_tail)

    def update(self):
        """Update wizard sprite on spacebar"""
        frameslowdown = 4 #wait 5 ticks on each frame 
        if (self.fireframe > 0):
            filename = 'frame_' + str(int(self.fireframe//frameslowdown))+ '.gif'
            wizardsurf = pygame.image.load(os.path.join('static', 'img', 'wizardfire' , filename))
            self.image = wizardsurf
            self.fireframe = 0 if (self.fireframe == 7*frameslowdown) else self.fireframe + 1
            
           
    def draw(self, screen):
        """Update self on screen"""
        screen.blit(self.image, self.rect)
