from collections import Counter
from functools import partial


Input = list[str]


def load_input(filename: str = "example") -> Input:
    with open(filename) as fp:
        return [line.strip() for line in fp]


def bit_counter(inputs: Input, pos: int) -> Counter:
    return Counter((bin[pos] for bin in inputs)).most_common()


def most_common_bit(inputs: Input, pos: int) -> str:
    counter: Counter = bit_counter(inputs, pos)
    if len(counter) > 1 and counter[0][1] == counter[1][1]:
        return max(counter[0][0], counter[1][0])
    return bit_counter(inputs, pos)[0][0]


def least_common_bit(inputs: Input, pos: int) -> str:
    counter: Counter = bit_counter(inputs, pos)
    if len(counter) > 1 and counter[-1][1] == counter[-2][1]:
        return min(counter[-1][0], counter[-2][0])
    return bit_counter(inputs, pos)[-1][0]


def gamma(inputs: Input) -> int:
    return int("".join(most_common_bit(inputs, i) for i in range(len(inputs[0]))), 2)


def epsilon(inputs: Input) -> int:
    return int("".join(least_common_bit(inputs, i) for i in range(len(inputs[0]))), 2)


def by_bit(bin: str, pos: int, bit: str) -> bool:
    return bin[pos] == bit


def o2(inputs: Input) -> int:
    filtered: list = inputs
    for pos in range(len(inputs[0])):
        filtered: list = list(
            filter(
                partial(by_bit, pos=pos, bit=most_common_bit(filtered, pos)), filtered
            )
        )
    return int(filtered[0], 2)


def co2(inputs: Input) -> int:
    filtered: list = inputs
    for i in range(len(inputs[0])):
        filtered: list = list(
            filter(partial(by_bit, pos=i, bit=least_common_bit(filtered, i)), filtered)
        )
    return int(filtered[0], 2)


def part1(inputs: Input) -> int:
    return gamma(inputs) * epsilon(inputs)


def part2(inputs: Input) -> int:
    return o2(inputs) * co2(inputs)


if __name__ == "__main__":
    inputs: Input = load_input("input")
    print(f"Day 3 Part 1 Answer: {part1(inputs)}")
    print(f"Day 3 Part 2 Answer: {part2(inputs)}")
