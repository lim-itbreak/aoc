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
    assert check("{([(<{}[<>[]}>{[]{[(<()>") == "}"
    assert check("[[<[([]))<([[{}[[()]]]") == ")"
    assert check("[{[{({}]{}}([{[{{{}}([]") == "]"
    assert check("[<(<(<(<{}))><([]([]()") == ")"
    assert check("<{([([[(<>()){}]>(<<{{") == ">"

    assert check("[({(<(())[]>[[{[]{<()<>>") == "}}]])})]"
    assert check("[(()[<>])]({[<{<<[]>>(") == ")}>]})"
    assert check("(((({<>}<{<{<>}{[]{[]{}") == "}}>}>))))"
    assert check("{<[[]]>}<{[{[{[]{()[[[]") == "]]}}]}]}>"
    assert check("<{([{{}}[<[[[<>{}]]]>[]]") == "])}>"


def test_calculate() -> None:
    assert score("}}]])})]") == 288957
    assert score(")}>]})") == 5566
    assert score("}}>}>))))") == 1480781
    assert score("]]}}]}]}>") == 995444
    assert score("])}>") == 294


def test_analyze() -> None:
    expected: Tuple[int, int] = (26397, 288957)
    assert analyze(example) == expected
