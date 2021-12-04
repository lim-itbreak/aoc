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


def part1(inputs: Input) -> int:
    numbers, boards = inputs
    winner: int = 0
    for number in numbers:
        for board in boards:
            if number in board:
                board[board.index(number)] = -1
                if check(board):
                    winner: int = max(winner, score(board) * number)
        if winner:
            break
    return winner


def part2(inputs: Input) -> int:
    return 0


if __name__ == "__main__":
    inputs: Input = load_input("input")
    print(f"Day 4 Part 1 Answer: {part1(inputs)}")
    print(f"Day 4 Part 2 Answer: {part2(inputs)}")
