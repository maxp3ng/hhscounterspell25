import pygame
import sys
from wizard import Wizard
from sound import Sound
from enemy import Enemy
from collisionEffect import CollisionEffect

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
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_COLOR_TOP = (60, 120, 180)

BG_COLOR_BOTTOM = (30, 60, 90)
BUTTON_COLOR = (0,0,0)
BUTTON_HOVER_COLOR = (0,0,0)
TEXT_COLOR = (255, 51, 139)

#Screen State
MAIN_MENU = 0
DIALOGUE = 1
GAMEPLAY = 2
ATTRIBUTIONS = 3

currentState =  MAIN_MENU

# Fonts
FONT = pygame.font.Font(pygame.font.get_default_font(), 40)
dialogueFont = pygame.font.Font(None, 24)


class Game:
    def __init__(self):
        # Create the game window
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Counterspell")  
        
        # Set up the game clock
        self.clock = pygame.time.Clock()
        
        # Create the player at the center of the screen
        self.wizard = Wizard(WINDOW_WIDTH // 4, WINDOW_HEIGHT // 3, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.projectiles = pygame.sprite.Group()

        self.enemy = Enemy(WINDOW_WIDTH // 1.25, WINDOW_HEIGHT //3, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.button_scale = 1.0  # Initial scale of the button
        self.scale_speed = 0.1  # Speed of scaling


        
        # Game state
        self.running = True
        self.time = 0
        self.current_state = MAIN_MENU
        self.collision_effects = CollisionEffect()
    
    def draw_gradient(self):
        """Draw a gradient background"""
        for y in range(WINDOW_HEIGHT):
            color = (
                BG_COLOR_TOP[0] + (BG_COLOR_BOTTOM[0] - BG_COLOR_TOP[0]) * y // WINDOW_HEIGHT,
                BG_COLOR_TOP[1] + (BG_COLOR_BOTTOM[1] - BG_COLOR_TOP[1]) * y // WINDOW_HEIGHT,
                BG_COLOR_TOP[2] + (BG_COLOR_BOTTOM[2] - BG_COLOR_TOP[2]) * y // WINDOW_HEIGHT,
            )
            pygame.draw.line(self.screen, color, (0, y), (WINDOW_WIDTH, y))

    def draw_button(self, x, y, w, h, text, hover, font_size=40, button_scale=1.0):
        """Draw a button with customizable font size and button scale"""
        color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, (x, y, w, h), border_radius=10)
    
        # Use the font size provided for rendering text
        button_font = pygame.font.Font("MightySouly-lxggD.ttf", font_size)
        button_text = button_font.render(text, True, TEXT_COLOR)
        self.screen.blit(button_text, (x + (w - button_text.get_width()) // 2, y + (h - button_text.get_height()) // 2))

        # Adjust the scaling of the button for smooth transitions
        target_scale = 1.1 if hover else 1.0
        self.button_scale += (target_scale - self.button_scale) * self.scale_speed

        # Calculate scaled button dimensions
        scaled_w = int(w * self.button_scale)
        scaled_h = int(h * self.button_scale)
        scaled_x = x - (scaled_w - w) // 2
        scaled_y = y - (scaled_h - h) // 2

        # Draw the button with the scaled dimensions
        pygame.draw.rect(self.screen, color, (scaled_x, scaled_y, scaled_w, scaled_h), border_radius=10)

        # Render the text on the scaled button
        button_text = button_font.render(text, True, TEXT_COLOR)
        text_x = scaled_x + (scaled_w - button_text.get_width()) // 2
        text_y = scaled_y + (scaled_h - button_text.get_height()) // 2
        self.screen.blit(button_text, (text_x, text_y))



    def main_menu(self):
        # Set background color to black
        self.screen.fill(BLACK)

        # Title settings using custom font
        title_font = pygame.font.Font("MightySouly-lxggD.ttf", 100)  # Use custom font here
        title_text = title_font.render("COUNTERSPELL", True, TEXT_COLOR)  # White text for contrast
        title_x = (WINDOW_WIDTH - title_text.get_width()) // 2
        title_y = WINDOW_HEIGHT // 6
        self.screen.blit(title_text, (title_x, title_y))

        # Button details
        button_x, button_y, button_w, button_h = (WINDOW_WIDTH - 200) // 2, (WINDOW_HEIGHT - 70) // 2, 200, 70
        button_sound = pygame.mixer.Sound('game-start.mp3')
        attribution_x, attribution_y, attribution_w, attribution_h = (WINDOW_WIDTH - 200) // 2, (WINDOW_HEIGHT - 20) // 2 + 100, 200, 70

        # Get mouse position and state
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Check if mouse is over the button
        button_hover = button_x < mouse_pos[0] < button_x + button_w and button_y < mouse_pos[1] < button_y + button_h
        attribution_button_hover = attribution_x < mouse_pos[0] < attribution_x + attribution_w and attribution_y < mouse_pos[1] < attribution_y + attribution_h
    
        # Draw Start button
        self.draw_button(button_x, button_y, button_w, button_h, "Start", button_hover)
    
        # Draw Attributions button with smaller font size and scale
        self.draw_button(attribution_x, attribution_y, attribution_w, attribution_h, "Credits", attribution_button_hover, font_size=30, button_scale=0.8)
    
        # Handle button clicks
        if button_hover and mouse_click[0]:
            self.currentLine = 0
            button_sound.play()
            self.current_state = DIALOGUE
        elif attribution_button_hover and mouse_click[0]:
            self.current_state = ATTRIBUTIONS

        pygame.display.flip()

    


    def dialogue(self):
        self.dialogueText = [
            "You have come far, my younger self. But there is still much you need to learn before you can take on the greater evil.",
            "I don’t know if I can do this, Master. These spells… they’re too fast for me.",
            "You must learn to keep up, or we both fail. This is not just a test of power—it’s a test of will. Protect yourself, protect me. Afterall, the only thing that separates us is time.",
            "But what if I can’t…? What happens if I fail?",
            "If I fail, you fail. If you fail, I fail. Our deaths would cause ripples in time and space itself.",
            "I’ll try. For the sake of our world."
        ]

        screen.fill(WHITE)

        if self.currentLine < len(self.dialogueText):
            text_surface = dialogueFont.render(self.dialogueText[self.currentLine], True, BLACK)
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            screen.blit(text_surface, text_rect) 

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
                if event.key == pygame.K_SPACE and self.current_state == DIALOGUE:
                    self.currentLine += 1
                    if self.currentLine >= len(self.dialogueText):
                        # Initialize sound
                        self.sound = Sound()
                        self.sound.background()  # Start playing music here
                        self.current_state = GAMEPLAY
                        self.time = 0
                        
                if event.key == pygame.K_SPACE and self.current_state == GAMEPLAY:
                    self.wizard.sendBasicProj(self.projectiles)
    def checkCollisions(self, time, projectiles):
        """Improved collision detection system"""
        # Create groups for different projectile types
        enemy_projectiles = []
        player_projectiles = []
        
        # Sort projectiles into groups
        for proj in projectiles:
            if proj.projType == "enemyball":
                enemy_projectiles.append(proj)
            elif proj.projType == "fireball_head":
                player_projectiles.append(proj)
        
        # Check if player projectiles hit the enemy
        if self.enemy.alive():
            for player_proj in player_projectiles:
                if player_proj.alive():
                    # Use the enemy's hitbox for more precise collision
                    if player_proj.rect.colliderect(self.enemy.hitbox):
                        print("Enemy hit!")  # Debug print
                        pygame.quit()
                        self.enemy.kill()
                        player_proj.kill()
                        return  # Exit after enemy dies
        
        # Check collisions between projectile groups
        for enemy_proj in enemy_projectiles:
            for player_proj in player_projectiles:
                if enemy_proj.alive() and player_proj.alive():
                    if enemy_proj.rect.colliderect(player_proj.rect):
                        enemy_proj.kill()
                        player_proj.kill()


    def update(self, time, projectiles):
        """Update game state"""
        if self.current_state == GAMEPLAY:
            self.wizard.update()
            self.enemy.update(time, projectiles)
            self.projectiles.update()
            self.checkCollisions(time, projectiles)
    
    def render(self):
        """Render the game state to the screen"""
        if self.current_state == MAIN_MENU:
            self.main_menu()
        elif self.current_state == DIALOGUE:
            self.dialogue()
        elif self.current_state == GAMEPLAY:
            self.screen.fill(WHITE)
        
            self.enemy.draw(self.screen)

            self.wizard.draw(self.screen)
            for projectile in self.projectiles:
                projectile.draw(self.screen) 
                self.collision_effects.draw(self.screen)
        elif self.current_state == ATTRIBUTIONS:
            self.screen.fill(BLACK)  # Background color for the Attributions screen
    
            # Display attributions text
            attribution_text = [
                "Game Developed by: Max Peng, Dimian Luo, and Alan Chau",
                "Music: Music from #Uppbeat (License code: ZJIAMNPTKDKDIECJ), and APT by Bruno Mars and Rose",
            ]
    
            font = pygame.font.Font(None, 40)
            y_offset = 100  # Starting y position for the text
            for line in attribution_text:
                text_surface = font.render(line, True, WHITE)
                text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, y_offset))
                self.screen.blit(text_surface, text_rect)
                y_offset += 50  # Space between lines

         # Add a back button
        back_button_x, back_button_y, back_button_w, back_button_h = 50, 50, 200, 70
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Check hover and draw the back button
        back_hover = (
            back_button_x < mouse_pos[0] < back_button_x + back_button_w
            and back_button_y < mouse_pos[1] < back_button_y + back_button_h
        )
        self.draw_button(back_button_x, back_button_y, back_button_w, back_button_h, "Back", back_hover)

        # Handle back button click
        if back_hover and mouse_click[0]:
            self.current_state = MAIN_MENU

        pygame.display.flip()


        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            # Handle input events
            self.handle_events()
            
            # Update game state
            self.update(self.time, self.projectiles)
            
            # Render the frame
            self.render()
            
            # Maintain consistent frame rate
            self.clock.tick(FPS)
            self.time += 1

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
