## **Nearest Exit from Entrance in Maze (LeetCode 1926)**

---

### **1. Problem statement with example**

You are given a `m x n` grid `maze` where:

* `"."` → empty cell
* `"+"` → wall

You are also given an **entrance** cell `[startRow, startCol]`.

👉 You can move in **4 directions** (up, down, left, right).
👉 You **cannot** go outside the maze or into walls.

👉 An **exit** is:

* any **boundary cell**
* **NOT the entrance itself**

👉 Return the **minimum number of steps to the nearest exit**, or `-1` if none exists.

**Constraints:**

* `1 <= m, n <= 100`
* Standard BFS grid problem
* Unweighted → shortest path → BFS

---

### **2. Diagram**

Example:

```
+ + . +
. . . +
+ + + .
```

Entrance:

```
(1,0)
```

Visual:

```
    0   1   2   3
  ----------------
0 | + | + | . | + |
1 | E | . | . | + |
2 | + | + | + | . |
```

Possible exits (boundary `.` except entrance):

* (0,2)
* (2,3)

---

### **3. Example I/O**

#### **Example 1**

```
Input:
maze = [["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."]]
entrance = [1,0]

Output: 2
```

**Explanation:**

```
(1,0) → (1,1) → (0,2)
```

---

#### **Example 2**

```
Input:
maze = [["+","+","+"],
        [".",".","."],
        ["+","+","+"]]
entrance = [1,0]

Output: 2
```

---

#### **Edge Case**

```
Input:
maze = [[".","+"]]
entrance = [0,0]

Output: -1
```

👉 Entrance is on boundary but **cannot count as exit**

---

### **4. Intuition & pattern recognition**

🔑 Signals:

* "nearest exit"
* "minimum steps"
* "grid movement"
* "unweighted"

👉 Immediate thought:

> **BFS from entrance**

---

💡 Key twist:

* Exit = **boundary cell**
* BUT exclude entrance

---

### **5. Simpler version**

#### **Simpler problems to build intuition**

* Flood Fill
  → basic grid traversal

* Rotting Oranges
  → BFS levels

* Shortest Path in Binary Matrix
  → shortest path BFS

---

#### **How this evolves**

| Step                     | Concept              |
| ------------------------ | -------------------- |
| Traverse grid            | DFS/BFS              |
| Find shortest path       | BFS                  |
| Add condition (boundary) | exit detection       |
| Final problem            | BFS + exit condition |

---

### **6. Brute force**

👉 Try all paths using DFS:

* Explore all possible routes
* Track shortest exit

❌ Problems:

* Exponential time
* Repeated visits

**Time:** exponential
**Space:** recursion stack

---

### **7. Optimal solution (BFS)**

```python
from collections import deque

def nearestExit(maze, entrance):
    m, n = len(maze), len(maze[0])
    
    queue = deque([(entrance[0], entrance[1], 0)])
    
    # mark entrance visited
    maze[entrance[0]][entrance[1]] = "+"
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while queue:
        r, c, steps = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # valid move
            if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                
                # check if exit (boundary)
                if nr == 0 or nr == m-1 or nc == 0 or nc == n-1:
                    return steps + 1
                
                queue.append((nr, nc, steps + 1))
                maze[nr][nc] = "+"  # mark visited
    
    return -1
```

---

### **Complexity**

* **Time:** O(m × n)
* **Space:** O(m × n)

---

### **8. Step-by-step trace**

Maze:

```
+ + . +
. . . +
+ + + .
```

Entrance = `(1,0)`

---

#### Step 1:

```
Queue = [(1,0,0)]
```

---

#### Step 2:

```
Pop (1,0)

Push:
(1,1,1)
```

Queue:

```
[(1,1,1)]
```

---

#### Step 3:

```
Pop (1,1)

Push:
(1,2,2)
```

Queue:

```
[(1,2,2)]
```

---

#### Step 4:

```
Pop (1,2)

Neighbor (0,2) → boundary → EXIT
```

👉 Return `2`

---

### **9. Related problems**

* Shortest Path in Binary Matrix
  → BFS shortest path with 8 directions

* Rotting Oranges
  → BFS layer expansion

* Walls and Gates
  → BFS from multiple sources

* 01 Matrix
  → BFS for nearest distance

* Shortest Path in Grid with Obstacles Elimination
  → BFS with extra state

---

### **Interview takeaway**

👉 When you see:

* nearest / minimum steps
* grid
* no weights

💡 Instantly say:

> **“BFS from source + level tracking”**

---

If you want, I can give you a **universal BFS grid template** (covers 90% problems including this, rotten oranges, 01 matrix, etc.).
