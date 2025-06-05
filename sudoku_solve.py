def print_grid(grid):
    print("\nSolved Sudoku:")
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num if num != 0 else ".", end=" ")
        print()

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, num, pos):
    row, col = pos
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(9)]:
        return False
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False
    return True

def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return True
    row, col = find
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def get_user_input():
    print("\nEnter your Sudoku puzzle (row-by-row, use 0 for empty cells):")
    grid = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != 9 or any(num < 0 or num > 9 for num in row):
                    raise ValueError
                grid.append(row)
                break
            except ValueError:
                print("Invalid row. Enter exactly 9 numbers between 0 and 9 separated by spaces.")
    return grid
    
if __name__ == "__main__":
    while True:
        sudoku_grid = get_user_input()
        print("\nSolving...")
        if solve_sudoku(sudoku_grid):
            print_grid(sudoku_grid)
        else:
            print("No solution exists for the given Sudoku puzzle.")

        choice = input("\nDo you want to solve another Sudoku? (yes/no): ").strip().lower()
        if choice not in ('yes', 'y'):
            print("Exiting the program.")
            break
