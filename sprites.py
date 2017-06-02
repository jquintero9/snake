import pygame
from base import Sprite
from window import window


class Snake(Sprite):

    SIZE = 16

    def __init__(self, x=0, y=0):
        super().__init__(x, y, Snake.SIZE, Snake.SIZE)

    def update(self):
        pass

    def render(self, screen):
        pygame.draw.rect(screen, (0, 23,111), (self.x, self.y, self.width, self.height), 1)

    def key_pressed(self, event, keys):
        pass


class SnakeHead(Snake):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.move_speed = 16
        self.dx = self.move_speed
        self.dy = 0
        self._move = {
            "up": False,
            "left": False,
            "right": False,
            "down": False
        }
        self.current_direction = ""

    def _change_move(self, new_move):
        for key in self._move:
            self._move[key] = False
        self._move[new_move] = True
        self.current_direction = new_move

    def __change_direction_move(self):
        if self._move["up"]:
            if self.x % self.width == 0:
                self.dy = -self.move_speed
                self.dx = 0
        elif self._move["right"]:
            if self.y % self.height == 0:
                self.dx = self.move_speed
                self.dy = 0
        elif self._move["down"]:
            if self.x % self.width== 0:
                self.dy = self.move_speed
                self.dx = 0
        elif self._move["left"]:
            if self.y % self.height == 0:
                self.dx = -self.move_speed
                self.dy = 0

    def __move(self):
        if not self.dx == 0:
            self.x += self.dx
        elif not self.dy == 0:
            self.y += self.dy

    def __check_screen_bounds(self):
        if self.x < -self.width:
            self.x = window.width
        elif self.y < -self.height:
            self.y = window.height
        elif self.x > window.width:
            self.x = -self.width
        elif self.y > window.height:
            self.y = -self.height

    def update(self):
        self.__change_direction_move()
        self.__move()
        self.__check_screen_bounds()

    def key_pressed(self, event, keys):
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_a] and (not self.current_direction == "right"):
                self._change_move("left")
            elif keys[pygame.K_w] and (not self.current_direction == "down"):
                self._change_move("up")
            elif keys[pygame.K_d] and (not self.current_direction == "left"):
                self._change_move("right")
            elif keys[pygame.K_s] and (not self.current_direction == "up"):
                self._change_move("down")


class SnakeBody(Snake):

    def __init__(self, x: int = 0, y: int = 0):
        super().__init__(x, y)

    def set_position(self, x, y):
        self.x = x
        self.y = y


class Fruit(Sprite):

    """
    This class represent snake's food.

    The fruit appear randomly when snake eat it.
    """

    SIZE_FRUIT = 16

    def __init__(self, x=0, y=0):
        super().__init__(x, y, Fruit.SIZE_FRUIT, Fruit.SIZE_FRUIT)

    def render(self, screen):
        pygame.draw.ellipse(screen, (126, 23, 23), (self.x, self.y, self.width, self.height))

    def update(self):
        pass

    def key_pressed(self, event, keys):
        pass