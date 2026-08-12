# Unique Binary Search Trees II

Generate **all structurally unique BSTs** that store values from `1` to `n`.

This is a classic **Catalan Number + Divide & Conquer Recursion** problem.

---

# 1. Problem Statement with Example

Given an integer `n`, return **all unique BSTs** containing values from:

```text id="ynct7m"
1 ... n
```

Return the root nodes of all possible BSTs.

A BST must satisfy:

```text id="aj5j2s"
left < root < right
```

---

## Example

Input:

```text id="h5hm2l"
n = 3
```

Output:

```text id="i1jjlwm"
[
  [1,null,2,null,3],
  [1,null,3,2],
  [2,1,3],
  [3,1,null,null,2],
  [3,2,null,1]
]
```

These are the 5 unique BSTs possible.

---

# 2. Diagram

For:

```text id="jjlwm8"
n = 3
```

Choose every number as root.

---

## Root = 1

Left subtree:

```text id="8h8a5m"
empty
```

Right subtree formed from:

```text id="0ktj3q"
[2,3]
```

```text id="xz8e4v"
    1
     \
      ?
```

---

## Root = 2

Left from `[1]`

Right from `[3]`

```text id="zdxn0u"
    2
   / \
  1   3
```

---

## Root = 3

Mirror of root=1 case.

```text id="iwlx4n"
      3
     /
    ?
```

---

# 3. Example I/O

## Example 1

Input:

```text id="e6aq9w"
n = 1
```

Output:

```text id="m3ltxn"
[
  [1]
]
```

Only one BST possible.

---

## Example 2

Input:

```text id="t3hnsu"
n = 2
```

Output:

```text id="r0ux4m"
[
  [1,null,2],
  [2,1]
]
```

Possible trees:

```text id="ccj6pc"
1         2
 \       /
  2     1
```

---

# 4. Intuition & Pattern Recognition

This is a **recursive construction problem**.

Key observation:

```text id="l9zn6q"
Every value can become root
```

If root is `i`:

* left subtree must use:

```text id="0o4pnm"
[start ... i-1]
```

* right subtree must use:

```text id="b3e7m2"
[i+1 ... end]
```

Now recursively generate all left trees and all right trees.

Then combine them.

---

## Pattern Recognition Signals

If problem says:

* “Generate all trees”
* “All possible BSTs”
* “Construct all combinations”

Think:

```text id="o7t9y8"
Divide & Conquer Recursion
```

---

## Interview Thinking

Say:

> “For every number, I can treat it as root. Then recursively generate all left BSTs and all right BSTs, and combine every pair.”

---

# 5. Simpler Version

---

## Simplest Problem

### “How many unique BSTs exist?”

LeetCode:

* Unique Binary Search Trees (LC 96)

That problem only asks for count.

This problem asks to actually build trees.

---

## Simpler Thinking

### If only one node

```text id="sx2fqo"
[1]
```

Only one BST.

---

### If two nodes

Possible roots:

```text id="pk9cqv"
1 or 2
```

Construct manually.

---

### Extend to n

For every root:

* recursively construct left
* recursively construct right
* combine all

---

## Relation to LC 96

LC 96:

```text id="xymj0h"
count(left) * count(right)
```

LC 95:

```text id="s1jq2r"
actually generate all left/right trees
```

Same recursion structure.

---

# 6. Brute Force

## Idea

Generate all binary trees and validate BST.

This is astronomically expensive.

---

## Complexity

Number of binary trees grows exponentially.

Very impractical.

---

# 7. Optimal Solution

## Core Recursive Function

Define:

```text id="1v1vpi"
build(start, end)
```

Meaning:

> Generate all BSTs using values from `start` to `end`.

---

## Base Case

If:

```text id="1sz06q"
start > end
```

return:

```text id="f6lkpg"
[None]
```

Important because:

* empty subtree is valid during combinations.

---

## Recursive Construction

For every root:

```text id="c9n7yn"
root = i
```

Generate:

```text id="d6k2f0"
leftTrees  = build(start, i-1)
rightTrees = build(i+1, end)
```

Now combine every pair.

---

# Optimal Code

```python id="e2znf4"
class Solution:
    def generateTrees(self, n):

        def build(start, end):

            # no nodes possible
            if start > end:
                return [None]

            result = []

            # choose every value as root
            for rootVal in range(start, end + 1):

                # all possible left subtrees
                leftTrees = build(start, rootVal - 1)

                # all possible right subtrees
                rightTrees = build(rootVal + 1, end)

                # combine every left/right pair
                for left in leftTrees:
                    for right in rightTrees:

                        root = TreeNode(rootVal)

                        root.left = left
                        root.right = right

                        result.append(root)

            return result

        return build(1, n)
```

---

# Complexity

Number of BSTs:

Catalan Number.

Approx:

```text id="4t8otq"
O(4^n / n^(3/2))
```

---

## Time Complexity

```text id="lvcj0g"
O(Cn * n)
```

Where:

* `Cn` = nth Catalan number

---

## Space Complexity

```text id="5u8m4t"
O(Cn * n)
```

Needed to store all trees.

---

# 8. Step-by-Step Trace

Example:

```text id="x64pxw"
n = 3
```

Call:

```text id="6d7hig"
build(1,3)
```

---

## Choose root = 1

Left:

```text id="z2pn3n"
build(1,0) = [None]
```

Right:

```text id="z3lypn"
build(2,3)
```

Possible right trees:

```text id="rx77hu"
2
 \
  3
```

and

```text id="0xnl33"
  3
 /
2
```

Attach both to root=1.

---

## Choose root = 2

Left:

```text id="9zjgto"
[1]
```

Right:

```text id="5wx4g6"
[3]
```

Tree:

```text id="t7cr2r"
    2
   / \
  1   3
```

---

## Choose root = 3

Mirror of root=1 case.

---

Total trees:

```text id="5p7b9g"
5
```

---

# 9. Related Problems

## 1. Unique Binary Search Trees (LC 96)

Same recursion idea but counting instead of building.

---

## 2. Different Ways to Add Parentheses

Generate all possible recursive structures by partitioning around each operator.

---

## 3. Full Binary Trees

Generate all valid tree combinations recursively.

---

## 4. Construct Binary Tree from Traversals

Tree construction recursion pattern.

---

## 5. Expression Add Operators

Recursive generation of all valid structures/combinations.
