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
    size: int = 3
    count: int = 0
    for i in range(len(inputs) - (size - 1)):
        window: int = sum(inputs[i : i + size])
        if i != 0:
            if window > previous:
                count += 1
        previous: int = window
    return count


if __name__ == "__main__":
    inputs: Input = load_input("input")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
