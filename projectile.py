import pygame
import random


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, projType):
        super().__init__()
        self.x = x
        self.y = y
        self.projType = projType
        self.direction = random.random() * 6 - 3

        self.speed = 5
        
        size = 10
        self.image = pygame.Surface([size, size])
        self.image.fill((0, 0, 0))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
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
