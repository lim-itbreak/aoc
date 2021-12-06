from typing import List, TextIO

Input = List[int]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [int(line) for line in fp]


def increases(inputs: Input, size: int = 1) -> int:
    count: int = 0
    previous: int = sum(inputs[:size])
    i: int
    for i in range(1, len(inputs) - (size - 1)):
        window: int = sum(inputs[i : i + size])
        if window > previous:
            count += 1
        previous: int = window
    return count


def part1(inputs: Input) -> int:
    return increases(inputs)


def part2(inputs: Input) -> int:
    return increases(inputs, size=3)


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
