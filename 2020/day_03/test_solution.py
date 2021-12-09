from solution import *

example: Input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 7
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 336
    assert part2(example) == expected
