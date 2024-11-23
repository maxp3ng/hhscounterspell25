from projectile import Projectile
import pygame
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Wizard(pygame.sprite.Sprite):
    projExists = False

    def __init__(self, x, y):
        super().__init__()
        # Create a simple rectangle for the player
        wizardsurf = pygame.image.load(os.path.join('static', 'img', 'wizardfire' , 'frame_0.gif'))
        self.fireframe = 0
        self.image = wizardsurf
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement speed
        self.speed = 5
        
    def sendBasicProj(self, projectiles):
        self.projExists = True
    
        basic_projectile = Projectile(WINDOW_WIDTH//2+110,WINDOW_HEIGHT//2+80,"basic")
        projectiles.add(basic_projectile)

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
