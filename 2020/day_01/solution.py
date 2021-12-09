from typing import List, TextIO

Input = List[int]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [int(line) for line in fp]


def part1(inputs: Input) -> int:
    i: int
    for i in range(len(inputs) - 1):
        j: int
        for j in range(i + 1, len(inputs)):
            if inputs[i] + inputs[j] == 2020:
                return inputs[i] * inputs[j]
    return 0


def part2(inputs: Input) -> int:
    i: int
    for i in range(len(inputs) - 2):
        j: int
        for j in range(i + 1, len(inputs) - 1):
            if inputs[i] + inputs[j] < 2020:
                k: int
                for k in range(j + 1, len(inputs)):
                    if inputs[i] + inputs[j] + inputs[k] == 2020:
                        return inputs[i] * inputs[j] * inputs[k]
    return 0


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
