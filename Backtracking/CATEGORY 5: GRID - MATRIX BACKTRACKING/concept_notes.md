# Matrix Backtracking — Word Search & Grid Problems

## 1. Pattern in One Minute

**Core idea:**
Backtracking on a matrix = **DFS + choose → explore → undo**, while tracking the current path/state.

Think:

> **“From this cell, what choices can I make next?”**

Typical structure:

```text
Start at a cell
   ↓
Mark it as used
   ↓
Try 4 directions
   ↓
If valid → DFS
   ↓
Undo / unmark
```

### Why this pattern exists

Use it when a solution is formed by **moving through neighboring cells**, and a choice made at one cell affects what cells can be used later.

Immediately think **Matrix Backtracking** when you see:

* `"word exists in grid"`
* Find a path through adjacent cells
* Cannot reuse the same cell
* Generate paths/configurations in a grid
* Maze/path exploration
* Need to try multiple directions
* Constraints are small enough for exponential search

---

# 2. Recognition Signals

### Strong signals

| Signal                             | Think                   |
| ---------------------------------- | ----------------------- |
| Grid + neighboring cells           | DFS                     |
| Need to explore all possible paths | Backtracking            |
| Cannot reuse a cell                | `visited` / mark-unmark |
| Word must be formed                | Word Search             |
| Move up/down/left/right            | 4-direction DFS         |
| Sometimes diagonal movement        | 8-direction DFS         |
| Need all possible paths            | Backtracking            |
| Need only existence                | Return early when found |

### Common disguise

A problem might not explicitly say "backtracking."

For example:

> Given a board containing letters, determine whether a word exists.

This is essentially:

```text
Choose starting cell
→ choose next matching neighbor
→ choose next...
→ undo if path fails
```

### When NOT to use it

Don't blindly use matrix backtracking.

* **Shortest path** → BFS/Dijkstra
* **Number of ways with overlapping subproblems** → DP
* **Simple connected component** → DFS/BFS
* **Find whether cells are reachable without path-specific constraints** → DFS/BFS
* Huge grid with large dimensions → exponential backtracking is usually impossible

---

# 3. Mental Model

For **Word Search**, remember:

1. Every cell can potentially be the starting point.
2. From a cell, try the allowed neighboring directions.
3. The next character must match the required character.
4. Once you use a cell, don't use it again in the current path.
5. Mark the cell as visited.
6. Recursively continue.
7. If the path fails, **undo the visited state**.
8. Then try another direction.
9. If the whole word is matched → success.
10. The important part is **state restoration**.

The fundamental recurrence:

```text
dfs(r, c, index)
    if word[index] doesn't match:
        return False

    if index == last character:
        return True

    mark (r,c) visited

    try neighbors

    unmark (r,c)

    return result
```

### The key distinction

Normal DFS:

> “Have I visited this cell globally?”

Backtracking DFS:

> **“Have I visited this cell on my current path?”**

That's why we **unmark** after recursion.

---

# 4. Boilerplate Template

### Word Search — canonical template

```python
class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            # All characters matched
            if i == len(word):
                return True

            # Invalid cell / mismatch / already used
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] != word[i]
            ):
                return False

            # Choose
            visited.add((r, c))

            # Explore
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if dfs(r + dr, c + dc, i + 1):
                    return True

            # Undo
            visited.remove((r, c))

            return False

        # Try every cell as starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
```

### The reusable skeleton

```python
def dfs(r, c, state):

    if invalid:
        return

    # CHOOSE
    mark(r, c)

    # EXPLORE
    for direction in directions:
        dfs(next_r, next_c, next_state)

    # UNDO
    unmark(r, c)
```

This is the **matrix-backtracking template worth memorizing**.

---

# 5. Variations

### 1. Word Search

**LeetCode 79**

```text
Grid + target string
→ DFS from every cell
→ match characters
→ don't reuse cell
```

---

### 2. Word Search II

**LeetCode 212**

Instead of searching for one word:

```text
Multiple words
+
same board
```

Use:

```text
Trie + Matrix Backtracking
```

The major optimization is:

> Build a Trie so that DFS can stop immediately when the current character sequence isn't a prefix of any word.

---

### 3. Maze / Path Finding

Instead of matching characters:

```python
if cell is valid:
    dfs(next_cell)
```

State may include:

```text
position
visited
path
```

---

### 4. Diagonal movement

Change:

```python
directions = [
    (1, 0), (-1, 0),
    (0, 1), (0, -1)
]
```

to:

```python
directions = [
    (1, 0), (-1, 0),
    (0, 1), (0, -1),
    (1, 1), (1, -1),
    (-1, 1), (-1, -1)
]
```

---

### 5. In-place visited marking

Instead of:

```python
visited.add((r, c))
...
visited.remove((r, c))
```

you can temporarily modify the board:

```python
original = board[r][c]
board[r][c] = "#"

dfs(...)

board[r][c] = original
```

Usually faster and uses **O(1) auxiliary visited space**.

---

### 6. Need the actual path

Instead of returning only `True/False`:

```python
path.append((r, c))
dfs(...)
path.pop()
```

Now the path itself becomes part of the backtracking state.

---

# 6. Common Pitfalls

### ❌ Forgetting to undo

```python
visited.add(cell)
dfs(...)
# forgot remove
```

This incorrectly prevents other paths from using the cell.

**Remember:**

> Every `add()` needs a corresponding `remove()`.

---

### ❌ Global visited instead of path-specific visited

A cell can be used in:

```text
Path A
```

and later reused in:

```text
Path B
```

So it must be restored after Path A finishes.

---

### ❌ Marking too late

Bad:

```python
dfs(neighbor)
visited.add(current)
```

Mark **before recursion**.

---

### ❌ Wrong base case

For Word Search:

```python
if i == len(word):
    return True
```

is cleaner than trying to access:

```python
word[i]
```

when `i == len(word)`.

---

### ❌ Forgetting every starting cell

You can't assume the word starts at `(0,0)`.

Need:

```python
for every cell:
    dfs(cell)
```

---

### ❌ Returning too early

You need to distinguish:

```text
One branch failed
```

from:

```text
All branches failed
```

If one direction fails, try the others.

---

### ❌ Not pruning

For Word Search II especially, blindly exploring every path is expensive.

Use:

```text
Trie
```

to prune impossible prefixes.

---

# 7. Interview Checklist

✓ Is this a **grid/matrix**?

✓ Do I need to explore **neighboring cells**?

✓ Are there **multiple possible directions**?

✓ Does the current choice affect what I can use later?

✓ Is cell reuse restricted?

✓ Do I need to explore **all possible paths**?

If yes:

> **DFS + Backtracking**

Then ask:

```text
What is my state?
→ (r, c, index)

What are my choices?
→ neighboring cells

What is my constraint?
→ bounds + visited + matching condition

What do I undo?
→ visited/path/board state
```

---

# 8. Must-Do Problems

### 🟢 Easy

**1. Letter Case Permutation — LC 784**
Useful for understanding choice branching, although not matrix-specific.

### 🟡 Medium

**🥇 TOP 1 — Word Search — LC 79**

The canonical matrix-backtracking problem.

**🥈 TOP 2 — Path with Maximum Gold — LC 1219**

Excellent for:

```text
grid DFS
+
visited
+
backtracking
+
optimization
```

**🥉 TOP 3 — Unique Paths III — LC 980**

Very important because the DFS state becomes more complex:

```text
position
+
visited
+
remaining cells
```

Other useful problems:

* Word Search II — LC 212
* Number of Islands — LC 200 *(DFS foundation, but not really backtracking)*
* The Maze — LC 490
* Rat in a Maze — classic backtracking
* All Paths From Source to Target — LC 797 *(graph version of the same idea)*

### 🔴 Hard

**Word Search II — LC 212**

Worth doing if you're interviewing for strong SDE/ML roles because it combines:

```text
Trie + DFS + Backtracking + Pruning
```

---

# 9. 30-Second Cheat Sheet

```text
MATRIX BACKTRACKING
────────────────────────────────

Recognition:
Grid + multiple paths + neighbors
+ path-specific constraints
+ cannot reuse / must explore possibilities

Core:
        CHOOSE
          ↓
        EXPLORE
          ↓
         UNDO

State:
(r, c, index, visited, ...)

Choices:
4 directions
or 8 directions

Template:

dfs(r, c, state):

    if invalid:
        return

    mark cell

    for direction:
        dfs(next cell)

    unmark cell


Most important:
Every path gets its own visited state.

Word Search:
Try every starting cell
→ match character
→ mark
→ explore 4 directions
→ unmark

Complexity:
Word Search ≈ O(R × C × 4^L)
where L = word length

Key variations:
• Word Search
• Word Search II → Trie + pruning
• Maze → path tracking
• Maximum Gold → maximize path sum
• Unique Paths III → visit every required cell

Mnemonic:
"GRID → CHOOSE → DFS → UNDO"
```

**If you're revising the whole Backtracking family, the matrix-specific progression I'd memorize is:**

**Subsets → Permutations → Combination Sum → Palindrome Partitioning → Matrix Backtracking/Word Search → Trie + Backtracking.**

That sequence makes the jump from **1D decision trees → path-based 2D decision trees** very easy to recall.
