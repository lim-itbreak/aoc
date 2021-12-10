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


def test_complete() -> None:
    assert complete("[({(<(())[]>[[{[]{<()<>>") == "}}]])})]"
    assert complete("[(()[<>])]({[<{<<[]>>(") == ")}>]})"
    assert complete("(((({<>}<{<{<>}{[]{[]{}") == "}}>}>))))"
    assert complete("{<[[]]>}<{[{[{[]{()[[[]") == "]]}}]}]}>"
    assert complete("<{([{{}}[<[[[<>{}]]]>[]]") == "])}>"


def test_calculate() -> None:
    assert score("}}]])})]") == 288957
    assert score(")}>]})") == 5566
    assert score("}}>}>))))") == 1480781
    assert score("]]}}]}]}>") == 995444
    assert score("])}>") == 294


def test_part1() -> None:
    expected: int = 26397
    assert part1(example) == expected


def test_part2() -> None:
    expected: int = 288957
    assert part2(example) == expected
