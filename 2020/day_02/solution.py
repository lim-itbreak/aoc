from typing import List, TextIO, Tuple

Input = List[Tuple[List[int], str, str]]


def load_input(filename: str = "example") -> Input:
    output: Input = []
    fp: TextIO
    with open(filename) as fp:
        line: str
        for line in fp:
            rule: str
            password: str
            rule, password = line.strip().split(": ")
            letter: str
            rule, letter = rule.split()
            numbers: List[int] = [int(i) for i in rule.split("-")]
            output.append((numbers, letter, password))
    return output


def part1(inputs: Input) -> int:
    return len(
        [
            password
            for rule, letter, password in inputs
            if password.count(letter) in range(rule[0], rule[1] + 1)
        ]
    )


def part2(inputs: Input) -> int:
    return len(
        [
            password
            for rule, letter, password in inputs
            if (password[rule[0] - 1], password[rule[1] - 1]).count(letter) == 1
        ]
    )


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
