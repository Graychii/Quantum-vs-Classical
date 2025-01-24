# Grover + A* Algorithm for Maze Solving

This project combines **Grover's quantum search algorithm** and the **A* pathfinding algorithm** to solve a maze. The goal is to find the shortest path from the start (`'S'`) to the goal (`'G'`) in a grid-based maze.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Algorithms Overview](#algorithms-overview)
   - [Grover's Algorithm](#grovers-algorithm)
   - [A* Algorithm](#a-algorithm)
3. [Implementation](#implementation)
   - [Maze Representation](#maze-representation)
   - [Grover's Algorithm Implementation](#grovers-algorithm-implementation)
   - [A* Algorithm Implementation](#a-algorithm-implementation)
   - [A* with Visualization](#a-with-visualization)
4. [How It Works](#how-it-works)
5. [Example](#example)
6. [Limitations](#limitations)
7. [Future Work](#future-work)

---

## Introduction

The project aims to solve a maze using a hybrid approach:
- **Grover's algorithm** is used to **find the goal state** (`'G'`) in the maze.
- **A*** is used to **find the shortest path** from the start (`'S'`) to the goal (`'G'`).

This combination leverages the strengths of both quantum and classical algorithms:
- Grover's algorithm provides a quadratic speedup for searching unsorted data.
- A* is an efficient classical algorithm for finding the shortest path in a graph or grid.

---

## Algorithms Overview

### Grover's Algorithm

Grover's algorithm is a quantum search algorithm that can find a marked item in an unsorted database with **O(√N)** complexity, where **N** is the number of items. In this project:
- The maze is treated as a database of cells.
- The goal state (`'G'`) is the marked item.
- Grover's algorithm amplifies the probability of the goal state, making it easier to find.

### A* Algorithm

A* is a classical pathfinding algorithm that finds the shortest path from a start node to a goal node in a graph or grid. It uses a heuristic function to estimate the cost to reach the goal, ensuring efficient exploration. In this project:
- The maze is represented as a grid.
- A* finds the shortest path from the start (`'S'`) to the goal (`'G'`).

---

## Implementation

### Maze Representation

The maze is represented as a 2D grid:
- `'S'`: Start position.
- `'G'`: Goal position.
- `0`: Walkable path.
- `1`: Wall (blocked path).

---

### Grover's Algorithm Implementation

1. **Oracle**:
   - The oracle marks the goal state by flipping its phase.
   - It uses a multi-controlled Z gate to mark the goal state.

2. **Diffusion Operator**:
   - The diffusion operator amplifies the probability of the marked state.

3. **Measurement**:
   - The quantum circuit is measured to obtain the goal state.

### A* Algorithm Implementation

1. **Heuristic**:
   - The Manhattan distance is used as the heuristic function.

2. **Priority Queue**:
   - Nodes are explored based on their estimated total cost (`f_score = g_score + heuristic`).

3. **Path Reconstruction**:
   - The shortest path is reconstructed by backtracking from the goal to the start.

---

## How It Works

1. **Input**:
   - A maze with a start (`'S'`), goal (`'G'`), walls (`1`), and paths (`0`).

2. **Grover's Algorithm**:
   - Grover's algorithm searches for the goal state (`'G'`) in the maze.
   - It returns a bitstring representing the goal's position.

3. **A* Algorithm**:
   - A* finds the shortest path from the start (`'S'`) to the goal (`'G'`).

4. **Output**:
   - The shortest path from the start to the goal.


---

# Comparison

## When to Use Grover's Algorithm

### Unstructured Search:
- Grover's algorithm is ideal for searching an unsorted database or unstructured data.
- **Example**: Finding a specific item in a large, unordered list.

### Quadratic Speedup:
- Use Grover's algorithm when a quadratic speedup over classical search is needed.
- **Example**: Searching for a specific configuration in a large solution space.

### Small to Medium-Sized Problems:
- Grover's algorithm is practical for small to medium-sized problems due to the exponential growth of quantum states.
- **Example**: Solving small mazes or puzzles.

---

## When to Use A* Algorithm

### Structured Search:
- A* is ideal for structured search problems, such as pathfinding in grids or graphs.
- **Example**: Finding the shortest path in a maze or road network.

### Heuristic Guidance:
- Use A* when a heuristic function can guide the search efficiently.
- **Example**: Navigating a robot through a known environment.

### Large-Scale Problems:
- A* is suitable for large-scale problems where classical algorithms are more practical than quantum algorithms.
- **Example**: Pathfinding in large maps or game environments.

---

## When to Use the Hybrid Approach

### Combining Strengths:
- Use the hybrid approach when you need the speedup of Grover's algorithm for searching and the efficiency of A* for pathfinding.
- **Example**: Solving mazes where the goal is unknown or dynamically changing.

### Quantum-Classical Integration:
- Use the hybrid approach when integrating quantum and classical computing is feasible and beneficial.
- **Example**: Research projects exploring hybrid algorithms.

### Small to Medium-Sized Mazes:
- The hybrid approach is practical for small to medium-sized mazes due to the limitations of quantum simulation.
- **Example**: Solving small mazes with quantum-inspired search.

---

## Limitations

### Quantum Simulation:
- Simulating Grover's algorithm for large mazes is computationally expensive.
- Current quantum hardware has limited qubits and high error rates.

### Maze Size:
- The hybrid approach is practical only for small mazes due to the exponential growth of quantum states.

### Oracle Design:
- Designing an oracle for large mazes is complex and error-prone.

---

## Future Work

### Optimize Oracle:
- Develop a more efficient oracle for larger mazes.

### Quantum Hardware:
- Implement the hybrid approach on real quantum hardware as it becomes more accessible.

### Hybrid Algorithms:
- Explore other combinations of quantum and classical algorithms for pathfinding.

---

## Conclusion

The combination of Grover's algorithm and A* provides a novel approach to solving mazes. While the current implementation is limited to small mazes, it demonstrates the potential of hybrid quantum-classical algorithms for solving real-world problems.