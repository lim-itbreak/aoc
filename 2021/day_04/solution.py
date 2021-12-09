from typing import List, TextIO

Input = List[List[int]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        return [
            [int(n) for n in section.replace(",", " ").split()]
            for section in fp.read().split("\n\n")
        ]


def check(board: List[int]) -> bool:
    size: int = int(len(board) ** 0.5)
    win: List[int] = size * [-1]
    if board.count(-1) >= size:
        i: int
        for i in range(size):
            if board[size * i : size * (i + 1)] == win:
                return True
            elif board[i::size] == win:
                return True
    return False


def score(board: List[int]) -> int:
    return sum(filter(lambda n: n != -1, board))


def play(inputs: Input) -> List[int]:
    scores: List[int] = []
    won: List[int] = []
    number: int
    for number in inputs[0]:
        i: int
        for i in range(1, len(inputs)):
            if i not in won:
                board: List[int] = inputs[i]
                if number in board:
                    board[board.index(number)] = -1
                    if check(board):
                        won.append(i)
                        scores.append(score(board) * number)
    return scores


def part1(inputs: Input) -> int:
    return play(inputs)[0]


def part2(inputs: Input) -> int:
    return play(inputs)[-1]


if __name__ == "__main__":
    print(f"Part 1 Answer: {part1(load_input(filename='puzzle'))}")
    print(f"Part 2 Answer: {part2(load_input(filename='puzzle'))}")
