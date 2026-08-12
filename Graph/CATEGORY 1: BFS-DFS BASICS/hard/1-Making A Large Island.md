## 🧩 **LeetCode: Making A Large Island (Graph / DFS + Hashing)**

---

## 1. **Problem statement with example**

You are given an `n x n` binary grid:

* `1` → land
* `0` → water

You can **change at most one `0` to `1`**.

👉 Return the **size of the largest island** possible after this change.

An island is a group of connected `1`s (4-directionally: up/down/left/right).

### Constraints

* `1 <= n <= 500`
* Time must be close to **O(n²)** → brute force DFS for each `0` will TLE.

---

## 2. **Diagram**

### Before flip:

```
1 0
0 1
```

Two separate islands of size 1.

### After flipping (0 → 1):

```
1 1
0 1
```

Now connected → size = 3

---

## 3. **Example I/O**

### Example 1 (Typical)

```
Input:
grid = [
 [1,0],
 [0,1]
]

Output: 3
```

👉 Flip any `0` → connects islands → max size = 3

---

### Example 2 (Edge case: all 1s)

```
Input:
grid = [
 [1,1],
 [1,1]
]

Output: 4
```

👉 No need to flip → already largest island

---

## 4. **Intuition & pattern recognition**

### 🔍 Pattern signals:

* Grid + connected components → **DFS/BFS**
* "Change one cell" → try all possibilities
* But brute force = **too slow**

---

### 💡 Key idea:

1. First **label each island with a unique ID**
2. Store its **area in a hashmap**
3. For every `0`, check its **neighbor islands**
4. Merge their areas (avoid duplicates!)

---

### 🧠 Interview thought:

> "Instead of recomputing island size every time, precompute all island sizes once and reuse."

---

## 5. **Simpler version**

### Simpler problem:

👉 Count size of each island (like **Max Area of Island**)

### Difference:

* That problem → just find max existing island
* This problem → **merge islands via one flip**

---

### Key jump:

```
Max Area of Island → static
Making Large Island → dynamic merge
```

---

## 6. **Brute force**

### Idea:

* For every `0`:

  * Flip it
  * Run DFS to compute island size
  * Restore

### Complexity:

* Time: **O(n⁴)** ❌ (TLE)
* Space: O(n²)

---

## 7. **Optimal solution (DFS + Labeling)**

### Steps:

1. Label islands with IDs: 2, 3, 4...
2. Store area in map: `{id → size}`
3. For each `0`:

   * Check neighbors
   * Sum unique island sizes + 1
4. Return max

---

### ✅ Code (Python)

```python
def largestIsland(grid):
    n = len(grid)
    island_id = 2
    area_map = {}

    # DFS to mark island and calculate area
    def dfs(r, c, id):
        if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1:
            return 0
        
        grid[r][c] = id
        area = 1
        
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            area += dfs(r + dr, c + dc, id)
        
        return area

    # Step 1: Label islands
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                area_map[island_id] = dfs(r, c, island_id)
                island_id += 1

    max_area = max(area_map.values(), default=0)

    # Step 2: Try flipping each 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                seen = set()
                new_area = 1

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n:
                        id = grid[nr][nc]
                        if id > 1 and id not in seen:
                            new_area += area_map[id]
                            seen.add(id)

                max_area = max(max_area, new_area)

    return max_area if max_area != 0 else n * n
```

---

### Complexity:

* Time: **O(n²)** ✅
* Space: **O(n²)**

---

## 8. **Step-by-step trace**

### Input:

```
1 0
0 1
```

---

### Step 1: Label islands

```
2 0
0 3
```

area_map:

```
2 → 1
3 → 1
```

---

### Step 2: Try flipping (0,1)

Neighbors:

* Left → 2
* Down → 3

```
new_area = 1 + 1 + 1 = 3
```

---

### Step 3: Try flipping (1,0)

Same result → 3

---

### Final answer:

```
3
```

---

## 9. **Related problems**

1. **Max Area of Island**
   → Base version: find largest island without modification

2. **Number of Islands**
   → Counting components instead of measuring size

3. **Surrounded Regions**
   → DFS marking + region transformation

4. **Island Perimeter**
   → Different property of islands

5. **Bricks Falling When Hit**
   → Advanced version using union-find + reverse thinking

---

## ⚡ Final takeaway

👉 Core trick:

> **Precompute island sizes + reuse via IDs**

👉 If you ever see:

* "flip one cell"
* "merge components"
* "maximize area"

→ Think:

```
Label + HashMap + Neighbor Merge
```

---

If you want, I can also give the **Union-Find version** (even more interview impressive).
