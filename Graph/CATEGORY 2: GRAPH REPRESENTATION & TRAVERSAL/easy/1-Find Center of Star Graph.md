## 🧩 **LeetCode: Find Center of Star Graph (Graph / Degree Observation)**

---

## 1. **Problem statement with example**

You are given a graph with `n` nodes labeled `1` to `n`.

* The graph is a **star graph**:

  * One **center node**
  * All other nodes are connected **only to the center**

👉 Given `edges`, return the **center node**.

---

### Constraints

* `3 <= n <= 10^5`
* `edges.length = n - 1`
* Graph is guaranteed to be a **valid star graph**

---

## 2. **Diagram**

### Star Graph Structure

```text
        2
        |
3 —— 1 —— 4
        |
        5
```

👉 Node `1` is the center (connected to all)

---

## 3. **Example I/O**

### Example 1 (Typical)

```text
Input:
edges = [[1,2],[2,3],[4,2]]

Output: 2
```

👉 Node `2` appears in every edge → center

---

### Example 2 (Edge case: minimal size)

```text
Input:
edges = [[1,2],[5,1],[1,3],[1,4]]

Output: 1
```

👉 Center appears in all edges

---

## 4. **Intuition & pattern recognition**

### 🔍 Pattern signals:

* "Star graph" → special structure
* One node connected to all others

---

### 💡 Key observation:

👉 The **center node appears in every edge**

Even better:

👉 The center must be **common in the first two edges**

---

### 🧠 Interview thinking:

> "In a star graph, the center is the only node shared across all edges. So just find intersection of first two edges."

---

## 5. **Simpler version**

### Simplest idea:

👉 Count degree of each node

* Node with degree `n-1` → center

---

### Related simpler problem:

👉 **Find the Town Judge**

* Judge has:

  * indegree = n-1
  * outdegree = 0

---

### Difference:

| Town Judge       | Star Graph    |
| ---------------- | ------------- |
| Directed         | Undirected    |
| Use degree array | No need       |
| O(n)             | O(1) possible |

---

### Key jump:

```text
Instead of counting,
use edge intersection
```

---

## 6. **Brute force**

### Idea:

* Count degree of each node

```python
degree[node] += 1
```

* Return node with max degree

---

### Complexity:

* Time: **O(n)**
* Space: **O(n)**

---

## 7. **Optimal solution (O(1))**

### 🔥 Trick:

Only check first two edges!

---

### ✅ Code (Python)

```python
def findCenter(edges):
    a, b = edges[0]
    c, d = edges[1]

    # Center must be common in both edges
    if a == c or a == d:
        return a
    else:
        return b
```

---

### Complexity:

* Time: **O(1)** ✅
* Space: **O(1)**

---

## 8. **Step-by-step trace**

### Input:

```text
edges = [[1,2],[2,3],[4,2]]
```

---

### Step 1:

```text
Edge1 → (1,2)
Edge2 → (2,3)
```

---

### Step 2:

```text
Common node = 2
```

---

### Final:

```text
Answer = 2
```

---

## 9. **Related problems**

1. **Find the Town Judge**
   → Degree-based identification

2. **Number of Connected Components in an Undirected Graph**
   → Graph structure basics

3. **Graph Valid Tree**
   → Tree properties

4. **Minimum Degree of a Connected Trio in a Graph**
   → Degree-based reasoning

---

## ⚡ Final takeaway

👉 This is a **pattern recognition problem**, not traversal.

### 🔥 Core trick:

```text
Center = common node in first 2 edges
```

---

### 🚀 Interview one-liner:

> "Since every edge connects to the center, the center must be the common node between any two edges."

---

If you want, I can show:

* Trick to detect **star graph validity**
* OR how this pattern appears in tricky variations (interview traps)
