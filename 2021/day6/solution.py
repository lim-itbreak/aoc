from collections import Counter
from typing import List, TextIO

Input = List[int]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [int(i) for i in fp.read().split(",")]


def lantern_fish(inputs: Input, days: int) -> int:
    day_in: Counter = Counter(inputs)
    _: int
    for _ in range(days):
        day_out: Counter = Counter()
        timer: int
        for timer in day_in:
            day_out[timer - 1] = day_in[timer]
        new: int = day_out.pop(-1, 0)
        day_out[6] += new
        day_out[8] = new
        day_in: Counter = day_out
    return sum(day_in[timer] for timer in day_in)


if __name__ == "__main__":
    inputs: Input = load_input(filename="input")
    print(f"Part 1 Answer: {lantern_fish(inputs, days=80)}")
    print(f"Part 2 Answer: {lantern_fish(inputs, days=256)}")
