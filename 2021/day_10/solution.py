from functools import reduce
from typing import Dict, List, TextIO

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
    return "".join(stack)  # line is incomplete - return unclosed openers


def complete(line: str) -> str:
    stack: str = check(line)
    if len(stack) > 0 and stack[0] in openers:  # line is incomplete
        return "".join(openers[code] for code in reversed(stack))
    return ""  # line was either complete or corrupted


def score(completion: str) -> int:
    points: Dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}
    return reduce(lambda total, code: total * 5 + points[code], completion, 0)


def part1(inputs: Input) -> int:
    points: Dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}
    errors: List[str] = []

    line: str
    for line in inputs:
        stack: str = check(line)
        if stack in closers:  # line is corrupted
            errors.append(stack)

    return sum(points[code] for code in errors)


def part2(inputs: Input) -> int:
    scores: List[int] = []
    line: str
    for line in inputs:
        stack: str = complete(line)
        if stack:  # line is incomplete
            scores.append(score(stack))
    scores.sort()
    return scores[(len(scores) - 1) // 2]


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
