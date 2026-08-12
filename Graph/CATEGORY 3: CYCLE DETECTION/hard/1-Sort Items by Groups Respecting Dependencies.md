## 🧩 Sort Items by Groups Respecting Dependencies (LeetCode 1203)

---

## 1. **Problem statement with example**

You are given:

* `n` items (0 → n-1)
* `m` groups (0 → m-1)
* `group[i]` → group of item `i` (`-1` means no group)
* `beforeItems[i]` → list of items that must come **before item i**

👉 Goal: Return a valid ordering of items such that:

1. All dependencies are satisfied
2. Items of the **same group are contiguous**

If not possible → return `[]`

---

### Example:

```
Input:
n = 8, m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]

Output:
[6,3,4,1,5,2,0,7]
```

---

## 2. **Diagram**

### Step 1: Assign groups to -1 items

```
Original group:
[-1,-1,1,0,0,1,0,-1]

Assign new groups:
[2,3,1,0,0,1,0,4]
```

---

### Step 2: Two-level graph

```
Item graph:
6 → 1
5 → 2
6 → 3 → 4

Group graph:
group(6)=0 → group(1)=3
group(5)=1 → group(2)=1 (ignored same group)
```

👉 Two DAGs:

* Item-level DAG
* Group-level DAG

---

## 3. **Example I/O**

### Example 1 (Typical)

```
Input:
n = 3, m = 1
group = [0,0,0]
beforeItems = [[],[0],[1]]

Output:
[0,1,2]
```

✔ Simple topological order

---

### Example 2 (Cycle case)

```
Input:
n = 3
beforeItems = [[2],[0],[1]]

Output: []
```

❌ Cycle exists

---

## 4. **Intuition & pattern recognition**

### 🔑 Signals:

* Dependencies → **Topological Sort**
* Groups constraint → **Hierarchical ordering**
* Contiguous grouping → **Sort groups first, then items**

---

### 💡 Key idea:

👉 This is **Topological Sort on TWO levels**

1. **Group-level topo sort**
2. **Item-level topo sort inside each group**

---

### 🧠 Interview thought:

> “This is DAG ordering + grouping constraint → do topo sort twice”

---

## 5. **Simpler version**

### Step 1:

* Ignore groups → just topo sort items
  👉 Classic **Course Schedule II**

### Step 2:

* Add grouping → enforce block ordering
  👉 Need separate group DAG

---

### Related simpler problems:

* **Course Schedule II** → topo sort
* **Alien Dictionary** → ordering with constraints
* **Parallel Courses** → DAG levels

---

### 🔁 Thinking progression:

```
Topo sort items
→ group items
→ topo sort groups
→ merge results
```

---

## 6. **Brute force**

### Idea:

* Try all permutations of items
* Check:

  * dependencies
  * group contiguity

### Complexity:

* ❌ O(n!) → impossible

---

## 7. **Optimal solution (2-level Topological Sort)**

---

### ✅ Steps:

### 1. Assign new group IDs to -1 items

```python
for i in range(n):
    if group[i] == -1:
        group[i] = m
        m += 1
```

---

### 2. Build graphs

* **Item graph**
* **Group graph**

---

### 3. Topological sort function

```python
from collections import deque

def topo_sort(graph, indegree, nodes):
    q = deque([node for node in nodes if indegree[node] == 0])
    order = []
    
    while q:
        node = q.popleft()
        order.append(node)
        
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    
    return order if len(order) == len(nodes) else []
```

---

### 4. Full solution

```python
from collections import defaultdict, deque

def sortItems(n, m, group, beforeItems):
    
    # Step 1: assign new groups
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1
    
    # Graphs
    item_graph = defaultdict(list)
    item_indegree = [0] * n
    
    group_graph = defaultdict(list)
    group_indegree = [0] * m
    
    # Step 2: build graphs
    for i in range(n):
        for prev in beforeItems[i]:
            item_graph[prev].append(i)
            item_indegree[i] += 1
            
            if group[prev] != group[i]:
                group_graph[group[prev]].append(group[i])
                group_indegree[group[i]] += 1
    
    # Step 3: topo sort groups
    group_order = topo_sort(group_graph, group_indegree, list(range(m)))
    if not group_order:
        return []
    
    # Step 4: topo sort items
    item_order = topo_sort(item_graph, item_indegree, list(range(n)))
    if not item_order:
        return []
    
    # Step 5: group items
    group_to_items = defaultdict(list)
    for item in item_order:
        group_to_items[group[item]].append(item)
    
    # Step 6: build result
    result = []
    for g in group_order:
        result.extend(group_to_items[g])
    
    return result
```

---

### Complexity:

* **Time:** O(n + dependencies)
* **Space:** O(n + dependencies)

---

## 8. **Step-by-step trace**

### Input:

```
group = [0,0,1]
beforeItems = [[],[0],[1]]
```

---

### Step 1: Graph

```
Item graph:
0 → 1 → 2

Group graph:
0 → 1
```

---

### Step 2: Topo group

```
[0, 1]
```

---

### Step 3: Topo item

```
[0, 1, 2]
```

---

### Step 4: Merge

```
Group 0 → [0,1]
Group 1 → [2]

Final = [0,1,2]
```

---

## 9. **Related problems**

1. **Course Schedule II**
   → Pure topological sort

2. **Alien Dictionary**
   → Order characters with constraints

3. **Parallel Courses**
   → DAG level processing

4. **Build a Matrix With Conditions**
   → Two independent topological sorts

5. **Sequence Reconstruction**
   → Validate unique topo ordering

---

## 🔥 Final Interview Punchline

> “This is a two-level topological sort: first sort groups, then sort items, and merge respecting group order.”

---

If you want, I can also give:

* ⚡ Cleaner intuitive version (most interviewers expect)
* ❗ Common mistakes (very important for this question)
