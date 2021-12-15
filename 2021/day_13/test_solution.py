from solution import *

example: Input = (
    {
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    },
    [
        (0, 7),
        (5, 0),
    ],
)


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_part1() -> None:
    expected: int = 17
    assert part1(example) == expected


def test_part2() -> None:
    expected: str = "#####\n#...#\n#...#\n#...#\n#####"
    assert part2(example) == expected
