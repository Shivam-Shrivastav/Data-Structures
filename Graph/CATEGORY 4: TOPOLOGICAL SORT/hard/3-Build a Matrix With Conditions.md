## **Build a Matrix With Conditions (LeetCode)**

---

## 1. **Problem statement with example**

You are given:

* An integer `k` → numbers from `1` to `k`
* Two lists:

  * `rowConditions`: `[a, b]` → `a` must be **above** `b`
  * `colConditions`: `[a, b]` → `a` must be **left of** `b`

### Goal:

Build a `k x k` matrix such that:

* Each number `1..k` appears **exactly once**
* All row & column constraints are satisfied

👉 If impossible → return `[]`

---

### Example:

```id="n1x9oj"
k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]
```

---

## 2. **Diagram**

### Row constraints (Top → Bottom):

```id="07q5c3"
1 → 2
3 → 2
```

### Column constraints (Left → Right):

```id="3ho5eq"
3 → 2 → 1
```

---

### Final layout idea:

```id="f7d9n3"
Row order:  [1, 3, 2]
Col order:  [3, 2, 1]

Matrix:

[ 0  0  1 ]
[ 3  0  0 ]
[ 0  2  0 ]
```

---

## 3. **Example I/O**

### Example 1 (Valid)

```id="j1v0fy"
Input:
k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]

Output:
Any valid matrix
```

✔ Multiple answers possible

---

### Example 2 (Cycle → invalid)

```id="y6cr7x"
k = 3
rowConditions = [[1,2],[2,1]]
colConditions = []

Output:
[]
```

❌ Cycle in row constraints → impossible

---

## 4. **Intuition & pattern recognition**

### 🔑 Signals:

* Relative ordering constraints
* "above/below", "left/right"
* Need to place elements respecting order

👉 This is:

> **Two independent Topological Sorts**

---

### Core idea:

* One topo sort for **rows**
* One topo sort for **columns**

Then:

```
position[value] = (row_index, col_index)
```

---

### Why it works:

* Row constraints = vertical ordering
* Column constraints = horizontal ordering
* Independent → combine positions

---

## 5. **Simpler version**

### Simplest:

👉 "Return topo ordering of nodes"

---

### Intermediate:

👉 "Course Schedule II"

* Only 1 ordering

---

### This problem:

👉 Two dimensions:

```id="gnf3g5"
Row order + Column order → 2D placement
```

---

### Thinking ladder:

```id="qjpyxm"
Topo sort (1D)
→ Two topo sorts
→ Map to matrix
```

---

## 6. **Brute force**

### Idea:

* Try all permutations of `1..k`
* Place in matrix and check constraints

### Complexity:

* Time: **O(k! × k²)**

❌ Impossible

---

## 7. **Optimal solution (Topo + Mapping)**

---

### Steps:

1. Build topo order for rows
2. Build topo order for columns
3. If either fails → return []
4. Map:

   ```
   value → (row_index, col_index)
   ```
5. Fill matrix

---

### Code (Python)

```python id="3y3ev4"
from collections import defaultdict, deque

def topo_sort(k, conditions):
    graph = defaultdict(list)
    indegree = [0] * (k + 1)
    
    for u, v in conditions:
        graph[u].append(v)
        indegree[v] += 1
    
    q = deque()
    for i in range(1, k + 1):
        if indegree[i] == 0:
            q.append(i)
    
    order = []
    
    while q:
        node = q.popleft()
        order.append(node)
        
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    
    return order if len(order) == k else []


def buildMatrix(k, rowConditions, colConditions):
    row_order = topo_sort(k, rowConditions)
    col_order = topo_sort(k, colConditions)
    
    if not row_order or not col_order:
        return []
    
    # Map value → column index
    col_pos = {val: i for i, val in enumerate(col_order)}
    
    # Initialize matrix
    matrix = [[0] * k for _ in range(k)]
    
    # Place elements
    for i, val in enumerate(row_order):
        j = col_pos[val]
        matrix[i][j] = val
    
    return matrix
```

---

### Complexity:

* Time: **O(k + edges)**
* Space: **O(k + edges)**

---

## 8. **Step-by-step trace**

### Input:

```id="8v82q9"
k = 3
row = [[1,2],[3,2]]
col = [[2,1],[3,2]]
```

---

### Row topo:

```id="cc5h2c"
Order = [1, 3, 2]
```

---

### Col topo:

```id="v9rt21"
Order = [3, 2, 1]
```

---

### Mapping:

```id="r98u1y"
col_pos:
3 → 0
2 → 1
1 → 2
```

---

### Fill matrix:

| Row idx | Value | Col idx | Placement        |
| ------- | ----- | ------- | ---------------- |
| 0       | 1     | 2       | matrix[0][2] = 1 |
| 1       | 3     | 0       | matrix[1][0] = 3 |
| 2       | 2     | 1       | matrix[2][1] = 2 |

---

### Final:

```id="hyhw71"
[0,0,1]
[3,0,0]
[0,2,0]
```

---

## 9. **Related problems**

1. **Course Schedule II**
   → Basic topo ordering

2. **Alien Dictionary**
   → Build graph + topo

3. **Parallel Courses III**
   → Order + accumulation

4. **Sequence Reconstruction**
   → Validate ordering uniqueness

5. **Largest Color Value in a Directed Graph**
   → Advanced topo with states

---

## 🚀 Interview takeaway

If you see:

* Relative ordering constraints
* 2D placement
* Independent dimensions

👉 Think:

> **"Topo sort each dimension separately, then combine positions"**

---

If you want, I can also show:

* How to detect **multiple valid matrices**
* DFS topo version
* Common pitfalls (very important for interviews)
