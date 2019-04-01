rows = 8
columns = 5
board = []

for row in range(rows):
    board.append([])
    for column in range(columns):
        if (row+column) % 2 == 0:
            board[row].append(0)
        else:
            board[row].append(1)

for row in board:
    print(row)
