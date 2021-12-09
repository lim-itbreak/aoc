from math import prod
from typing import List, TextIO

Input = List[str]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [line.strip() for line in fp]


def part1(inputs: Input, right: int = 3, down: int = 1) -> int:
    path: List[str] = []
    x: int = 0
    y: int
    for y in range(down, len(inputs), down):
        x += right
        path.append(inputs[y][x % len(inputs[0])])
    return path.count("#")


def part2(inputs: Input) -> int:
    return prod(
        part1(inputs, right, down)
        for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    )


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
