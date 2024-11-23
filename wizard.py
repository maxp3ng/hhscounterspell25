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
        wizardsurf = pygame.image.load(os.path.join('static', 'img', 'wizard.png'))
        self.image = wizardsurf
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement speed
        self.speed = 5
        
    def sendBasicProj(self, projectiles):
        self.projExists = True
    
        basic_projectile = Projectile(WINDOW_WIDTH//2,WINDOW_HEIGHT//2,"basic")
        projectiles.add(basic_projectile)

    def update(self):
        """Update player position based on keyboard input"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            pass
           
    def draw(self, screen):
        """Draw the player to the screen"""
        screen.blit(self.image, self.rect)
