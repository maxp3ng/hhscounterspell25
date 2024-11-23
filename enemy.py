from projectile import Projectile
import pygame
import os
import random

file_path = "tempsong.txt" 
file = open(file_path, "r")

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
    projExists = False

    def __init__(self, x, y):
        super().__init__()
        # Create a simple rectangle for the player
        enemysurf = pygame.image.load(os.path.join('static', 'img', 'enemyfire' , 'frame_0_delay-0.1s.gif'))
        self.fireframe = 0
        self.image = enemysurf
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement speed
        self.speed = 5
        
    def sendBasicProj(self, projectiles):
        self.projExists = True
    
        basic_projectile = Projectile(WINDOW_WIDTH//2+110,WINDOW_HEIGHT//2+80,"basic")
        projectiles.add(basic_projectile)

    def enemyProj(self, char):
        if (char == "x"):
            self.sendBasicProj()
        pass

    def read_next_character(file):
        char = file.read(1)  # Read one character
        return char if char else None

    def update(self):
        """Update player position based on keyboard input"""
        keys = pygame.key.get_pressed()
        frameslowdown = 4 #wait 5 ticks on each frame 
        char = self.read_next_character(file)
        self.enemyProj(self, char)
        if (self.fireframe > 0):
            filename = 'frame_' + str(int(self.fireframe//frameslowdown))+ '.gif'
            wizardsurf = pygame.image.load(os.path.join('static', 'img', 'wizardfire' , filename))
            self.image = wizardsurf
            self.fireframe = 0 if (self.fireframe == 7*frameslowdown) else self.fireframe + 1
            
           
    def draw(self, screen):
        """Draw the player to the screen"""
        screen.blit(self.image, self.rect)
