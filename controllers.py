import random
from window import window
from sprites import Fruit, SnakeBody, SnakeHead
from utils import Stack


class SnakeController(object):

    def __init__(self):
        self._snake = []
        self._snake.append(SnakeHead(x=3*16, y=15*16))

    @property
    def __head(self):
        if not len(self._snake) == 0:
            return self._snake[0]
        else:
            return None

    def __add_body(self):
        last_body = self._snake[-1]
        x = y = 0

        if self.__head.current_direction == "right":
            x = last_body.x - SnakeBody.SIZE
            y = last_body.y
        elif self.__head.current_direction == "up":
            x = last_body.x
            y = last_body.y + SnakeBody.SIZE
        elif self.__head.current_direction == "left":
            x = last_body.x + SnakeBody.SIZE
            y = last_body.y
        elif self.__head.current_direction == "down":
            x = last_body.x
            y = last_body.y - SnakeBody.SIZE

        self._snake.append(SnakeBody(x, y))

    def __snake_moving(self):
        index = len(self._snake) - 1

        while index > 0:
            body = self._snake[index]
            previous_body = self._snake[index-1]
            if isinstance(body, SnakeBody):
                body.set_position(previous_body.x, previous_body.y)

            index -= 1

        if self.__head:
            self.__head.update()

    def __check_collision(self, element):

        col_element = element.x // SnakeHead.SIZE
        row_element = element.y // SnakeHead.SIZE

        col_head = self.__head.x // SnakeHead.SIZE
        row_head = self.__head.y // SnakeHead.SIZE

        return col_element == col_head and row_element == row_head

    @property
    def collided(self):
        collided = False

        for index, body in enumerate(self._snake):
            if index == 0:
                continue

            if self.__check_collision(body):
                collided = True
                break

        return collided

    def update(self, fruit_controller):
        self.__snake_moving()
        if self.__check_collision(fruit_controller.fruit):
            fruit_controller.delete_fruit()
            self.__add_body()

    def render(self, screen):
        for snake_body in self._snake:
            snake_body.render(screen)

    def key_pressed(self, event, keys):
        if self.__head:
            self.__head.key_pressed(event, keys)


class FruitController(object):

    def __init__(self):
        self._fruits = Stack()
        self._create_fruit()

    @property
    def fruit(self):
        return self._fruits.peek()

    def delete_fruit(self):
        self._fruits.pop()
        self._create_fruit()

    def _create_fruit(self):
        rows = window.height // Fruit.SIZE_FRUIT
        cols = window.width // Fruit.SIZE_FRUIT

        x = random.randrange(cols) * Fruit.SIZE_FRUIT
        y = random.randrange(rows) * Fruit.SIZE_FRUIT

        self._fruits.push(Fruit(x, y))

    def render(self, screen):
        if not self._fruits.is_empty():
            self.fruit.render(screen)

    def update(self):
        pass
