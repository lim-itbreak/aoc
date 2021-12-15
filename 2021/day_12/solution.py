from copy import deepcopy
from typing import List, Set, TextIO

Input = List[List[str]]


def load_input(filename: str) -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [line.strip().split("-") for line in fp]


def traverse(
    cave: str, caves: Input, path: List[str], paths: Set[str], limit: int = 1
) -> None:
    path.append(cave)
    if cave == "end":
        paths.add(",".join(path))
    else:
        cave1: str
        cave2: str
        for cave1, cave2 in caves:
            if (
                cave == cave1
                and cave2 != "start"
                and (cave2.isupper() or path.count(cave2) < limit)
            ):
                traverse(
                    cave2,
                    caves,
                    deepcopy(path),
                    paths,
                    limit=1 if cave2.islower() and cave2 in path else limit,
                )
            elif (
                cave == cave2
                and cave1 != "start"
                and (cave1.isupper() or path.count(cave1) < limit)
            ):
                traverse(
                    cave1,
                    caves,
                    deepcopy(path),
                    paths,
                    limit=1 if cave1.islower() and cave1 in path else limit,
                )


def part1(inputs: Input) -> int:
    paths: Set[str] = set()
    traverse("start", inputs, [], paths)
    return len(paths)


def part2(inputs: Input) -> int:
    paths: Set[str] = set()
    traverse("start", inputs, [], paths, limit=2)
    return len(paths)


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
