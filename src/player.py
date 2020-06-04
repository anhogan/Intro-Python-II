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
  
  def on_take(self, item):
    self.items.append(item)
    self.current_room.items.remove(item)
    print(f'You have successfully picked up {self.item.name}')

  def on_drop(self, item):
    self.items.remove(item)
    self.current_room.items.append(item)
    print(f'You have dropped {self.item.name}')

  def print_items(self):
    if len(self.items) > 0:
      print('Your current items:\n')
      for i in self.items:
        print(f'{i.name} - {i.description}')
    else:
      print('You have no items - explore the map to find some and add them to your collection!')