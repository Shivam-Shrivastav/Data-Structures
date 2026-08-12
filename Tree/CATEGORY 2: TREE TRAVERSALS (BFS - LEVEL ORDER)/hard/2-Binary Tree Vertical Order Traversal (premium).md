# Binary Tree Vertical Order Traversal

LeetCode 314 (Premium) — Tree + BFS + Column Mapping

---

# 1. Problem Statement

Given the `root` of a binary tree, return the **vertical order traversal** of its nodes.

Rules:

* Nodes are grouped column-wise.
* Root is at column `0`
* Left child → `col - 1`
* Right child → `col + 1`

Return columns from:

* leftmost → rightmost

Within the same column:

* top-to-bottom order

If two nodes are:

* same row
* same column

then order them:

* left-to-right (BFS order)

---

## Example

```text id="9kg0p5"
        3
      /   \
     9     8
    / \   / \
   4   0 1   7
```

Columns:

```text id="ff5l9w"
col -2 : [4]
col -1 : [9]
col  0 : [3,0,1]
col  1 : [8]
col  2 : [7]
```

Answer:

```python id="0m9wb4"
[[4],[9],[3,0,1],[8],[7]]
```

---

## Constraints

* Number of nodes: `[0, 100]`
* `-100 <= Node.val <= 100`

---

# 2. Diagram

```text id="7b8tpd"
               3(0)
            /        \
        9(-1)        8(+1)
       /    \       /    \
   4(-2)  0(0)   1(0)   7(+2)
```

Observe:

```text id="f59t3u"
0 and 1 are in same column.
```

Need:

```text id="lwzz44"
[3,0,1]
```

NOT sorted by value.

This is the BIG difference from LC 987.

---

# 3. Example I/O

## Example 1

### Input

```text id="1znfgh"
root = [3,9,8,4,0,1,7]
```

### Output

```text id="cyzjlwm"
[[4],[9],[3,0,1],[8],[7]]
```

---

## Example 2

### Input

```text id="moj3z6"
root = [3,9,8,4,0,1,7,null,null,null,2,5]
```

Tree:

```text id="gx8kqy"
         3
       /   \
      9     8
     / \   / \
    4   0 1   7
         \ /
          2 5
```

### Output

```text id="5lg0s9"
[[4],[9],[3,0,1],[8,2,5],[7]]
```

---

# 4. Intuition & Pattern Recognition

This is a **column grouping BFS** problem.

Key requirement:

```text id="7i6r4j"
Same row + same column
must preserve LEFT-TO-RIGHT order.
```

That immediately suggests:

```text id="xtgl1t"
Use BFS.
```

Because BFS naturally processes:

* top-to-bottom
* left-to-right

---

# Pattern Recognition Signals

Keywords:

* “Vertical order”
* “Columns”
* “Top to bottom”
* “Left to right tie-breaking”

This usually means:

```text id="oq0tpj"
BFS + coordinate tracking
```

NOT DFS sorting.

---

# 5. Simpler Version

---

## Simpler Problem

### Binary Tree Level Order Traversal

Regular BFS:

* group by level

---

## Add One Extra Dimension

Instead of grouping by:

* level

group by:

* column

---

## Why BFS Matters

Suppose:

```text id="ztbb5s"
    0
   / \
  1   2
```

If both children somehow land same column later:

* BFS preserves left-before-right automatically.

DFS may break ordering.

---

# Difference From LC 987

### Vertical Order Traversal of a Binary Tree

LC 987:

* requires sorting by value for ties

LC 314:

* preserve traversal order instead

So:

| Problem | Tie Rule      |
| ------- | ------------- |
| LC 314  | left-to-right |
| LC 987  | smaller value |

That changes:

* BFS vs sorting strategy

---

# 6. Brute Force

## Idea

1. Compute coordinates
2. Store `(row, col, value)`
3. Sort everything

Works but unnecessary.

---

## Complexity

```text id="6xrbfa"
O(n log n)
```

due to sorting.

---

# 7. Optimal Solution

## Best Interview Solution

Use:

* BFS queue
* column index
* hashmap

Because BFS already guarantees:

* top-down
* left-right ordering

No sorting by row/value needed.

---

# Optimal Code

```python id="8p1z2c"
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root):

        if not root:
            return []

        # column -> list of node values
        cols = defaultdict(list)

        q = deque([(root, 0)])

        min_col = max_col = 0

        while q:

            node, col = q.popleft()

            cols[col].append(node.val)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                q.append((node.left, col - 1))

            if node.right:
                q.append((node.right, col + 1))

        res = []

        for c in range(min_col, max_col + 1):
            res.append(cols[c])

        return res
```

---

# Why This Works

BFS processes:

```text id="hmg7dq"
level-by-level
left-to-right
```

So insertion order into column list is already correct.

No sorting required.

---

# Complexity

## Time

```text id="8f0j5s"
O(n)
```

---

## Space

```text id="y65i1m"
O(n)
```

Queue + hashmap.

---

# 8. Step-by-Step Trace

Input:

```text id="tfzcl3"
        3
      /   \
     9     8
    / \   / \
   4   0 1   7
```

---

## BFS Start

Queue:

```text id="n3jot6"
[(3,0)]
```

Map:

```text id="vdmjlwm"
0 -> [3]
```

---

## Process 9 and 8

Queue:

```text id="vfjlwm"
[(9,-1), (8,1)]
```

Map:

```text id="k3q7fi"
-1 -> [9]
 0 -> [3]
 1 -> [8]
```

---

## Process 4,0,1,7

Queue order:

```text id="7n78vv"
4 -> 0 -> 1 -> 7
```

Map becomes:

```text id="vtzwx6"
-2 -> [4]
-1 -> [9]
 0 -> [3,0,1]
 1 -> [8]
 2 -> [7]
```

Final:

```python id="s2q4y4"
[[4],[9],[3,0,1],[8],[7]]
```

---

# 9. Related Problems

---

### Vertical Order Traversal of a Binary Tree

Harder version requiring value sorting for ties.

---

### Binary Tree Level Order Traversal

Foundation BFS traversal problem.

---

### Binary Tree Right Side View

Level-order visibility problem.

---

### Top View of Binary Tree

Column-based visibility traversal.

---

### Bottom View of Binary Tree

Another BFS + column tracking problem.
