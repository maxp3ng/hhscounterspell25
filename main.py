import pygame
import sys
from wizard import Wizard
from sound import Sound
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
BG_COLOR_TOP = (60, 120, 180)
BG_COLOR_BOTTOM = (30, 60, 90)
BUTTON_COLOR = (255, 255, 255)
BUTTON_HOVER_COLOR = (200, 200, 200)
TEXT_COLOR = (0, 0, 0)

#Screen State
MAIN_MENU = 0
DIALOGUE = 1
GAMEPLAY = 2

currentState =  MAIN_MENU

# Fonts
FONT = pygame.font.Font(pygame.font.get_default_font(), 40)

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

        # Initialize sound
        self.sound = Sound()
        self.sound.background()  # Start playing music here

        self.enemy = Enemy(WINDOW_WIDTH // 1.25, WINDOW_HEIGHT //3)
        self.projectiles = pygame.sprite.Group()
        
        # Game state
        self.running = True
        self.current_state = MAIN_MENU

    
    def draw_gradient(self):
        """Draw a gradient background"""
        for y in range(WINDOW_HEIGHT):
            color = (
                BG_COLOR_TOP[0] + (BG_COLOR_BOTTOM[0] - BG_COLOR_TOP[0]) * y // WINDOW_HEIGHT,
                BG_COLOR_TOP[1] + (BG_COLOR_BOTTOM[1] - BG_COLOR_TOP[1]) * y // WINDOW_HEIGHT,
                BG_COLOR_TOP[2] + (BG_COLOR_BOTTOM[2] - BG_COLOR_TOP[2]) * y // WINDOW_HEIGHT,
            )
            pygame.draw.line(self.screen, color, (0, y), (WINDOW_WIDTH, y))

    def draw_button(self, x, y, w, h, text, hover):
        """Draw the start button"""
        color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, (x, y, w, h), border_radius=10)
        button_text = FONT.render(text, True, TEXT_COLOR)
        self.screen.blit(button_text, (x + (w - button_text.get_width()) // 2, y + (h - button_text.get_height()) // 2))

    def main_menu(self):
        """Display the main menu"""
        self.draw_gradient()

        # Button details
        button_x, button_y, button_w, button_h = (WINDOW_WIDTH - 200) // 2, (WINDOW_HEIGHT - 70) // 2, 200, 70

        # Get mouse position and state
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Check if mouse is over the button
        button_hover = button_x < mouse_pos[0] < button_x + button_w and button_y < mouse_pos[1] < button_y + button_h
        
        # Draw Start button
        self.draw_button(button_x, button_y, button_w, button_h, "Start", button_hover)
        
        # Handle button click
        if button_hover and mouse_click[0]:
            self.current_state = GAMEPLAY

        pygame.display.flip()

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
                if event.key == pygame.K_SPACE and self.current_state == GAMEPLAY:
                    self.wizard.sendBasicProj(self.projectiles)
                    self.wizard.fireframe()


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
                    self.wizard.fireframe()

                    
    def update(self):
        """Update game state"""
        if self.current_state == GAMEPLAY:
            self.wizard.update()
            self.enemy.update()
            self.projectiles.update()
    
    def render(self):
        """Render the game state to the screen"""
        if self.current_state == MAIN_MENU:
            self.main_menu()
        elif self.current_state == GAMEPLAY:
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
