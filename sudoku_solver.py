import tkinter as tk
from tkinter import messagebox

SIZE = 9

entries = [[None for _ in range(SIZE)] for _ in range(SIZE)]


def is_safe(board, row, col, num):

    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if is_safe(board, row, col, num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True


def get_board():

    board = []

    for i in range(9):

        row = []

        for j in range(9):

            value = entries[i][j].get()

            if value == "":
                row.append(0)
            else:
                try:
                    num = int(value)

                    if num < 1 or num > 9:
                        raise ValueError

                    row.append(num)

                except:
                    messagebox.showerror(
                        "Invalid Input",
                        "Only numbers 1-9 are allowed."
                    )
                    return None

        board.append(row)

    return board


def display_board(board):

    for i in range(9):
        for j in range(9):

            entries[i][j].delete(0, tk.END)

            if board[i][j] != 0:
                entries[i][j].insert(0, str(board[i][j]))


def solve_board():

    board = get_board()

    if board is None:
        return

    if solve(board):
        display_board(board)
    else:
        messagebox.showinfo("Sudoku", "No Solution Exists")


def clear_board():

    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)


def load_example():

    puzzle = [
        [3,0,6,5,0,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,0,6,3,0,0]
    ]

    display_board(puzzle)


root = tk.Tk()

root.title("Sudoku Solver")

for i in range(9):

    for j in range(9):

        e = tk.Entry(
            root,
            width=2,
            font=("Arial", 18),
            justify="center"
        )

        e.grid(row=i, column=j, padx=2, pady=2)

        entries[i][j] = e


solve_btn = tk.Button(
    root,
    text="Solve",
    width=12,
    command=solve_board,
    bg="lightgreen"
)

solve_btn.grid(row=10, column=1, columnspan=2, pady=10)

clear_btn = tk.Button(
    root,
    text="Clear",
    width=12,
    command=clear_board,
    bg="tomato"
)

clear_btn.grid(row=10, column=3, columnspan=2)

example_btn = tk.Button(
    root,
    text="Load Example",
    width=12,
    command=load_example,
    bg="lightblue"
)

example_btn.grid(row=10, column=5, columnspan=3)

root.mainloop()