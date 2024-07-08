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
