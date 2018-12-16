from typing import NamedTuple
from dataclasses import dataclass
import enum
import collections

with open("input.txt") as f:
    cave = [line.strip() for line in f.readlines()]

class Point(NamedTuple("Point", [("x", int), ("y", int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    @property
    def cardinal_points(self):
        return [self + d for d in [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]]

@dataclass
class Unit:
    race: str
    position: Point
    hp: int = 200
    ap: int = 3

class ElfDied(Exception): pass

class Grid(dict):
    def __init__(self, lines, ap=3):
        super().__init__()

        self.units = []

        for i, line in enumerate(lines):
            for j, el in enumerate(line):
                self[Point(i, j)] = el == "#"

                if el in ["E", "G"]:
                    self.units.append(Unit(race=el, position=Point(i, j), ap={ "E": ap, "G": 3 }[el]))

    def play(self):
        rounds = 0
        while True:
            if self.round():
                break
            rounds += 1
            
        return rounds * sum(unit.hp for unit in self.units if unit.hp > 0)

    def round(self):
        for unit in sorted(self.units, key=lambda unit: unit.position):
            if unit.hp > 0 and self.move(unit):
                return True

    def move(self, unit):
        targets = [target for target in self.units if unit.race != target.race and target.hp > 0]
        occupied = set(u2.position for u2 in self.units if u2.hp > 0 and unit != u2)

        if not targets:
            return True

        in_range = set(pt for target in targets for pt in target.position.cardinal_points if not self[pt] and pt not in occupied)

        if not unit.position in in_range:
            move = self.find_move(unit.position, in_range)

            if move:
                unit.position = move

        opponents = [target for target in targets if target.position in unit.position.cardinal_points]

        if opponents:
            target = min(opponents, key=lambda unit: (unit.hp, unit.position))
            target.hp -= unit.ap

            if target.hp <= 0 and target.race == "E":
                raise ElfDied()

    def find_move(self, position, targets):
        visiting = collections.deque([(position, 0)])
        meta = { position: (0, None) }
        seen = set()
        occupied = {unit.position for unit in self.units if unit.hp > 0}

        while visiting:
            pos, dist = visiting.popleft()
            for cardinal in pos.cardinal_points:
                if self[cardinal] or cardinal in occupied:
                    continue

                if cardinal not in meta or meta[cardinal] > (dist + 1, pos):
                    meta[cardinal] = (dist + 1, pos)

                if cardinal in seen:
                    continue

                if not any(cardinal == visit[0] for visit in visiting):
                    visiting.append((cardinal, dist + 1))

            seen.add(pos)

        try:
            min_dist, closest = min((dist, pos) for pos, (dist, parent) in meta.items() if pos in targets)
        except ValueError:
            return

        while meta[closest][0] > 1:
            closest = meta[closest][1]

        return closest

grid = Grid(cave)

# they can't do better than instantly killing them
for ap in range(4, 200):
    try:
        outcome, elf_died = Grid(cave, ap).play()
    except ElfDied:
        continue
    else:
        print(outcome)
        break
