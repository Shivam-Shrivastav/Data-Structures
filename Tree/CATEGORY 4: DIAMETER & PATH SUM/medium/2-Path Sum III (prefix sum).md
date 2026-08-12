# Path Sum III

LeetCode 437 — Tree + Prefix Sum + DFS

---

# 1. Problem Statement

Given:

* the `root` of a binary tree
* an integer `targetSum`

Return the number of paths where:

```text id="ps3_1"
sum of node values == targetSum
```

---

# Important

A valid path:

* must move downward
* parent → child only
* does NOT need to start at root
* does NOT need to end at leaf

---

## Example

```text id="ps3_2"
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1
```

Target:

```text id="ps3_3"
8
```

Valid paths:

```text id="ps3_4"
5 -> 3
5 -> 2 -> 1
-3 -> 11
```

Answer:

```text id="ps3_5"
3
```

---

## Constraints

* Number of nodes: `[0, 1000]`
* `-10^9 <= Node.val <= 10^9`

Important:

* negative numbers exist
* sliding window DOES NOT work

---

# 2. Diagram

```text id="ps3_6"
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1
```

Highlighted valid paths:

```text id="ps3_7"
5 -> 3         = 8
5 -> 2 -> 1    = 8
-3 -> 11       = 8
```

---

# 3. Example I/O

## Example 1

### Input

```text id="ps3_8"
root = [10,5,-3,3,2,null,11,3,-2,null,1]
targetSum = 8
```

### Output

```text id="ps3_9"
3
```

---

## Example 2

### Input

```text id="ps3_10"
root = [1]
targetSum = 1
```

### Output

```text id="ps3_11"
1
```

---

# 4. Intuition & Pattern Recognition

This problem is MUCH trickier than:

### Path Sum

because:

* path can start anywhere
* path can end anywhere
* only direction constraint exists

---

# Naive Thinking

At every node:

* start DFS
* explore all downward paths

Works but inefficient.

---

# Real Insight

This becomes identical to:

```text id="ps3_12"
Subarray Sum Equals K
```

but on a tree.

---

# Prefix Sum Idea

Suppose current path sum is:

```text id="ps3_13"
currSum
```

If earlier we had:

```text id="ps3_14"
currSum - target
```

then:

```text id="ps3_15"
(current path segment)
=
target
```

Exactly same prefix-sum trick as arrays.

---

# Visual Example

Suppose current root-path sums:

```text id="ps3_16"
10 -> 15 -> 18
```

Current sum:

```text id="ps3_17"
18
```

Target:

```text id="ps3_18"
8
```

Need earlier prefix:

```text id="ps3_19"
18 - 8 = 10
```

If prefix `10` existed:

* path between them sums to 8.

That path is:

```text id="ps3_20"
5 -> 3
```

---

# Pattern Recognition Signals

Keywords:

* “count paths”
* “sum equals k”
* “can start anywhere”
* “downward paths”

Usually means:

```text id="ps3_21"
Prefix Sum
```

especially with:

* sums
* counting
* arbitrary starting point

---

# 5. Simpler Version

---

## Simpler Problem

### Subarray Sum Equals K

Array version.

---

# Array Logic

If:

```text id="ps3_22"
prefixSum[j] - prefixSum[i] = target
```

then subarray:

* `i+1 → j`
* sums to target

---

# Tree Generalization

Root-to-current-node path behaves like:

* an array path

So:

* same prefix-sum logic works.

---

# Simpler Thinking Path

### Array prefix sums

↓

### Root-to-node path prefix sums

↓

### HashMap stores previous sums

↓

### Count valid path endings at current node

---

# 6. Brute Force

For every node:

1. start DFS
2. compute all downward path sums

---

# Complexity

## Time

```text id="ps3_23"
O(n^2)
```

Worst case skewed tree.

---

# 7. Optimal Solution

# Prefix Sum + DFS

---

# Core Formula

At current node:

```text id="ps3_24"
currSum - target
```

If this exists before:

* valid path found.

---

# HashMap Meaning

```python id="ps3_25"
prefix[prefix_sum]
=
how many times seen
```

---

# Optimal Code

```python id="ps3_26"
from collections import defaultdict

class Solution:

    def pathSum(self, root, targetSum):

        prefix = defaultdict(int)

        # important base case
        prefix[0] = 1

        self.count = 0

        def dfs(node, currSum):

            if not node:
                return

            # current prefix sum
            currSum += node.val

            # check valid path endings
            self.count += prefix[currSum - targetSum]

            # add current prefix
            prefix[currSum] += 1

            # recurse
            dfs(node.left, currSum)
            dfs(node.right, currSum)

            # BACKTRACK
            prefix[currSum] -= 1

        dfs(root, 0)

        return self.count
```

---

# Why `prefix[0] = 1`?

Suppose:

```text id="ps3_27"
currSum == target
```

Then:

```text id="ps3_28"
currSum - target = 0
```

Need one valid empty prefix.

Allows:

* paths starting from root.

---

# Why Backtracking Needed?

When returning from subtree:

* remove current path contribution

Otherwise:

* sibling subtree incorrectly sees prefixes.

This is VERY important.

---

# Complexity

## Time

```text id="ps3_29"
O(n)
```

Each node visited once.

---

## Space

```text id="ps3_30"
O(h)
```

Recursion stack + hashmap depth.

Worst case skewed:

* `O(n)`

---

# 8. Step-by-Step Trace

Input:

```text id="ps3_31"
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1
```

Target:

```text id="ps3_32"
8
```

---

# DFS Trace

---

## Node 10

```text id="ps3_33"
currSum = 10
need = 2
```

No match.

Store:

```text id="ps3_34"
prefix[10] += 1
```

---

## Node 5

```text id="ps3_35"
currSum = 15
need = 7
```

No match.

Store:

```text id="ps3_36"
prefix[15] += 1
```

---

## Node 3

```text id="ps3_37"
currSum = 18
need = 10
```

`prefix[10] = 1`

Found one valid path:

```text id="ps3_38"
5 -> 3
```

Count:

```text id="ps3_39"
1
```

---

## Node 1

Path:

```text id="ps3_40"
5 -> 2 -> 1
```

Again:

```text id="ps3_41"
currSum - target exists
```

Count becomes:

```text id="ps3_42"
2
```

---

## Node 11

Path:

```text id="ps3_43"
-3 -> 11
```

Count becomes:

```text id="ps3_44"
3
```

Final answer:

```text id="ps3_45"
3
```

---

# 9. Related Problems

---

### Subarray Sum Equals K

Array prefix-sum foundation for this problem.

---

### Path Sum

Root-to-leaf boolean version.

---

### Path Sum II

Return all valid root-to-leaf paths.

---

### Binary Tree Maximum Path Sum

Advanced path aggregation problem.

---

### Count Complete Tree Nodes

Another tree optimization using structure insights.
