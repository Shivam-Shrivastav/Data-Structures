## **Minimum Jumps to Reach Home (LeetCode 1654)**

---

### **1. Problem statement with example**

You are given:

* An array `forbidden[]` → positions you **cannot land on**
* Integers:

  * `a` → forward jump distance
  * `b` → backward jump distance
  * `x` → target position

👉 You start at position `0`.

Rules:

* You can jump:

  * forward → `+a`
  * backward → `-b`
* ❗ You **cannot jump backward twice in a row**
* ❗ Cannot land on forbidden positions
* ❗ Positions are ≥ 0 (no negative)

👉 Return the **minimum number of jumps** to reach `x`, or `-1` if impossible.

---

### **2. Diagram**

Example:

```text
Start: 0

Forward jumps: +a
Backward jumps: -b

0 → a → 2a → ...
    ← b
```

State visualization:

```text
(position, last_move)

Example:
(3, forward)
(5, backward)
```

---

### **3. Example I/O**

#### **Example 1**

```text
Input:
forbidden = [14,4,18,1,15]
a = 3, b = 15, x = 9

Output: 3
```

**Explanation:**

```text
0 → 3 → 6 → 9
```

---

#### **Example 2**

```text
Input:
forbidden = [8,3,16,6,12,20]
a = 15, b = 13, x = 11

Output: -1
```

---

#### **Edge Case**

```text
x = 0 → Output: 0
```

---

### **4. Intuition & pattern recognition**

🔑 Signals:

* "minimum jumps"
* forward/backward rules
* restrictions on moves

👉 This is NOT simple BFS

💡 Because:

* State depends on **previous move**

---

👉 State becomes:

```text
(position, last_move_was_backward_or_not)
```

---

👉 Why needed?

* Because:
  ❌ can't do backward twice
  ✔ so same position can behave differently

---

### **5. Simpler version**

#### **Build from:**

* Jump Game III
  → BFS with jumps

* Minimum Knight Moves
  → BFS shortest path

* Shortest Path in Grid with Obstacles Elimination
  → BFS with state

---

#### **Build-up**

| Step                     | Concept        |
| ------------------------ | -------------- |
| Simple jumps             | BFS            |
| Add forbidden            | prune states   |
| Add backward restriction | need state     |
| Final                    | BFS with state |

---

👉 Key jump:

> From **position BFS → state BFS**

---

### **6. Brute force**

👉 Try all sequences (DFS)

❌ Problems:

* infinite loops possible
* exponential

---

### **7. Optimal solution (BFS + state)**

---

### **Key optimization**

👉 Limit search space:

* You don’t need to go infinitely right

💡 Upper bound:

```text
max_limit = max(forbidden ∪ {x}) + a + b + buffer
```

---

### **Code**

```python
from collections import deque

def minimumJumps(forbidden, a, b, x):
    forbidden_set = set(forbidden)
    
    # define upper bound
    upper = max(max(forbidden, default=0), x) + a + b + 2000
    
    queue = deque([(0, 0, False)])  # (position, steps, last_was_back)
    visited = set([(0, False)])
    
    while queue:
        pos, steps, last_back = queue.popleft()
        
        if pos == x:
            return steps
        
        # forward move
        next_pos = pos + a
        if (0 <= next_pos <= upper and
            next_pos not in forbidden_set and
            (next_pos, False) not in visited):
            
            visited.add((next_pos, False))
            queue.append((next_pos, steps + 1, False))
        
        # backward move (only if last wasn't backward)
        if not last_back:
            next_pos = pos - b
            if (0 <= next_pos and
                next_pos not in forbidden_set and
                (next_pos, True) not in visited):
                
                visited.add((next_pos, True))
                queue.append((next_pos, steps + 1, True))
    
    return -1
```

---

### **Complexity**

* **Time:** O(N) (bounded search space)
* **Space:** O(N)

---

### **8. Step-by-step trace (core idea)**

Example:

```text
forbidden = [14,4,18,1,15]
a = 3, b = 15, x = 9
```

---

#### Step 1:

```text
Queue = [(0,0,F)]
```

---

#### Step 2:

```text
From 0:
→ forward → 3
```

Queue:

```text
[(3,1,F)]
```

---

#### Step 3:

```text
From 3:
→ 6
→ backward → invalid (negative)
```

---

#### Step 4:

```text
From 6:
→ 9 (target)
```

👉 Answer = 3

---

### **9. Related problems**

* Jump Game III
  → BFS on positions

* Open the Lock
  → BFS with constraints

* Sliding Puzzle
  → BFS on configurations

* Minimum Knight Moves
  → BFS shortest path

* Shortest Path Visiting All Nodes
  → BFS with extended state

---

### **🔥 Interview takeaway**

👉 If:

* jumps + constraints
* previous move affects future

💡 Say:

> **“We need BFS with state (position + last move info)”**

---

### **💡 Golden insight**

> “We must include last move in state because it changes the validity of future moves (no consecutive backward).”

---

If you want, I can give you a **pattern decision tree** (when to use normal BFS vs state BFS vs Dijkstra) — super useful in interviews.
