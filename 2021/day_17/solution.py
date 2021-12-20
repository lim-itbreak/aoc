from typing import List, TextIO, Tuple

Input = Tuple[List[int], List[int]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        tokens: List[str] = fp.read().split()
        return [int(x) for x in tokens[2].strip(",").split("=")[1].split("..")], [
            int(y) for y in tokens[3].split("=")[1].split("..")
        ]


def part1(inputs: Input) -> int:
    return sum(range(abs(inputs[1][0])))


def part2(inputs: Input) -> int:
    x_min: int = inputs[0][0]
    x_max: int = inputs[0][1]
    y_min: int = inputs[1][0]
    y_max: int = inputs[1][1]

    swap: int = 0
    if x_min < 0:
        swap = x_min
        x_min = abs(x_max)
        x_max = abs(swap)

    x: int = 0
    y: int = 0
    n: int = 0

    while x < x_min:
        n += 1
        x += n
    vx_min: int = n
    vx_max: int = x_max

    vy_min: int = y_min
    vy_max: int = abs(y_min) - 1

    v: List[Tuple[int, int]] = []

    vx: int
    for vx in range(vx_min, vx_max + 1):
        vy: int
        for vy in range(vy_min, vy_max + 1):
            x = 0
            y = 0
            n = 0
            while x < x_max and y > y_min:
                x += max(vx - n, 0)
                y += vy - n
                n += 1
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    v.append((-vx if swap else vx, vy))
                    break

    return len(v)


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
