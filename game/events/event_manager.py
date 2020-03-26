from weakref import WeakKeyDictionary

class EventManager:
  
  def __init__(self):
    self._listeners = WeakKeyDictionary()

  def subscribe(self, listener):
    self._listeners[listener] = 1
  
  def unsubscribe(self, listener):
    if listener in self._listeners:
      del self._listeners[listener]
      
  def notify(self, event):
    for listener in self._listeners:
      listener.notify(event)