from solution import *

example: Input = [1721, 979, 366, 299, 675, 1456]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 514579
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 241861950
    assert part2(example) == expected
