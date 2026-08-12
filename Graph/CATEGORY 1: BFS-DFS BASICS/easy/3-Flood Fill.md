## 733. Flood Fill
**Category:** **GRAPH / DFS / BFS / MATRIX TRAVERSAL**

**Problem:** You are given an image represented by an `m x n` grid of integers, a starting pixel `(sr, sc)`, and a new color `newColor`. Perform a flood fill starting from `(sr, sc)`, changing all connected pixels with the same color as the starting pixel to `newColor`. Return the modified image.

**Example:**
```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: Starting from (1,1), all connected 1's change to 2
```

```
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 0
Output: [[0,0,0],[0,0,0]]
Explanation: New color same as old, no changes
```

---

### **Relation to Graph Traversal Problems**
**Similar to:** **Number of Islands (200)** but **color fill** instead of counting
**How it's different:**
1. **Number of Islands:** Count connected components of '1's
2. **Flood Fill:** Change color of connected region of same color
3. **Key Insight:** DFS/BFS from starting pixel, change all reachable cells with original color

**Key Insight:** 
- Get original color of starting pixel
- If original color == newColor, return image immediately
- DFS/BFS to all 4-directionally adjacent cells with same original color
- Change them to newColor

---

### 1. DFS Recursive Solution
```python
def floodFill(image, sr, sc, newColor):
    m, n = len(image), len(image[0])
    original_color = image[sr][sc]
    
    # If already same color, no change needed
    if original_color == newColor:
        return image
    
    def dfs(i, j):
        # Check boundaries and if color matches original
        if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != original_color:
            return
        
        # Change color
        image[i][j] = newColor
        
        # Explore 4 directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    dfs(sr, sc)
    return image
```
**TC:** O(m × n) worst case | **SC:** O(m × n) recursion stack

---

### 2. DFS with Visited Set (No modification needed)
```python
def floodFill(image, sr, sc, newColor):
    m, n = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == newColor:
        return image
    
    visited = [[False] * n for _ in range(m)]
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or image[i][j] != original_color:
            return
        
        visited[i][j] = True
        image[i][j] = newColor
        
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    dfs(sr, sc)
    return image
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 3. BFS Solution (Queue)
```python
from collections import deque

def floodFill(image, sr, sc, newColor):
    m, n = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == newColor:
        return image
    
    queue = deque([(sr, sc)])
    image[sr][sc] = newColor
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while queue:
        i, j = queue.popleft()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and image[ni][nj] == original_color:
                image[ni][nj] = newColor
                queue.append((ni, nj))
    
    return image
```
**TC:** O(m × n) | **SC:** O(m × n) worst case for queue

---

### 4. Iterative DFS (Using Stack)
```python
def floodFill(image, sr, sc, newColor):
    m, n = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == newColor:
        return image
    
    stack = [(sr, sc)]
    image[sr][sc] = newColor
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while stack:
        i, j = stack.pop()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and image[ni][nj] == original_color:
                image[ni][nj] = newColor
                stack.append((ni, nj))
    
    return image
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 5. Using sys.setrecursionlimit (For very deep recursion)
```python
import sys
sys.setrecursionlimit(10**6)

def floodFill(image, sr, sc, newColor):
    m, n = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == newColor:
        return image
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != original_color:
            return
        
        image[i][j] = newColor
        
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    dfs(sr, sc)
    return image
```

---

**Key Insight:**
- Flood fill is essentially connected component traversal
- Only change cells with same original color as starting cell
- If newColor == originalColor, no work needed
- 4-directional connectivity (up, down, left, right)

**Example Walkthrough (DFS):**
```
image = [
  [1,1,1],
  [1,1,0],
  [1,0,1]
]
sr=1, sc=1, newColor=2, original_color=1

Start dfs(1,1):
  image[1][1] = 2
  dfs(2,1): image[2][1]=1? Actually image[2][1]=0 (different) → skip
  dfs(0,1): image[0][1]=1 → change to 2, dfs(0,0), dfs(0,2), dfs(1,1)...
  dfs(1,2): image[1][2]=0 → skip
  dfs(1,0): image[1][0]=1 → change to 2, continue...

After all:
  [2,2,2]
  [2,2,0]
  [2,0,1]
```

**Visual Process:**
```
Step 1: Original
1 1 1
1 1 0
1 0 1

Step 2: Start at (1,1) change to 2
1 1 1
1 2 0
1 0 1

Step 3: Spread to (0,1),(1,0),(2,1?) no (2,1)=0
2 2 2
2 2 0
2 0 1
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**DFS Recursive** | O(m×n) | O(m×n) | Simple, intuitive | Stack overflow for large grids |
**BFS** | O(m×n) | O(m×n) | No recursion, level order | Slightly more code |
**Iterative DFS** | O(m×n) | O(m×n) | No recursion | Uses explicit stack |

**Graph Traversal Family:**

| Problem | Key Difference |
|---------|---------------|
**733. Flood Fill** | Change color of connected region |
**200. Number of Islands** | Count connected components |
**695. Max Area of Island** | Find largest component |
**130. Surrounded Regions** | Capture border-connected regions |
**417. Pacific Atlantic Water Flow** | Multi-source BFS/DFS |

**Edge Cases:**
- Starting pixel already newColor → return image unchanged
- Single cell image → change if different color
- Grid with all same color → entire grid changes
- Starting pixel at corner → still works

**Why Check original_color == newColor:**
- Without this, DFS would run infinitely
- Because we change color but condition checks original_color
- Actually with correct condition, it would still work (cells become newColor, not original)
- But it's an optimization to avoid unnecessary traversal

**When to Use DFS vs BFS:**
- **DFS:** Simpler code, good for smaller grids
- **BFS:** Better for large grids, no stack overflow risk
- **Both:** Same time complexity, choose based on preference

**Common Pitfalls:**
- Forgetting to check boundaries
- Not storing original color before modification
- Using 8-directional connectivity instead of 4
- Not handling the case where newColor == originalColor