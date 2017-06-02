import pygame
from base import StateManager
from states import Game
from controllers import FruitController, SnakeController
from window import window

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = window.width, window.height
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SNAKE")
    clock = pygame.time.Clock()

    FPS = 14
    run = True

    state_manager = StateManager()
    state_manager.set_state(Game(state_manager=state_manager,
                                 snake_controller=SnakeController(),
                                 fruit_controller=FruitController()))

    while run:
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, HEIGHT))

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            state_manager.key_pressed(event, keys)

            if event.type == pygame.QUIT:
                run = False

        state_manager.update()

        if state_manager.state.game_over:
            state_manager.set_state(Game(state_manager=state_manager,
                                         fruit_controller=FruitController(),
                                         snake_controller=SnakeController()))

        state_manager.render(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

