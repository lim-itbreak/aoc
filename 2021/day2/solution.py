from typing import TextIO

Input = list[tuple[str, int]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [
            (direction, int(value))
            for direction, value in (line.split() for line in fp)
        ]


def part1(inputs: Input) -> int:
    horizontal: int = 0
    vertical: int = 0
    direction: str
    value: int
    for direction, value in inputs:
        match direction:
            case "forward":
                horizontal += value
            case "down":
                vertical += value
            case "up":
                vertical -= value
    return horizontal * vertical


def part2(inputs: Input) -> int:
    horizontal: int = 0
    vertical: int = 0
    aim: int = 0
    direction: str
    value: int
    for direction, value in inputs:
        match direction:
            case "forward":
                horizontal += value
                vertical += aim * value
            case "down":
                aim += value
            case "up":
                aim -= value
    return horizontal * vertical


if __name__ == "__main__":
    inputs: Input = load_input(filename="input")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
