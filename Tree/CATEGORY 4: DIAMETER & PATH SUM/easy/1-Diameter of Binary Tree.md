# Diameter of Binary Tree

LeetCode 543 — Tree + DFS + Postorder Traversal

---

# 1. Problem Statement

Given the `root` of a binary tree, return the **diameter** of the tree.

Diameter means:

```text id="d0k4pa"
Length of the longest path
between any two nodes.
```

Important:

* path may or may not pass through root
* length measured in:

  * number of EDGES
  * not nodes

---

## Example

```text id="2lm8wf"
         1
        / \
       2   3
      / \
     4   5
```

Longest path:

```text id="7sjq3v"
4 -> 2 -> 1 -> 3
```

Edges count:

```text id="jlwm9ad"
3
```

Answer:

```text id="jlwm1ae"
3
```

---

## Constraints

* Number of nodes: `[1, 10^4]`

Important:

* longest path can exist entirely inside subtree
* not necessarily through root

---

# 2. Diagram

```text id="jlwm3ae"
         1
        / \
       2   3
      / \
     4   5
```

At node `1`:

```text id="jlwm5ae"
left height = 2
right height = 1
```

Possible diameter through node:

```text id="jlwm7ae"
2 + 1 = 3
```

---

# Core Insight Diagram

For every node:

```text id="jlwm9ae"
possible diameter
=
left subtree height
+
right subtree height
```

---

# 3. Example I/O

## Example 1

### Input

```text id="jlwm0af"
root = [1,2,3,4,5]
```

### Output

```text id="jlwm2af"
3
```

---

## Example 2

### Input

```text id="jlwm4af"
root = [1,2]
```

### Output

```text id="jlwm6af"
1
```

---

# 4. Intuition & Pattern Recognition

This problem LOOKS like:

* longest path problem

But actual trick is:

```text id="jlwm8af"
Use subtree heights.
```

---

# Key Observation

Suppose at some node:

```text id="jlwm1ag"
left subtree height = L
right subtree height = R
```

Then longest path THROUGH this node:

```text id="jlwm3ag"
L + R
```

because:

* go deepest left
* pass through current node
* go deepest right

---

# Important Insight

Diameter:

* may pass through current node
* OR entirely inside left subtree
* OR entirely inside right subtree

So:

* check every node globally.

---

# Pattern Recognition Signals

Keywords:

* “longest path”
* “tree diameter”
* “path between nodes”

Usually means:

```text id="jlwm5ag"
Postorder DFS
```

because:

* children heights needed before parent.

---

# 5. Simpler Version

---

## Simpler Problem

### Maximum Depth of Binary Tree

Compute subtree heights.

---

# This Problem Extension

Instead of only:

```python id="jlwm7ag"
height = 1 + max(left,right)
```

we ALSO compute:

```python id="’wini9ag"
diameter = left + right
```

at every node.

---

# Simpler Thinking Path

### Step 1

Compute subtree heights

↓

### Step 2

At each node:

* combine left + right heights

↓

### Step 3

Track global maximum

---

# 6. Brute Force

For every node:

1. compute left subtree height
2. compute right subtree height
3. update answer

But height computation repeated many times.

---

# Complexity

```text id="jlwm0ah"
O(n^2)
```

Worst case skewed tree.

---

# 7. Optimal Solution

# Bottom-Up DFS

While computing height:

* simultaneously update diameter.

---

# Key DFS Meaning

```python id="jlwm2ah"
dfs(node)
returns:
height of subtree
```

While returning:

* update global diameter.

---

# Optimal Code

```python id="jlwm4ah"
class Solution:

    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def dfs(node):

            if not node:
                return 0

            # subtree heights
            left = dfs(node.left)
            right = dfs(node.right)

            # path through current node
            self.diameter = max(
                self.diameter,
                left + right
            )

            # return subtree height
            return 1 + max(left, right)

        dfs(root)

        return self.diameter
```

---

# Why This Works

At every node:

```text id="’wini6ah"
left + right
```

represents:

* longest path crossing current node.

Taking maximum across all nodes:

* gives overall diameter.

---

# Complexity

## Time

```text id="’wini8ah"
O(n)
```

Each node visited once.

---

## Space

```text id="
```


```text id="jlwm1ai"
O(h)
```

Recursion stack.

Worst case:

* skewed tree → `O(n)`

Balanced tree:

* `O(log n)`

---

# 8. Step-by-Step Trace

Input:

```text id="’wini3ai"
         1
        / \
       2   3
      / \
     4   5
```

---

# DFS Bottom-Up

---

## Node 4

```text id="’wini5ai"
left = 0
right = 0

diameter = 0
height = 1
```

---

## Node 5

```text id="’wini7ai"
height = 1
```

---

## Node 2

Children heights:

```text id="’wini9ai"
left = 1
right = 1
```

Possible diameter:

```text id="’wini0aj"
1 + 1 = 2
```

Update:

```text id="’wini2aj"
diameter = 2
```

Return height:

```text id="’wini4aj"
1 + max(1,1)
= 2
```

---

## Node 3

```text id="’wini6aj"
height = 1
```

---

## Node 1

Children heights:

```text id="’wini8aj"
left = 2
right = 1
```

Possible diameter:

```text id="’wini1ak"
2 + 1 = 3
```

Update:

```text id="’wini3ak"
diameter = 3
```

Return height:

```text id="’wini5ak"
3
```

Final answer:

```text id="’wini7ak"
3
```

---

# 9. Related Problems

---

### Maximum Depth of Binary Tree

Foundation subtree height recursion.

---

### Balanced Binary Tree

Uses bottom-up height propagation.

---

### Longest Univalue Path

Diameter-style path computation with constraints.

---

### Binary Tree Maximum Path Sum

Advanced path aggregation problem.

---

### Find Leaves of Binary Tree

Bottom-up DFS grouping using heights.
