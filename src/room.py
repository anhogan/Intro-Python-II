from item import Item

class Room:
  def __init__(self, name, description, items=[]):
    super().__init__()
    self.name = name
    self.description = description
    self.items = [Item(i[0], i[1]) for i in items]

  def __str__(self):
    return f'{self.name} - {self.description}'

  def __repr__(self):
    return f'{self.name} - {self.description}'

  def print_items(self):
    if len(self.items) > 0:
      print('It has the following items:\n')
      for i in self.items:
        print(f'{i.name} - {i.description}')
    else:
      print('There are no items in this room')

  def search_items(self, item):
    for i in self.items:
      if i.name.lower() == item:
        print('Valid item')
      else:   
        print('Item does not exist in this room.')
        print(f'{self.print_items()}')
