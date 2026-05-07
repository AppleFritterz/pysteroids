import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__(self.containers)
        self.font = pygame.font.SysFont('Arial', 30)
        self.color = 'white'
        self.pos = (x, y)
        self.score = 0

    def increment_score(self, increment):
        self.score += increment

    def draw(self, screen):
        scoreboard_text = f"Score: {self.score}"
        score_surface = self.font.render(scoreboard_text, True, self.color)
        screen.blit(score_surface, self.pos)
