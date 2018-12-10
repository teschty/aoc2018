with open("input.txt") as f:
    text = f.read()

class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev or self
        self.next = next or self
    
    def insert_after(self, node):
        node.next = self.next
        node.prev = self

        self.next.prev = node
        self.next = node
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

        return self.value

text_parts = text.split()
num_players = int(text_parts[0])
num_marbles = int(text_parts[6])

player_scores = [0 for _ in range(num_players)]

cur_marble = Node(0)
cur_player = 0

for marble in range(1, num_marbles):
    if marble % 23 != 0:
        insert_marble = cur_marble.next
        cur_marble = insert_marble.insert_after(Node(marble))
    else:
        player_scores[cur_player] += marble

        remove_marble = cur_marble
        for _ in range(7):
            remove_marble = remove_marble.prev

        remove_marble.remove()
        player_scores[cur_player] += remove_marble.value
        cur_marble = remove_marble.next

    cur_player = (cur_player + 1) % num_players

print(max(player_scores))
