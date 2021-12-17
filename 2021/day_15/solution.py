from heapq import heappop, heappush
from sys import maxsize
from typing import List, TextIO, Tuple

Input = List[int]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [int(risk) for risk in fp.read().replace("\n", "")]


def load_input_full(filename: str = "example") -> Input:
    cave: Input = []
    fp: TextIO
    with open(filename) as fp:
        line: str
        for line in fp:
            row: Input = [int(risk) for risk in line.strip()]
            cave.extend(row)
            _: int
            for _ in range(4):
                i: int
                for i in range(len(row)):
                    row[i] += 1
                    if row[i] == 10:
                        row[i] = 1
                cave.extend(row)
        row = cave.copy()
        for _ in range(4):
            for i in range(len(row)):
                row[i] += 1
                if row[i] == 10:
                    row[i] = 1
            cave.extend(row)
    return cave


def a_star(risk):
    size: int = int(len(risk) ** 0.5)

    def neighbors(position: int) -> List[int]:
        locations: List[int] = []

        x: int = position % size
        y: int = position // size
        if x > 0:
            locations.append((x - 1) + y * size)
        if x < size - 1:
            locations.append((x + 1) + y * size)
        if y > 0:
            locations.append(x + (y - 1) * size)
        if y < size - 1:
            locations.append(x + (y + 1) * size)

        return locations

    def h(pos: int) -> int:
        return (size - 1 - pos % size) + (size - 1 - pos // size)

    g: List[int] = [maxsize] * len(risk)
    g[0] = 0

    f: List[int] = [maxsize] * len(risk)
    f[0] = h(0)

    d: List[Tuple[int, int]] = []
    heappush(d, (f[0], 0))

    while d:
        _: int
        pos: int
        _, pos = heappop(d)
        if pos == len(risk) - 1:
            return g[pos]
        loc: int
        for loc in neighbors(pos):
            _risk_: int = g[pos] + risk[loc]
            if _risk_ < g[loc]:
                g[loc] = _risk_
                f[loc] = g[loc] + h(loc)
                heappush(d, (f[loc], loc))


if __name__ == "__main__":
    print(f"Part 1 Answer: {a_star(load_input(filename='puzzle'))}")
    print(f"Part 2 Answer: {a_star(load_input_full(filename='puzzle'))}")
