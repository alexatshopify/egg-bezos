import pyglet

import game.constants.settings as constants
from game.events.event_manager import EventManager
from game.controllers.controller import Controller
from game.models.game import Game

class Window(pyglet.window.Window):
  def __init__(self, *args, **kwargs):
    super(Window, self).__init__(width=constants.WIDTH, height=constants.HEIGHT, *args, **kwargs)
    pyglet.clock.schedule_interval(self.update, 1.0/constants.FPS)

    self.eventManager = EventManager()
    self.controller = Controller(self.eventManager)
    self.game = Game(self.eventManager)

  def on_key_release(self, symbol, modifiers):
    self.controller.on_key_release(symbol, modifiers)

  def on_key_press(self, symbol, modifiers):
    self.controller.on_key_press(symbol, modifiers)

  def update(self, *args, **kwargs):
    self.controller.update()