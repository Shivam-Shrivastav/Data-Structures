## 🔹 Word Search (Backtracking + DFS)

---

## 1. Problem Statement with Example

Given a 2D grid of characters and a string `word`, return **true** if the word exists in the grid.

👉 You can move:

* Up, Down, Left, Right
* Cannot reuse the same cell

---

### Example

```
board =
[
 ["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]
]

word = "ABCCED"

Output: true
```

---

### Constraints

* m, n ≤ ~6–10 (small grid → DFS works)
* word length ≤ m * n
* Each cell used **once per path**

---

## 2. Diagram (DFS Path Exploration)

```
Word = "ABCCED"

Grid:

A B C E
S F C S
A D E E

Path:
(0,0) A →
(0,1) B →
(0,2) C →
(1,2) C →
(2,2) E →
(2,1) D
```

---

## 3. Example I/O

### Example 1 (Typical)

```
Input:
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"

Output: true
```

---

### Example 2 (Edge Case)

```
word = "ABCB"
Output: false
```

👉 Cannot reuse same cell

---

## 4. Intuition & Pattern Recognition

### 🚨 Signals

* “Search word in grid”
* “Adjacent moves”
* “No reuse of cells”

👉 Classic:

> **DFS + Backtracking on grid**

---

### Core Idea

For each cell:

* If it matches first character → start DFS

At each step:

* Match next character
* Mark visited
* Explore 4 directions
* Backtrack

---

### Interview Thought

> “This is a grid DFS problem where I try all paths and backtrack to avoid revisiting cells.”

---

## 5. Simpler Version

### Step 1: Grid DFS

👉 **Number of Islands**

* Explore connected components

---

### Step 2: Path Constraint

👉 **Path with Maximum Gold**

* Cannot revisit cells

---

### Step 3: Combine

👉 Current problem =

* DFS + path matching + backtracking

---

### Thinking Flow

```
Start from each cell
   ↓
DFS match characters
   ↓
Backtrack if mismatch
```

---

## 6. Brute Force

### Idea

* Try all paths of length = word length

### Complexity

* Time: **O(m * n * 4^L)**
  (L = length of word)

---

## 7. Optimal Solution (DFS + Backtracking)

---

### Code

```python
class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            # all chars matched
            if i == len(word):
                return True
            
            # boundary + mismatch check
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[i]):
                return False
            
            # mark visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # explore all 4 directions
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))
            
            # backtrack
            board[r][c] = temp
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
```

---

### Complexity

* Time: **O(m * n * 4^L)**
* Space: O(L) recursion

---

## 8. Step-by-Step Trace

### Input:

```
word = "ABCCED"
```

---

### Start from (0,0) = 'A'

```
i=0 → 'A' ✔
```

---

### Move to (0,1)

```
i=1 → 'B' ✔
```

---

### Move to (0,2)

```
i=2 → 'C' ✔
```

---

### Move to (1,2)

```
i=3 → 'C' ✔
```

---

### Move to (2,2)

```
i=4 → 'E' ✔
```

---

### Move to (2,1)

```
i=5 → 'D' ✔
```

---

### i == len(word)

✅ Found → return True

---

## 9. Related Problems

1. **Word Search II**
   → Multiple words + Trie optimization

2. **Number of Islands**
   → Basic grid DFS

3. **Path with Maximum Gold**
   → Backtracking on grid

4. **Surrounded Regions**
   → DFS boundary traversal

5. **Shortest Path in Binary Matrix**
   → Grid traversal (BFS variant)

---

## 🔥 Interview One-Liner

👉 *“I run DFS from every cell, matching characters step-by-step while marking visited cells and backtracking to explore all possible paths.”*

---

If you want, next I can:

* ⚡ Show **Word Search II (Trie + DFS)** — very important upgrade
* ⚡ Give **pruning tricks** to reduce 4^L branching
* ⚡ Show **why marking in-place is faster than visited[][]**
