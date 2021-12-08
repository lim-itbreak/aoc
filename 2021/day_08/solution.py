from typing import Dict, FrozenSet, Iterable, List, TextIO

Input = List[List[List[FrozenSet[str]]]]


def convert(line: str) -> List[FrozenSet[str]]:
    return [frozenset(token) for token in line.split()]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [[convert(string) for string in line.split("|")] for line in fp]


def decode(signals: Iterable[FrozenSet[str]]) -> Dict[FrozenSet[str], str]:
    mapping: Dict[FrozenSet[str], str] = {}

    signal: FrozenSet[str]
    for signal in signals:
        match len(signal):
            case 2:
                mapping[signal] = "1"
                one: FrozenSet[str] = signal
            case 4:
                mapping[signal] = "4"
                four: FrozenSet[str] = signal
            case 3:
                mapping[signal] = "7"
            case 7:
                mapping[signal] = "8"
    for signal in signals:
        match len(signal):
            case 5:
                if len(signal.intersection(four)) == 2:
                    mapping[signal] = "2"
                elif signal.issuperset(one):
                    mapping[signal] = "3"
                else:
                    mapping[signal] = "5"
            case 6:
                if signal.issuperset(four):
                    mapping[signal] = "9"
                elif signal.issuperset(one):
                    mapping[signal] = "0"
                else:
                    mapping[signal] = "6"

    return mapping


def read(digits: List[FrozenSet[str]], mapping: Dict[FrozenSet[str], str]) -> int:
    return int("".join(mapping[signal] for signal in digits))


def part1(inputs: Input) -> int:
    return sum(
        len([digit for digit in digits if len(digit) in (2, 4, 3, 7)])
        for _, digits in inputs
    )


def part2(inputs: Input) -> int:
    return sum(read(digits, decode(signals)) for signals, digits in inputs)


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
