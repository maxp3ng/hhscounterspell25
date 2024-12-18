from projectile import Projectile
import pygame
import os
import random



class Enemy(pygame.sprite.Sprite):
    projExists = False

    def __init__(self, x, y, WINDOW_WIDTH, WINDOW_HEIGHT):
        super().__init__()
        # Create a simple rectangle for the player
        enemysurf = pygame.image.load(os.path.join('static', 'img', 'enemyfire' , 'frame_0_delay-0.1s.gif'))
        self.fireframe = 0
        self.image = enemysurf
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Create a smaller hitbox for more precise collisions
        self.hitbox = pygame.Rect(x + self.rect.width//4, 
                                y + self.rect.height//4,
                                self.rect.width//2, 
                                self.rect.height//2)
        
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.WINDOW_WIDTH = WINDOW_WIDTH 
        
        file_path = "tempsong.txt" 
        self.file = open(file_path)
        # Movement speed
        self.speed = 25
        
        # Add alive status
        self.is_alive = True


    def sendBasicProj(self, projectiles):
        self.projExists = True
    

        enemyball_x = 300 
        enemyball_y = -80
        enemyball = Projectile(self.WINDOW_WIDTH//2+enemyball_x,self.WINDOW_HEIGHT//2+enemyball_y,"enemyball", 0)
        projectiles.add(enemyball)

    def enemyProj(self, char, projectiles):
        if (char == "x"):
            self.sendBasicProj(projectiles)
        pass

    def read_next_character(self, file, time):
        if (time%10 == 0):
            char = file.read(1)  # Read one character
            return char if char else None
        return None


    
    def kill(self):
        """Override kill to handle death properly"""
        self.is_alive = False
        super().kill()
        
    def alive(self):
        """Check if enemy is alive"""
        return self.is_alive

    def update(self, time, projectiles):
        if not self.is_alive:
            return

        char = self.read_next_character(self.file, time)
        self.enemyProj(char, projectiles)

        frameslowdown = 4 #wait 5 ticks on each frame 
        if (self.fireframe > 0):
            filename = 'frame_' + str(int(self.fireframe//frameslowdown))+ '.gif'
            enemysurf = pygame.image.load(os.path.join('static', 'img', 'enemyfire' , filename))
            self.image = enemysurf
            self.fireframe = 0 if (self.fireframe == 7*frameslowdown) else self.fireframe + 1
            
        # Update hitbox position to match sprite
        self.hitbox.x = self.rect.x + self.rect.width//4
        self.hitbox.y = self.rect.y + self.rect.height//4 

    def draw(self, screen):
        """Draw the player to the screen"""
        screen.blit(self.image, self.rect)
        if self.is_alive:
            screen.blit(self.image, self.rect)
