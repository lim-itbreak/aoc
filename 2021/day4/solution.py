Input = tuple[list[int], list[list[int]]]


def load_input(filename: str = "example") -> Input:
    with open(filename) as fp:
        numbers: list[int] = [int(n) for n in fp.readline().split(",")]
        boards: list[list[int]] = []
        board: list[int] = []
        fp.readline()  # skip the blank line
        for line in fp:
            if not line.strip():
                boards.append(board)
                board: list[int] = []
            else:
                board.extend([int(n) for n in line.split()])
        boards.append(board)
        return numbers, boards


def check(board: list[int]) -> bool:
    size: int = 5
    win: list[int] = size * [-1]
    if board.count(-1) >= size:
        for i in range(size):
            if board[size * i : size * (i + 1)] == win:
                return True
            elif board[i::size] == win:
                return True
    return False


def score(board: list[int]) -> int:
    return sum(filter(lambda n: n != -1, board))


def play(inputs: Input) -> int:
    numbers, boards = inputs
    won: list[int] = []
    scores: list[int] = []
    for number in numbers:
        for i in range(len(boards)):
            if i not in won:
                board = boards[i]
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
    print(f"Day 4 Part 1 Answer: {part1(load_input('input'))}")
    print(f"Day 4 Part 2 Answer: {part2(load_input('input'))}")
