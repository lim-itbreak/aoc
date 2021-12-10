from itertools import chain
from math import prod
from typing import List, Set, TextIO, Tuple

Input = List[List[int]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [[int(number) for number in line.strip()] for line in fp]


def adjacent_points(x: int, y: int, heights: Input) -> List[Tuple[int, int]]:
    points: List[Tuple[int, int]] = []
    if x > 0:
        points.append((x - 1, y))
    if x < len(heights[y]) - 1:
        points.append((x + 1, y))
    if y > 0:
        points.append((x, y - 1))
    if y < len(heights) - 1:
        points.append((x, y + 1))
    return points


def adjacent_heights(x: int, y: int, heights) -> List[int]:
    return [heights[y][x] for x, y in adjacent_points(x, y, heights)]


def low_point(x: int, y: int, heights: Input) -> bool:
    return all(heights[y][x] < height for height in adjacent_heights(x, y, heights))


def low_points(heights: Input) -> List[Tuple[int, int]]:
    return list(
        chain(
            *(
                [(x, y) for x in range(len(heights[y])) if low_point(x, y, heights)]
                for y in range(len(heights))
            )
        )
    )


def basin_points(
    curr_point: Tuple[int, int],
    prev_height: int,
    heights: Input,
    basin: Set[Tuple[int, int]],
) -> None:
    x: int
    y: int
    x, y = curr_point
    if prev_height <= heights[y][x] < 9:
        basin.add(curr_point)

        point: Tuple[int, int]
        for point in adjacent_points(x, y, heights):
            if point not in basin:
                basin_points(point, heights[y][x], heights, basin)


def part1(inputs: Input) -> int:
    return sum(1 + inputs[y][x] for x, y in low_points(inputs))


def part2(inputs: Input) -> int:
    sizes: List[int] = []
    point: Tuple[int, int]
    for point in low_points(inputs):
        basin: Set[Tuple[int, int]] = set()
        basin_points(point, inputs[point[1]][point[0]], inputs, basin)
        sizes.append(len(basin))
    sizes.sort(reverse=True)
    return prod(sizes[:3])


if __name__ == "__main__":
    inputs: Input = load_input(filename="puzzle")
    print(f"Part 1 Answer: {part1(inputs)}")
    print(f"Part 2 Answer: {part2(inputs)}")
