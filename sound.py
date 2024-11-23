import pygame

class Sound:
    def __init__(self):
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the sound file (ensure the file is in the same directory)
        try:
            pygame.mixer.music.load("pookatori-and-friends-kevin-macleod-main-version-24903-04-07.mp3")
        except pygame.error as e:
            print(f"Error loading sound file: {e}")
            return

    def background(self):
        # Play the music in a loop (-1 means infinite looping)
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(loops=-1)
            print("Playing background music.")
