with open("input.txt") as f:
    text = f.read()

text_parts = text.split()
num_players = int(text_parts[0])
# num_marbles = int(text_parts[6])

for num_marbles in range(10, 10000):
    circle = [0, 1]
    player_scores = [0 for _ in range(num_players)]

    cur_marble = 1
    cur_player = 0
    for marble in range(2, num_marbles):
        if marble % 23 != 0:
            insert_idx = (cur_marble + 2) % len(circle)
            circle.insert(insert_idx, marble)
            cur_marble = insert_idx
        else:
            player_scores[cur_player] += marble
            remove_idx = (cur_marble - 7) % len(circle)
            player_scores[cur_player] += circle.pop(remove_idx)
            cur_marble = remove_idx

        cur_player = (cur_player + 1) % num_players

    print(num_players, end="\t")
    print(max(player_scores))
