from solution import *

example: Input = [3, 4, 3, 1, 2]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_18_days() -> None:
    expected: int = 26
    assert lantern_fish(example, days=18) == expected


def test_80_days() -> None:
    expected: int = 5934
    assert lantern_fish(example, days=80) == expected


def test_256_days() -> None:
    expected: int = 26984457539
    assert lantern_fish(example, days=256) == expected
