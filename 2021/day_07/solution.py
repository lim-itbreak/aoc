from collections import Counter
from functools import cache
from typing import List, TextIO

Input = List[int]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [int(i) for i in fp.read().split(",")]


@cache
def sum_range(dist: int) -> int:
    return sum(range(dist + 1))


def fuel(positions: Input, constant_burn: bool = True) -> List[int]:
    crabs: Counter[int] = Counter(positions)
    consumption: List[int] = []
    align_to: int
    for align_to in range(max(crabs)):
        consumed: List[int] = []
        pos: int
        for pos in crabs:
            if align_to != pos:
                dist = abs(align_to - pos)
                consumed.append(
                    (dist if constant_burn else sum_range(dist)) * crabs[pos]
                )
        consumption.append(sum(consumed))
    return consumption


def part1(inputs: Input) -> int:
    return min(fuel(inputs))


def part2(inputs: Input) -> int:
    return min(fuel(inputs, constant_burn=False))


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
