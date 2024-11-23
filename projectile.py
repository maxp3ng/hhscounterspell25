import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, projType):
        super().__init__()
        self.x = x
        self.y = y
        self.projType = projType

        self.speed = 5
        
        size = 10
        self.image = pygame.Surface([size, size])
        self.image.fill((0, 0, 0))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Moves in an arc TODO"""
        self.rect.x += 5

           
    def draw(self, screen):
        """Draw the player to the screen"""
        screen.blit(self.image, self.rect)
