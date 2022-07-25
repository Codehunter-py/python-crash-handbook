
import sys 
import pygame 
from settings import Settings

class Invasion:

    def __init__(self):
        pygame.init()
        self.setting = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Invasion")

    def run_game(self):
        """Start the main loop for the game"""

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.setting.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = Invasion()
    ai.run_game()
