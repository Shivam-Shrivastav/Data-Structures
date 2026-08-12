# Lowest Common Ancestor of a Binary Tree III (Premium)

LeetCode Premium: Lowest Common Ancestor of a Binary Tree III

---

# 1. Problem Statement with Example

You are given two nodes `p` and `q` in a binary tree.

Each node contains:

```java id="bbavt0"
Node {
    int val;
    Node left;
    Node right;
    Node parent;
}
```

Return their:

```text id="z1d4q8"
Lowest Common Ancestor (LCA)
```

---

# Key Difference

Unlike normal LCA problems:

```text id="v4n7m2"
You are NOT given the root
```

But each node has:

```text id="j7u5w1"
parent pointer
```

---

# Example

```text id="s8x2m6"
           3
         /   \
        5     1
       / \
      6   2
```

Find:

```text id="p0k5r9"
p = 6
q = 2
```

Answer:

```text id="y2t8w4"
5
```

because:

* 5 is lowest node containing both.

---

# 2. Diagram

Paths upward:

```text id="d7m1x3"
6 -> 5 -> 3
2 -> 5 -> 3
```

First common node:

```text id="x8q4u2"
5
```

That is LCA.

---

# Key Insight

Because we have parent pointers:

```text id="u5n7p1"
tree becomes like linked list upward
```

We can move upward from nodes directly.

---

# 3. Example I/O

## Example 1

### Input

```text id="n4x7u8"
p = 5
q = 1
```

### Output

```text id="q8m2v5"
3
```

---

## Example 2

### Input

```text id="v0t6r3"
p = 5
q = 4
```

### Output

```text id="c9w1m7"
5
```

---

## Example 3

### Input

```text id="j2x8u6"
p = 1
q = 1
```

### Output

```text id="f5r9n0"
1
```

---

# 4. Intuition & Pattern Recognition

This problem is actually:

```text id="w7m3u2"
Intersection of Two Linked Lists
```

in disguise.

---

# Why?

Suppose:

```text id="d5q8m1"
p path:
p -> parent -> parent -> root

q path:
q -> parent -> parent -> root
```

Eventually both paths merge.

Exactly like:

```text id="f2v7n4"
Y-shaped linked lists
```

---

# Brilliant Trick

Use two pointers:

```text id="t8k5u3"
a starts at p
b starts at q
```

Move upward.

When pointer becomes null:

```text id="g1x4w7"
redirect to other node
```

Eventually they meet at LCA.

Same trick as:

```text id="p9m2u6"
Intersection of Two Linked Lists
```

---

# Interview Recognition Signal

Whenever you see:

```text id="k7u4n8"
parent pointer
```

Think:

```text id="v3m8x1"
move upward instead of DFS from root
```

And if two upward paths merge:

```text id="m5q7u2"
linked list intersection trick
```

---

# 5. Simpler Version

---

## Simplest Version

### Question

Find depth of a node using parent pointers.

Easy:

```text id="r8u1w4"
keep moving upward
```

---

## Upgrade

Now find first common ancestor.

Naive idea:

```text id="w2n5x8"
store all ancestors of p in set
walk upward from q
```

Works.

---

## Better Insight

This is identical to:

```text id="d9m4u7"
finding intersection of two linked lists
```

Use two pointers with switching trick.

---

# Simpler Related Problems

### 1. Intersection of Two Linked Lists

Exact same pointer trick.

---

### 2. Lowest Common Ancestor of a Binary Tree

Standard DFS LCA.

---

### 3. Lowest Common Ancestor of a Binary Search Tree

BST-optimized LCA.

---

## Transition to this problem

```text id="j6r2x9"
Normal LCA:
go downward from root

LCA III:
go upward using parent pointers
```

---

# 6. Brute Force

## Idea

1. Store all ancestors of p in HashSet
2. Move upward from q
3. First common node = LCA

---

# Complexity

```text id="f1u8m3"
Time:  O(H)
Space: O(H)
```

Where:

* `H` = tree height

---

# 7. Optimal Solution

## Core Idea

Use linked-list intersection trick.

---

# Why Switching Works

Suppose:

```text id="t4m7u2"
distance(p -> LCA) = a
distance(q -> LCA) = b
```

After switching:

both pointers travel:

```text id="m9x3u1"
a + b
```

So they align automatically.

---

# Clean Interview Code (Java)

```java id="n7u2x5"
class Solution {

    public Node lowestCommonAncestor(Node p, Node q) {

        Node a = p;
        Node b = q;

        while (a != b) {

            // move upward
            a = (a == null) ? q : a.parent;

            b = (b == null) ? p : b.parent;
        }

        return a;
    }
}
```

---

# Complexity

```text id="v8m4x2"
Time:  O(H)
Space: O(1)
```

Excellent interview solution.

---

# 8. Step-by-Step Trace

Tree:

```text id="u3n5w8"
           3
         /   \
        5     1
       / \
      6   2
```

Find:

```text id="m2u7x4"
p = 6
q = 2
```

---

# Upward Paths

```text id="j1m9u6"
6 -> 5 -> 3
2 -> 5 -> 3
```

---

# Pointer Simulation

| a | b |
| - | - |
| 6 | 2 |
| 5 | 5 |

Pointers meet.

Answer:

```text id="q7u4m1"
5
```

---

# Harder Example

```text id="r5n8u3"
p = 6
q = 1
```

Paths:

```text id="y4m1u8"
6 -> 5 -> 3
1 -> 3
```

After switching:

Both eventually meet at:

```text id="k8u2m5"
3
```

---

# 9. Related Problems

### 1. Intersection of Two Linked Lists

Exact same pointer-switching idea.

---

### 2. Lowest Common Ancestor of a Binary Tree

Classic recursive LCA.

---

### 3. Lowest Common Ancestor of a Binary Tree II

LCA with missing-node validation.

---

### 4. Binary Tree Paths

Ancestor/path traversal concepts.

---

### 5. Step-By-Step Directions From a Binary Tree Node to Another

Advanced path/LCA combination problem.
