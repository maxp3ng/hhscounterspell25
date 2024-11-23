import pygame
import sys
from wizard import Wizard
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Constants
info = pygame.display.Info()
WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        # Create the game window
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Counterspell")  
        
        # Set up the game clock
        self.clock = pygame.time.Clock()
        
        # Create the player at the center of the screen
        self.wizard = Wizard(WINDOW_WIDTH // 4, WINDOW_HEIGHT // 3)
        self.projectiles = pygame.sprite.Group()

        self.enemy = Enemy(WINDOW_WIDTH // 1.25, WINDOW_HEIGHT //3)
        self.projectiles = pygame.sprite.Group()
        
        # Game state
        self.running = True

    
    def handle_events(self):
        """Handle game events like keyboard input and window closing"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.wizard.sendBasicProj(self.projectiles)

                    
    def update(self):
        """Update game state"""
        self.wizard.update()
        self.enemy.update()
        self.projectiles.update() 
    
    def render(self):
        """Render the game state to the screen"""
        self.screen.fill(WHITE)
        
        self.enemy.draw(self.screen)
        
        self.wizard.draw(self.screen)
        for projectile in self.projectiles:
            projectile.draw(self.screen) 

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
