from solution import *

example1: Input = [
    ["start", "A"],
    ["start", "b"],
    ["A", "c"],
    ["A", "b"],
    ["b", "d"],
    ["A", "end"],
    ["b", "end"],
]
example2: Input = [
    ["dc", "end"],
    ["HN", "start"],
    ["start", "kj"],
    ["dc", "start"],
    ["dc", "HN"],
    ["LN", "dc"],
    ["HN", "end"],
    ["kj", "sa"],
    ["kj", "HN"],
    ["kj", "dc"],
]
example3: Input = [
    ["fs", "end"],
    ["he", "DX"],
    ["fs", "he"],
    ["start", "DX"],
    ["pj", "DX"],
    ["end", "zg"],
    ["zg", "sl"],
    ["zg", "pj"],
    ["pj", "he"],
    ["RW", "he"],
    ["fs", "DX"],
    ["pj", "RW"],
    ["zg", "RW"],
    ["start", "pj"],
    ["he", "WI"],
    ["zg", "he"],
    ["pj", "fs"],
    ["start", "RW"],
]


def test_load_input() -> None:
    expected: Input

    expected = example1
    assert load_input(filename="example1") == expected

    expected = example2
    assert load_input(filename="example2") == expected

    expected = example3
    assert load_input(filename="example3") == expected


def test_traverse() -> None:
    expected: Set[str]
    paths: Set[str]

    expected = {
        "start,A,b,A,c,A,end",
        "start,A,b,A,end",
        "start,A,b,end",
        "start,A,c,A,b,A,end",
        "start,A,c,A,b,end",
        "start,A,c,A,end",
        "start,A,end",
        "start,b,A,c,A,end",
        "start,b,A,end",
        "start,b,end",
    }
    paths = set()
    traverse("start", example1, [], paths)
    assert paths == expected

    expected = {
        "start,HN,dc,HN,end",
        "start,HN,dc,HN,kj,HN,end",
        "start,HN,dc,end",
        "start,HN,dc,kj,HN,end",
        "start,HN,end",
        "start,HN,kj,HN,dc,HN,end",
        "start,HN,kj,HN,dc,end",
        "start,HN,kj,HN,end",
        "start,HN,kj,dc,HN,end",
        "start,HN,kj,dc,end",
        "start,dc,HN,end",
        "start,dc,HN,kj,HN,end",
        "start,dc,end",
        "start,dc,kj,HN,end",
        "start,kj,HN,dc,HN,end",
        "start,kj,HN,dc,end",
        "start,kj,HN,end",
        "start,kj,dc,HN,end",
        "start,kj,dc,end",
    }
    paths = set()
    traverse("start", example2, [], paths)
    assert paths == expected

    expected = {
        "start,A,b,A,b,A,c,A,end",
        "start,A,b,A,b,A,end",
        "start,A,b,A,b,end",
        "start,A,b,A,c,A,b,A,end",
        "start,A,b,A,c,A,b,end",
        "start,A,b,A,c,A,c,A,end",
        "start,A,b,A,c,A,end",
        "start,A,b,A,end",
        "start,A,b,d,b,A,c,A,end",
        "start,A,b,d,b,A,end",
        "start,A,b,d,b,end",
        "start,A,b,end",
        "start,A,c,A,b,A,b,A,end",
        "start,A,c,A,b,A,b,end",
        "start,A,c,A,b,A,c,A,end",
        "start,A,c,A,b,A,end",
        "start,A,c,A,b,d,b,A,end",
        "start,A,c,A,b,d,b,end",
        "start,A,c,A,b,end",
        "start,A,c,A,c,A,b,A,end",
        "start,A,c,A,c,A,b,end",
        "start,A,c,A,c,A,end",
        "start,A,c,A,end",
        "start,A,end",
        "start,b,A,b,A,c,A,end",
        "start,b,A,b,A,end",
        "start,b,A,b,end",
        "start,b,A,c,A,b,A,end",
        "start,b,A,c,A,b,end",
        "start,b,A,c,A,c,A,end",
        "start,b,A,c,A,end",
        "start,b,A,end",
        "start,b,d,b,A,c,A,end",
        "start,b,d,b,A,end",
        "start,b,d,b,end",
        "start,b,end",
    }
    paths = set()
    traverse("start", example1, [], paths, limit=2)
    assert paths == expected


def test_part1() -> None:
    expected: int

    expected = 10
    assert part1(example1) == expected

    expected = 19
    assert part1(example2) == expected

    expected = 226
    assert part1(example3) == expected


def test_part2() -> None:
    expected: int

    expected = 36
    assert part2(example1) == expected

    expected = 103
    assert part2(example2) == expected

    expected = 3509
    assert part2(example3) == expected
