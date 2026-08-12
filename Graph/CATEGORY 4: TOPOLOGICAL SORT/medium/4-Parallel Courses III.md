## 🧠 Parallel Courses III (LeetCode 2050)

---

## 1. **Problem Statement with Example**

You are given:

* `n` courses labeled `1 → n`
* `relations[i] = [prev, next]` → you must complete `prev` before `next`
* `time[i]` → time required to complete course `i`

👉 You can take **multiple courses in parallel** (if prerequisites are done)

### Goal:

Return the **minimum time required to complete all courses**

---

### ✅ Key constraint:

* Graph is a **DAG (Directed Acyclic Graph)**

---

## 2. **Diagram (Dependency Graph + Time Flow)**

```text
Example:

relations = [[1,3],[2,3]]
time = [3,2,5]

Graph:

   1 (3)
     \
      → 3 (5)
     /
   2 (2)

Execution:

- Course 1 finishes at time 3
- Course 2 finishes at time 2
- Course 3 can start only after max(3,2) = 3
- So finish time = 3 + 5 = 8
```

---

## 3. **Example I/O**

### Example 1:

```
Input:
n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]

Output:
8
```

Explanation:

* 1 → finishes at 3
* 2 → finishes at 2
* 3 starts at max(3,2)=3 → ends at 8

---

### Example 2 (Edge Case):

```
Input:
n = 2
relations = []
time = [5,7]

Output:
7
```

Explanation:

* No dependencies ⇒ run in parallel
* Max time = 7

---

## 4. **Intuition & Pattern Recognition**

### 🔥 Signals:

* Dependencies (DAG)
* Parallel execution
* Need **minimum total time**

👉 This screams:
➡️ **Topological Sort + DP (Longest Path in DAG)**

---

### 💡 Key Insight:

* Each course depends on multiple parents
* It can only start after **all prerequisites are done**

👉 So:

```
finish_time[node] = max(finish_time[prev]) + time[node]
```

👉 We take **max**, not sum
Because courses run in parallel

---

### 🧠 Interview Thought:

> “This is not shortest path — it’s longest path in a DAG (critical path problem)”

---

## 5. **Simpler Version**

### Step 1: No dependencies

* Answer = max(time)

---

### Step 2: Linear chain

```
1 → 2 → 3
```

* Answer = sum of times

---

### Step 3: Tree/DAG

* Multiple parents
* Need max of incoming paths

---

### Related simpler problems:

1. **Course Schedule**
   → Only checks if possible

2. **Course Schedule II**
   → Gives ordering

3. **Parallel Courses**
   → Counts semesters (levels)

---

### Transition:

| Problem            | Difference               |
| ------------------ | ------------------------ |
| Course Schedule II | Just ordering            |
| Parallel Courses   | Levels (BFS layers)      |
| **This**           | Weighted DAG → DP needed |

---

## 6. **Brute Force**

### Idea:

* Try all possible orders (topo orders)
* Compute total time

❌ Exponential → infeasible

---

### Slightly better:

* DFS from each node to compute max path

### Complexity:

* Time: **O(n²)** (recomputing paths)
* Space: O(n)

---

## 7. **Optimal Solution (Topo + DP)**

### 🚀 Idea:

* Use **Kahn’s Algorithm (BFS Topo)**
* Maintain `finish_time[i]`

---

### Algorithm:

1. Build graph + indegree
2. Push nodes with indegree 0
3. Initialize:

   ```
   finish_time[i] = time[i]
   ```
4. For each node:

   ```
   for neighbor:
       finish_time[nei] = max(finish_time[nei],
                              finish_time[node] + time[nei])
   ```

---

### Code:

```python
def minimumTime(n, relations, time):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    # Build graph
    for u, v in relations:
        graph[u].append(v)
        indegree[v] += 1

    # Queue for topo sort
    q = deque()

    # DP array: finish time
    finish_time = [0] * (n + 1)

    # Initialize
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            finish_time[i] = time[i - 1]

    # BFS
    while q:
        node = q.popleft()

        for nei in graph[node]:
            # Update max path
            finish_time[nei] = max(
                finish_time[nei],
                finish_time[node] + time[nei - 1]
            )

            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return max(finish_time)
```

---

### Complexity:

* Time: **O(n + edges)**
* Space: O(n + edges)

---

## 8. **Step-by-Step Trace**

### Input:

```
n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]
```

---

### Initialization:

```
indegree = [0,0,0,2]
finish_time = [0,3,2,0]
queue = [1,2]
```

---

### Step 1:

* Pop 1

```
update 3:
finish_time[3] = max(0, 3 + 5) = 8
indegree[3] = 1
```

---

### Step 2:

* Pop 2

```
update 3:
finish_time[3] = max(8, 2 + 5) = 8
indegree[3] = 0 → push 3
```

---

### Step 3:

* Pop 3 → done

---

### Final:

```
finish_time = [0,3,2,8]
Answer = 8
```

---

## 9. **Related Problems**

1. **Course Schedule II**
   → Base topo sort problem

2. **Parallel Courses**
   → Counts levels instead of weighted time

3. **Longest Increasing Path in a Matrix**
   → Same idea: longest path in DAG

4. **Minimum Height Trees**
   → Different use of topo (reverse thinking)

5. **Alien Dictionary**
   → Graph ordering problem

---

## ⚡ Final Interview Takeaway

* DAG + dependencies + time ⇒ **Longest Path Problem**
* Use:

  * Topo sort (Kahn’s BFS)
  * DP on nodes

👉 Formula:

```
finish[child] = max(finish[child], finish[parent] + time[child])
```

---

If you want next level:
👉 DFS + memo (clean alternative)
👉 How to detect this vs Dijkstra vs BFS instantly (very important pattern distinction)
