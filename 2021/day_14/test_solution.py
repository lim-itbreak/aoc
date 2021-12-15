from solution import *

example: Input = (
    "NNCB",
    {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    },
)


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_polymerize() -> None:
    expected: int
    elements: Counter[str]

    expected = 97
    assert polymerize(example[0], example[1], steps=5).total() == expected  # type: ignore

    elements = polymerize(example[0], example[1], steps=10)

    expected = 3073
    assert elements.total() == expected  # type: ignore

    expected = 1749
    assert elements["B"] == expected

    expected = 298
    assert elements["C"] == expected

    expected = 161
    assert elements["H"] == expected

    expected = 865
    assert elements["N"] == expected

    elements = polymerize(example[0], example[1], steps=40)

    expected = 2192039569602
    assert elements["B"] == expected

    expected = 3849876073
    assert elements["H"] == expected


def test_part1() -> None:
    expected: int = 1588
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 2188189693529
    assert part2(example) == expected
