# Add on_take method that prints a string (You have picked up [NAME]) and prints confirmation
# Add on_drop method that removes item and prints confirmation 

class Item:
  def __init__(self, name, description):
    super().__init__()
    self.name = name
    self.description = description

  @property
  def name(self):
    return self.name

  @name.setter
  def name(self, n):
    if " " in n:
      raise Exception('Name must be one word')