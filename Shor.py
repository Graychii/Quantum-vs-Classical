import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer
from qiskit.primitives import Sampler
import networkx as nx
from typing import List, Tuple
import concurrent.futures

class MazePathFinder:
    def __init__(self, maze: List[List]):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = self._find_position('S')
        self.goal = self._find_position('G')
        self.graph = self._create_graph()
        self.sampler = Sampler()
        print(f"Start position: {self.start}")
        print(f"Goal position: {self.goal}")

    def _find_position(self, marker: str) -> Tuple[int, int]:
        for i in range(self.rows):
            for j in range(self.cols):
                if str(self.maze[i][j]) == marker:
                    return (i, j)
        raise ValueError(f"Could not find {marker} in maze")

    def _is_valid_position(self, pos: Tuple[int, int]) -> bool:
        i, j = pos
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.maze[i][j] != 1
        return False

    def _create_graph(self) -> nx.Graph:
        G = nx.Graph()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] != 1:
                    G.add_node((i, j))
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if self._is_valid_position((ni, nj)):
                            G.add_edge((i, j), (ni, nj))
        
        print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
        return G

    def _create_oracle(self, valid_paths: List[List[Tuple[int, int]]]) -> QuantumCircuit:
        n_qubits = self.rows * self.cols
        oracle = QuantumCircuit(n_qubits)
        valid_states = []
        for path in valid_paths:
            state = ['0'] * (self.rows * self.cols)
            for i, j in path:
                state[i * self.cols + j] = '1'
            valid_states.append(''.join(state))
        for state in valid_states:
            state_int = int(state, 2)
            oracle.z(state_int % n_qubits)
        
        return oracle

    def _apply_grover_diffusion(self, qc: QuantumCircuit) -> None:
        n_qubits = self.rows * self.cols
        qc.h(range(n_qubits))
        qc.x(range(n_qubits))
        control_qubits = list(range(n_qubits - 1))
        target_qubit = n_qubits - 1
        qc.h(target_qubit)
        qc.mcx(control_qubits, target_qubit)
        qc.h(target_qubit)
        qc.x(range(n_qubits))
        qc.h(range(n_qubits))

    def find_path(self) -> List[Tuple[int, int]]:
        print("Using Grover's algorithm")
        try:
            all_paths = list(nx.all_simple_paths(self.graph, self.start, self.goal))
            if not all_paths:
                print("No valid paths found")
                return []
            
            print(f"Found {len(all_paths)} possible paths")
            
            n_qubits = self.rows * self.cols
            qr = QuantumRegister(n_qubits)
            cr = ClassicalRegister(n_qubits)
            qc = QuantumCircuit(qr, cr)
            qc.h(range(n_qubits))
            oracle = self._create_oracle(all_paths)
            
            n_iterations = int(np.pi/4 * np.sqrt(2**n_qubits / len(all_paths)))
            print(f"Performing {n_iterations} Grover iterations")
            
            for i in range(n_iterations):
                qc = qc.compose(oracle)
                self._apply_grover_diffusion(qc)

            qc.measure(qr, cr)
            job = self.sampler.run(qc, shots=1000)
            result = job.result()
            counts = result.quasi_dists[0]
            max_count_state = max(counts.items(), key=lambda x: x[1])[0]
            path = []
            state_bin = format(max_count_state, f'0{n_qubits}b')
            for i in range(len(state_bin)):
                if state_bin[i] == '1':
                    row = i // self.cols
                    col = i % self.cols
                    path.append((row, col))

            print(f"Quantum path found: {path}")
            return path
            
        except nx.NetworkXNoPath:
            print("No path exists between start and goal")
            return []

def solve_maze(maze):
    print("Input maze:")
    for row in maze:
        print(' '.join(str(cell) for cell in row))
    print()
    
    pathfinder = MazePathFinder(maze)
    path = pathfinder.find_path()
    
    if not path:
        print("No path found!")
        return maze, []
    
    solution_maze = [row[:] for row in maze]
    for row, col in path:
        if str(solution_maze[row][col]) not in ['S', 'G']:
            solution_maze[row][col] = '*'
    
    print("\nSolution maze:")
    for row in solution_maze:
        print(' '.join(str(cell) for cell in row))
    
    return solution_maze, path

maze = [
    ['S', 0, 1],
    [0, 0, 'G']]

solution_maze, path = solve_maze(maze)