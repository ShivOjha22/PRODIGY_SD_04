def print_grid(grid, box_size):
    size = len(grid)
    print("\nSolved Sudoku:")
    for i in range(size):
        if i % box_size == 0 and i != 0:
            print("-" * (size * 2 + box_size - 1))
        for j in range(size):
            if j % box_size == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

def is_valid(grid, row, col, num, box_size):
    size = len(grid)
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(size)]:
        return False

    start_row = (row // box_size) * box_size
    start_col = (col // box_size) * box_size
    for i in range(start_row, start_row + box_size):
        for j in range(start_col, start_col + box_size):
            if grid[i][j] == num:
                return False
    return True

def solve(grid, box_size):
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 0:
                for num in range(1, size + 1):
                    if is_valid(grid, row, col, num, box_size):
                        grid[row][col] = num
                        if solve(grid, box_size):
                            return True
                        grid[row][col] = 0
                return False
    return True

def get_user_grid(size):
    print(f"\nEnter your Sudoku puzzle row by row (use 0 for empty cells):")
    grid = []
    for i in range(size):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != size or any(n < 0 or n > size for n in row):
                    raise ValueError
                grid.append(row)
                break
            except ValueError:
                print(f"Invalid input. Please enter exactly {size} numbers (0 to {size}) separated by spaces.")
    return grid

def main():
    while True:
        print("\n Sudoku Solver")
        print("Choose grid size:")
        print("1. 4x4")
        print("2. 9x9")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            size = 4
            box_size = 2
        elif choice == "2":
            size = 9
            box_size = 3
        else:
            print("Invalid choice. Try again.")
            continue

        grid = get_user_grid(size)

        print("\nSolving...")
        if solve(grid, box_size):
            print_grid(grid, box_size)
        else:
            print("No solution found.")

        again = input("\nDo you want to solve another puzzle? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
