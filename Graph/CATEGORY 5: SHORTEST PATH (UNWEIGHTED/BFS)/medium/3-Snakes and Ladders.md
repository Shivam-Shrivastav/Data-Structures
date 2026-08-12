## **Snakes and Ladders (LeetCode 909)**

---

### **1. Problem statement with example**

You are given an `n x n` board representing a **Snakes and Ladders game**.

* Cells are labeled from `1 → n²` in **Boustrophedon order** (zig-zag).
* You start at square `1`.
* In one move, you can roll a dice → go from `curr → curr + (1 to 6)`.

👉 If the destination cell has:

* `-1` → stay there
* any number → **jump to that number** (snake or ladder)

👉 Return the **minimum number of moves to reach n²**, or `-1` if impossible.

---

### **2. Diagram**

Example board (3x3):

```text
[[-1,-1,-1],
 [-1, 9, 8],
 [-1,-1,-1]]
```

Numbering (zig-zag):

```text
7 ← 8 ← 9
↓         ↑
6 → 5 → 4
↓
1 → 2 → 3
```

👉 From `2`, if ladder → go to `9`

---

### **3. Example I/O**

#### **Example 1**

```text
Input:
board = [[-1,-1,-1],
         [-1,9,8],
         [-1,-1,-1]]

Output: 1
```

**Explanation:**

```text
1 → 2 → ladder → 9 (end)
```

---

#### **Example 2**

```text
Input:
board = [[-1,-1],
         [-1,3]]

Output: 1
```

---

#### **Edge Case**

```text
Input:
board = [[-1,-1,-1],
         [-1,-1,-1],
         [-1,-1,-1]]

Output: depends on dice rolls (BFS handles it)
```

---

### **4. Intuition & pattern recognition**

🔑 Signals:

* "minimum moves"
* "dice (1–6)"
* "jumps (snakes/ladders)"

👉 Think:

> **Graph + BFS**

---

💡 Key idea:

* Each number = node
* Edges = possible dice moves (1–6)
* Snake/Ladder = forced jump

👉 We want:

> **Shortest path from 1 → n²**

---

### **5. Simpler version**

#### **Simpler problems**

* Minimum Knight Moves
  → BFS with movement options

* Shortest Path in Binary Matrix
  → BFS shortest path

* Jump Game III
  → graph traversal with jumps

---

#### **Build-up thinking**

| Step           | Concept              |
| -------------- | -------------------- |
| Linear board   | simple BFS           |
| Add dice moves | multiple edges       |
| Add jumps      | override destination |
| Final problem  | BFS with mapping     |

---

### **6. Brute force**

👉 Try all dice sequences (DFS)

* Explore all paths
* Track minimum moves

❌ Problem:

* Exponential explosion

**Time:** O(6^n)
**Space:** recursion stack

---

### **7. Optimal solution (BFS)**

---

### **Key helper: number → (row, col)**

Because of zig-zag pattern.

```python
def get_position(num, n):
    r = (num - 1) // n
    c = (num - 1) % n
    
    if r % 2 == 1:
        c = n - 1 - c
        
    return n - 1 - r, c
```

---

### **Main BFS**

```python
from collections import deque

def snakesAndLadders(board):
    n = len(board)
    
    queue = deque([(1, 0)])  # (cell, moves)
    visited = set([1])
    
    while queue:
        curr, moves = queue.popleft()
        
        if curr == n * n:
            return moves
        
        for i in range(1, 7):  # dice
            next_cell = curr + i
            if next_cell > n * n:
                continue
            
            r, c = get_position(next_cell, n)
            
            # if snake/ladder exists
            if board[r][c] != -1:
                next_cell = board[r][c]
            
            if next_cell not in visited:
                visited.add(next_cell)
                queue.append((next_cell, moves + 1))
    
    return -1
```

---

### **Complexity**

* **Time:** O(n²)
* **Space:** O(n²)

---

### **8. Step-by-step trace**

Board:

```text
[[-1,-1,-1],
 [-1, 9, 8],
 [-1,-1,-1]]
```

---

#### Step 1:

```text
Queue = [(1,0)]
```

---

#### Step 2:

```text
From 1:
Try dice → 2,3,4,5,6,7

At 2 → ladder → 9
```

Queue:

```text
[(9,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
```

---

#### Step 3:

```text
Pop (9,1) → reached end
```

👉 Return `1`

---

### **9. Related problems**

* Minimum Knight Moves
  → BFS with fixed moves

* Open the Lock
  → BFS with transitions

* Jump Game III
  → BFS with jumps

* Shortest Path Visiting All Nodes
  → BFS + state compression

* Word Ladder
  → BFS shortest transformation

---

### **Interview takeaway**

👉 Whenever:

* "minimum moves"
* "dice / transitions"
* "state jumps"

💡 Say:

> **“This is BFS on implicit graph (state = cell)”**

---

### **🔥 Key insight to say in interview**

> “Even though it looks like a board game, it's just a shortest path problem where each cell is a node and dice rolls define edges.”

---

If you want, next I can give you a **universal “state BFS template”** (covers this, word ladder, open lock, etc.) — very powerful for interviews.
