# 🧮 Dijkstra’s Algorithm with Advanced Heaps – COSC 520 (Advanced Data Structures)

This repository contains my assignment 2 for **COSC 520 – Advanced Algorithms** at **UBC Okanagan**.  
The objective of this assignment was to **explore and benchmark advanced data structures**

---

## 🎯 Project Overview

The assignment required selecting **three comparable advanced data structures**, implementing them in Python, and analyzing their **theoretical and empirical performance**.

I chose to focus on **three priority queue structures** commonly used in graph algorithms:

- **Binary Heap** – classical structure used in most Dijkstra implementations.  
- **Pairing Heap** – self-adjusting heap known for its simplicity and strong practical performance.  
- **Fibonacci Heap** – theoretically optimal heap with *amortized* O(1) `decrease_key`, often cited in algorithmic theory.

These data structures were implemented from scratch, tested thoroughly, and integrated into a **unified Dijkstra implementation** to compare their runtime scalability.

---

## 📂 Repository Structure

```bash
cosc520_A2/
│
├── data_structures/
│   ├── binary_heap.py          # Binary Min Heap implementation with decrease_key()
│   ├── pairing_heap.py         # Pairing Heap with full cut/link + decrease_key()
│   └── fibonacci_heap.py       # Fibonacci Heap with node linking and consolidation
│
├── util/
│   └── generate_graph.py       # Random weighted graph generator with tqdm progress bar
│
├── unit_tests/
│   ├── test_binary_heap.py     # Unit tests for BinaryHeap
│   ├── test_pairing_heap.py    # Unit tests for PairingHeap (including missing key)
│   ├── test_fibonacci_heap.py  # Unit tests for FibonacciHeap
│   ├── test_dijkstra.py        # Tests Dijkstra correctness on all heaps
│   └── test_graph_generator.py # Tests random graph generator reproducibility
│
├── dijkstra.py                 # Unified Dijkstra implementation supporting all 3 heaps
├── runtime_analysis.py         # Benchmark script for large graph performance and plotting
├── plots                       # Generated runtime plots
├── some_name.latex             # Latex file for report
├── some_name.pdf               # Final Report
└── README.md                   # Project documentation (this file)
```

---

## ⚙️ Code Documentation

### `data_structures/`
Each heap file implements:
- `insert(node, priority)`
- `extract_min() → (node, priority)`
- `decrease_key(node, new_priority)`
- `is_empty()`
- `__len__()`

All are fully independent, class-based implementations with docstrings and internal helper methods (`_sift_up`, `_link`, `_consolidate`, etc.).

### `dijkstra.py`
- Implements a **unified version of Dijkstra’s algorithm**.  
- Accepts a `heap_type` argument: `"binary"`, `"pairing"`, or `"fibonacci"`.  
- Returns a dictionary `{node: shortest_distance}`.  
- Verified via unit tests for correctness on sample graphs.

### `util/generate_graph.py`
Generates random **directed weighted graphs** as adjacency lists:

```python
{node: [(neighbor, weight), ...]}
```

Includes a **tqdm progress bar** for visual tracking.

**Parameters:**
- `num_nodes`: number of vertices  
- `num_edges`: number of edges  
- `weight_range`: min/max weight range  
- `seed`: random seed for reproducibility  
- `show_progress`: whether to display tqdm  

### `runtime_analysis.py`
- Benchmarks Dijkstra’s algorithm on graphs of increasing size for all 3 heaps.
- Display progress bars and timing results  
- Save the runtime comparison plot as `runtime_comparison.png` under `plots/`

---

## 🧩 Running the Code

### ⚙️ 1️⃣ Install Dependencies
Before running any scripts, make sure you have the required libraries installed:

```bash
pip install matplotlib tqdm
```

### 🧪 2️⃣ Run Unit Tests
All modules include dedicated unit tests verifying correctness and stability.

**Run all tests at once:**
```bash
python -m unittest discover -s unit_tests -p "test_*.py" -v
```

This executes:
- Heap functionality tests (`insert`, `extract_min`, `decrease_key`)
- Graph generator validation (no self-loops, reproducibility)
- Dijkstra correctness across all heap types

**Run individual test files (optional):**
```bash
python -m unittest unit_tests/test_binary_heap.py -v
python -m unittest unit_tests/test_pairing_heap.py -v
python -m unittest unit_tests/test_fibonacci_heap.py -v
python -m unittest unit_tests/test_dijkstra.py -v
python -m unittest unit_tests/test_graph_generator.py -v
```

### 🚀 3️⃣ Run the Runtime Benchmark
The final benchmark compares the performance of all three heap implementations within Dijkstra’s algorithm.

**Run the benchmark:**
```bash
python runtime_analysis.py
```

---

## 📖 Final Report — `some_name.pdf`

The accompanying final report provides an in-depth written analysis of the project’s theoretical and experimental findings.  
It is designed to complement the codebase with detailed explanations and reflections.

### 🧾 The report includes:
- **Theoretical analysis** of time and space complexity for all three heap implementations.  
- **Implementation details** with explanations of key functions and design decisions.  
- **Runtime benchmark results**  
- **Discussion of trade-offs** between theoretical optimality and real-world performance.  
- **Scaling considerations** including Python overhead and memory constraints.  

---

## 👨‍💻 Author

**Aarav Gosalia**  
M. Sc. Computer Science | B.Sc. Data Science, Minor in Economics  
**University of British Columbia – Okanagan**  
📍 *Kelowna, BC, Canada*  
🌐 [aaravjgosalia.com](https://aaravjgosaliia.com)
