from solution import *

example: Input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_load_input() -> None:
    expected: Input = example
    assert load_input() == expected


def test_check() -> None:
    expected: str

    expected = "}"
    assert check("{([(<{}[<>[]}>{[]{[(<()>") == expected

    expected = ")"
    assert check("[[<[([]))<([[{}[[()]]]") == expected

    expected = "]"
    assert check("[{[{({}]{}}([{[{{{}}([]") == expected

    expected = ")"
    assert check("[<(<(<(<{}))><([]([]()") == expected

    expected = ">"
    assert check("<{([([[(<>()){}]>(<<{{") == expected

    expected = "}}]])})]"
    assert check("[({(<(())[]>[[{[]{<()<>>") == expected

    expected = ")}>]})"
    assert check("[(()[<>])]({[<{<<[]>>(") == expected

    expected = "}}>}>))))"
    assert check("(((({<>}<{<{<>}{[]{[]{}") == expected

    expected = "]]}}]}]}>"
    assert check("{<[[]]>}<{[{[{[]{()[[[]") == expected

    expected = "])}>"
    assert check("<{([{{}}[<[[[<>{}]]]>[]]") == expected


def test_calculate() -> None:
    expected: int

    expected = 288957
    assert score("}}]])})]") == expected

    expected = 5566
    assert score(")}>]})") == expected

    expected = 1480781
    assert score("}}>}>))))") == expected

    expected = 995444
    assert score("]]}}]}]}>") == expected

    expected = 294
    assert score("])}>") == expected


def test_analyze() -> None:
    expected: Tuple[int, int] = (26397, 288957)
    assert analyze(example) == expected
