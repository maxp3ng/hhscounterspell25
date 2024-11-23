import pygame
import random

class CollisionEffect:
    def __init__(self):
        self.particles = []
        
    def create_effect(self, x, y, color=(255, 0, 0)):
        """Create a particle effect at the collision point"""
        for _ in range(10):  # Number of particles
            particle = {
                'x': x,
                'y': y,
                'dx': random.uniform(-3, 3),
                'dy': random.uniform(-3, 3),
                'lifetime': 20,  # How many frames the particle lives
                'color': color,
                'size': random.randint(2, 5)
            }
            self.particles.append(particle)
    
    def update(self):
        """Update particle positions and remove dead particles"""
        # Update existing particles
        for particle in self.particles[:]:  # Create a copy of the list to modify it
            particle['x'] += particle['dx']
            particle['y'] += particle['dy']
            particle['lifetime'] -= 1
            
            # Remove dead particles
            if particle['lifetime'] <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen):
        """Draw all particles"""
        for particle in self.particles:
            alpha = int((particle['lifetime'] / 20) * 255)  # Fade out
            surf = pygame.Surface((particle['size'], particle['size']), pygame.SRCALPHA)
            
            # Create color with alpha
            color = (*particle['color'], alpha)
            pygame.draw.circle(surf, color, 
                             (particle['size']//2, particle['size']//2), 
                             particle['size']//2)
            
            screen.blit(surf, (particle['x'] - particle['size']//2, 
                             particle['y'] - particle['size']//2))
