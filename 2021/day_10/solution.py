from functools import reduce
from typing import Dict, List, TextIO, Tuple

Input = List[str]
openers: Dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
closers: Dict[str, str] = {")": "(", "]": "[", "}": "{", ">": "<"}


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [line.strip() for line in fp]


def check(line: str) -> str:
    stack: List[str] = []
    code: str
    for code in line:
        if code in openers:
            stack.append(code)
        elif closers[code] == stack[-1]:
            stack.pop()
        else:
            return code  # line is corrupted - return unexpected closer
    if stack:  # line is incomplete - return closers to complete
        return "".join(openers[code] for code in reversed(stack))
    return ""  # line is complete


def score(completion: str) -> int:
    points: Dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}
    return reduce(lambda total, code: total * 5 + points[code], completion, 0)


def analyze(inputs: Input) -> Tuple[int, int]:
    points: Dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}
    errors: List[str] = []
    scores: List[int] = []

    line: str
    for line in inputs:
        code: str = check(line)
        if code in closers:  # line is corrupted
            errors.append(code)
        elif code:  # line is incomplete
            scores.append(score(code))
    scores.sort()

    return sum(points[code] for code in errors), scores[(len(scores) - 1) // 2]


if __name__ == "__main__":
    part1: int
    part2: int
    part1, part2 = analyze(load_input(filename="puzzle"))
    print(f"Part 1 Answer: {part1}")
    print(f"Part 2 Answer: {part2}")
