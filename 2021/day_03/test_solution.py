from solution import *

example: Input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_most_common_bit() -> None:
    expected: str = "1"
    assert most_common_bit(example, 0) == expected


def test_least_common_bit() -> None:
    expected: str = "0"
    assert least_common_bit(example, 0) == expected


def test_gamma() -> None:
    expected: int = 22
    assert gamma(example) == expected


def test_epsilon() -> None:
    expected: int = 9
    assert epsilon(example) == expected


def test_by_bit() -> None:
    expected: bool = True
    assert by_bit(example[0], 0, "0") == expected


def test_o2() -> None:
    expected: int = 23
    assert o2(example) == expected


def test_co2() -> None:
    expected: int = 10
    assert co2(example) == expected


def test_part1() -> None:
    expected: int = 198
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 230
    assert part2(example) == expected
