from abc import ABC, abstractmethod

class Model(ABC):

  def __init__(self, event_manager):
    self.event_manager = event_manager
    self.event_manager.subscribe(self)

  @abstractmethod
  def notify(self, event):
    pass