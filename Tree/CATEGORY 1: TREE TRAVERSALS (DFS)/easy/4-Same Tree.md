# Same Tree

## 1. Problem Statement with Example

Given the roots of two binary trees `p` and `q`, return `True` if they are the **same tree**, otherwise return `False`.

Two binary trees are considered the same if:

1. They have the same structure
2. Corresponding nodes have the same values

LeetCode: Same Tree

---

### Example

Input:

```text id="1l8zw5"
p = [1,2,3]
q = [1,2,3]
```

Tree:

```text id="6j4g0k"
    1
   / \
  2   3
```

Output:

```python id="1oy6lr"
True
```

Because:

* structure matches
* all corresponding values match

---

### Constraints

* Number of nodes in both trees: `0 <= n <= 100`
* `-10^4 <= Node.val <= 10^4`

---

# 2. Diagram

## Same Trees

```text id="6v8u9r"
Tree p:             Tree q:

    1                   1
   / \                 / \
  2   3               2   3
```

Result:

```python id="k09vl7"
True
```

---

## Different Trees

```text id="vwmb67"
Tree p:             Tree q:

    1                   1
   /                     \
  2                       2
```

Result:

```python id="q8yxx1"
False
```

Even though values exist,
structure differs.

---

# 3. Example I/O

## Example 1 (Typical)

Input:

```text id="3mjlwm"
p = [1,2,3]
q = [1,2,3]
```

Output:

```python id="s65l8r"
True
```

Explanation:

* Every node matches.

---

## Example 2 (Different Structure)

Input:

```text id="q7dxm0"
p = [1,2]
q = [1,null,2]
```

Output:

```python id="7p3m7w"
False
```

Explanation:

* Left child vs right child mismatch.

---

## Example 3 (Different Values)

Input:

```text id="o4hzn1"
p = [1,2,1]
q = [1,1,2]
```

Output:

```python id="0n6k4r"
False
```

Explanation:

* Same structure
* Different node values

---

# 4. Intuition & Pattern Recognition

This is a classic **tree DFS comparison** problem.

Signal:

> “Check if two trees are identical”

Immediately think:

```text id="0slbl5"
Compare nodes recursively
```

At every step:

* current values must match
* left subtrees must match
* right subtrees must match

---

## Core recursive idea

Two trees are same iff:

```text id="n1b2z6"
1. Current nodes equal
2. Left subtrees equal
3. Right subtrees equal
```

---

## Interview recognition

Whenever problem says:

* identical trees
* compare trees
* symmetric structure
* subtree equality

Think:

* DFS recursion
* simultaneous traversal

---

## Mental model

Compare both trees together:

```text id="rj6ovv"
(p node) ↔ (q node)
```

At every recursive call:

* both NULL → valid
* one NULL → invalid
* values differ → invalid

Otherwise continue recursively.

---

# 5. Simpler Version

## Simplest Version

Compare just two single nodes.

```text id="xht3jl"
p = 5
q = 5
```

Answer:

```python id="l5eb8n"
True
```

Now extend:

* compare children too
* recursively entire tree

---

## Related simpler problems

### 1. Maximum Depth of Binary Tree

LeetCode: Maximum Depth of Binary Tree

Uses DFS recursion on tree.

Difference:

* computes height instead of comparing nodes.

---

### 2. Symmetric Tree

LeetCode: Symmetric Tree

Very similar.

Difference:

* compares mirrored children:

  * left.left ↔ right.right
  * left.right ↔ right.left

---

## Thinking progression

```text id="i3g7kw"
Compare current nodes
    ↓
Compare left subtrees
    ↓
Compare right subtrees
    ↓
Combine results with AND
```

---

# 6. Brute Force

One brute approach:

1. Serialize both trees
2. Compare serialized arrays/strings

Example preorder serialization:

```text id="jlwm5j"
1,2,null,null,3,null,null
```

If serialized outputs equal → trees equal.

---

## Brute Force Code

```python id="m8x6yl"
class Solution:
    def isSameTree(self, p, q):

        def serialize(node):

            if not node:
                return ["null"]

            return (
                [node.val]
                + serialize(node.left)
                + serialize(node.right)
            )

        return serialize(p) == serialize(q)
```

---

## Complexity

* Time: `O(n)`
* Space: `O(n)`

Extra serialization storage used.

---

# 7. Optimal Solution

## Recursive DFS (Most Interview Friendly)

```python id="jlwm6v"
class Solution:
    def isSameTree(self, p, q):

        # Both nodes are null
        if not p and not q:
            return True

        # One node is null
        if not p or not q:
            return False

        # Values differ
        if p.val != q.val:
            return False

        # Compare left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )
```

---

## Why this works

For trees to be identical:

```text id="5c5c2s"
Current nodes equal
AND
Left subtrees equal
AND
Right subtrees equal
```

If any condition fails:

* whole comparison fails

---

## Iterative BFS Solution

```python id="xg9ksm"
from collections import deque

class Solution:
    def isSameTree(self, p, q):

        queue = deque([(p, q)])

        while queue:

            node1, node2 = queue.popleft()

            # Both null
            if not node1 and not node2:
                continue

            # One null
            if not node1 or not node2:
                return False

            # Value mismatch
            if node1.val != node2.val:
                return False

            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True
```

---

## Complexity

### Recursive

* Time: `O(n)`
* Space: `O(h)`

### Iterative

* Time: `O(n)`
* Space: `O(n)`

---

# 8. Step-by-Step Trace

Input:

```text id="11mbc8"
p = [1,2,3]
q = [1,2,3]
```

Trees:

```text id="5s1c0r"
    1
   / \
  2   3
```

---

## Recursive Trace

| Step | p Node | q Node | Result |
| ---- | ------ | ------ | ------ |
| 1    | 1      | 1      | equal  |
| 2    | 2      | 2      | equal  |
| 3    | NULL   | NULL   | True   |
| 4    | NULL   | NULL   | True   |
| 5    | 3      | 3      | equal  |
| 6    | NULL   | NULL   | True   |
| 7    | NULL   | NULL   | True   |

Final:

```python id="4y1gkj"
True
```

---

# 9. Related Problems

### 1. Symmetric Tree

Very similar recursive comparison, but mirrored.

---

### 2. Subtree of Another Tree

Uses Same Tree logic repeatedly on subtrees.

---

### 3. Maximum Depth of Binary Tree

Basic DFS recursion on trees.

---

### 4. Invert Binary Tree

Another recursive tree manipulation problem.

---

### 5. Symmetric Tree

Core pattern of comparing recursive structures.
