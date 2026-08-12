# Binary Tree Right Side View

LeetCode: Binary Tree Right Side View

---

# 1. Problem Statement with Example

Given the `root` of a binary tree, imagine standing on the **right side** of the tree.

Return the values of the nodes you can see from top to bottom.

---

# Example

Input:

```text id="rsv1"
            1
          /   \
         2     3
          \     \
           5     4
```

Output:

```python id="rsv2"
[1,3,4]
```

---

# Why?

Visible nodes from right side:

```text id="rsv3"
Level 0 → 1
Level 1 → 3
Level 2 → 4
```

Node `2` and `5` are hidden behind right-side nodes.

---

# Constraints

* `0 <= number of nodes <= 100`
* `-100 <= Node.val <= 100`

---

# 2. Diagram

# Tree

```text id="rsv4"
            1
          /   \
         2     3
          \     \
           5     4
```

---

# Level-by-Level View

```text id="rsv5"
Level 0:
[1]       → visible = 1

Level 1:
[2,3]     → visible = 3

Level 2:
[5,4]     → visible = 4
```

---

# Key Observation

```text id="rsv6"
Rightmost node of each level is visible.
```

This is the biggest interview insight.

---

# BFS Visualization

```text id="rsv7"
Queue levels:

[1]
[2,3]
[5,4]
```

Take:

* last node from every level.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="rsv8"
root = [1,2,3,null,5,null,4]
```

Output:

```python id="rsv9"
[1,3,4]
```

---

## Example 2 (Single Node)

Input:

```text id="rsv10"
root = [1]
```

Output:

```python id="rsv11"
[1]
```

---

## Example 3 (Empty Tree)

Input:

```text id="rsv12"
root = []
```

Output:

```python id="rsv13"
[]
```

---

# 4. Intuition & Pattern Recognition

This is a classic:

```text id="rsv14"
BFS level traversal problem
```

Very similar to:

Binary Tree Level Order Traversal

---

# Core Insight

At each level:

```text id="rsv15"
Only the LAST node matters.
```

Because from the right side:

* rightmost node blocks others.

---

# Main Idea

Using BFS:

1. Process one level at a time
2. Track last node processed
3. Add it to result

---

# Important Interview Recognition

Whenever problem says:

* visible nodes
* left view
* right view
* per-level selection

Think:

```text id="rsv16"
BFS by levels
```

---

# Alternative DFS Insight

If we traverse:

```text id="rsv17"
Root → Right → Left
```

then first node visited at each depth is visible.

This gives elegant DFS solution too.

---

# 5. Simpler Version

---

# Simplest Version

```text id="rsv18"
    1
```

Output:

```python id="rsv19"
[1]
```

---

# Slightly Harder

```text id="rsv20"
      1
     / \
    2   3
```

Right side:

```text id="rsv21"
1
3
```

Output:

```python id="rsv22"
[1,3]
```

---

# Related Simpler Problems

### 1. Binary Tree Level Order Traversal

LeetCode: Binary Tree Level Order Traversal

Core BFS level traversal.

---

### 2. Binary Tree Zigzag Level Order Traversal

LeetCode: Binary Tree Zigzag Level Order Traversal

Another BFS-by-level variation.

---

### 3. Average of Levels in Binary Tree

LeetCode: Average of Levels in Binary Tree

Per-level BFS aggregation.

---

# Thinking Progression

```text id="rsv23"
Need nodes visible per level
        ↓
Process tree level-by-level
        ↓
Take rightmost node
```

---

# 6. Brute Force

## Idea

For every level:

* collect all nodes
* take last node

Using DFS height-based traversal.

---

# Brute Force Complexity

## Time

```text id="rsv24"
O(n^2)
```

Repeated level traversals.

---

## Space

```text id="rsv25"
O(h)
```

---

# 7. Optimal Solution

# BFS Level Traversal

```python id="rsv26"
from collections import deque

class Solution:

    def rightSideView(self, root):

        if not root:
            return []

        result = []

        queue = deque([root])

        while queue:

            level_size = len(queue)

            for i in range(level_size):

                node = queue.popleft()

                # Last node of level
                if i == level_size - 1:
                    result.append(node.val)

                # Add children
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
```

---

# Why This Works

At each BFS iteration:

```text id="rsv27"
Queue contains one full level
```

The last processed node:

```text id="rsv28"
i == level_size - 1
```

is the rightmost node.

---

# Important Interview Insight

We do NOT need:

* actual geometric visibility
* coordinates

Just:

* rightmost node per level.

---

# Elegant DFS Solution

## Idea

Traverse:

```text id="rsv29"
Root → Right → Left
```

First node visited at each depth becomes visible.

---

# DFS Code

```python id="rsv30"
class Solution:

    def rightSideView(self, root):

        result = []

        def dfs(node, depth):

            if not node:
                return

            # First node at this depth
            if depth == len(result):
                result.append(node.val)

            # Visit right first
            dfs(node.right, depth + 1)

            dfs(node.left, depth + 1)

        dfs(root, 0)

        return result
```

---

# Why DFS Works

Since we visit:

```text id="rsv31"
Right subtree before left subtree
```

the first node encountered at every depth:

* is the visible rightmost node.

---

# Complexity

## BFS

* Time: `O(n)`
* Space: `O(n)`

## DFS

* Time: `O(n)`
* Space: `O(h)`

---

# 8. Step-by-Step Trace

Input:

```text id="rsv32"
            1
          /   \
         2     3
          \     \
           5     4
```

---

# BFS Trace

---

# Level 0

Queue:

```text id="rsv33"
[1]
```

Rightmost:

```python id="rsv34"
1
```

Result:

```python id="rsv35"
[1]
```

---

# Level 1

Queue:

```text id="rsv36"
[2,3]
```

Rightmost:

```python id="rsv37"
3
```

Result:

```python id="rsv38"
[1,3]
```

---

# Level 2

Queue:

```text id="rsv39"
[5,4]
```

Rightmost:

```python id="rsv40"
4
```

Final:

```python id="rsv41"
[1,3,4]
```

---

# 9. Related Problems

### 1. Binary Tree Level Order Traversal

Core BFS-by-level traversal.

---

### 2. Binary Tree Left Side View

Same idea but take leftmost node.

---

### 3. Binary Tree Zigzag Level Order Traversal

Another BFS level-order variation.

---

### 4. Average of Levels in Binary Tree

Per-level aggregation problem.

---

### 5. Find Largest Value in Each Tree Row

Another BFS-per-level selection problem.
