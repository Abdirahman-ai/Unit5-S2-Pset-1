#  Unit 5: Season 2: Problem Set Version 1

# Problem 1:
class Pokemon():
  def  __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp # hit points
    self.damage = damage # The amount of damage this pokemon does to its opponent every attack

  def attack(self, opponent):
    opponent.hp -= self.damage
    if opponent.hp <= 0:
      opponent.hp = 0
      print(opponent.name + " has fainted!")
    else:
      print(f"{self.name} dealt {self.damage} damage to {opponent.name}!")

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

# Problem 2: Convert to Linked List
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

# Problem 3: Add First
def add_first(head, new_node):
  new_node.next = head
  return new_node


# Using the Linked List from Problem 2
print("****")
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)


# Problem 4: Get Tail

def get_tail(head):
  if not head:
    return None

  current = head
  while current.next:
    current = current.next

  return current.value

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)

num1.next = num2
num2.next = num3

# linked list: num1->num2->num3
head = num1
tail = get_tail(head)
print(tail)

# Problem 5: Replace Node
def ll_replace(head, original, replacement):
  current = head 
  while current:
    if current.value == original:
      current.value = replacement
    current = current.next


num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5
print(num1.value, "->", num1.next.value, "->", num1.next.next.value)

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
print(num1.value, "->", num1.next.value, "->", num1.next.next.value)

# Problem 6: List Nodes
def listify_first_n(head, n):
  pass
  ls = []
  current = head
  while n > 0 and current:
    ls.append(current.value)
    current = current.next
    n -= 1
  return ls

# linked list: a -> b -> c
a = Node("a")
b = Node("b")
c = Node("c")

# Linking nodes
a.next = b
b.next = c

head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
j = Node('j')
k = Node('k')
l = Node('l')

# Linking Nodes
j.next = k
k.next = l

head2 = j
lst2 = listify_first_n(head2, 5)
print(lst2)

# Problem 7: Insert Value
def ll_insert(head, val, i):

  # Handle the case where the list is initially empty or `i` is 0
  if not head or i == 0:
      return Node(val, head)

  length = 0
  current = head
  while current:
    length += 1
    if length == i:
      new_node = Node(val, current.next)
      current.next = new_node
    else:
      current = current.next

  if i > length:
    current.next = Node(val)

  return head

# linked list: 3 -> 8 -> 12 -> 9
head = Node(3)
node2 = Node(8)
node3 = Node(12)
node4 = Node(9)

head.next = node2
node2.next = node3
node3.next = node4

ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9
# Testing for my own understanding
curr = head 
while curr.next: 
  print(curr.value, "->", end=" ")
  curr = curr.next
print(curr.value)

# Problem 8: Linked Listify
def list_to_linked_list(lst):
  pass
  head = Node(lst[0])
  current = head
  for i in range(1, len(lst)):
    new_node = Node(lst[i])
    current.next = new_node
    current = current.next
  return head

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list) # Only prints the head element!

curr = linked_list 
while curr.next: 
  print(curr.value, "->", end=" ")
  curr = curr.next
print(curr.value)

# Problem 9: Doubly Linked List
class Node2:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

lst = ["Poliwag", "Poliwhirl", "Poliwrath"]

poliwag = Node2("Poliwag")
poliwhirl = Node2("Poliwhirl")
poliwrath = Node2("Poliwrath")

poliwag.next = poliwhirl
poliwhirl.next = poliwrath

poliwrath.prev = poliwhirl
poliwhirl.prev = poliwag

print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)

# Problem 10: Print Backwards

def print_reverse(tail):
  current = tail
  while current:
    print(current.value, end=" ")
    current = current.prev

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
print_reverse(poliwrath)