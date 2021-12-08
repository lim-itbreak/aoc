from solution import *

example: Input = [
    [
        [
            frozenset("be"),
            frozenset("cfbegad"),
            frozenset("cbdgef"),
            frozenset("fgaecd"),
            frozenset("cgeb"),
            frozenset("fdcge"),
            frozenset("agebfd"),
            frozenset("fecdb"),
            frozenset("fabcd"),
            frozenset("edb"),
        ],
        [
            frozenset("fdgacbe"),
            frozenset("cefdb"),
            frozenset("cefbgd"),
            frozenset("gcbe"),
        ],
    ],
    [
        [
            frozenset("edbfga"),
            frozenset("begcd"),
            frozenset("cbg"),
            frozenset("gc"),
            frozenset("gcadebf"),
            frozenset("fbgde"),
            frozenset("acbgfd"),
            frozenset("abcde"),
            frozenset("gfcbed"),
            frozenset("gfec"),
        ],
        [
            frozenset("fcgedb"),
            frozenset("cgb"),
            frozenset("dgebacf"),
            frozenset("gc"),
        ],
    ],
    [
        [
            frozenset("fgaebd"),
            frozenset("cg"),
            frozenset("bdaec"),
            frozenset("gdafb"),
            frozenset("agbcfd"),
            frozenset("gdcbef"),
            frozenset("bgcad"),
            frozenset("gfac"),
            frozenset("gcb"),
            frozenset("cdgabef"),
        ],
        [frozenset("cg"), frozenset("cg"), frozenset("fdcagb"), frozenset("cbg")],
    ],
    [
        [
            frozenset("fbegcd"),
            frozenset("cbd"),
            frozenset("adcefb"),
            frozenset("dageb"),
            frozenset("afcb"),
            frozenset("bc"),
            frozenset("aefdc"),
            frozenset("ecdab"),
            frozenset("fgdeca"),
            frozenset("fcdbega"),
        ],
        [
            frozenset("efabcd"),
            frozenset("cedba"),
            frozenset("gadfec"),
            frozenset("cb"),
        ],
    ],
    [
        [
            frozenset("aecbfdg"),
            frozenset("fbg"),
            frozenset("gf"),
            frozenset("bafeg"),
            frozenset("dbefa"),
            frozenset("fcge"),
            frozenset("gcbea"),
            frozenset("fcaegb"),
            frozenset("dgceab"),
            frozenset("fcbdga"),
        ],
        [
            frozenset("gecf"),
            frozenset("egdcabf"),
            frozenset("bgf"),
            frozenset("bfgea"),
        ],
    ],
    [
        [
            frozenset("fgeab"),
            frozenset("ca"),
            frozenset("afcebg"),
            frozenset("bdacfeg"),
            frozenset("cfaedg"),
            frozenset("gcfdb"),
            frozenset("baec"),
            frozenset("bfadeg"),
            frozenset("bafgc"),
            frozenset("acf"),
        ],
        [
            frozenset("gebdcfa"),
            frozenset("ecba"),
            frozenset("ca"),
            frozenset("fadegcb"),
        ],
    ],
    [
        [
            frozenset("dbcfg"),
            frozenset("fgd"),
            frozenset("bdegcaf"),
            frozenset("fgec"),
            frozenset("aegbdf"),
            frozenset("ecdfab"),
            frozenset("fbedc"),
            frozenset("dacgb"),
            frozenset("gdcebf"),
            frozenset("gf"),
        ],
        [
            frozenset("cefg"),
            frozenset("dcbef"),
            frozenset("fcge"),
            frozenset("gbcadfe"),
        ],
    ],
    [
        [
            frozenset("bdfegc"),
            frozenset("cbegaf"),
            frozenset("gecbf"),
            frozenset("dfcage"),
            frozenset("bdacg"),
            frozenset("ed"),
            frozenset("bedf"),
            frozenset("ced"),
            frozenset("adcbefg"),
            frozenset("gebcd"),
        ],
        [
            frozenset("ed"),
            frozenset("bcgafe"),
            frozenset("cdgba"),
            frozenset("cbgef"),
        ],
    ],
    [
        [
            frozenset("egadfb"),
            frozenset("cdbfeg"),
            frozenset("cegd"),
            frozenset("fecab"),
            frozenset("cgb"),
            frozenset("gbdefca"),
            frozenset("cg"),
            frozenset("fgcdab"),
            frozenset("egfdb"),
            frozenset("bfceg"),
        ],
        [frozenset("gbdfcae"), frozenset("bgc"), frozenset("cg"), frozenset("cgb")],
    ],
    [
        [
            frozenset("gcafb"),
            frozenset("gcf"),
            frozenset("dcaebfg"),
            frozenset("ecagb"),
            frozenset("gf"),
            frozenset("abcdeg"),
            frozenset("gaef"),
            frozenset("cafbge"),
            frozenset("fdbac"),
            frozenset("fegbdc"),
        ],
        [
            frozenset("fgae"),
            frozenset("cfgab"),
            frozenset("fg"),
            frozenset("bagce"),
        ],
    ],
]


def test_convert() -> None:
    expected: List[FrozenSet[str]] = [
        frozenset("acedgfb"),
        frozenset("cdfbe"),
        frozenset("gcdfa"),
        frozenset("fbcad"),
        frozenset("dab"),
        frozenset("cefabd"),
        frozenset("cdfgeb"),
        frozenset("eafb"),
        frozenset("cagedb"),
        frozenset("ab"),
    ]
    convert("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab") == expected


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_decode() -> None:
    expected: Dict[FrozenSet[str], str] = {
        frozenset("acedgfb"): "8",
        frozenset("cdfbe"): "5",
        frozenset("gcdfa"): "2",
        frozenset("fbcad"): "3",
        frozenset("dab"): "7",
        frozenset("cefabd"): "9",
        frozenset("cdfgeb"): "6",
        frozenset("eafb"): "4",
        frozenset("cagedb"): "0",
        frozenset("ab"): "1",
    }
    assert decode(expected) == expected


def test_read() -> None:
    assert (
        read(
            [
                frozenset("cdfeb"),
                frozenset("fcadb"),
                frozenset("cdfeb"),
                frozenset("cdbaf"),
            ],
            {
                frozenset("acedgfb"): "8",
                frozenset("cdfbe"): "5",
                frozenset("gcdfa"): "2",
                frozenset("fbcad"): "3",
                frozenset("dab"): "7",
                frozenset("cefabd"): "9",
                frozenset("cdfgeb"): "6",
                frozenset("eafb"): "4",
                frozenset("cagedb"): "0",
                frozenset("ab"): "1",
            },
        )
        == 5353
    )

    expected: List[int] = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
    assert [read(digits, decode(signals)) for signals, digits in example] == expected


def test_part1() -> None:
    expected: int = 26
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 61229
    assert part2(example) == expected
