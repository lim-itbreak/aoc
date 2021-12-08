from solution import *

example: Input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_part1() -> None:
    output: List[int] = consumption(example)
    assert output[2] == 37 == min(output)
    assert output[1] == 41
    assert output[3] == 39
    assert output[10] == 71


def test_part2() -> None:
    output: List[int] = consumption(example, constant_burn=False)
    assert output[5] == 168 == min(output)
    assert output[2] == 206
