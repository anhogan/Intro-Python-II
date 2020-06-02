# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    super().__init__()
    self.name = name
    self.description = description
    self.n_to = ''
    self.s_to = ''
    self.e_to = ''
    self.w_to = ''

  def __repr__(self):
    return f'Name: {self.name}, Description: {self.description}, North To: {self.n_to}, South To: {self.s_to}, East To: {self.e_to}, West To: {self.w_to}'