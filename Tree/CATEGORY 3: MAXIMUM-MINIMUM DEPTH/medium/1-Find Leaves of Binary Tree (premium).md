# Find Leaves of Binary Tree

LeetCode 366 (Premium) — Tree + DFS + Postorder

---

# 1. Problem Statement

Given the `root` of a binary tree:

1. Collect all leaf nodes
2. Remove them
3. Repeat until tree becomes empty

Return:

* list of leaves removed at each round

---

## Example

```text id="4x0d9y"
        1
      /   \
     2     3
    / \
   4   5
```

Round 1:

* remove `[4,5,3]`

Remaining:

```text id="hkt7qt"
      1
     /
    2
```

Round 2:

* remove `[2]`

Remaining:

```text id="jlwm91"
1
```

Round 3:

* remove `[1]`

Answer:

```python id="jlwm0k"
[[4,5,3],[2],[1]]
```

---

## Constraints

* Number of nodes: `[1, 100]`
* `-100 <= Node.val <= 100`

Important:

* Need grouping by “removal round”
* Simulating deletions literally is inefficient

---

# 2. Diagram

```text id="jlwm5c"
Initial Tree:

        1
      /   \
     2     3
    / \
   4   5
```

---

## Round 1 Leaves

```text id="jlwm3f"
4, 5, 3
```

Remove:

```text id="jlwm7d"
        1
       /
      2
```

---

## Round 2 Leaves

```text id="jlwm4f"
2
```

Remove:

```text id="jlwm6r"
1
```

---

## Round 3 Leaves

```text id="jlwm2z"
1
```

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm8a"
root = [1,2,3,4,5]
```

### Output

```python id="jlwm1k"
[[4,5,3],[2],[1]]
```

---

## Example 2

### Input

```text id="jlwm6k"
root = [1]
```

### Output

```python id="jlwm5v"
[[1]]
```

---

# 4. Intuition & Pattern Recognition

This problem LOOKS like:

* repeated deletion simulation

But the actual trick is:

```text id="jlwm9w"
Leaves removed at same round
have same "height from bottom".
```

This is the key insight.

---

# Core Observation

Suppose:

```text id="jlwm7p"
leaf node height = 0
```

Then:

```text id="jlwm8p"
parent of leaf height = 1
```

Then:

```text id="jlwm3v"
grandparent height = 2
```

Exactly matching:

* removal rounds.

---

# Visual Insight

```text id="jlwm1z"
        1(h=2)
      /       \
   2(h=1)    3(h=0)
   /   \
4(0)  5(0)
```

Grouping by height:

```text id="jlwm0a"
height 0 -> [4,5,3]
height 1 -> [2]
height 2 -> [1]
```

DONE.

---

# Pattern Recognition Signals

Keywords:

* “Remove leaves repeatedly”
* “Rounds”
* “Bottom-up”

Usually means:

```text id="jlwm6n"
Postorder DFS
```

because:

* children processed before parent.

---

# 5. Simpler Version

---

## Simpler Problem

### Maximum Depth of Binary Tree

Depth from top:

```python id="jlwm4w"
1 + max(left,right)
```

---

## This Problem

Instead compute:

```text id="jlwm5p"
height from bottom
```

Leaf:

```text id="jlwm9k"
0
```

Parent:

```text id="jlwm7l"
1
```

---

# Simpler Thinking Path

### Tree height problem

↓

### Reverse perspective

↓

### Group nodes by bottom-height

↓

### Bottom-height = removal round

---

# 6. Brute Force

## Literal Simulation

Repeat:

1. find all leaves
2. remove them
3. store result

until tree empty.

---

# Complexity

Each round scans whole tree.

Worst case skewed tree:

```text id="jlwm3c"
O(n^2)
```

---

# 7. Optimal Solution

# Postorder DFS

---

# Key Formula

```python id="jlwm6s"
height = 1 + max(left_height, right_height)
```

But:

* null node height = -1

So:

* leaf height becomes 0

Perfect for indexing result.

---

# Optimal Code

```python id="jlwm0b"
from collections import defaultdict

class Solution:
    def findLeaves(self, root):

        res = defaultdict(list)

        def dfs(node):

            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            height = 1 + max(left, right)

            # group by removal round
            res[height].append(node.val)

            return height

        dfs(root)

        return list(res.values())
```

---

# Why `null = -1`?

Because:

```text id="jlwm4j"
leaf height should become 0
```

So:

```python id="jlwm2b"
1 + max(-1,-1)
= 0
```

Perfect.

---

# Complexity

## Time

```text id="jlwm8j"
O(n)
```

Each node visited once.

---

## Space

```text id="jlwm1m"
O(n)
```

Result + recursion stack.

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm6f"
        1
      /   \
     2     3
    / \
   4   5
```

---

# DFS Processing

---

## Node 4

```text id="jlwm3a"
left = -1
right = -1

height = 0
```

Store:

```text id="jlwm0f"
res[0] = [4]
```

---

## Node 5

```text id="jlwm7s"
height = 0
```

Store:

```text id="jlwm9s"
res[0] = [4,5]
```

---

## Node 2

```text id="jlwm2k"
left = 0
right = 0

height = 1
```

Store:

```text id="jlwm6d"
res[1] = [2]
```

---

## Node 3

```text id="jlwm5k"
height = 0
```

Store:

```text id="jlwm4d"
res[0] = [4,5,3]
```

---

## Node 1

```text id="jlwm8d"
left = 1
right = 0

height = 2
```

Store:

```text id="jlwm1n"
res[2] = [1]
```

Final:

```python id="jlwm5f"
[[4,5,3],[2],[1]]
```

---

# 9. Related Problems

---

### Maximum Depth of Binary Tree

Same subtree height recursion.

---

### Diameter of Binary Tree

Uses postorder height calculations.

---

### Balanced Binary Tree

Postorder DFS height propagation.

---

### Binary Tree Pruning

Bottom-up subtree removal logic.

---

### Delete Leaves With a Given Value

Leaf deletion with recursive pruning.
