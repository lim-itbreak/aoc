from typing import Dict, FrozenSet, List, TextIO, Tuple

Input = List[Tuple[List[FrozenSet[str]], List[FrozenSet[str]]]]


def load_input(filename: str = "example") -> Input:
    notes: Input = []
    fp: TextIO
    with open(filename) as fp:
        line: str
        for line in fp:
            signals: str
            digits: str
            signals, digits = line.split("|")
            signals: List[FrozenSet[str]] = [
                frozenset(signal) for signal in signals.split()
            ]
            digits: List[FrozenSet[str]] = [
                frozenset(digit) for digit in digits.split()
            ]
            notes.append((signals, digits))
    return notes


def part1(inputs: Input) -> int:
    return sum(
        len([digit for digit in digits if len(digit) in (2, 4, 3, 7)])
        for _, digits in inputs
    )


def part2(inputs: Input) -> int:
    decoded: List[int] = []

    signals: List[FrozenSet[str]]
    digits: List[FrozenSet[str]]
    for signals, digits in inputs:
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

        decoded.append(int("".join(mapping[signal] for signal in digits)))
    return sum(decoded)


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
