# Binary Tree Maximum Path Sum

LeetCode 124 — Tree + DFS + Postorder Traversal

---

# 1. Problem Statement

Given the `root` of a binary tree, return the **maximum path sum**.

A path:

* can start at ANY node
* can end at ANY node
* must follow parent-child connections
* cannot reuse nodes

---

# Important

Path does NOT need to:

* start at root
* end at leaf

Path can be:

```text id="btmps_1"
left subtree -> node -> right subtree
```

---

## Example

```text id="btmps_2"
        1
       / \
      2   3
```

Best path:

```text id="btmps_3"
2 -> 1 -> 3
```

Sum:

```text id="btmps_4"
6
```

---

## Example 2

```text id="btmps_5"
         -10
         /  \
        9    20
            /  \
           15   7
```

Best path:

```text id="btmps_6"
15 -> 20 -> 7
```

Sum:

```text id="btmps_7"
42
```

---

## Constraints

* Number of nodes: `[1, 3 * 10^4]`
* `-1000 <= Node.val <= 1000`

Important:

* negative values exist
* path can stop anywhere

---

# 2. Diagram

```text id="btmps_8"
             -10
             /  \
            9    20
                /  \
               15   7
```

At node `20`:

```text id="btmps_9"
left gain  = 15
right gain = 7
```

Possible path through 20:

```text id="btmps_10"
15 + 20 + 7 = 42
```

This becomes global answer.

---

# 3. Example I/O

## Example 1

### Input

```text id="btmps_11"
root = [1,2,3]
```

### Output

```text id="btmps_12"
6
```

---

## Example 2

### Input

```text id="btmps_13"
root = [-10,9,20,null,null,15,7]
```

### Output

```text id="btmps_14"
42
```

---

# 4. Intuition & Pattern Recognition

This is one of the MOST important tree DP problems.

The key trick:

```text id="btmps_15"
At each node:
there are TWO different meanings.
```

---

# Meaning 1 — Global Path Through Node

Possible complete path:

```text id="btmps_16"
left_gain + node + right_gain
```

This may become answer.

---

# Meaning 2 — Return Value to Parent

Parent can only continue ONE direction.

So return:

```text id="btmps_17"
node + max(left_gain, right_gain)
```

NOT both.

This distinction is the entire problem.

---

# Visual

```text id="btmps_18"
        node
       /    \
   left     right
```

Global candidate:

```text id="btmps_19"
left + node + right
```

Returned upward:

```text id="btmps_20"
node + max(left,right)
```

because parent path cannot branch twice.

---

# Negative Value Insight

If subtree contribution is negative:

```text id="btmps_21"
ignore it completely
```

Why include something that reduces sum?

So:

```python id="btmps_22"
max(0, subtree_gain)
```

---

# Pattern Recognition Signals

Keywords:

* “maximum path”
* “any node”
* “tree path sum”

Usually means:

```text id="btmps_23"
Tree DP + Postorder DFS
```

---

# 5. Simpler Version

---

## Simpler Problem

### Diameter of Binary Tree

At every node:

```text id="btmps_24"
left_height + right_height
```

---

# This Problem Extension

Instead of heights:

* use path sums

And:

* ignore negative branches.

---

# Simpler Thinking Path

### Diameter

```text id="btmps_25"
left + right
```

↓

### Maximum Path Sum

```text id="btmps_26"
left_gain + node + right_gain
```

↓

### Return only one side upward

because path cannot fork upward.

---

# 6. Brute Force

For every node:

1. explore all possible paths
2. compute sums

Explodes combinatorially.

---

# Complexity

Very inefficient.

---

# 7. Optimal Solution

# Postorder DFS

---

# Key DFS Meaning

```python id="btmps_27"
dfs(node)
returns:
maximum gain extending upward
```

Meaning:

* best single-branch path including node.

---

# Optimal Code

```python id="btmps_28"
class Solution:

    def maxPathSum(self, root):

        self.answer = float('-inf')

        def dfs(node):

            if not node:
                return 0

            # ignore negative branches
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # best path THROUGH current node
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

            # return single branch upward
            return node.val + max(
                left_gain,
                right_gain
            )

        dfs(root)

        return self.answer
```

---

# Why `max(0, dfs(...))`?

Suppose subtree contributes:

```text id="btmps_29"
-15
```

Adding it only worsens answer.

So:

* discard it
* use 0 instead.

---

# Why Return Only One Side?

Suppose parent also wants to continue path.

If current node already uses:

* left branch
* right branch

then adding parent would create:

```text id="btmps_30"
3-way fork
```

Invalid path.

So upward path must remain linear.

---

# Complexity

## Time

```text id="btmps_31"
O(n)
```

Each node visited once.

---

## Space

```text id="btmps_32"
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

```text id="btmps_33"
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

```text id="btmps_34"
left = 0
right = 0

current_path = 15
answer = 15

return 15
```

---

## Node 7

```text id="btmps_35"
current_path = 7
answer = 15

return 7
```

---

## Node 20

```text id="btmps_36"
left_gain = 15
right_gain = 7
```

Current path:

```text id="btmps_37"
15 + 20 + 7 = 42
```

Update:

```text id="btmps_38"
answer = 42
```

Return upward:

```text id="btmps_39"
20 + max(15,7)
= 35
```

---

## Node 9

```text id="btmps_40"
current_path = 9
```

---

## Node -10

```text id="btmps_41"
left_gain = 9
right_gain = 35
```

Current path:

```text id="btmps_42"
9 + (-10) + 35
= 34
```

Global answer remains:

```text id="btmps_43"
42
```

Final answer:

```text id="btmps_44"
42
```

---

# 9. Related Problems

---

### Diameter of Binary Tree

Same postorder aggregation structure.

---

### Maximum Depth of Binary Tree

Foundation subtree recursion.

---

### Path Sum III

Path-sum reasoning in trees.

---

### Longest Univalue Path

Diameter-style path merging with conditions.

---

### House Robber III

Tree DP with multiple recursive states.
