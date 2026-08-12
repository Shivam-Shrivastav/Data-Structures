# Vertical Order Traversal of a Binary Tree

LeetCode 987 — Tree + DFS/BFS + Sorting

---

# 1. Problem Statement

Given the `root` of a binary tree, return its **vertical order traversal**.

Each node has a position:

* root → `(row=0, col=0)`
* left child → `(row+1, col-1)`
* right child → `(row+1, col+1)`

Return nodes column by column from:

* leftmost column → rightmost column

Rules:

1. Sort by column
2. If same column → smaller row first
3. If same row & same column → smaller value first

---

## Example

```text id="w76bb4"
        3
      /   \
     9     20
          /  \
         15   7
```

Coordinates:

```text id="06m6ut"
3   -> (0,0)
9   -> (1,-1)
20  -> (1,1)
15  -> (2,0)
7   -> (2,2)
```

Vertical traversal:

```text id="7kk8i5"
[
  [9],
  [3,15],
  [20],
  [7]
]
```

---

## Constraints

* Number of nodes: `[1, 1000]`
* `0 <= Node.val <= 1000`

Important:

* Need stable ordering
* Same position conflicts matter

---

# 2. Diagram

```text id="ekxz7m"
              3(0,0)
            /        \
      9(1,-1)      20(1,1)
                   /      \
             15(2,0)     7(2,2)
```

Columns:

```text id="4iw5qm"
col -1 : [9]
col  0 : [3,15]
col  1 : [20]
col  2 : [7]
```

---

## Important Tie Case

```text id="xgm4nx"
        1
       / \
      2   3
       \ /
        5 4
```

Coordinates:

```text id="ukw2hq"
5 -> (2,0)
4 -> (2,0)
```

Same row + same column.

Need:

```text id="u9wwsh"
[4,5]
```

because smaller value first.

This is the KEY trick.

---

# 3. Example I/O

## Example 1

### Input

```text id="tx5j8m"
root = [3,9,20,null,null,15,7]
```

### Output

```text id="o3ic7h"
[[9],[3,15],[20],[7]]
```

---

## Example 2 (Tie Case)

### Input

```text id="d3a5xd"
root = [1,2,3,4,6,5,7]
```

Tree:

```text id="lcphnf"
        1
      /   \
     2     3
    / \   / \
   4   6 5   7
```

### Output

```text id="3tb6bb"
[[4],[2],[1,5,6],[3],[7]]
```

Explanation:

* `5` and `6` both at `(2,0)`
* smaller value first → `[5,6]`

---

# 4. Intuition & Pattern Recognition

This is NOT ordinary level order traversal.

The real problem is:

```text id="4cwq5s"
Store geometric coordinates
then sort properly.
```

---

## Pattern Recognition

Signals:

* “Vertical”
* “Columns”
* “Row/column coordinates”
* “Ordering rules”

Usually means:

```text id="mk0w2k"
DFS/BFS + coordinate tracking + sorting
```

---

## Core Insight

Every node can be represented as:

```text id="u0q0lx"
(col, row, value)
```

If we collect all nodes:

```python id="ic2v77"
(col, row, val)
```

Then sort:

```python id="7x4p0u"
sort by:
1. col
2. row
3. val
```

Problem becomes easy.

---

# 5. Simpler Version

---

## Simpler Problem

### Binary Tree Vertical Order Traversal

In LC 314:

* only vertical grouping needed
* no tie-breaking by value

Simple BFS works.

---

## What Changed in LC 987?

Now:

* if same row + same col
* smaller value first

That forces global sorting.

---

## Simpler Thinking Path

### Step 1

Normal BFS:

* process level-wise

↓

### Step 2

Track columns:

* add `col`

↓

### Step 3

Need exact ordering:

* add `row`

↓

### Step 4

Need tie resolution:

* sort by value too

↓

Final representation:

```python id="lqpj9t"
(col, row, val)
```

---

# 6. Brute Force

## Idea

1. Traverse tree
2. Store nodes grouped by column
3. Sort inside each column manually

---

## Complexity

Could become:

```text id="q1qj3u"
O(n log n)
```

because sorting unavoidable.

---

# 7. Optimal Solution

## Best Interview Solution

Use:

* DFS
* coordinates
* global sorting

---

# Optimal Code

```python id="6mwdvj"
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root):

        nodes = []

        def dfs(node, row, col):

            if not node:
                return

            # store coordinates + value
            nodes.append((col, row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        # sort by:
        # col -> row -> value
        nodes.sort()

        res = defaultdict(list)

        for col, row, val in nodes:
            res[col].append(val)

        return list(res.values())
```

---

# Why Sorting Works

Python tuple sorting:

```python id="w6shmw"
(col, row, val)
```

automatically sorts by:

1. col
2. row
3. val

Exactly what problem asks.

---

# Complexity

## Time

```text id="1w5h9p"
O(n log n)
```

Sorting dominates.

---

## Space

```text id="1gg7ng"
O(n)
```

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm5w"
        1
      /   \
     2     3
    / \   / \
   4   6 5   7
```

---

## DFS Collection

Store:

| Node | Row | Col | Tuple    |
| ---- | --- | --- | -------- |
| 1    | 0   | 0   | (0,0,1)  |
| 2    | 1   | -1  | (-1,1,2) |
| 4    | 2   | -2  | (-2,2,4) |
| 6    | 2   | 0   | (0,2,6)  |
| 3    | 1   | 1   | (1,1,3)  |
| 5    | 2   | 0   | (0,2,5)  |
| 7    | 2   | 2   | (2,2,7)  |

---

## After Sorting

```python id="m18g1m"
[
(-2,2,4),
(-1,1,2),
(0,0,1),
(0,2,5),
(0,2,6),
(1,1,3),
(2,2,7)
]
```

Notice:

```text id="5k7xg4"
(0,2,5) comes before (0,2,6)
```

because value smaller.

---

## Group By Column

```text id="qjlwm6"
-2 -> [4]
-1 -> [2]
 0 -> [1,5,6]
 1 -> [3]
 2 -> [7]
```

Final:

```python id="l2b8te"
[[4],[2],[1,5,6],[3],[7]]
```

---

# 9. Related Problems

---

### Binary Tree Vertical Order Traversal

Simpler vertical grouping without tie-breaking.

---

### Binary Tree Level Order Traversal

Foundation BFS traversal problem.

---

### Top View of Binary Tree

Column-based visibility problem.

---

### Bottom View of Binary Tree

Another coordinate-based traversal variation.

---

### Diagonal Traversal of Binary Tree

Advanced geometric traversal pattern.
