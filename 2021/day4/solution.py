from typing import List, TextIO, Tuple

Input = Tuple[List[int], List[List[int]]]


def load_input(filename: str = "example") -> Input:
    fp: TextIO
    with open(filename) as fp:
        numbers: List[int] = [int(n) for n in fp.readline().split(",")]
        boards: List[List[int]] = []
        board: List[int] = []
        line: str
        for line in fp:
            if not line.strip():
                if board:
                    boards.append(board)
                    board: List[int] = []
            else:
                board.extend([int(n) for n in line.split()])
        if board:
            boards.append(board)
        return numbers, boards


def check(board: List[int]) -> bool:
    size: int = 5
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
    numbers: List[int]
    boards: List[List[int]]
    numbers, boards = inputs
    won: List[int] = []
    scores: List[int] = []
    number: int
    for number in numbers:
        i: int
        for i in range(len(boards)):
            if i not in won:
                board: List[int] = boards[i]
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
