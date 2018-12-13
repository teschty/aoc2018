from typing import List

UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
# ordered such that -1 => right, +1 => left
dir_map = { "^": UP, "<": LEFT, "v": DOWN, ">": RIGHT }
dir_delta_map = { UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1) }

class CrashException(BaseException):
    def __init__(self, pos):
        self.pos = pos

def get_track(tracks, cart):
    y, x = cart.pos[0], cart.pos[1]
    return tracks[y][x]

class Cart:
    def __init__(self, dir: int, pos: List[int], coord_map):
        self.dir = dir
        self.pos = pos
        self.next_turn = 0
        coord_map[self.pos] = self
    
    def move(self, tracks, coord_map):
        coord_map.pop(self.pos)

        delta_pos = dir_delta_map[self.dir]
        new_pos = (self.pos[0] + delta_pos[0], self.pos[1] + delta_pos[1])

        if new_pos in coord_map:
            raise CrashException(new_pos)

        self.pos = new_pos
        coord_map[new_pos] = self

        self.process_track(get_track(tracks, self))

    def process_track(self, track: str):
        if track == "+":
            self.dir += [1, 0, -1][self.next_turn]
            self.next_turn = (self.next_turn + 1) % 3
        elif track == "/":
            self.dir = [RIGHT, DOWN, LEFT, UP][self.dir]
        elif track =="\\":
            self.dir = [LEFT, UP, RIGHT, DOWN][self.dir]

        self.dir = self.dir % 4

def process_input(lines):
    carts = []
    tracks = []
    coord_map = {}

    for line_idx, line in enumerate(lines):
        track_line = ""

        for c_idx, c in enumerate(line):
            pos = (line_idx, c_idx)

            if c in ["v", "^", "<", ">"]:
                track_line += "|" if c in ["v", "^"] else "-"
                carts.append(Cart(dir_map[c], pos, coord_map))
            else:
                track_line += c

        tracks.append(track_line)
    
    return (carts, tracks, coord_map)

def run_simulation(lines):
    carts, tracks, coord_map = process_input(lines)

    while True:
        sorted_carts: List[Cart] = sorted(carts, key=lambda c: c.pos)

        for cart in sorted_carts:
            try:
                cart.move(tracks, coord_map)
            except CrashException as e:
                return f"{e.pos[1]},{e.pos[0]}"

with open("input.txt") as f:
    lines = map(str.rstrip, f.readlines())

print(run_simulation(lines))
        