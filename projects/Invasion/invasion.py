
import sys 
import pygame 
from settings import Settings
from ship import Ship

class Invasion:

    def __init__(self):
        pygame.init()
        self.setting = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""

        while True: 
            self._check_events()
            self._update_screen()
            self.ship.update()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False


    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        pygame.display.flip()
            
if __name__ == '__main__':
    ai = Invasion()
    ai.run_game()
