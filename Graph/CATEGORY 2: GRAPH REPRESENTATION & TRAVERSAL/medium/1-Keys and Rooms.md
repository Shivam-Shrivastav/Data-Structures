## 🧩 **LeetCode: Keys and Rooms (Graph / DFS-BFS Reachability)**

---

## 1. **Problem statement with example**

You are given `n` rooms labeled `0 → n-1`.

* Each room contains **keys to other rooms**
* You start in **room 0**
* Each key is an index of another room

👉 Return **true if you can visit all rooms**, else false.

---

### Constraints

* `1 <= rooms.length <= 1000`
* `0 <= rooms[i].length <= 1000`
* Total keys ≤ 3000

---

## 2. **Diagram**

### Example:

```text
Room 0 → [1,3]
Room 1 → [3,0,1]
Room 2 → [2]
Room 3 → [0]
```

Graph view:

```text
0 → 1 → 3
↓         ↑
3 --------
 
2 → 2 (isolated)
```

👉 Room `2` is unreachable

---

## 3. **Example I/O**

### Example 1 (All reachable)

```text
Input:
rooms = [[1],[2],[3],[]]

Output: true
```

👉 0 → 1 → 2 → 3

---

### Example 2 (Not reachable)

```text
Input:
rooms = [[1,3],[3,0,1],[2],[0]]

Output: false
```

👉 Room `2` never reached

---

## 4. **Intuition & pattern recognition**

### 🔍 Signals:

* Rooms = nodes
* Keys = directed edges
* Start from node `0`

👉 Classic **graph reachability**

---

### 💡 Core idea:

👉 Traverse graph from node `0` and check if all nodes are visited

---

### 🧠 Interview thinking:

> "This is just DFS/BFS — can I reach all nodes starting from 0?"

---

## 5. **Simpler version**

### Simplest thinking:

👉 From a node, visit all reachable nodes

---

### Related base problem:

👉 **Find if Path Exists in Graph**

* There: check path between two nodes
* Here: check reachability of **all nodes**

---

### Transition:

```text
Check 1 path → Check full coverage
```

---

## 6. **Brute force**

### Idea:

* Try all possible ways to open rooms

### Complexity:

* Exponential ❌
* Not needed

---

## 7. **Optimal solution**

---

### ✅ Approach 1: DFS

```python
def canVisitAllRooms(rooms):
    visited = set()

    def dfs(room):
        visited.add(room)

        for key in rooms[room]:
            if key not in visited:
                dfs(key)

    dfs(0)
    return len(visited) == len(rooms)
```

---

### ✅ Approach 2: BFS

```python
from collections import deque

def canVisitAllRooms(rooms):
    visited = set([0])
    queue = deque([0])

    while queue:
        room = queue.popleft()

        for key in rooms[room]:
            if key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(rooms)
```

---

### Complexity:

* Time: **O(n + total_keys)**
* Space: **O(n)**

---

## 8. **Step-by-step trace (DFS)**

### Input:

```text
rooms = [[1],[2],[3],[]]
```

---

### Step 1:

```text
Start at room 0
visited = {0}
```

---

### Step 2:

```text
Go to room 1
visited = {0,1}
```

---

### Step 3:

```text
Go to room 2
visited = {0,1,2}
```

---

### Step 4:

```text
Go to room 3
visited = {0,1,2,3}
```

---

### Final:

```text
All rooms visited → True
```

---

## 9. **Related problems**

1. **Find if Path Exists in Graph**
   → Check reachability between two nodes

2. **Number of Provinces**
   → Count connected components

3. **Clone Graph**
   → Graph traversal

4. **Course Schedule**
   → Directed graph dependency

5. **All Paths From Source to Target**
   → Explore all paths

---

## ⚡ Final takeaway

👉 This is a **pure reachability problem**

### 🔥 Core pattern:

```text
Start from node 0
→ Traverse graph
→ Check if all nodes visited
```

---

### 🚀 Interview one-liner:

> "I’ll run DFS/BFS from room 0 and check if all rooms are reachable."

---

If you want, next I can:

* Show **how this becomes tricky (cycle + revisiting traps)**
* Or give a **graph pattern decision tree (super useful in interviews)**
