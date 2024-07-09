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
