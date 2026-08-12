# Longest Univalue Path

LeetCode 687 — Tree + DFS + Postorder Traversal

---

# 1. Problem Statement

Given the `root` of a binary tree:

Return the length of the **longest path** where:

* every node in the path has the SAME value.

The path:

* may or may not pass through root
* length measured in:

  * number of EDGES
  * not nodes

---

## Example

```text id="lup_1"
          5
         / \
        4   5
       / \   \
      1   1   5
```

Longest same-value path:

```text id="lup_2"
5 -> 5 -> 5
```

Edges:

```text id="lup_3"
2
```

Answer:

```text id="lup_4"
2
```

---

## Example 2

```text id="lup_5"
          1
         / \
        4   5
       / \   \
      4   4   5
```

Longest univalue path:

```text id="lup_6"
4 -> 4 -> 4
```

Edges:

```text id="lup_7"
2
```

---

## Constraints

* Number of nodes: `[0, 10^4]`
* `-1000 <= Node.val <= 1000`

Important:

* path must contain equal values ONLY
* path may bend through parent

---

# 2. Diagram

```text id="lup_8"
            1
           / \
          4   5
         / \   \
        4   4   5
```

At node `4`:

```text id="lup_9"
left chain  = 1
right chain = 1
```

Possible path through node:

```text id="lup_10"
1 + 1 = 2
```

---

# Key Insight Diagram

```text id="lup_11"
         parent(4)
          /    \
      4-chain  4-chain
```

If child value matches parent:

* extend chain

Else:

* chain breaks.

---

# 3. Example I/O

## Example 1

### Input

```text id="lup_12"
root = [5,4,5,1,1,null,5]
```

### Output

```text id="lup_13"
2
```

---

## Example 2

### Input

```text id="lup_14"
root = [1,4,5,4,4,null,5]
```

### Output

```text id="lup_15"
2
```

---

# 4. Intuition & Pattern Recognition

This problem is EXTREMELY similar to:

### Diameter of Binary Tree

But with:

* an extra constraint
* values must match.

---

# Core Observation

At every node:

* compute longest same-value chain from left
* compute longest same-value chain from right

If child value differs:

* chain length becomes 0

---

# Two Different Meanings Again

---

## Meaning 1 — Global Path Through Node

Possible answer:

```text id="lup_16"
left_chain + right_chain
```

---

## Meaning 2 — Return Value to Parent

Can only extend ONE direction upward:

```text id="lup_17"
max(left_chain, right_chain)
```

Exactly same pattern as:

* Diameter
* Binary Tree Maximum Path Sum

---

# Pattern Recognition Signals

Keywords:

* “longest path”
* “same value”
* “through node”

Usually means:

```text id="lup_18"
Postorder DFS
```

---

# 5. Simpler Version

---

## Simpler Problem

### Diameter of Binary Tree

Compute:

```text id="lup_19"
left_height + right_height
```

---

# This Problem Adds

Only extend path if:

```python id="lup_20"
child.val == node.val
```

Otherwise:

* contribution becomes zero.

---

# Simpler Thinking Path

### Diameter logic

↓

### Restrict connections to equal values

↓

### Build same-value chains

↓

### Merge left + right chains

---

# 6. Brute Force

For every node:

1. explore all same-value paths
2. compute maximum

Very inefficient.

---

# Complexity

Potentially exponential exploration.

---

# 7. Optimal Solution

# Postorder DFS

---

# Key DFS Meaning

```python id="lup_21"
dfs(node)
returns:
longest same-value chain upward
```

Meaning:

* max edges continuing upward through parent.

---

# Optimal Code

```python id="lup_22"
class Solution:

    def longestUnivaluePath(self, root):

        self.answer = 0

        def dfs(node):

            if not node:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            left_chain = 0
            right_chain = 0

            # extend left chain
            if node.left and node.left.val == node.val:

                left_chain = left_len + 1

            # extend right chain
            if node.right and node.right.val == node.val:

                right_chain = right_len + 1

            # possible full path through node
            self.answer = max(
                self.answer,
                left_chain + right_chain
            )

            # return ONE direction upward
            return max(left_chain, right_chain)

        dfs(root)

        return self.answer
```

---

# Why Return Only One Chain?

Parent can only continue:

* left OR right

Returning both would create:

* branching path
* invalid.

---

# Why Add `+1`?

Because:

* edge from current node to matching child contributes one edge.

---

# Complexity

## Time

```text id="lup_23"
O(n)
```

Each node visited once.

---

## Space

```text id="lup_24"
O(h)
```

Recursion stack.

Worst case:

* skewed tree → `O(n)`

Balanced:

* `O(log n)`

---

# 8. Step-by-Step Trace

Input:

```text id="lup_25"
            1
           / \
          4   5
         / \   \
        4   4   5
```

---

# DFS Bottom-Up

---

## Left Leaf 4

```text id="lup_26"
return 0
```

No child edges.

---

## Right Leaf 4

```text id="lup_27"
return 0
```

---

## Parent 4

Children match value:

```text id="lup_28"
left_chain = 1
right_chain = 1
```

Possible path:

```text id="lup_29"
1 + 1 = 2
```

Update answer:

```text id="lup_30"
2
```

Return upward:

```text id="lup_31"
max(1,1) = 1
```

---

## Node 5

Right child matches:

```text id="lup_32"
right_chain = 1
```

Path:

```text id="lup_33"
1
```

Global answer remains:

```text id="lup_34"
2
```

Final answer:

```text id="lup_35"
2
```

---

# 9. Related Problems

---

### Diameter of Binary Tree

Core path-merging recursion pattern.

---

### Binary Tree Maximum Path Sum

Advanced path aggregation problem.

---

### Maximum Depth of Binary Tree

Foundation subtree recursion.

---

### Balanced Binary Tree

Bottom-up DFS propagation.

---

### Path Sum III

Path-based tree traversal reasoning.
