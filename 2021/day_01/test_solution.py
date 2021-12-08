from solution import *

example: Input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 7
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 5
    assert part2(example) == expected
