## **Minimum Moves to Move a Box to Target Location (LeetCode 1263)**

---

### **1. Problem statement with example**

You are given a grid where:

* `#` → wall
* `.` → empty
* `S` → player
* `B` → box
* `T` → target

👉 You can move the **player** in 4 directions.
👉 The player can **push the box** (not pull).
👉 A push happens when:

* player is adjacent to box
* moves into box → box moves forward

👉 Goal:

> Minimum number of **pushes** to move box to target

---

**Constraints:**

* Grid size ≤ 20 × 20
* Player moves are free
* Only **pushes count**

---

### **2. Diagram**

Example:

```text
######
#T...#
#..B.#
#..S.#
######
```

State representation:

```text
Player (S)
Box (B)
Target (T)
```

👉 Player must go **behind the box** to push:

```text
S → (behind B) → push → B moves
```

---

### **3. Example I/O**

#### **Example 1**

```text
Input:
grid = [["#","#","#","#","#","#"],
        ["#","T",".",".",".","#"],
        ["#",".","#","B",".","#"],
        ["#",".",".",".",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]]

Output: 3
```

---

#### **Edge Case**

```text
No path to push box → Output: -1
```

---

### **4. Intuition & pattern recognition**

🔑 Signals:

* "minimum pushes" (NOT steps)
* player + box interaction
* grid + constraints

---

👉 This is NOT simple BFS

💡 Key idea:

* Two types of movement:

  1. Player moves (free)
  2. Box moves (cost = 1)

---

👉 So we need:

> **0-1 BFS / BFS on states**

---

💡 State becomes:

```text
(player_row, player_col, box_row, box_col)
```

---

👉 Why tricky?

* Player must reach **correct side of box before pushing**
* So we need BFS inside BFS

---

### **5. Simpler version**

#### **Build intuition from:**

* Shortest Path in Binary Matrix
  → basic BFS

* Nearest Exit from Entrance in Maze
  → shortest path

* Shortest Path in Grid with Obstacles Elimination
  → BFS with extra state

---

#### **Build-up thinking**

| Step         | Concept               |
| ------------ | --------------------- |
| Grid BFS     | movement              |
| Add state    | track more variables  |
| Player + box | multi-agent state     |
| Final        | BFS on (player + box) |

---

👉 Key jump:

> From single position → **multi-entity state**

---

### **6. Brute force**

👉 Try all sequences:

* simulate player + box moves

❌ Impossible:

* huge branching
* repeated states

---

### **7. Optimal solution (0-1 BFS / BFS on pushes)**

---

### **Core idea**

* Outer BFS → counts pushes
* Inner BFS → checks if player can reach position to push

---

### **Code**

```python
from collections import deque

def minPushBox(grid):
    m, n = len(grid), len(grid[0])
    
    # find positions
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                player = (i, j)
            elif grid[i][j] == 'B':
                box = (i, j)
            elif grid[i][j] == 'T':
                target = (i, j)
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    def canReach(start, target_pos, box_pos):
        """Check if player can reach target_pos without crossing box"""
        queue = deque([start])
        visited = set([start])
        
        while queue:
            r, c = queue.popleft()
            if (r, c) == target_pos:
                return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    grid[nr][nc] != '#' and
                    (nr, nc) != box_pos and
                    (nr, nc) not in visited):
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return False
    
    # BFS on pushes
    queue = deque([(box, player, 0)])  # box_pos, player_pos, pushes
    visited = set([(box, player)])
    
    while queue:
        box_pos, player_pos, pushes = queue.popleft()
        
        if box_pos == target:
            return pushes
        
        br, bc = box_pos
        
        for dr, dc in directions:
            new_box = (br + dr, bc + dc)
            player_needed = (br - dr, bc - dc)
            
            # valid positions
            if not (0 <= new_box[0] < m and 0 <= new_box[1] < n):
                continue
            if not (0 <= player_needed[0] < m and 0 <= player_needed[1] < n):
                continue
            
            if grid[new_box[0]][new_box[1]] == '#':
                continue
            if grid[player_needed[0]][player_needed[1]] == '#':
                continue
            
            # check player reachability
            if canReach(player_pos, player_needed, box_pos):
                new_state = (new_box, box_pos)
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_box, box_pos, pushes + 1))
    
    return -1
```

---

### **Complexity**

* **Time:** O((m×n)²)
* **Space:** O(m×n)

---

### **8. Step-by-step trace (core idea)**

Initial:

```text
Player = S
Box = B
Pushes = 0
```

---

👉 Try all directions:

* Can player reach **behind box?**
* If yes → push

---

Example:

```text
Step 1:
Player moves behind box

Step 2:
Push box → pushes = 1

Step 3:
Repeat
```

---

### **9. Related problems**

* Sokoban
  → classic version of this problem

* Shortest Path in Grid with Obstacles Elimination
  → BFS with extra state

* Minimum Moves to Reach Target with Rotations
  → multi-state BFS

* Sliding Puzzle
  → BFS on configurations

* Open the Lock
  → BFS over states

---

### **🔥 Interview takeaway**

👉 If:

* multiple entities (player + box)
* movement constraints
* optimize pushes (not steps)

💡 Say:

> **“We need BFS on composite state + inner BFS for feasibility”**

---

### **💡 Golden insight**

> “The tricky part is separating player movement (free) from box pushes (cost), which leads to BFS over box states and DFS/BFS for player reachability.”

---

If you want, next I can give you a **MASTER template for multi-state BFS problems** (this + sliding puzzle + lock problems).
