class Node:
  def __init__(self , item = None , next = None):
    self.item = item
    self.next =  next
class SLL:
  def __init__(self , head = None ):
    self.head = head
  def is_empty(self ):
    if self.head == None:
      return True
    else:
      return False
  def insert_at_start(self , data):
    if self.head == None:
      self.head = Node(item = data)
    else:
      newnode = Node(item = data ,next = self.head )
      self.head = newnode
  def insert_at_last(self , data):
    if self.head == None :
      self.head = Node(item = data ,next = None)
    else:
      head = self.head
      while head.next != None :
        head = head.next
      head.next = Node(item =data , next = None)
  def search(self , value):
    temp = self.head
    while temp.next != None:
      if temp.item == value:
        return temp
      else:
        temp = temp.next
    return None
  def insert_after(self , data , after_value):
    temp = self.head
    while temp.next != None :
      if temp.item == after_value :
        temp_next = temp.next
        temp.next = Node(item = data , next = temp_next)
        return
      else:
        temp = temp.next
    return None
  def insert_after_node(self , temp , data):
    if temp != None:
      temp_next = temp.next
      temp.next = Node(item = data , next= temp_next)
  def print(self):
    temp =self.head
    while temp != None :
      print(temp.item , end = " ")
      temp = temp.next
  
  def delete_first(self):
    if self.head != None:
      self.head = self.head.next
  def delete_last(self):
    if self.head == None:
      pass
    elif self.head.next == None:
      self.head = None
    else:
      temp = self.head
      while temp.next.next != None:
        temp = temp.next
      temp.next = None
  
  def delete_node(self , value):
    if self.next == None:
        pass
    elif self.head.next != None:
      if self.head.next.item == value:
        if self.head.next.next != None:
          next = self.head.next.next
          self.head.next = next
        else:
          self.head.next = None
    temp = self.head
    if temp.item == value:
      self.head = temp.next
    else:
      while temp.next.next.next != None:
          if temp.next.item == value:
            temp_next = temp.next.next
            temp.next = temp_next
          else:
            temp = temp.next
  def __iter__(self):
    return SLLiter(self.head)
        

class SLLiter:
  def __init__(self , start ):
    self.current = start
  def __iter__(self):
    return self
  def __next__(self):
    if not self.current :
      raise StopIteration
    data = self.current.item
    self.current = self.current.next
    return data
    



mylist = SLL()
mylist.insert_at_start(1)
mylist.insert_at_start(2)
mylist.insert_at_start(3)
mylist.insert_at_start(4)
mylist.insert_at_start(5)
mylist.insert_after(10 , 4)
mylist.insert_after_node(mylist.search(2) , 100)
mylist.print()
  