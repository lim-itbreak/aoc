from solution import *

example: Input = ([20, 30], [-10, -5])


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 45
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 112
    assert part2(example) == expected
