from collections import Counter
from typing import List, TextIO

Input = List[int]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [int(i) for i in fp.read().split(",")]


def minimize_fuel(inputs: Input, constant_burn: bool):
    crabs: Counter[int] = Counter(inputs)
    fuel: List[int] = []
    align: int
    for align in range(max(crabs)):
        used: int = 0
        pos: int
        for pos in crabs:
            dist = abs(align - pos)
            used += (dist if constant_burn else sum(range(dist + 1))) * crabs[pos]
        fuel.append(used)
    return min(fuel)


def part1(inputs: Input) -> int:
    return minimize_fuel(inputs, constant_burn=True)


def part2(inputs: Input) -> int:
    return minimize_fuel(inputs, constant_burn=False)


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
