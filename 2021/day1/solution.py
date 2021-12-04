Input = list[int]


def load_input(filename: str = "example") -> Input:
    with open(filename) as fp:
        return [int(line) for line in fp]


def part1(inputs: Input) -> int:
    count: int = 0
    previous: int = inputs[0]
    for i in range(1, len(inputs)):
        if inputs[i] > previous:
            count += 1
        previous: int = inputs[i]
    return count


def part2(inputs: Input):
    count: int = 0
    for i in range(len(inputs) - 2):
        window: int = inputs[i] + inputs[i + 1] + inputs[i + 2]
        if i != 0:
            if window > previous:
                count += 1
        previous: int = window
    return count


if __name__ == "__main__":
    inputs: Input = load_input("input")
    print(f"Day 1 Part 1 Answer: {part1(inputs)}")
    print(f"Day 1 Part 2 Answer: {part2(inputs)}")
