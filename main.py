import pygame
import sys
from wizard import Wizard

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        # Create the game window
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("My Game")
        
        # Set up the game clock
        self.clock = pygame.time.Clock()
        
        # Create the player at the center of the screen
        self.wizard = Wizard(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.projectiles = pygame.sprite.Group()
        
        # Game state
        self.running = True
  
    def sendBasicProj(self):
        #self.projectile = Projectile(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
        self.projExists = True
    
    def handle_events(self):
        """Handle game events like keyboard input and window closing"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    
    def update(self):
        """Update game state"""
        # Update player position
        self.wizard.update()
    
    def render(self):
        """Render the game state to the screen"""
        # Clear the screen
        self.screen.fill(WHITE)
        
        # Draw the player
        self.wizard.draw(self.screen)
        
        # Update the display
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            # Handle input events
            self.handle_events()
            
            # Update game state
            self.update()
            
            # Render the frame
            self.render()
            
            # Maintain consistent frame rate
            self.clock.tick(FPS)

def main():
    # Create and run the game
    game = Game()
    game.run()
    
    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    # RENDER YOUR GAME HERE
    
    pygame.display.flip()


pygame.quit()
