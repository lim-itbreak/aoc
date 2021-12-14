from itertools import chain
from typing import List, TextIO, Tuple

Input = List[List[int]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [[int(number) for number in line.strip()] for line in fp]


def step(octopuses: Input) -> int:
    i: int
    for i in range(len(octopuses)):
        j: int
        for j in range(len(octopuses[i])):
            octopuses[i][j] += 1

    flashed: List[Tuple[int, int]] = []
    flash: List[Tuple[int, int]] = flashing(octopuses, flashed)
    while flash:
        for i, j in flash:
            if i > 0:
                octopuses[i - 1][j] += 1
                if j > 0:
                    octopuses[i - 1][j - 1] += 1
                if j < len(octopuses[i]) - 1:
                    octopuses[i - 1][j + 1] += 1
            if i < len(octopuses) - 1:
                octopuses[i + 1][j] += 1
                if j > 0:
                    octopuses[i + 1][j - 1] += 1
                if j < len(octopuses[i]) - 1:
                    octopuses[i + 1][j + 1] += 1
            if j > 0:
                octopuses[i][j - 1] += 1
            if j < len(octopuses[i]) - 1:
                octopuses[i][j + 1] += 1
        flashed.extend(flash)
        flash = flashing(octopuses, flashed)

    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            if octopuses[i][j] > 9:
                octopuses[i][j] = 0

    return len(flashed)


def flashing(octopuses: Input, flashed: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return list(
        chain(
            *(
                [
                    (i, j)
                    for j in range(len(octopuses[i]))
                    if octopuses[i][j] > 9 and (i, j) not in flashed
                ]
                for i in range(len(octopuses))
            )
        )
    )


def part1(inputs: Input, steps: int) -> int:
    return sum(step(inputs) for _ in range(steps))


def part2(inputs: Input) -> int:
    steps: int = 0
    while True:
        step(inputs)
        steps += 1
        if set(chain(*inputs)) == {0}:
            return steps


if __name__ == "__main__":
    print(f"Part 1 Answer: {part1(load_input(filename='puzzle'), steps=100)}")
    print(f"Part 2 Answer: {part2(load_input(filename='puzzle'))}")
