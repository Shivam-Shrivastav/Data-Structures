# Deepest Leaves Sum

LeetCode 1302 — Tree + BFS/DFS

---

# 1. Problem Statement

Given the `root` of a binary tree, return the **sum of values of the deepest leaf nodes**.

A deepest leaf:

* belongs to the maximum depth level in the tree.

---

## Example

```text id="4pd9m0"
            1
          /   \
         2     3
        / \     \
       4   5     6
      /           \
     7             8
```

Deepest level:

```text id="q5ihnd"
7 and 8
```

Sum:

```text id="jlwm8l"
7 + 8 = 15
```

---

## Constraints

* Number of nodes: `[1, 10^4]`
* `1 <= Node.val <= 100`

Important:

* only deepest level matters
* need level/depth tracking

---

# 2. Diagram

```text id="jlwm6x"
Depth 0:                 1

Depth 1:            2         3

Depth 2:         4     5         6

Depth 3:      7                     8
```

Deepest leaves:

```text id="jlwm3e"
7, 8
```

Answer:

```text id="jlwm2n"
15
```

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm7n"
root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
```

### Output

```text id="jlwm4c"
15
```

---

## Example 2

### Input

```text id="jlwm1a"
root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
```

### Output

```text id="jlwm0c"
19
```

---

# 4. Intuition & Pattern Recognition

This is fundamentally:

```text id="jlwm5n"
Level Order Traversal
```

because:

* we care about deepest level only.

---

# Key Observation

If we process tree level-by-level:

```text id="jlwm8c"
the LAST processed level
is the deepest level.
```

So:

* compute sum at each level
* overwrite previous sum
* final sum = answer

---

# Pattern Recognition Signals

Keywords:

* “deepest leaves”
* “deepest level”
* “last level”

Usually means:

```text id="jlwm4b"
BFS level traversal
```

---

# Alternative DFS Insight

Can also:

* track max depth seen
* accumulate sum at deepest depth

---

# 5. Simpler Version

---

## Simpler Problem

### Binary Tree Level Order Traversal

Level-by-level BFS.

---

## Add One Extra Thing

Instead of storing levels:

```text id="jlwm9p"
store level sum
```

Only keep:

* latest level sum

because deepest level overwrites earlier ones.

---

# Simpler Thinking Path

### BFS traversal

↓

### Process one level at a time

↓

### Compute current level sum

↓

### Last level sum = deepest leaves sum

---

# 6. Brute Force

## Two Pass Approach

1. Compute maximum depth
2. Traverse again and sum nodes at that depth

---

# Complexity

## Time

```text id="jlwm6c"
O(n)
```

But requires two traversals.

---

# 7. Optimal Solution

# BFS Level Order Solution

Most natural solution.

---

# Optimal BFS Code

```python id="jlwm3m"
from collections import deque

class Solution:
    def deepestLeavesSum(self, root):

        q = deque([root])

        while q:

            level_sum = 0

            for _ in range(len(q)):

                node = q.popleft()

                level_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        # final processed level
        return level_sum
```

---

# Why This Works

At every iteration:

* `level_sum` stores current level total

Since BFS processes:

* top → bottom

The final level processed:

* deepest level

So final `level_sum` is answer.

---

# Complexity

## Time

```text id="jlwm1b"
O(n)
```

---

## Space

```text id="jlwm7c"
O(w)
```

where:

* `w = max width of tree`

---

# DFS Alternative

Track:

* deepest depth
* running sum

---

# DFS Code

```python id="jlwm0d"
class Solution:

    def deepestLeavesSum(self, root):

        self.max_depth = -1
        self.answer = 0

        def dfs(node, depth):

            if not node:
                return

            # new deepest level found
            if depth > self.max_depth:

                self.max_depth = depth
                self.answer = node.val

            # same deepest level
            elif depth == self.max_depth:

                self.answer += node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return self.answer
```

---

# DFS Insight

Whenever:

* deeper level discovered

reset sum.

Whenever:

* same deepest level found

add to sum.

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm5d"
            1
          /   \
         2     3
        / \     \
       4   5     6
      /           \
     7             8
```

---

# BFS Trace

---

## Level 0

Queue:

```text id="jlwm9b"
[1]
```

Sum:

```text id="jlwm6p"
1
```

---

## Level 1

Queue:

```text id="jlwm3p"
[2,3]
```

Sum:

```text id="jlwm2f"
5
```

---

## Level 2

Queue:

```text id="jlwm7e"
[4,5,6]
```

Sum:

```text id="jlwm4e"
15
```

---

## Level 3

Queue:

```text id="jlwm1p"
[7,8]
```

Sum:

```text id="jlwm0p"
15
```

Queue empty.

Return:

```text id="jlwm8g"
15
```

---

# 9. Related Problems

---

### Binary Tree Level Order Traversal

Foundation BFS level traversal problem.

---

### Maximum Depth of Binary Tree

Computing deepest level.

---

### Average of Levels in Binary Tree

Another per-level aggregation problem.

---

### Find Largest Value in Each Tree Row

Level-wise computation variation.

---

### Binary Tree Right Side View

Level-order visibility traversal.
