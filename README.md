## Maze Solver

This Python project provides a maze-solving algorithm that can find a path from the starting point (marked 'A') to the ending point (marked 'B') using either Depth-First Search (DFS) or Breadth-First Search (BFS). The project consists of three classes: `Node`, `FrontierStack`, `FrontierQueue`, and `Maze`. Additionally, there is a main script, `maze_solver.py`, that demonstrates the usage of the maze-solving algorithm.

## Classes

### 1. `Node` Class

Represents a node in the search space. Each node has a state, a parent node, and an action that led to the current state.

### 2. `FrontierStack` Class

Implements a stack for managing nodes in the frontier. It supports operations such as checking if it's empty, adding a node, checking if a state is present, returning states in the frontier, and popping a node.

### 3. `FrontierQueue` Class

Inherits from `FrontierStack` and represents a queue. It overrides the `popNode` method to dequeue nodes from the front of the queue.

### 4. `Maze` Class

Represents a maze with walls, a starting point, and an ending point. It reads the maze from a file, initializes the maze's properties, and provides methods for solving the maze (`solve`), printing the maze (`printMaze`), and finding neighboring states (`neighbors`).

- Set `debug = True` during object creation to enable debug mode and track the steps taken during the maze-solving process.

## Main Script: `maze_solver.py`

This script serves as the entry point for running the maze solver. It takes a maze file and an optional algorithm parameter (default is DFS) from the command line. The script then initializes a `Maze` object, solves the maze, and prints the input maze, the number of states explored, and the solved maze.

### Usage

```bash
python maze_solver.py file.maze [algo]
```

- `file.maze`: The path to the maze file.
- `[algo]`: (Optional) The algorithm to use for solving the maze. Supported values are 'BFS' for Breadth-First Search or 'DFS' for Depth-First Search. If not provided, DFS is selected by default.

## Example

```bash
python maze_solver.py example.maze BFS
```

This command will solve the maze in the file `example.maze` using Breadth-First Search.

## Maze File Format

The maze file should contain a grid of characters representing the maze layout. Valid characters include:

- 'A': Starting point
- 'B': Ending point
- ' ': Open path
- Any other character: Wall

Ensure that the maze contains exactly one starting point ('A') and one ending point ('B').

## Demo Run
![image](https://github.com/AdityaDwivediAtGit/MazeSolver/assets/107645490/ceab01b9-e567-40ef-906a-56446ef7f188)



The image above shows a demo run of the maze-solving algorithm in action.

## Dependencies

The project does not have any external dependencies beyond the Python standard library.

Feel free to explore and use this maze-solving algorithm for your own projects!
