from room import Room
from item import Item

class Player:
  def __init__(self, name, current_room, items=[]):
    super().__init__()
    self.name = name
    self.current_room = current_room
    self.items = [Item(i[0], i[1]) for i in items]

  def __str__(self):
    return f'Name: {self.name}, Current Room: {self.current_room}'

  def move_room(self, direction):
    if getattr(self.current_room, f'{direction}_to'):
        self.current_room = getattr(self.current_room, f'{direction}_to')