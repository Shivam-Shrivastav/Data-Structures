# Populating Next Right Pointers in Each Node II

LeetCode 117 — Tree + Level Order Traversal / Pointer Manipulation

---

# 1. Problem Statement

You are given a binary tree (NOT necessarily perfect).

Each node has:

* `val`
* `left`
* `right`
* `next`

Your task is to connect each node’s `next` pointer to its immediate right node on the same level.

If there is no node to the right, set `next = NULL`.

You must do this using **constant extra space** (excluding recursion stack).

Return the root after connecting all pointers.

---

## Example

Given:

```text
        1
      /   \
     2     3
    / \      \
   4   5      7
```

After connecting:

```text
        1 -> NULL
      /   \
     2 -> 3 -> NULL
    / \      \
   4 -> 5 -> 7 -> NULL
```

---

## Constraints

* Number of nodes: `[0, 6000]`
* `-100 <= Node.val <= 100`
* Tree is NOT perfect
* Must use O(1) extra space

---

# 2. Diagram

```text
Level 0:
        1 -----------------> NULL

Level 1:
      /   \
     2 -----------------> 3 -------> NULL

Level 2:
    / \      \
   4 --> 5 --> 7 -------> NULL
```

Key challenge:

```text
5 and 7 are NOT siblings.
Need cross-parent linking.
```

That is why simple sibling logic from LC 116 fails.

---

# 3. Example I/O

## Example 1

### Input

```text
root = [1,2,3,4,5,null,7]
```

### Output

```text
[1,#,2,3,#,4,5,7,#]
```

### Explanation

* `2.next = 3`
* `4.next = 5`
* `5.next = 7`

---

## Example 2 (Edge Case)

### Input

```text
root = []
```

### Output

```text
[]
```

### Explanation

Empty tree.

---

# 4. Intuition & Pattern Recognition

This is a **level traversal** problem.

But instead of using:

* queue (BFS)
* extra memory

we use:

* already-built `next` pointers
* to traverse current level
* while building next level

---

## Key Observation

Once a level is connected:

```text
2 -> 3 -> NULL
```

we can traverse that entire level using:

```python
curr = curr.next
```

So:

* current level helps us build next level
* no queue required

---

## Interview Recognition Signals

### Signals for this pattern

* “Connect nodes level-wise”
* “Use constant extra space”
* “Binary tree”
* “Next pointers”

This usually means:

```text
Use already established next pointers
to traverse levels.
```

---

# 5. Simpler Version

---

## Simpler Problem → LC 116

### Populating Next Right Pointers in Each Node

In LC 116:

* tree is PERFECT
* every parent has:

  * left child
  * right child

Connections become easy:

```python
node.left.next = node.right
node.right.next = node.next.left
```

---

## Why LC 117 is Harder

In this problem:

* tree may be sparse
* child may not exist
* cannot assume sibling exists

Example:

```text
    2 ----> 3
   /          \
  4            7
```

Need:

```text
4.next = 7
```

even though:

* different parents
* missing children

---

## Simpler Thinking Path

### Step 1

Perfect tree:

* direct sibling linking

↓

### Step 2

General tree:

* must dynamically discover next available child

↓

### Step 3

Need a “linked list building” process per level

That leads naturally to:

* dummy node
* tail pointer

---

# 6. Brute Force

Use BFS queue.

---

## Idea

For every level:

1. process all nodes
2. connect adjacent nodes
3. push children into queue

---

## Code

```python
from collections import deque

class Solution:
    def connect(self, root):

        if not root:
            return root

        q = deque([root])

        while q:

            size = len(q)
            prev = None

            for _ in range(size):

                node = q.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            prev.next = None

        return root
```

---

## Complexity

### Time

```text
O(n)
```

### Space

```text
O(n)
```

(queue)

---

# 7. Optimal Solution (O(1) Space)

## Core Idea

For each level:

* traverse using current `next`
* build next level linked list

We use:

* `dummy` → start of next level
* `tail` → last connected node

---

## Visual

Current level:

```text
2 -> 3 -> NULL
```

While traversing:

* collect children

Build:

```text
4 -> 5 -> 7 -> NULL
```

Then move to:

```python
curr = dummy.next
```

---

# Optimal Code

```python
class Solution:
    def connect(self, root):

        curr = root   # current level start

        while curr:

            dummy = Node(0)   # start of next level
            tail = dummy      # tail for building next level

            # traverse current level
            while curr:

                # connect left child
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next

                # connect right child
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                # move horizontally in current level
                curr = curr.next

            # move to next level
            curr = dummy.next

        return root
```

---

# Complexity

## Time

```text
O(n)
```

Each node visited once.

---

## Space

```text
O(1)
```

No queue.

---

# 8. Step-by-Step Trace

Input:

```text
        1
      /   \
     2     3
    / \      \
   4   5      7
```

---

## Level 0

```text
curr = 1
dummy -> NULL
tail = dummy
```

Process `1`

```text
tail.next = 2
tail = 2

tail.next = 3
tail = 3
```

Built next level:

```text
2 -> 3
```

Move:

```text
curr = dummy.next = 2
```

---

## Level 1

Current:

```text
2 -> 3
```

Initialize:

```text
dummy -> NULL
tail = dummy
```

---

### Process 2

```text
connect 4
connect 5
```

Built:

```text
4 -> 5
```

---

### Move to 3

(using `curr.next`)

Process `3`

```text
connect 7
```

Built:

```text
4 -> 5 -> 7
```

Move:

```text
curr = 4
```

---

## Level 2

Current:

```text
4 -> 5 -> 7
```

No children.

End.

---

# 9. Related Problems

---

### Populating Next Right Pointers in Each Node

Simpler version using perfect tree properties.

---

### Binary Tree Right Side View

Level traversal pattern; process nodes level by level.

---

### Binary Tree Level Order Traversal

Classic BFS foundation for understanding this problem.

---

### Flatten Binary Tree to Linked List

Pointer manipulation in trees.

---

### Vertical Order Traversal of a Binary Tree

Advanced traversal organization beyond standard BFS.
