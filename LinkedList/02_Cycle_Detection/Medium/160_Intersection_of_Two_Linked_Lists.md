# 160. Intersection of Two Linked Lists

## 1. Problem Statement with Example

Given the heads of two singly linked lists `headA` and `headB`, return the node where the two lists intersect.

If the two linked lists have no intersection, return `None`.

### Important Clarification

* Intersection means **same node in memory**, not same value.
* After intersection, both linked lists share the same remaining nodes.

### Example

```text
List A: 4 → 1 \
                 8 → 4 → 5
List B:    5 → 6 → 1 /
```

The lists intersect at node with value `8`.

### Constraints

* Number of nodes can be large → need efficient solution.
* Must preserve original linked list structure.
* Follow-up expects:

  * Time: `O(m + n)`
  * Space: `O(1)`

---

# 2. Diagram

```text
headA
  |
  v
4 → 1 → 8 → 4 → 5
          ^
          |
5 → 6 → 1
          ^
          |
        headB
```

After node `8`, both lists are literally the same chain.

---

# 3. Example I/O

## Example 1 (Typical)

### Input

```text
A = [4,1,8,4,5]
B = [5,6,1,8,4,5]
Intersect at node value = 8
```

### Output

```text
8
```

### Why?

Both linked lists share the exact node starting from `8`.

---

## Example 2 (No Intersection)

### Input

```text
A = [1,2,3]
B = [4,5]
```

### Output

```text
None
```

### Why?

No common node exists.

---

## Example 3 (Edge Case)

### Input

```text
A = [1]
B = [1]
```

But these are different nodes.

### Output

```text
None
```

### Why?

Values same ≠ nodes same.

---

# 4. Intuition & Pattern Recognition

## Key Signal

Whenever problem says:

* “find common node”
* “shared tail”
* “same memory reference”
* “linked lists merge”

→ Think:

# **Two Pointer Alignment**

---

## Core Observation

If one list is longer:

```text
A length = 5
B length = 3
```

The longer list reaches the intersection later.

We need both pointers to traverse equal distance.

---

## Genius Trick

When pointer reaches end:

* redirect it to other list’s head

Eventually:

```text
Pointer A distance = lenA + lenB
Pointer B distance = lenB + lenA
```

So they become aligned automatically.

---

## Interview Thought Process

> “I need both pointers to cover same total distance without calculating lengths explicitly.”

That immediately hints at:

# Pointer switching trick

---

# 5. Simpler Version

## Simplest Problem

### “Find intersection of two equal-length linked lists.”

```text
1 → 2 → 8 → 9
3 → 4 → 8 → 9
```

Easy:

* Move both pointers together.
* First equal node = answer.

---

## Next Harder Version

### Different Lengths

```text
A: 1 → 2 → 3 → 8 → 9
B:      4 → 8 → 9
```

Need alignment first.

---

## Traditional Thinking

1. Find lengths
2. Move longer list ahead
3. Then move together

This works.

---

## Final Optimization

Instead of manually aligning:

```text
a = a.next else headB
b = b.next else headA
```

Automatic alignment happens.

---

## Related Simpler Problems

### 1. Cracking the Coding Interview style classic problem

Teaches pointer alignment.

### 2. Reverse Linked List

Builds pointer movement intuition.

### 3. Linked List Cycle

Uses elegant two-pointer synchronization.

### 4. Merge Two Sorted Lists

Teaches simultaneous traversal.

---

# 6. Brute Force

## Idea

For every node in A:

* Traverse all nodes in B
* Check if nodes are same.

---

## Code

```python
class Solution:
    def getIntersectionNode(self, headA, headB):

        a = headA

        while a:
            b = headB

            while b:
                if a == b:
                    return a
                b = b.next

            a = a.next

        return None
```

---

## Complexity

### Time

O(m \times n)

### Space

O(1)

Very slow.

---

# 7. Optimal Solution

## Best Approach — Two Pointer Switching

---

## Core Idea

When pointer reaches end:

* jump to other list’s head

Eventually both pointers travel equal total distance.

---

## Code

```python
class Solution:
    def getIntersectionNode(self, headA, headB):

        a = headA
        b = headB

        # Continue until both pointers become same
        while a != b:

            # If end reached, jump to other list
            a = a.next if a else headB

            # If end reached, jump to other list
            b = b.next if b else headA

        return a
```

---

## Why It Works

Suppose:

```text
A = 5 nodes
B = 3 nodes
```

Traversal becomes:

```text
Pointer A:
A + B

Pointer B:
B + A
```

Both travel same total distance.

Thus they meet at:

* intersection node OR
* `None`

---

## Complexity

### Time

O(m+n)

### Space

O(1)

---

# 8. Step-by-Step Trace

## Example

```text
A: 4 → 1 → 8 → 4 → 5
B: 5 → 6 → 1 → 8 → 4 → 5
```

---

| Step | Pointer A | Pointer B |
| ---- | --------- | --------- |
| 1    | 4         | 5         |
| 2    | 1         | 6         |
| 3    | 8         | 1         |
| 4    | 4         | 8         |
| 5    | 5         | 4         |
| 6    | None      | 5         |
| 7    | 5         | None      |
| 8    | 6         | 4         |
| 9    | 1         | 1         |
| 10   | 8         | 8         |

Pointers meet at node `8`.

---

# 9. Related Problems

## 1. Linked List Cycle

Uses fast/slow pointer synchronization.

---

## 2. Linked List Cycle II

Finds exact meeting/start node using pointer mathematics.

---

## 3. Palindrome Linked List

Uses slow/fast pointers + reversal.

---

## 4. Merge Two Sorted Lists

Simultaneous traversal of two linked lists.

---

## 5. Copy List with Random Pointer

Advanced linked-list pointer manipulation.

---

# Interview One-Liner

> “Switch heads when pointer reaches end so both pointers travel equal total distance and automatically align at the intersection.”
