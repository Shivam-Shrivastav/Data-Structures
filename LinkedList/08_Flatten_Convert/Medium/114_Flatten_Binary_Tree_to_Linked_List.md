# Flatten Binary Tree to Linked List

You are given the root of a binary tree.
Flatten the tree into a "linked list" **in-place** using the tree’s right pointers.

Rules:

* The flattened list should follow the **same order as preorder traversal**:
  Root → Left → Right
* Every node’s left pointer must become `null`
* Use the right pointer as the next pointer

---

## Example

Input tree:

```text
        1
       / \
      2   5
     / \   \
    3   4   6
```

Flattened tree:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

Result sequence:

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

Constraints:

* Number of nodes: `[0, 2000]`
* `-100 <= Node.val <= 100`
* Must modify tree in-place

---

# Diagram

## Core Idea

For every node:

1. Flatten left subtree
2. Flatten right subtree
3. Move left subtree to the right
4. Attach original right subtree at the end

```text
Before:

        1
       / \
      2   5
     / \
    3   4

After moving left to right:

        1
         \
          2
         / \
        3   4

Then append old right subtree:

1 -> 2 -> 3 -> 4 -> 5
```

---

# Example I/O

## Example 1

Input:

```python
root = [1,2,5,3,4,null,6]
```

Output:

```python
[1,null,2,null,3,null,4,null,5,null,6]
```

Explanation:

* Preorder traversal is:
  `1 -> 2 -> 3 -> 4 -> 5 -> 6`
* Flattened list follows same order.

---

## Example 2 (Edge Case)

Input:

```python
root = []
```

Output:

```python
[]
```

Explanation:

* Empty tree remains empty.

---

# Intuition & Pattern Recognition

This problem screams:

* “Modify tree in-place”
* “Follow preorder traversal”
* “Turn tree into linked list”

Key observation:

Preorder traversal order is already the desired linked list order.

So the real problem becomes:

> How do we rearrange pointers so the tree physically becomes preorder order?

Interview recognition:

Whenever you see:

* “flatten tree”
* “in-place”
* “linked list”
* “preorder”

Think:

* DFS recursion
* Rewire pointers during postorder processing

---

# Simpler Version

## Simplest Version

### Problem:

Return preorder traversal of a tree.

LeetCode:

* Binary Tree Preorder Traversal

You learn:

```text
Root -> Left -> Right
```

---

## Next Simpler Problem

Convert tree traversal into linked structure.

Example:

```text
1
 \
  2
   \
    3
```

You start understanding:

* right pointer acts like `next`
* left pointers become useless

---

## Final Jump to This Problem

Now instead of:

* storing preorder in array

You:

* physically rearrange pointers
* do it in-place

Main difficulty:

```text
Preserve original right subtree
while inserting left subtree.
```

---

# Brute Force

## Idea

1. Do preorder traversal
2. Store nodes in array
3. Reconnect sequentially

---

## Code

```python
class Solution:
    def flatten(self, root):
        nodes = []

        def preorder(node):
            if not node:
                return

            nodes.append(node)

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None
```

---

## Complexity

Time:

```text
O(n)
```

Space:

```text
O(n)
```

(extra array)

---

# Optimal Solution

## Core Trick

For each node:

* Flatten left subtree
* Flatten right subtree
* Put left subtree on right
* Find tail of new right chain
* Attach old right subtree

---

## Clean Interview Solution

```python
class Solution:
    def flatten(self, root):

        def dfs(node):
            if not node:
                return None

            # Leaf node itself is the tail
            if not node.left and not node.right:
                return node

            # Flatten left and right subtrees
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            # If left subtree exists
            if left_tail:

                # Save original right subtree
                temp = node.right

                # Move left subtree to right
                node.right = node.left
                node.left = None

                # Attach original right subtree
                left_tail.right = temp

            # Return the rightmost tail
            return right_tail or left_tail

        dfs(root)
```

---

# Complexity

Time:

```text
O(n)
```

Space:

```text
O(h)
```

* `h` = tree height
* recursion stack

Worst case:

```text
O(n)
```

Balanced tree:

```text
O(log n)
```

---

# Step-by-Step Trace

Input:

```text
        1
       / \
      2   5
     / \   \
    3   4   6
```

---

## Step 1

Process node `3`

```text
3 is leaf
return 3
```

---

## Step 2

Process node `4`

```text
4 is leaf
return 4
```

---

## Step 3

Process node `2`

Before:

```text
    2
   / \
  3   4
```

Move left to right:

```text
2
 \
  3
   \
    4
```

Return tail = `4`

---

## Step 4

Process node `6`

Leaf → return `6`

---

## Step 5

Process node `5`

```text
5
 \
  6
```

Return tail = `6`

---

## Step 6

Process node `1`

Before:

```text
        1
       / \
      2   5
```

After moving left subtree:

```text
1
 \
  2
   \
    3
     \
      4
```

Attach old right subtree:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

Done.

---

# Related Problems

1. Binary Tree Preorder Traversal
   Learn preorder DFS pattern.

2. Invert Binary Tree
   Practice recursive tree pointer manipulation.

3. Construct String from Binary Tree
   Uses preorder traversal structure thinking.

4. Serialize and Deserialize Binary Tree
   Heavy traversal + tree restructuring concepts.

5. Populating Next Right Pointers in Each Node
   Another pointer rewiring tree problem.
