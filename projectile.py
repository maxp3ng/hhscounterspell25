import pygame
import os
import random



def load_scaled_image(image_path, scale_factor=0.5):
    """Load and scale image by a factor (e.g., 0.5 for half size)"""
    image = pygame.image.load(image_path).convert_alpha()
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, projType, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.projType = projType
        self.direction = direction
        self.fireframe = 0

        self.speed = 5
        self.projType = projType 


        fireball_x = -260
        fireball_y = -80
        if (projType == "fireball_head"):
            wizardsurf = load_scaled_image(os.path.join('static', 'img', 'fireball' , 'frame_0.png'), 0.2)
            self.image = wizardsurf
        elif (projType == "fireball_tail"):
            wizardsurf = load_scaled_image(os.path.join('static', 'img', 'fireball' , 'frame_1.png'), 0.2)
            self.image = pygame.transform.flip(wizardsurf, True, False)
        elif (projType == "enemyball"):
            wizardsurf = load_scaled_image(os.path.join('static', 'img', 'fireball' , 'frame_0.png'), 0.2)
            self.image = pygame.transform.grayscale(wizardsurf)
        else:
            raise Exception("impossible ball type detected! ")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Moves in an arc """
        self.rect.x += -5 if (self.projType == "enemyball") else 5
        if (self.direction == "up"):
            self.rect.y += self.direction 
        else:
            self.rect.y -= self.direction
           
    def draw(self, screen):
        """Draw the player to the screen"""
        screen.blit(self.image, self.rect)
