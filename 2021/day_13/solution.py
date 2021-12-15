from typing import List, Set, TextIO, Tuple

Input = Tuple[Set[Tuple[int, int]], List[Tuple[int, int]]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        paper: str
        instructions: str
        paper, instructions = fp.read().split("\n\n")

        dots: Set[Tuple[int, int]] = {
            tuple(map(int, dot.split(","))) for dot in paper.split()  # type: ignore
        }

        folds: List[Tuple[int, int]] = []
        for fold in instructions.splitlines():
            value: int = int(fold.split("=")[1])
            if "x" in fold:
                folds.append((value, 0))
            else:
                folds.append((0, value))

    return dots, folds


def fold(paper: Set[Tuple[int, int]], line: Tuple[int, int]) -> Set[Tuple[int, int]]:
    folded: Set[Tuple[int, int]] = set()
    dot: Tuple[int, int]
    for dot in paper:
        if line[0]:
            if dot[0] > line[0]:
                folded.add((line[0] - (dot[0] - line[0]), dot[1]))
            else:
                folded.add(dot)
        else:
            if dot[1] > line[1]:
                folded.add((dot[0], line[1] - (dot[1] - line[1])))
            else:
                folded.add(dot)
    return folded


def part1(inputs: Input) -> int:
    return len(fold(inputs[0], inputs[1][0]))


def part2(inputs: Input) -> str:
    paper: Set[Tuple[int, int]] = inputs[0]
    line: Tuple[int, int]
    for line in inputs[1]:
        paper = fold(paper, line)
    max_x: int = max(dot[0] for dot in paper) + 1
    max_y: int = max(dot[1] for dot in paper) + 1
    grid: List[List[str]] = [["."] * max_x for _ in range(max_y)]

    x: int
    y: int
    for x, y in paper:
        grid[y][x] = "#"
    return "\n".join("".join(row) for row in grid)


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer:\n{part2(inputs)}")
