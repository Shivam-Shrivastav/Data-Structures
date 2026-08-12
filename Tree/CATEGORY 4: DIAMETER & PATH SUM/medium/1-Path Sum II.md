# Path Sum II

LeetCode 113 — Tree + DFS + Backtracking

---

# 1. Problem Statement

Given:

* the `root` of a binary tree
* an integer `targetSum`

Return **all root-to-leaf paths** where:

```text id="6vb1mo"
sum of node values
== targetSum
```

Each path should be returned as a list of node values.

---

# Important

A valid path:

* starts at root
* ends at leaf

Leaf node:

* no children

---

## Example

```text id="zjlwm1"
                5
              /   \
             4     8
            /     / \
          11    13   4
         /  \       / \
        7    2     5   1
```

Target:

```text id="zjlwm2"
22
```

Valid paths:

```text id="zjlwm3"
5 -> 4 -> 11 -> 2
5 -> 8 -> 4 -> 5
```

Output:

```python id="zjlwm4"
[
  [5,4,11,2],
  [5,8,4,5]
]
```

---

## Constraints

* Number of nodes: `[0, 5000]`
* `-1000 <= Node.val <= 1000`

Important:

* must return ALL paths
* path copying/backtracking required

---

# 2. Diagram

```text id="zjlwm5"
                5
              /   \
             4     8
            /     / \
          11    13   4
         /  \       / \
        7    2     5   1
```

Root-to-leaf sums:

```text id="zjlwm6"
5+4+11+7 = 27
5+4+11+2 = 22 ✓
5+8+13 = 26
5+8+4+5 = 22 ✓
5+8+4+1 = 18
```

---

# 3. Example I/O

## Example 1

### Input

```text id="zjlwm7"
root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
targetSum = 22
```

### Output

```python id="zjlwm8"
[[5,4,11,2],[5,8,4,5]]
```

---

## Example 2

### Input

```text id="zjlwm9"
root = [1,2,3]
targetSum = 5
```

### Output

```python id="zjlwm10"
[]
```

No valid root-to-leaf path.

---

# 4. Intuition & Pattern Recognition

This is an extension of:

### Path Sum

LC 112:

* only asks IF path exists

LC 113:

* asks for ALL valid paths

---

# Core Difference

Now we must:

1. track current path
2. store successful paths
3. backtrack afterward

---

# Pattern Recognition Signals

Keywords:

* “all paths”
* “root-to-leaf”
* “return combinations”

Usually means:

```text id="zjlwm11"
DFS + Backtracking
```

---

# Core Insight

At every node:

* add node to current path
* recurse downward
* remove node before returning

That last step is:

```text id="zjlwm12"
Backtracking
```

---

# 5. Simpler Version

---

## Simpler Problem

### Path Sum

Only return:

* True / False

No path storage needed.

---

# This Problem Adds

Need:

* actual path construction

---

# Simpler Thinking Path

### Path Sum I

```python id="zjlwm13"
return True if path exists
```

↓

### Path Sum II

```python id="zjlwm14"
store all successful paths
```

↓

Need:

* current path array
* append/pop

---

# 6. Brute Force

Generate all root-to-leaf paths:

1. compute sum
2. filter valid ones

---

# Complexity

Could waste unnecessary computations.

---

# 7. Optimal Solution

# DFS + Backtracking

---

# Key DFS Meaning

```python id="zjlwm15"
dfs(node, remaining_sum, current_path)
```

At each node:

1. add node to path
2. subtract value
3. recurse
4. backtrack

---

# Optimal Code

```python id="zjlwm16"
class Solution:

    def pathSum(self, root, targetSum):

        res = []

        def dfs(node, remaining, path):

            if not node:
                return

            # include current node
            path.append(node.val)

            # leaf node
            if not node.left and not node.right:

                if remaining == node.val:

                    # copy current path
                    res.append(path[:])

            else:

                dfs(node.left,
                    remaining - node.val,
                    path)

                dfs(node.right,
                    remaining - node.val,
                    path)

            # backtrack
            path.pop()

        dfs(root, targetSum, [])

        return res
```

---

# Why `path[:]` Needed?

Because:

* `path` keeps changing during recursion

Need snapshot copy.

Without copying:

* all answers become corrupted.

---

# Why Backtracking Needed?

Suppose:

```text id="zjlwm17"
path = [5,4,11]
```

After exploring left child:

* must remove child before exploring sibling.

Otherwise:

* path becomes incorrect.

---

# Complexity

## Time

```text id="zjlwm18"
O(n)
```

Every node visited once.

Copying paths can add extra cost depending on output size.

---

## Space

```text id="zjlwm19"
O(h)
```

Recursion depth.

Ignoring output storage.

---

# 8. Step-by-Step Trace

Input:

```text id="zjlwm20"
                5
              /   \
             4     8
            /     / \
          11    13   4
         /  \       / \
        7    2     5   1
```

Target:

```text id="zjlwm21"
22
```

---

# DFS Trace

---

## Node 5

Path:

```text id="zjlwm22"
[5]
```

Remaining:

```text id="zjlwm23"
17
```

---

## Node 4

Path:

```text id="zjlwm24"
[5,4]
```

Remaining:

```text id="zjlwm25"
13
```

---

## Node 11

Path:

```text id="zjlwm26"
[5,4,11]
```

Remaining:

```text id="z’wini27"
2
```

---

## Node 7

Path:

```text id="z’wini28"
[5,4,11,7]
```

Remaining:

```text id="z’wini29"
-5
```

Invalid leaf.

Backtrack:

```text id="z’wini30"
[5,4,11]
```

---

## Node 2

Path:

```text id="z’wini31"
[5,4,11,2]
```

Remaining:

```text id="z’wini32"
0
```

Leaf + valid:

Store:

```python id="z’wini33"
[5,4,11,2]
```

---

Continue similarly:

Store:

```python id="z’wini34"
[5,8,4,5]
```

Final:

```python id="z’wini35"
[
 [5,4,11,2],
 [5,8,4,5]
]
```

---

# 9. Related Problems

---

### Path Sum

Boolean version of same root-to-leaf DFS.

---

### Path Sum III

Path can start/end anywhere.

---

### Combination Sum

Classic DFS + backtracking pattern.

---

### Binary Tree Paths

Generate all root-to-leaf paths.

---

### Pseudo-Palindromic Paths in a Binary Tree

Root-to-leaf DFS with path property checking.
