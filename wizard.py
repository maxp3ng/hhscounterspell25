import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Wizard(pygame.sprite.Sprite):
    projExists = False

    def __init__(self, x, y):
        super().__init__()
        # Create a simple rectangle for the player
        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement speed
        self.speed = 5
      
    def update(self):
        """Update player position based on keyboard input"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            pass
           
    def draw(self, screen):
        """Draw the player to the screen"""
        screen.blit(self.image, self.rect)
