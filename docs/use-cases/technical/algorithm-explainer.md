# Algorithm Explainer

## Description
Algorithm Explainer breaks down complex algorithms and data structures into step-by-step plain English explanations with worked examples, time/space complexity analysis, and practical use-case context. It makes dense algorithmic code understandable to any developer.

## Why Hermes
Hermes traces algorithm execution with concrete examples, explains the intuition behind why an algorithm works (not just how), and correctly analyzes Big O complexity including average vs. worst-case distinctions — producing explanations that stick rather than just restating code in prose.

## Quickstart
```bash
python examples/technical/debugging_tools.py explain-algorithm \
  --code "def quicksort(arr): ..." \
  --detail intermediate
```

## Sample Input
```python
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist
```

## Expected Output Format
```
Algorithm Explanation: Dijkstra's Shortest Path

THE GOAL
Find the shortest path from a single source node to every other node in a
weighted graph (where all edge weights are non-negative).

THE INTUITION
Think of it as an expanding "wave" from the start node. At each step, expand to the
nearest unvisited node — because once you've found the cheapest way to reach a node,
no future path through a more-expensive node can be cheaper (given non-negative weights).

STEP-BY-STEP WALKTHROUGH
Graph: A--(1)-->B, A--(4)-->C, B--(2)-->C, B--(5)-->D, C--(1)-->D
Start: A

Step 1: dist = {A:0, B:inf, C:inf, D:inf}, PQ: [(0,A)]
Step 2: Pop (0,A). Visit A. Update B->1, C->4. PQ: [(1,B),(4,C)]
Step 3: Pop (1,B). Visit B. Update C->3, D->6. PQ: [(3,C),(4,C),(6,D)]
Step 4: Pop (3,C). Visit C. Update D->4. PQ: [(4,C),(4,D),(6,D)]
Step 5: Pop (4,C) — already visited, skip.
Step 6: Pop (4,D). Visit D.
Result: {A:0, B:1, C:3, D:4}

COMPLEXITY
  Time:  O((V + E) log V) with a binary heap
  Space: O(V) for dist and visited

WHEN TO USE
  - GPS routing, network packet routing
  - Game AI pathfinding (A* is an extension)
  - Any single-source shortest path with non-negative weights

LIMITATIONS
  - Does NOT work with negative edge weights (use Bellman-Ford instead)
  - For unweighted graphs, BFS is simpler and O(V+E)
```

## Tips
- Use `--detail beginner`, `--detail intermediate`, or `--detail advanced` to adjust depth.
- Provide a small concrete graph/input for the walkthrough to be maximally clear.
- Use `--compare bfs` or `--compare bellman-ford` to get a side-by-side comparison.
- Works for any named algorithm — just describe it or paste the implementation.
