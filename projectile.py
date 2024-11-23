import pygame
import os
from collections import deque

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
        
        # Initialize position history for head projectiles
        self.position_history = deque(maxlen=3)  # Reduced history length for closer following
        self.tail = None
        
        fireball_x = -260
        fireball_y = -80
        
        if (projType == "fireball_head"):
            wizardsurf = load_scaled_image(os.path.join('static', 'img', 'fireball', 'frame_0.png'), 0.2)
            self.image = wizardsurf
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.tail = Projectile(self.rect.x - 15, y, "fireball_tail", direction)
        elif (projType == "fireball_tail"):
            wizardsurf = load_scaled_image(os.path.join('static', 'img', 'fireball', 'frame_1.png'), 0.2)
            self.image = pygame.transform.flip(wizardsurf, True, False)
            self.tail = None
        elif (projType == "enemyball"):
            wizardsurf = load_scaled_image(os.path.join('static', 'img', 'fireball', 'frame_0.png'), 0.2)
            self.image = pygame.transform.grayscale(wizardsurf)
        else:
            raise Exception("impossible ball type detected!")
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Moves in an arc"""
        if self.projType == "fireball_head":
            # Update head position first
            self.rect.x += 5
            if self.direction == "up":
                self.rect.y += self.direction
            else:
                self.rect.y -= self.direction

            # Store current position after moving
            self.position_history.append((self.rect.x, self.rect.y))
            
            # Update tail position to follow very closely
            if self.tail:
                # Make tail follow closely behind the head
                self.tail.rect.x = self.rect.x - 15  # Reduced offset
                self.tail.rect.y = self.rect.y
                
        elif self.projType == "enemyball":
            self.rect.x -= 5
            if self.direction == "up":
                self.rect.y += self.direction
            else:
                self.rect.y -= self.direction

    def kill(self):
        """Override kill to also remove tail"""
        if self.projType == "fireball_head" and self.tail:
            self.tail.kill()
        super().kill()

    def draw(self, screen):
        """Draw the projectile and its tail to the screen"""
        # Draw tail first so it appears behind the head
        if self.tail:
            self.tail.draw(screen)
        screen.blit(self.image, self.rect)
