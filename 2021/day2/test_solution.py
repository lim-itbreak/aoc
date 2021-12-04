from solution import *


def test_load_input() -> None:
    expected: Input = [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 150
    assert part1(load_input()) == expected


def test_part2() -> None:
    expected: int = 900
    assert part2(load_input()) == expected
