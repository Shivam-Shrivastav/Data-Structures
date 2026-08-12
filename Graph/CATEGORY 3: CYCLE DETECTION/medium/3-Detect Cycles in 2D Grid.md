## 🧩 Detect Cycles in 2D Grid (LeetCode)

---

## 1. **Problem statement with example**

You are given a 2D grid of characters. You need to determine if there exists a **cycle** in the grid.

A **cycle** is defined as:

* A path of **4 or more cells**
* All cells have the **same character**
* You can move in **4 directions** (up, down, left, right)
* You **cannot revisit the immediate previous cell**, but revisiting any other visited cell forms a cycle

### Example:

```
Input:
grid = [
  ['a','a','a','a'],
  ['a','b','b','a'],
  ['a','b','b','a'],
  ['a','a','a','a']
]

Output: true
```

👉 There is a cycle of `'a'` forming a loop around the border.

### Constraints:

* 1 ≤ m, n ≤ 500
* Grid size can be large → O(m*n) needed
* Graph is implicit (grid-based)

---

## 2. **Diagram**

```
Grid:

a  a  a  a
a  b  b  a
a  b  b  a
a  a  a  a

Cycle path (a's):

(0,0) → (0,1) → (0,2) → (0,3)
  ↓                         ↓
(1,0)                   (1,3)
  ↓                         ↓
(2,0)                   (2,3)
  ↓                         ↓
(3,0) → (3,1) → (3,2) → (3,3)

Forms a loop ✅
```

---

## 3. **Example I/O**

### Example 1 (Typical)

```
Input:
grid = [
 ['a','a','a'],
 ['a','b','a'],
 ['a','a','a']
]

Output: true
```

✔ Outer `'a'` forms a cycle

---

### Example 2 (Edge case)

```
Input:
grid = [
 ['a','b'],
 ['c','d']
]

Output: false
```

❌ No cycle possible

---

## 4. **Intuition & pattern recognition**

### 🔑 Key signals:

* Grid → think **Graph**
* Same character constraint → **connected components**
* Cycle detection → classic graph problem

### 💡 Key idea:

This is **cycle detection in an undirected graph**

BUT:

* We must **ignore the parent node** (very important)
* Otherwise every edge looks like a cycle

### 🧠 Interview thought:

> "Grid + same value + cycle → DFS with parent tracking"

---

## 5. **Simpler version**

### Step 1: Basic version

* Detect cycle in **undirected graph**
  👉 Standard DFS with parent

### Step 2: Convert grid → graph

* Each cell = node
* Edges = adjacent same-value cells

### Step 3: Apply DFS cycle detection

---

### Related simpler problems:

* **Number of Provinces** → connected components
* **Find if Path Exists in Graph** → traversal
* **Cycle Detection in Graph (Undirected)** → exact base logic

👉 Difference here:

* Graph is **implicit**
* Need to check **same character constraint**

---

## 6. **Brute force**

### Idea:

* Try all paths from each cell
* Track visited path (not global)
* Check if revisit happens

### Complexity:

* Time: ❌ Exponential (bad)
* Space: ❌ High recursion stack

👉 Not feasible

---

## 7. **Optimal solution (DFS with parent tracking)**

### ✅ Key idea:

* Maintain `visited` matrix
* For each unvisited cell:

  * DFS
  * Pass `(parent_row, parent_col)`
* If you visit an already visited cell **not equal to parent → cycle**

---

### Code (Python)

```python
def containsCycle(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]

    def dfs(r, c, pr, pc):
        # mark current as visited
        visited[r][c] = True
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # boundary check
            if 0 <= nr < rows and 0 <= nc < cols:
                # same character constraint
                if grid[nr][nc] != grid[r][c]:
                    continue
                
                # if not visited → continue DFS
                if not visited[nr][nc]:
                    if dfs(nr, nc, r, c):
                        return True
                else:
                    # visited and not parent → cycle
                    if (nr, nc) != (pr, pc):
                        return True
        
        return False

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                if dfs(i, j, -1, -1):
                    return True
    
    return False
```

---

### Complexity:

* **Time:** O(m * n)
* **Space:** O(m * n)

---

## 8. **Step-by-step trace**

### Input:

```
grid = [
 ['a','a','a'],
 ['a','b','a'],
 ['a','a','a']
]
```

---

### Steps:

| Step | Cell          | Action                       | Visited | Cycle? |
| ---- | ------------- | ---------------------------- | ------- | ------ |
| 1    | (0,0)         | Start DFS                    | ✔       | -      |
| 2    | (0,1)         | Move right                   | ✔       | -      |
| 3    | (0,2)         | Move right                   | ✔       | -      |
| 4    | (1,2)         | Move down                    | ✔       | -      |
| 5    | (2,2)         | Move down                    | ✔       | -      |
| 6    | (2,1)         | Move left                    | ✔       | -      |
| 7    | (2,0)         | Move left                    | ✔       | -      |
| 8    | (1,0)         | Move up                      | ✔       | -      |
| 9    | Back to (0,0) | Already visited & not parent | ✔       | ✅ YES  |

---

## 9. **Related problems**

1. **Number of Provinces**
   → Same DFS idea without cycle detection

2. **Find if Path Exists in Graph**
   → Basic traversal, no cycle logic

3. **Course Schedule**
   → Cycle detection in **directed graph**

4. **Graph Valid Tree**
   → Check if no cycles exist

5. **Redundant Connection**
   → Detect edge causing cycle (Union-Find)

---

## 🔥 Final Interview Punchline

> “This is cycle detection in an undirected graph represented as a grid. The key trick is tracking the parent to avoid false cycle detection.”

---

If you want, I can also give:

* 🔁 BFS version
* ⚡ Union-Find approach (very powerful for this)
