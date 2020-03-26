from .model import Model
from game.models.character import Character

class Game(Model):

  def __init__(self, event_manager):
    self.event_manager = event_manager
    self.event_manager.subscribe(self)
    self.characters = [Character(event_manager)]

  def notify(self, event):
    pass