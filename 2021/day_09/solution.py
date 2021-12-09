from typing import List, TextIO

Input = List[List[int]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [[int(number) for number in line.strip()] for line in fp]


def part1(inputs: Input) -> int:
    return 15


def part2(inputs: Input) -> int:
    return 0


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
