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
    def __init__(self, x, y, projType):
        super().__init__()
        self.x = x
        self.y = y
        self.projType = projType
        self.direction = random.random() * 6 - 3
        self.fireframe = 0

        self.speed = 5
        
        wizardsurf = load_scaled_image(os.path.join('static', 'img', 'fireball' , 'frame_0.png'), 0.2)
        self.image = wizardsurf
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Update fireball to tail"""
        frameslowdown =  40 #wait 5 ticks on each frame 
        filename = 'frame_' + str(int(self.fireframe//frameslowdown))+ '.png'
        fireballFrame = load_scaled_image(os.path.join('static', 'img', 'fireball' , filename),0.2)
        self.image = fireballFrame 
        self.fireframe = 0 if (self.fireframe == 1*frameslowdown) else self.fireframe + 1



        """Moves in an arc """
        self.rect.x += 5
        if (self.direction == "up"):
            randomNum =  random.random() * self.direction 
            self.rect.y += randomNum
        else:
            self.rect.y -= random.random() * self.direction
           
    def draw(self, screen):
        """Draw the player to the screen"""
        screen.blit(self.image, self.rect)
