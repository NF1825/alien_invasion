class GameStats:
    """Track statistics for Alien Invasion game."""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        #High score should never be reset.
        self.high_score = 0

        self.game_active = False
    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1