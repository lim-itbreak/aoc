from solution import *


def test_load_input() -> None:
    expected: Input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 37
    assert part1(load_input()) == expected


def test_part2() -> None:
    expected: int = 168
    assert part2(load_input()) == expected
