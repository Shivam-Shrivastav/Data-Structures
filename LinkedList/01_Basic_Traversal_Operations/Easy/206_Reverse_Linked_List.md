# Reverse Linked List

LeetCode #206 — Easy
Pattern: Linked List, Pointer Manipulation

---

# 1. Problem Statement with Example

Given the head of a singly linked list, reverse the list and return the new head.

---

### Constraints

* Number of nodes: `0 <= n <= 5000`
* `-5000 <= Node.val <= 5000`

---

### Example

Input:

```text id="o3v8f8"
1 -> 2 -> 3 -> 4 -> 5
```

Output:

```text id="9c1l5p"
5 -> 4 -> 3 -> 2 -> 1
```

---

# 2. Diagram

Original:

```text id="5vr97o"
1 -> 2 -> 3 -> 4 -> 5 -> None
```

Goal:

```text id="c3f3m4"
5 -> 4 -> 3 -> 2 -> 1 -> None
```

---

## Core Reversal Step

Suppose:

```text id="xk7qg2"
prev = 1 <- 2

curr = 3 -> 4 -> 5
```

We reverse link:

```python id="9l3mdh"
curr.next = prev
```

After reversal:

```text id="ptpq0g"
1 <- 2 <- 3    4 -> 5
```

---

# 3. Example I/O

## Example 1 (Typical)

### Input

```text id="n3oqrb"
head = [1,2,3,4,5]
```

### Output

```text id="m4gn90"
[5,4,3,2,1]
```

---

## Example 2 (Edge Case)

### Input

```text id="trg6wd"
head = [1]
```

### Output

```text id="2r95a2"
[1]
```

### Why?

Single node reversed is same node.

---

# 4. Intuition & Pattern Recognition

### Core Problem

Every node points forward:

```text id="q7pqrc"
1 -> 2 -> 3
```

Need to make it point backward:

```text id="gnyu9u"
1 <- 2 <- 3
```

---

### Key Insight

While reversing:

* Do NOT lose next node
* Save next first

---

### Essential Variables

```python id="3t4nn6"
prev = None
curr = head
```

At each step:

```python id="eppmq0"
nextNode = curr.next
curr.next = prev
```

---

### Pattern Recognition

Whenever asked:

* Reverse linked list
* Reverse sublist
* Reverse k nodes

Think:

> “Three pointers: prev, curr, next”

---

### Interview Thinking

I need:

1. Save next node
2. Reverse pointer
3. Move pointers forward

---

# 5. Simpler Version

## Simplest Version

Reverse:

```text id="l38n2k"
1 -> 2
```

Steps:

```text id="m2l4r1"
2 -> 1
```

Core operation:

```python id="4ohpkx"
curr.next = prev
```

---

## How it scales

For larger list:

```text id="o2c36s"
1 -> 2 -> 3 -> 4
```

Repeat same reversal one node at a time.

---

## Related simpler problems

### 1. Reverse String

Same concept of reversing direction/order.

### 2. Middle of Linked List

Basic traversal practice.

### 3. Merge Two Sorted Lists

Pointer manipulation confidence.

### 4. Remove Linked List Elements

Pointer rewiring basics.

---

# 6. Brute Force

## Idea

* Store node values in array
* Reverse array
* Create new linked list

---

## Brute Force Code

```python id="ru9k9p"
class Solution:
    def reverseList(self, head):

        values = []

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        values.reverse()

        dummy = ListNode(0)
        tail = dummy

        for v in values:
            tail.next = ListNode(v)
            tail = tail.next

        return dummy.next
```

---

## Complexity

### Time

```text id="cfm1kl"
O(n)
```

### Space

```text id="8txzpb"
O(n)
```

---

# 7. Optimal Solution

## Key Insight

Reverse links in-place.

Maintain:

* `prev`
* `curr`
* `nextNode`

---

## Optimal Code (Iterative)

```python id="3k4qlq"
class Solution:
    def reverseList(self, head):

        prev = None
        curr = head

        while curr:

            # Save next node
            nextNode = curr.next

            # Reverse pointer
            curr.next = prev

            # Move prev and curr forward
            prev = curr
            curr = nextNode

        # prev becomes new head
        return prev
```

---

## Complexity

### Time

```text id="g63m9r"
O(n)
```

Each node visited once.

---

### Space

```text id="x8mjlwm"
O(1)
```

In-place reversal.

---

# 8. Step-by-Step Trace

Input:

```text id="jlwm3y"
1 -> 2 -> 3 -> None
```

---

| Step  | prev | curr | nextNode | Action         |
| ----- | ---- | ---- | -------- | -------------- |
| Start | None | 1    | -        | initialize     |
| 1     | None | 1    | 2        | reverse 1→None |
| 2     | 1    | 2    | 3        | reverse 2→1    |
| 3     | 2    | 3    | None     | reverse 3→2    |
| End   | 3    | None | -        | return prev    |

---

Final list:

```text id="8mb8c4"
3 -> 2 -> 1 -> None
```

---

# 9. Related Problems

### 1. Reverse Linked List II

Reverse only a sub-part of list.

### 2. Reverse Nodes in k-Group

Advanced grouped reversal.

### 3. Palindrome Linked List

Uses reverse second half technique.

### 4. Reorder List

Uses reverse + merge together.

### 5. Swap Nodes in Pairs

Another pointer rewiring problem.
