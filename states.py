from base import State


class Game(State):

    def __init__(self, state_manager, snake_controller, fruit_controller):
        super().__init__(state_manager)
        self.snake_controller = snake_controller
        self.fruit_controller = fruit_controller

    def update(self):
        self.snake_controller.update(self.fruit_controller)
        self.fruit_controller.update()

    @property
    def game_over(self):
        return self.snake_controller.collided

    def render(self, screen):
        self.snake_controller.render(screen)
        self.fruit_controller.render(screen)

    def key_pressed(self, event, keys):
        self.snake_controller.key_pressed(event, keys)

    def __repr__(self):
        return super().__repr__()
