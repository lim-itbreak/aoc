from solution import *


def test_load_input() -> None:
    expected: Input = [
        [[0, 9], [5, 9]],
        [[8, 0], [0, 8]],
        [[9, 4], [3, 4]],
        [[2, 2], [2, 1]],
        [[7, 0], [7, 4]],
        [[6, 4], [2, 0]],
        [[0, 9], [2, 9]],
        [[3, 4], [1, 4]],
        [[0, 0], [8, 8]],
        [[5, 5], [8, 2]],
    ]
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 5
    assert part1(load_input()) == expected


def test_part2() -> None:
    expected: int = 12
    assert part2(load_input()) == expected
