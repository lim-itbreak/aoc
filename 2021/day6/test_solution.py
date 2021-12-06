from solution import *


def test_load_input() -> None:
    expected: Input = [3, 4, 3, 1, 2]
    assert load_input() == expected


def test_lantern_fish() -> None:
    expected: int = 26
    assert lantern_fish(load_input(), days=18) == expected

    expected: int = 5934
    assert lantern_fish(load_input(), days=80) == expected

    expected: int = 26984457539
    assert lantern_fish(load_input(), days=256) == expected