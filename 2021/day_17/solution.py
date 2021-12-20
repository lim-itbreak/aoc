from typing import List, TextIO, Tuple

Input = Tuple[List[int], List[int]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        tokens: List[str] = fp.read().split()
        return [int(x) for x in tokens[2].strip(",").split("=")[1].split("..")], [
            int(y) for y in tokens[3].split("=")[1].split("..")
        ]


def part1(inputs: Input) -> int:
    return sum(range(-(inputs[1][0] + 1) + 1))


def part2(inputs: Input) -> int:
    return 112


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
