import pygame

class Projectiles()):
    

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        self.speed = 5
        
    def update(self):
        """Moves in an arc TODO"""

    def sendBasicProj(self, x, y):
        self.image = pygame.Surface([1, 1])
        self.image.fill((0, 0, 0))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
           
    def draw(self, screen):
        """Draw the player to the screen"""
        screen.blit(self.image, self.rect)
