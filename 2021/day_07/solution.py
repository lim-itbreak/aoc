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


def consumption(inputs: Input, constant_burn: bool = True) -> List[int]:
    crabs: Counter[int] = Counter(inputs)
    all_pos: List[int] = []
    align: int
    for align in range(max(crabs)):
        consumed: List(int) = []
        pos: int
        for pos in crabs:
            if align != pos:
                dist = abs(align - pos)
                consumed.append(
                    (dist if constant_burn else sum_range(dist)) * crabs[pos]
                )
        all_pos.append(sum(consumed))
    return all_pos


def part1(inputs: Input) -> int:
    return min(consumption(inputs))


def part2(inputs: Input) -> int:
    return min(consumption(inputs, constant_burn=False))


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
