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


def play(bingo: Input) -> List[int]:
    scores: List[int] = []
    won: List[int] = []
    number: int
    for number in bingo[0]:
        i: int
        for i in range(1, len(bingo)):
            if i not in won:
                board: List[int] = bingo[i]
                if number in board:
                    board[board.index(number)] = -1
                    if check(board):
                        won.append(i)
                        scores.append(score(board) * number)
    return scores


if __name__ == "__main__":
    scores: List[int] = play(load_input(filename="puzzle"))
    print(f"Part 1 Answer: {scores[0]}")
    print(f"Part 2 Answer: {scores[-1]}")
