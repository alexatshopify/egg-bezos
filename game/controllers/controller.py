from game.events.character_move_event import CharacterMoveEvent
from game.models.character import Character

class Controller:

  def __init__(self, event_manager):
    self.eventManager = event_manager
    self.eventManager.subscribe(self)

  def on_key_release(self, symbol, modifiers):
    pass

  def on_key_press(self, symbol, modifiers):
    self.eventManager.notify(CharacterMoveEvent())

  def update(self):
    pass