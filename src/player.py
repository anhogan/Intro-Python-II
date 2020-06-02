# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    super().__init__()
    self.name = name
    self.current_room = current_room

  def __repr__(self):
    return f'Name: {self.name}, Current Room: {self.current_room}'