from solution import *

example: Input = [
    ([1, 3], "a", "abcde"),
    ([1, 3], "b", "cdefg"),
    ([2, 9], "c", "ccccccccc"),
]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 2
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 1
    assert part2(example) == expected
