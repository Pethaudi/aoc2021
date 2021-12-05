from day4.board import Board

with open("4.1.input") as file:
    lines = file.readlines()

    draws = list(map(int, lines[0].split(",")))
    lines.remove(lines[0])
    boards: list[Board] = []

    joined = "".join(lines)
    stack = []
    for line in joined.split("\n"):
        if len(line) == 0 and len(stack) != 0:
            stacked = " ".join(stack)
            board = []
            for entry in stacked.split(" "):
                if len(entry) > 0:
                    board.append(entry)

            board.reverse()
            boards.append(Board(list(map(int, board))))
            stack = []
            continue

        stack.append(line)

    finished = False
    for draw in draws:
        for board in boards:
            board.selectNumber(draw)
            if board.hasWon():
                print(board.sumOfUnselected() * board.stack.pop())
                finished = True
                break

        if finished:
            break