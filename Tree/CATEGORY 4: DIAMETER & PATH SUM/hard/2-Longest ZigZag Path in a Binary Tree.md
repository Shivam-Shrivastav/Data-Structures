# Longest ZigZag Path in a Binary Tree

LeetCode: Longest ZigZag Path in a Binary Tree

## 1. Problem Statement with Example

You are given the root of a binary tree.

A **ZigZag path** means:

* If you move left, next move must be right.
* If you move right, next move must be left.
* Continue alternating directions.

The **length** of a ZigZag path = number of edges visited.

Return the **longest ZigZag path length** in the tree.

### Example

```text
        1
       / \
      2   3
       \
        4
       /
      5
       \
        6
```

One ZigZag path:

```text
2 -> 4 -> 5 -> 6
R    L    R
```

Length = 3 edges.

### Constraints

* Number of nodes: up to 5 * 10^4
* Need better than O(N²)
* DFS per node is acceptable
* Recursion depth may matter in skewed trees

---

# 2. Diagram

```text
Suppose we are at node 4

        4
       / \
      5   x
       \
        6

If previous move was RIGHT:
we now MUST go LEFT

If previous move was LEFT:
we now MUST go RIGHT
```

DFS state:

```text
(node, direction, currentLength)

direction =
- LEFT  -> previous move was left
- RIGHT -> previous move was right
```

---

# 3. Example I/O

## Example 1

### Input

```text
        1
       / \
      2   3
       \
        4
       /
      5
       \
        6
```

### Output

```text
3
```

### Why?

Path:

```text
2 -> 4 -> 5 -> 6
R    L    R
```

3 alternating edges.

---

## Example 2 (Edge Case)

### Input

```text
1
```

### Output

```text
0
```

### Why?

No edges exist.

---

# 4. Intuition & Pattern Recognition

This is a **Tree DFS + State Tracking** problem.

### Key observation

At every node:

* If previous move was LEFT:

  * next valid move = RIGHT
* If previous move was RIGHT:

  * next valid move = LEFT

So the DFS must remember:

```text
1. current node
2. previous direction
3. current zigzag length
```

### Interview recognition signal

Whenever you see:

* “alternate”
* “switch direction”
* “turn by turn”
* “cannot repeat same action”

Think:

```text
DFS/BFS with STATE
```

Very similar to:

* alternating parity
* alternating colors
* alternating moves

---

# 5. Simpler Version

## Simplest Version

### Question

Find longest path going only LEFT repeatedly.

Easy DFS.

---

## Next Upgrade

Find longest path where direction alternates.

Now previous direction matters.

So state becomes:

```text
(node, prevDirection)
```

---

## Related simpler LeetCode questions

### 1. Maximum Depth of Binary Tree

Learn basic tree DFS traversal.

### 2. Diameter of Binary Tree

Learn:

* compute answer globally during DFS
* path-based tree thinking

### 3. Binary Tree Longest Consecutive Sequence

Tree DFS carrying state from parent.

### Transition to this problem

```text
Depth problem:
only node matters

Consecutive sequence:
(node + previous value)

ZigZag:
(node + previous direction)
```

That is the entire jump.

---

# 6. Brute Force

## Idea

Start DFS from every node:

* try starting LEFT
* try starting RIGHT

For every node, explore maximum ZigZag.

### Complexity

For each node, we may traverse many nodes again.

```text
Time:  O(N²)
Space: O(H)
```

(H = tree height)

---

# 7. Optimal Solution

## Core Idea

At every node:

* Continue ZigZag in opposite direction
* Restart length when same direction repeats

We do ONE DFS traversal.

---

## Clean Interview Code (Java)

```java
class Solution {

    int ans = 0;

    public int longestZigZag(TreeNode root) {

        dfs(root.left, true, 1);
        dfs(root.right, false, 1);

        return ans;
    }

    private void dfs(TreeNode node, boolean cameFromLeft, int length) {

        if (node == null) {
            return;
        }

        ans = Math.max(ans, length);

        if (cameFromLeft) {

            // must go right to continue zigzag
            dfs(node.right, false, length + 1);

            // restart from left child
            dfs(node.left, true, 1);

        } else {

            // must go left to continue zigzag
            dfs(node.left, true, length + 1);

            // restart from right child
            dfs(node.right, false, 1);
        }
    }
}
```

---

## Complexity

```text
Time:  O(N)
Space: O(H)
```

* Each node visited constant number of times
* H = recursion stack

---

# 8. Step-by-Step Trace

Tree:

```text
        1
       / \
      2   3
       \
        4
       /
      5
       \
        6
```

---

## Initial Calls

```text
dfs(2, LEFT, 1)
dfs(3, RIGHT, 1)
```

---

## Traversal Table

| Node | Prev Direction | Length | Action   |
| ---- | -------------- | ------ | -------- |
| 2    | LEFT           | 1      | go RIGHT |
| 4    | RIGHT          | 2      | go LEFT  |
| 5    | LEFT           | 3      | go RIGHT |
| 6    | RIGHT          | 4      | end      |

But answer counts edges:

```text
4 nodes visited
=> 3 edges
```

Global max becomes:

```text
3
```

---

# 9. Related Problems

### 1. Diameter of Binary Tree

Tree path computation using DFS.

---

### 2. Binary Tree Longest Consecutive Sequence

Carry parent state while traversing.

---

### 3. Longest Univalue Path

Longest path satisfying a condition.

---

### 4. All Nodes Distance K in Binary Tree

Tree traversal with additional traversal state.

---

### 5. Diameter of N-Ary Tree

Generalization of longest-path DFS thinking.
