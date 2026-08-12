# Path Sum

LeetCode 112 — Tree + DFS

---

# 1. Problem Statement

Given the `root` of a binary tree and an integer `targetSum`:

Return `true` if the tree has a **root-to-leaf** path such that:

```text id="k7p2qx"
sum of node values
along the path
== targetSum
```

Otherwise return `false`.

---

## Important

A valid path must:

* start at root
* end at a leaf

Leaf node:

* no left child
* no right child

---

## Example

```text id="r5x0mj"
            5
          /   \
         4     8
        /     / \
       11    13  4
      /  \         \
     7    2         1
```

Target:

```text id="jlwm8ak"
22
```

Valid path:

```text id="jlwm0al"
5 -> 4 -> 11 -> 2
```

Sum:

```text id="jlwm2al"
22
```

Answer:

```text id="jlwm4al"
True
```

---

## Constraints

* Number of nodes: `[0, 5000]`
* `-1000 <= Node.val <= 1000`

Important:

* negative values possible
* must end at leaf

---

# 2. Diagram

```text id="jlwm6al"
                5
              /   \
             4     8
            /     / \
          11    13   4
         /  \          \
        7    2          1
```

Root-to-leaf sums:

```text id="’wini8al"
5+4+11+7  = 27
5+4+11+2  = 22  ✓
5+8+13    = 26
5+8+4+1   = 18
```

---

# 3. Example I/O

## Example 1

### Input

```text id="’wini1am"
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22
```

### Output

```text id="’wini3am"
true
```

---

## Example 2

### Input

```text id="’wini5am"
root = [1,2,3]
targetSum = 5
```

### Output

```text id="’wini7am"
false
```

Possible sums:

* `1+2 = 3`
* `1+3 = 4`

No 5.

---

## Edge Case

### Input

```text id="’wini9am"
root = []
targetSum = 0
```

### Output

```text id="’wini0an"
false
```

---

# 4. Intuition & Pattern Recognition

This is a classic:

```text id="’wini2an"
Root-to-leaf DFS traversal
```

problem.

---

# Core Observation

At every node:

* subtract current value from target
* recurse downward

Eventually:

```text id="’wini4an"
If leaf node makes remaining sum = 0
→ valid path exists
```

---

# Pattern Recognition Signals

Keywords:

* “root-to-leaf”
* “path sum”
* “target sum”

Usually means:

```text id="’wini6an"
DFS recursion
```

because:

* naturally explores paths.

---

# Key Recursive Insight

Suppose:

```text id="’wini8an"
target = 22
current node = 5
```

Then remaining target becomes:

```text id="’wini1ao"
22 - 5 = 17
```

Children now need:

* path sum = 17

---

# 5. Simpler Version

---

## Simplest Tree

```text id="’wini3ao"
    5
```

Target:

```text id="’wini5ao"
5
```

Leaf + exact match:

* return `True`

---

# Slightly Bigger

```text id="’wini7ao"
    1
   /
  2
```

Target:

```text id="’wini9ao"
3
```

At node 1:

* remaining = 2

At node 2:

* remaining = 0 AND leaf

Answer:

* True

---

# Simpler Thinking Path

### Start with target sum

↓

### Consume current node value

↓

### Pass remaining target downward

↓

### At leaf:

* remaining must become zero

---

# 6. Brute Force

Generate all root-to-leaf paths:

1. compute sums
2. compare with target

---

# Complexity

Extra path storage unnecessary.

---

# 7. Optimal Solution

# DFS Recursive Solution

---

# Key Logic

At leaf:

```python id="’wini0ap"
remaining_sum == node.val
```

means valid path found.

---

# Optimal Code

```python id="’wini2ap"
class Solution:

    def hasPathSum(self, root, targetSum):

        if not root:
            return False

        # leaf node
        if not root.left and not root.right:

            return targetSum == root.val

        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining)
            or
            self.hasPathSum(root.right, remaining)
        )
```

---

# Why This Works

Each recursive call asks:

```text id="’wini4ap"
"Can my subtree complete
the remaining sum?"
```

Eventually:

* leaf either satisfies target
* or fails.

---

# Complexity

## Time

```text id="’wini6ap"
O(n)
```

Worst case visit all nodes.

---

## Space

```text id="’wini8ap"
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

```text id="’wini1aq"
                5
              /   \
             4     8
            /     / \
          11    13   4
         /  \          \
        7    2          1
```

Target:

```text id="’wini3aq"
22
```

---

# DFS Trace

---

## Node 5

Remaining:

```text id="’wini5aq"
22 - 5 = 17
```

---

## Node 4

Remaining:

```text id="’wini7aq"
17 - 4 = 13
```

---

## Node 11

Remaining:

```text id="’wini9aq"
13 - 11 = 2
```

---

## Node 7

Remaining:

```text id="’wini0ar"
2 - 7 = -5
```

Leaf:

* not zero

Return:

* False

---

## Node 2

Remaining:

```text id="’wini2ar"
2 - 2 = 0
```

Leaf AND zero:

```text id="’wini4ar"
True
```

Propagates upward.

Final answer:

```text id="’wini6ar"
True
```

---

# 9. Related Problems

---

### Path Sum II

Return all valid root-to-leaf paths.

---

### Path Sum III

Path can start/end anywhere.

---

### Binary Tree Maximum Path Sum

Advanced path aggregation problem.

---

### Sum Root to Leaf Numbers

Accumulate path values recursively.

---

### Pseudo-Palindromic Paths in a Binary Tree

Root-to-leaf DFS path property checking.
