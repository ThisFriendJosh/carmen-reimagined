import pygame
from dataclasses import dataclass

@dataclass
class Theme:
    bg_color: tuple = (18, 18, 20)
    fg_color: tuple = (235, 235, 235)
    accent: tuple = (255, 204, 0)

class BaseState:
    def __init__(self, router): self.router = router
    def handle_event(self, event): pass
    def update(self, dt): pass
    def draw(self): pass

class MenuState(BaseState):
    def __init__(self, router):
        super().__init__(router)
        self.font = pygame.font.SysFont(None, 36)
        self.options = ["Start Example Case", "Quit"]
        self.hover = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.hover = (self.hover + 1) % len(self.options)
            if event.key in (pygame.K_UP, pygame.K_w):
                self.hover = (self.hover - 1) % len(self.options)
            if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                if self.hover == 0:
                    self.router.set_state("travel")
                else:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

    def draw(self):
        s = self.router.screen
        s.fill(self.router.theme.bg_color)
        title = self.font.render("Carmen Sandiego Reimagined", True, self.router.theme.accent)
        s.blit(title, (40, 40))
        for i, opt in enumerate(self.options):
            color = self.router.theme.fg_color if i != self.hover else self.router.theme.accent
            text = self.font.render(f"> {opt}" if i==self.hover else opt, True, color)
            s.blit(text, (60, 120 + i*40))

class TravelState(BaseState):
    def __init__(self, router):
        super().__init__(router)
        self.font = pygame.font.SysFont(None, 28)
        self.cities = ["Anchorage", "Seattle", "San Francisco", "Honolulu"]
        self.index = 0
        self.message = "Use ← → to choose, Enter to 'fly'."

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                self.index = (self.index + 1) % len(self.cities)
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.index = (self.index - 1) % len(self.cities)
            if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                self.router.set_state("menu")

    def draw(self):
        s = self.router.screen
        s.fill(self.router.theme.bg_color)
        label = self.font.render("Travel (prototype)", True, self.router.theme.fg_color)
        s.blit(label, (40, 40))
        city = self.font.render(self.cities[self.index], True, self.router.theme.accent)
        s.blit(city, (60, 100))
        hint = self.font.render(self.message, True, self.router.theme.fg_color)
        s.blit(hint, (60, 140))

class GameStateRouter:
    def __init__(self, theme, screen):
        self.theme = theme
        self.screen = screen
        self.states = {
            "menu": MenuState(self),
            "travel": TravelState(self),
        }
        self.state = self.states["menu"]

    def set_state(self, name):
        self.state = self.states[name]

    def handle_event(self, event):
        self.state.handle_event(event)

    def update(self, dt):
        pass

    def draw(self):
        self.state.draw()
