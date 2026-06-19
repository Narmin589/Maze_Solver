import copy


RIGHT=0
BOTTOM=1
LEFT=2
TOP=3

def readMaze(filename):
    try:
        with open(filename, 'r') as f:

            rows, cols = map(int, f.readline().split())
            finish_coords = list(map(int, f.readline().split()))

            maze_structure = []

            for r in range(rows):
                line = f.readline().split()
                row_data = []

                for square in line:
                    walls = [int(x) for x in square]
                    row_data.append(walls)

                maze_structure.append(row_data)

            return maze_structure, finish_coords, rows, cols

    except FileNotFoundError:
        return None, None, 0, 0
def searchMaze(maze, current, target, path):
    """
    A recursive brute-force search to find the exit.
    """
    
    if current == target: 
        return path 

    r, c = current
    
    
    movements = {
        RIGHT:  (0, 1),
        BOTTOM: (1, 0),
        LEFT:   (0, -1),
        TOP:    (-1, 0)
    } 

    for direction in [RIGHT, BOTTOM, LEFT, TOP]:
        
        if maze[r][c][direction] == 0: 
            
            dr, dc = movements[direction]
            next_sq = [r + dr, c + dc]

            
            if next_sq not in path: 
                
                new_path = copy.deepcopy(path) 
                new_path.append(next_sq) 

                
                discovery = searchMaze(maze, next_sq, target, new_path)
                
            
                if discovery is not None:
                    return discovery 

    
    return None 

def main():
    print("Welcome to the Maze Solver!")
    file_name = input("Please enter the filename of the maze: ")
    
    maze, finish, total_rows, total_cols = readMaze(file_name) 
    if maze is None:
        print("Error: Could not load maze.")
        return

    
    start_row = int(input("Please enter the starting row: "))
    while not (0 <= start_row < total_rows): 
        print(f"Invalid, enter a number between 0 and {total_rows - 1} (inclusive):")
        start_row = int(input())

    start_col = int(input("Please enter the starting column: "))
    while not (0 <= start_col < total_cols): 
        print(f"Invalid, enter a number between 0 and {total_cols - 1} (inclusive):")
        start_col = int(input())

    solution = searchMaze(maze, [start_row, start_col], finish, [[start_row, start_col]])

    
    if solution:
        print("Solution found!") 
        for pos in solution:
            print(f"({pos[0]}, {pos[1]})")
    else:
        print("No solution found!") 

if __name__ == "__main__":
    main() 