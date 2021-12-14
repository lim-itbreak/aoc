from solution import *

example: Input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_part1() -> None:
    consumption: List[int] = fuel(example)
    expected: int

    expected = 37
    assert consumption[2] == expected == min(consumption)

    expected = 41
    assert consumption[1] == expected

    expected = 39
    assert consumption[3] == expected

    expected = 71
    assert consumption[10] == expected


def test_part2() -> None:
    consumption: List[int] = fuel(example, constant_burn=False)
    expected: int

    expected = 168
    assert consumption[5] == expected == min(consumption)

    expected = 206
    assert consumption[2] == expected
