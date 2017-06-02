from abc import ABCMeta, abstractmethod
from utils import Stack


class StateManager(object):

    """
    This controller manage all game states.
    """
    GAME = 0

    def __init__(self):
        self.__states = Stack()
        self.current_state = StateManager.GAME

    @property
    def state(self):
        return self.__states.peek()

    def set_state(self, state):
        self.__states.pop()
        self.__states.push(state)

    def update(self):
        self.__states.peek().update()

    def render(self, screen):
        self.__states.peek().render(screen)

    def key_pressed(self, event, keys):
        self.__states.peek().key_pressed(event, keys)


class State(metaclass=ABCMeta):

    """
    This class represent one state of game, for example Game, Menus, etc
    """
    def __init__(self, state_manager):
        self.state_manager = state_manager

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    @abstractmethod
    def key_pressed(self, event, keys):
        pass

    def __repr__(self):
        return str(type(self))


class Sprite(metaclass=ABCMeta):

    """
    This class represent an object that it can be positioned in window.
    """

    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width >= 0:
            self._width = width
        else:
            raise ValueError("El acho debe ser positivo.")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height > 0:
            self._height = height
        else:
            raise ValueError("El alto debe ser positivo")

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    @abstractmethod
    def key_pressed(self, event, keys):
        pass

