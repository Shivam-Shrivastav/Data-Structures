## 🧩 **LeetCode: Escape a Large Maze (Graph / BFS + Geometry Insight)**

---

## 1. **Problem statement with example**

You are given:

* A **1,000,000 x 1,000,000 grid**
* Some cells are **blocked**
* A **source** and a **target**

You can move **up, down, left, right**.

👉 Return **true if there exists a path** from source to target, else false.

---

### ⚠️ Constraints (critical for approach)

* `0 <= blocked.length <= 200`
* Grid is HUGE → cannot explore fully
* Coordinates range: `[0, 10^6)`

---

## 2. **Diagram**

### Intuition: Blocked cells can form a cage

```text
   X X X
   X S X
   X   X
     T

S = source trapped
T = outside
```

👉 If blocked cells surround source → cannot escape

---

## 3. **Example I/O**

### Example 1 (Trapped)

```text
Input:
blocked = [[0,1],[1,0]]
source = [0,0]
target = [0,2]

Output: false
```

👉 Source is enclosed

---

### Example 2 (Free space)

```text
Input:
blocked = []
source = [0,0]
target = [999999,999999]

Output: true
```

👉 Nothing blocks movement

---

## 4. **Intuition & pattern recognition**

### 🔍 Signals:

* Huge grid → **can't BFS fully**
* Small blocked set → **bounded obstruction**

---

### 💡 Core insight (this is the trick)

Blocked cells can form **only a limited enclosure**

Max enclosed area:

```text
n * (n - 1) / 2
```

Where `n = len(blocked)`

👉 Max ≈ 20,000 cells

---

### 🧠 Interview thinking:

> "If I can explore more than ~20k cells, then I’m definitely not trapped."

---

### 🔥 Strategy:

* Run BFS from source
* Stop early if:

  * reach target → ✅
  * visited > LIMIT → ✅ escaped enclosure

👉 Also run BFS from target (important!)

---

## 5. **Simpler version**

### Base problem:

👉 **Shortest Path in Binary Matrix**

* Standard BFS
* Explore entire grid

---

### Difference:

| Normal BFS   | This Problem      |
| ------------ | ----------------- |
| Explore all  | Early stop        |
| Small grid   | Huge grid         |
| Reach target | Prove not trapped |

---

### Key shift:

```text
Not finding path,
but proving escape possibility
```

---

## 6. **Brute force**

### Idea:

* BFS entire grid

### Complexity:

* Time: **O(10^12)** ❌ impossible
* Space: ❌ impossible

---

## 7. **Optimal solution (Bounded BFS)**

---

### ✅ Code (Python)

```python
def isEscapePossible(blocked, source, target):
    BLOCKED = set(map(tuple, blocked))
    LIMIT = len(blocked) * (len(blocked) - 1) // 2

    def bfs(start, end):
        visited = set()
        queue = [tuple(start)]
        visited.add(tuple(start))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            x, y = queue.pop(0)

            if [x, y] == end:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < 10**6 and 0 <= ny < 10**6:
                    if (nx, ny) not in BLOCKED and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

            # 🔥 Critical condition
            if len(visited) > LIMIT:
                return True  # escaped

        return False

    return bfs(source, target) and bfs(target, source)
```

---

### Complexity:

* Time: **O(B²)** (~40k max)
* Space: **O(B²)**

---

## 8. **Step-by-step trace**

### Input:

```text
blocked = [[0,1],[1,0]]
source = [0,0]
target = [0,2]
```

---

### Step 1: BFS from source

Visited:

```text
(0,0)
```

Neighbors:

* (0,1) ❌ blocked
* (1,0) ❌ blocked

👉 No expansion

---

### Step 2:

```text
visited size = 1 < LIMIT
→ stuck → return False
```

---

### Final:

```text
False
```

---

## 9. **Related problems**

1. **Number of Islands**
   → Basic grid traversal

2. **The Maze**
   → BFS with constraints

3. **Pacific Atlantic Water Flow**
   → Reachability reasoning

4. **Walls and Gates**
   → BFS propagation

5. **Making A Large Island**
   → Grid + component optimization

---

## ⚡ Final takeaway

👉 This problem is about **thinking, not traversal**

### 🔥 Core trick:

```text
Bounded BFS + early termination
```

---

### 🚀 Interview one-liner:

> "Since blocked cells are limited, they can only enclose a bounded region. If BFS exceeds that region, escape is guaranteed."

---

If you want, next I can break down:

* 👉 WHY `n(n-1)/2` (this is what most people fail to explain)
* 👉 Visual proof + intuition (super helpful for interviews)
