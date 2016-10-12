from Linked_List import Linked_List

class Deque:

  def __init__(self):
    self._list = Linked_List()

  def __str__(self):
    return str(self._list)

  def __len__(self):
    return len(self._list)

  def push_front(self, val):
    if len(self) == 0:
      self._list.append_element(val)
    else:
      self._list.insert_element_at(val, 0)

  def pop_front(self):
    return self._list.remove_element_at(0)

  def peek_front(self):
    return self._list.get_element_at(0)

  def push_back(self, val):
    self._list.append_element(val)

  def pop_back(self):
    return self._list.remove_element_at(len(self) - 1)

  def peek_back(self):
    return self._list.get_element_at(len(self) - 1)

