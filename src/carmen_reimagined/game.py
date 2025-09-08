import pygame
from .states import GameStateRouter
from .assets import Theme

WIDTH, HEIGHT = 960, 540
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Carmen Sandiego Reimagined")
    clock = pygame.time.Clock()
    theme = Theme()
    router = GameStateRouter(theme=theme, screen=screen)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            router.handle_event(event)
        router.update(dt)
        router.draw()
        pygame.display.flip()

    pygame.quit()
