from collections import Counter
from typing import Dict, List, TextIO, Tuple

Input = Tuple[str, Dict[str, str]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        template: str
        insertions: str
        template, insertions = fp.read().split("\n\n")
        pairs: Dict[str, str] = dict(
            pair.split(" -> ") for pair in insertions.splitlines()  # type: ignore
        )
    return template, pairs


def polymerize(template: str, insertions: Dict[str, str], steps: int) -> Counter[str]:
    pair_count: Counter[str] = Counter()
    element_count: Counter[str] = Counter()

    i: int
    for i in range(len(template)):
        if i < len(template) - 1:
            pair_count[template[i] + template[i + 1]] += 1
        element_count[template[i]] += 1

    _: int
    for _ in range(steps):
        polymer: Counter[str] = pair_count.copy()

        pair: str
        for pair in polymer:
            if pair in insertions:
                n: int = polymer[pair]
                pair_count[pair] -= n
                pair_count[pair[0] + insertions[pair]] += n
                pair_count[insertions[pair] + pair[1]] += n
                element_count[insertions[pair]] += n

    return element_count


def part1(inputs: Input) -> int:
    elements: List[Tuple[str, int]] = polymerize(
        inputs[0], inputs[1], steps=10
    ).most_common()
    return elements[0][1] - elements[-1][1]


def part2(inputs: Input) -> int:
    elements: List[Tuple[str, int]] = polymerize(
        inputs[0], inputs[1], steps=40
    ).most_common()
    return elements[0][1] - elements[-1][1]


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
