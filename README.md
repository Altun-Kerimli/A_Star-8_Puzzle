# A_Star-8_Puzzle
An 8-puzzle solver using the A* search algorithm.

## Overview
This project is an implementation of an AI agent to solve the 8-puzzle problem using the A* search algorithm. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one empty space. The goal is to move the tiles around until they are in a specified target configuration.

## How It Works
The project is divided into two main classes:

1. **Dugum (Node) Class:**
   - Represents a state of the puzzle.
   - Contains methods to generate child nodes by moving the blank tile (0) in different directions.
   - Ensures that invalid or previously visited states are not considered.
   - Uses the A* search algorithm to find the optimal path to the target configuration.

2. **Ajan (Agent) Class:**
   - Manages the puzzle-solving process.
   - Calculates the cost functions (`fn`, `hn`, and `gn`) to determine the best moves.
   - Displays the puzzle state at each step of the solving process.

### Key Methods:
- `find`: Locates the position of the blank tile in the puzzle.
- `shuffle`: Moves the blank tile in a specified direction and returns the resulting puzzle configuration.
- `copy`: Creates a copy of a given puzzle configuration.
- `generate_child`: Generates all possible valid child states from the current state and selects the one with the lowest cost.
- `hn`: Heuristic function that counts the number of misplaced tiles.
- `fn`: Evaluation function that combines the heuristic and the path cost.
- `display`: Displays the current state of the puzzle and the associated costs.

## Usage
To use this project, you need to define the initial and target configurations of the puzzle. The example provided in the code initializes the agent with a specific problem and target state and runs the solving process.

## Conclusion
This project provides a clear implementation of the A* search algorithm to solve the 8-puzzle problem, demonstrating the core concepts of heuristic search and cost evaluation. It is a useful reference for understanding and implementing AI search algorithms in Python.
