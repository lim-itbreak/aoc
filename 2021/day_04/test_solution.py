from copy import deepcopy

from solution import *

example: Input = (
    [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ],
    [
        [
            22,
            13,
            17,
            11,
            0,
            8,
            2,
            23,
            4,
            24,
            21,
            9,
            14,
            16,
            7,
            6,
            10,
            3,
            18,
            5,
            1,
            12,
            20,
            15,
            19,
        ],
        [
            3,
            15,
            0,
            2,
            22,
            9,
            18,
            13,
            17,
            5,
            19,
            8,
            7,
            25,
            23,
            20,
            11,
            10,
            24,
            4,
            14,
            21,
            16,
            12,
            6,
        ],
        [
            14,
            21,
            17,
            24,
            4,
            10,
            16,
            15,
            9,
            19,
            18,
            8,
            23,
            26,
            20,
            22,
            11,
            13,
            6,
            5,
            2,
            0,
            12,
            3,
            7,
        ],
    ],
)


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_check() -> None:
    board: List[int] = deepcopy(example[1][0])

    expected: bool = False
    board[0:4] = 4 * [-1]
    assert check(board) == expected

    expected: bool = True
    board[4] = -1
    assert check(board) == expected


def test_score() -> None:
    expected: int = 278
    board: List[int] = deepcopy(example[1][0])
    board[0] = -1
    assert score(board) == expected


def test_part1() -> None:
    expected: int = 4512
    assert part1(deepcopy(example)) == expected


def test_part2() -> None:
    expected: int = 1924
    assert part2(deepcopy(example)) == expected
