from collections import Counter
from typing import List, TextIO, Tuple

Input = List[List[List[int]]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [
            [[int(c) for c in p.split(",")] for p in line.split("->")] for line in fp
        ]


def danger_will_robinson(inputs: Input, diagonals: bool = False) -> int:
    vents: List[Tuple[int]] = []
    p1: List[int]
    p2: List[int]
    for p1, p2 in inputs:
        x1: int
        y1: int
        x1, y1 = p1
        x2: int
        y2: int
        x2, y2 = p2
        x3: int = -1 if x2 - x1 < 1 else 1
        y3: int = -1 if y2 - y1 < 1 else 1
        if x1 == x2 or y1 == y2:
            x: int
            for x in range(x1, max(0, x2 + x3), x3):
                y: int
                for y in range(y1, max(0, y2 + y3), y3):
                    vents.append((x, y))
        elif diagonals:
            vents.extend(
                zip(range(x1, max(0, x2 + x3), x3), range(y1, max(0, y2 + y3), y3))
            )
    vent_count: Counter = Counter(vents)
    return len([p for p in vent_count if vent_count[p] > 1])


def part1(inputs: Input) -> int:
    return danger_will_robinson(inputs)


def part2(inputs: Input) -> int:
    return danger_will_robinson(inputs, diagonals=True)


if __name__ == "__main__":
    inputs: Input = load_input(filename="input")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
