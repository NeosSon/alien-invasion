
import pygame.font

class Scoreboard:
    """A class to report scoring information."""
    
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image.
        self.prep_score()
        self.prep_level()
        
    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str =  "Score: " + str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "Lvl: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_level(self):
        """Draw level to the screen."""
        self.screen.blit(self.level_image, self.level_rect)