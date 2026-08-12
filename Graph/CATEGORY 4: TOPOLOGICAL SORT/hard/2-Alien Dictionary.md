## **Alien Dictionary (LeetCode)**

---

## 1. **Problem statement with example**

You are given a sorted list of words from an **alien language**.
The words are sorted according to some **unknown character order**.

### Goal:

Return a **valid ordering of characters** in this alien language.
If no valid ordering exists → return `""`.

---

### Key rules:

* Compare **adjacent words**
* First different character gives ordering
* If prefix conflict exists → invalid

---

### Example:

```
words = ["wrt","wrf","er","ett","rftt"]
```

Output:

```
"wertf"
```

---

### Constraints:

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 100`
* Characters are lowercase English letters

---

## 2. **Diagram**

```
Compare adjacent words:

"wrt" vs "wrf" → t → f
"wrf" vs "er"  → w → e
"er"  vs "ett" → r → t
"ett" vs "rftt"→ e → r

Graph:

w → e → r → t → f
```

---

## 3. **Example I/O**

### Example 1 (Typical)

```
Input:
["wrt","wrf","er","ett","rftt"]

Output:
"wertf"
```

✔ Valid ordering from constraints

---

### Example 2 (Invalid case)

```
Input:
["abc","ab"]

Output:
""
```

❌ Invalid because:

* "abc" comes before "ab"
* Prefix violation → impossible ordering

---

## 4. **Intuition & pattern recognition**

### 🔑 Signals:

* Unknown order → **derive ordering**
* Words are sorted → gives constraints
* Dependency between characters

👉 This is:

> **Topological Sort on Characters**

---

### Key idea:

* Build graph of characters
* Each edge: `a → b` means `a` comes before `b`
* Then do **topological sort**

---

### Why it works:

* Ordering constraints = directed edges
* Valid ordering = topo ordering
* Cycle → invalid → return ""

---

## 5. **Simpler version**

### Simplest:

👉 "Given edges, return topo order"

* Direct graph input
* Solve using Kahn’s or DFS topo

---

### Intermediate:

👉 "Course Schedule II"

* Courses = characters
* Prerequisites = ordering

---

### This problem twist:

👉 Graph is **not given directly**
You must:

1. **Extract edges from word pairs**
2. Then apply topo sort

---

### Thinking ladder:

```
Topo Sort (given graph)
→ Build graph from constraints
→ Extract constraints from strings
```

---

## 6. **Brute force**

### Idea:

* Try all permutations of characters
* Check which satisfies ordering

### Complexity:

* Time: **O(k!)**
* Space: **O(k)**

❌ Impossible for k = 26

---

## 7. **Optimal solution (Topo Sort - Kahn’s BFS)**

---

### Steps:

1. Initialize graph + indegree
2. Add all unique characters
3. Compare adjacent words → build edges
4. Handle prefix invalid case
5. Perform BFS topo sort

---

### Code (Python)

```python
from collections import defaultdict, deque

def alienOrder(words):
    # Step 1: initialize graph
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}
    
    # Step 2: build graph
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        
        # Prefix invalid case
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
        
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break
    
    # Step 3: topo sort
    q = deque([c for c in indegree if indegree[c] == 0])
    res = []
    
    while q:
        char = q.popleft()
        res.append(char)
        
        for nei in graph[char]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    
    # Step 4: check cycle
    return "".join(res) if len(res) == len(indegree) else ""
```

---

### Complexity:

* Time: **O(C + E)**
  (C = total chars, E = edges)
* Space: **O(C + E)**

---

## 8. **Step-by-step trace**

### Input:

```
["wrt","wrf","er","ett","rftt"]
```

---

### Build edges:

```
t → f
w → e
r → t
e → r
```

---

### Indegree:

```
w:0, e:1, r:1, t:1, f:1
```

---

### Queue:

```
[w]
```

---

### BFS:

| Step | Node | Result | Updates      |
| ---- | ---- | ------ | ------------ |
| 1    | w    | w      | e indegree→0 |
| 2    | e    | we     | r indegree→0 |
| 3    | r    | wer    | t indegree→0 |
| 4    | t    | wert   | f indegree→0 |
| 5    | f    | wertf  | done         |

---

### Final:

```
"wertf"
```

---

## 9. **Related problems**

1. **Course Schedule**
   → Detect if topo ordering exists (cycle check)

2. **Course Schedule II**
   → Return actual ordering

3. **Parallel Courses III**
   → Topo + DP propagation

4. **Largest Color Value in a Directed Graph**
   → Topo + state tracking

5. **Sequence Reconstruction**
   → Validate uniqueness of ordering

---

## 🚀 Interview takeaway

When you see:

* Sorted dictionary
* Unknown ordering
* Constraints from comparisons

👉 Think:

> **"Build graph from adjacent comparisons + Topological Sort"**

---

If you want, I can also show:

* DFS topo version (cycle detection via colors)
* Trick to detect **multiple valid answers vs unique order**
* Common mistakes interviewers expect (very important)

