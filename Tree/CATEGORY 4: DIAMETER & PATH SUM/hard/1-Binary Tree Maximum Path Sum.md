# Binary Tree Maximum Path Sum

LeetCode 124 — Tree + DFS + Postorder Traversal

---

# 1. Problem Statement

Given the `root` of a binary tree, return the **maximum path sum**.

A path:

* can start at ANY node
* can end at ANY node
* must follow parent-child connections
* cannot revisit nodes

---

# Important

The path:

* does NOT need to start at root
* does NOT need to end at leaf
* can pass through a node and use BOTH children

Path length is based on:

* node values sum
* not edge count

---

## Example 1

```text id="bmps2_1"
        1
       / \
      2   3
```

Best path:

```text id="bmps2_2"
2 -> 1 -> 3
```

Sum:

```text id="bmps2_3"
6
```

---

## Example 2

```text id="bmps2_4"
         -10
         /  \
        9    20
            /  \
           15   7
```

Best path:

```text id="bmps2_5"
15 -> 20 -> 7
```

Sum:

```text id="bmps2_6"
42
```

---

## Constraints

* Number of nodes: `[1, 3 * 10^4]`
* `-1000 <= Node.val <= 1000`

Important:

* negative numbers exist
* answer may be a single node

---

# 2. Diagram

```text id="bmps2_7"
             -10
             /  \
            9    20
                /  \
               15   7
```

At node `20`:

```text id="bmps2_8"
left gain  = 15
right gain = 7
```

Possible full path:

```text id="bmps2_9"
15 + 20 + 7 = 42
```

This becomes global answer.

---

# Core Insight Diagram

At every node:

```text id="bmps2_10"
        node
       /    \
   left     right
```

Two different meanings exist.

---

## Meaning 1 — Full Path Through Node

Possible answer candidate:

```text id="bmps2_11"
left_gain + node + right_gain
```

This path:

* starts in left subtree
* passes through node
* ends in right subtree

---

## Meaning 2 — Value Returned to Parent

Parent can continue only ONE side.

So return:

```text id="bmps2_12"
node + max(left_gain, right_gain)
```

NOT both.

This distinction is the entire problem.

---

# 3. Example I/O

## Example 1

### Input

```text id="bmps2_13"
root = [1,2,3]
```

### Output

```text id="bmps2_14"
6
```

---

## Example 2

### Input

```text id="bmps2_15"
root = [-10,9,20,null,null,15,7]
```

### Output

```text id="bmps2_16"
42
```

---

# 4. Intuition & Pattern Recognition

This problem is a classic:

```text id="bmps2_17"
Tree DP / Postorder DFS
```

problem.

---

# Key Observation

At every node:

* compute best gain from left subtree
* compute best gain from right subtree

Then:

* combine them through current node.

---

# Important Negative Value Insight

Suppose subtree gain:

```text id="bmps2_18"
-25
```

Adding it only hurts answer.

So:

```python id="bmps2_19"
max(0, subtree_gain)
```

Meaning:

* ignore negative paths completely.

---

# Pattern Recognition Signals

Keywords:

* “maximum path”
* “any node”
* “tree path sum”

Usually means:

```text id="bmps2_20"
Postorder DFS
```

because:

* child information required first.

---

# 5. Simpler Version

---

## Simpler Problem

### Diameter of Binary Tree

At each node:

```text id="bmps2_21"
left_height + right_height
```

---

# This Problem Extension

Replace:

* heights

with:

* path gains

And:

* discard negative branches.

---

# Simpler Thinking Path

### Diameter

```text id="bmps2_22"
left + right
```

↓

### Maximum Path Sum

```text id="bmps2_23"
left_gain + node + right_gain
```

↓

### Return only one side upward

because parent path cannot fork.

---

# 6. Brute Force

For every node:

1. explore all possible paths
2. compute sums

Very expensive.

---

# Complexity

Can become exponential.

---

# 7. Optimal Solution

# Postorder DFS

---

# Key DFS Meaning

```python id="bmps2_24"
dfs(node)
returns:
maximum gain extending upward
```

Meaning:

* best single branch path including current node.

---

# Optimal Code

```python id="bmps2_25"
class Solution:

    def maxPathSum(self, root):

        self.answer = float('-inf')

        def dfs(node):

            if not node:
                return 0

            # ignore negative branches
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # full path through current node
            current_path = (
                node.val
                + left_gain
                + right_gain
            )

            # update global answer
            self.answer = max(
                self.answer,
                current_path
            )

            # return ONE branch upward
            return node.val + max(
                left_gain,
                right_gain
            )

        dfs(root)

        return self.answer
```

---

# Why Return Only One Side?

Suppose parent also wants continuation.

If current node returns:

* left branch
* AND right branch

then parent path becomes:

```text id="bmps2_26"
3-way split
```

Invalid.

A path must remain linear.

---

# Why Use `max(0, gain)`?

Negative subtree decreases total sum.

So:

* better to exclude it entirely.

---

# Complexity

## Time

```text id="bmps2_27"
O(n)
```

Each node visited once.

---

## Space

```text id="bmps2_28"
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

```text id="bmps2_29"
         -10
         /  \
        9    20
            /  \
           15   7
```

---

# DFS Bottom-Up

---

## Node 15

```text id="bmps2_30"
left = 0
right = 0

current_path = 15
answer = 15

return 15
```

---

## Node 7

```text id="bmps2_31"
current_path = 7
```

---

## Node 20

```text id="bmps2_32"
left_gain = 15
right_gain = 7
```

Current full path:

```text id="bmps2_33"
15 + 20 + 7 = 42
```

Update:

```text id="bmps2_34"
answer = 42
```

Return upward:

```text id="bmps2_35"
20 + max(15,7)
= 35
```

---

## Node -10

```text id="bmps2_36"
left_gain = 9
right_gain = 35
```

Current path:

```text id="bmps2_37"
9 + (-10) + 35
= 34
```

Global answer remains:

```text id="bmps2_38"
42
```

Final answer:

```text id="bmps2_39"
42
```

---

# 9. Related Problems

---

### Diameter of Binary Tree

Same postorder path-merging pattern.

---

### Longest Univalue Path

Path merging with value constraints.

---

### Maximum Depth of Binary Tree

Foundation subtree recursion.

---

### Path Sum III

Path-sum reasoning on trees.

---

### House Robber III

Tree DP with recursive state transitions.
