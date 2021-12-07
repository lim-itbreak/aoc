from typing import List, TextIO, Tuple

Input = List[Tuple[str, int]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [
            (direction, int(value))
            for direction, value in (line.split() for line in fp)
        ]


def position(inputs: Input, aiming: bool = False):
    horizontal: int = 0
    vertical: int = 0
    aim: int = 0

    direction: str
    value: int
    for direction, value in inputs:
        match direction:
            case "forward":
                horizontal += value
                if aiming:
                    vertical += aim * value
            case "down":
                if aiming:
                    aim += value
                else:
                    vertical += value
            case "up":
                if aiming:
                    aim -= value
                else:
                    vertical -= value

    return horizontal * vertical


def part1(inputs: Input) -> int:
    return position(inputs)


def part2(inputs: Input) -> int:
    return position(inputs, aiming=True)


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
