# Delete the Middle Node of a Linked List

LeetCode 2095 — Delete the middle node of a linked list and return the modified head.

---

# 1. Problem Statement with Example

Given the `head` of a singly linked list, delete the middle node and return the head of the modified list.

### Middle Definition

If there are `n` nodes:

```text id="v4h1h3"
middle index = floor(n / 2)
```

(0-indexed)

---

## Example

```text id="4blw8m"
Input:
1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6

Output:
1 -> 3 -> 4 -> 1 -> 2 -> 6
```

Explanation:

* Total nodes = 7
* Middle index = 3
* Node value = 7
* Delete it

---

## Constraints

* `1 <= n <= 10^5`
* Must modify linked list in-place

---

# 2. Diagram

## Slow-Fast Pointer Visualization

```text id="pn4n0g"
List:
1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6

Initial:
slow = 1
fast = 1

Move:
slow +1 step
fast +2 steps

Iteration 1:
slow = 3
fast = 4

Iteration 2:
slow = 4
fast = 1

Iteration 3:
slow = 7
fast = 6

slow reached middle node.
```

To delete middle:

```text id="3oszh1"
Need node BEFORE middle

prev -> middle -> next

Change:
prev.next = middle.next
```

---

# 3. Example I/O

## Example 1 (Odd Length)

```text id="z0ajb9"
Input:
1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6

Output:
1 -> 3 -> 4 -> 1 -> 2 -> 6
```

Middle node = `7`

---

## Example 2 (Even Length)

```text id="w0xw8j"
Input:
1 -> 2 -> 3 -> 4

Output:
1 -> 2 -> 4
```

Length = 4

Middle index = `floor(4/2)=2`

Delete node `3`.

---

## Example 3 (Edge Case)

```text id="66dq4f"
Input:
1

Output:
[]
```

Single node itself is middle.

Deleting it gives empty list.

---

# 4. Intuition & Pattern Recognition

## Signals for This Pattern

Whenever problem says:

* "middle node"
* "nth from end"
* "one pass"
* linked list traversal optimization

Think:

> "slow-fast pointer"

---

# Core Insight

Fast moves 2x speed.

When fast reaches end:

```text id="5ojw2m"
slow is exactly at middle
```

But deletion requires:

```text id="x2xk6q"
node BEFORE middle
```

So maintain `prev`.

---

# Interview Recognition

## Array Version

Deleting middle in array:

```python id="rjlwm4"
arr.pop(len(arr)//2)
```

Easy because indexing exists.

---

## Linked List Difficulty

No indexing.

Need traversal.

Efficient way:

```text id="dd1nhz"
fast = 2x speed
slow = 1x speed
```

This naturally lands slow at midpoint.

---

# 5. Simpler Version

# Simplest Version

### Question

"Find middle node of linked list."

That is:

## Middle of the Linked List

---

## Difference Here

Instead of returning middle:

```text id="blwbxv"
Need to DELETE it
```

So now we also track:

```text id="uvr7tw"
prev node
```

---

# Simpler Problems That Lead Here

---

## 1. Middle of the Linked List

Learn midpoint detection.

---

## 2. Remove Linked List Elements

Learn deletion mechanics:

```text id="jjlwmn"
prev.next = curr.next
```

---

## 3. Remove Nth Node From End of List

More advanced deletion using two pointers.

Very related pattern.

---

# Thinking Progression

```text id="jtpohv"
Find middle
    ↓
Need node before middle
    ↓
Track prev pointer
    ↓
Reconnect links
```

---

# 6. Brute Force

## Idea

1. Traverse once → count length
2. Find middle index
3. Traverse again to node before middle
4. Delete

---

## Code

```python id="5kgm6z"
class Solution:
    def deleteMiddle(self, head):

        # Single node case
        if not head.next:
            return None

        # Count nodes
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        middle = n // 2

        # Reach node before middle
        curr = head

        for _ in range(middle - 1):
            curr = curr.next

        # Delete middle
        curr.next = curr.next.next

        return head
```

---

# Complexity

### Time

O(n)

(two traversals)

### Space

O(1)

---

# 7. Optimal Solution

# Idea

Use slow-fast pointers in ONE traversal.

Maintain:

* `slow` → middle
* `prev` → node before middle

When traversal ends:

```text id="g1z5kq"
prev.next = slow.next
```

---

# Optimal Code

```python id="y5r4hz"
class Solution:
    def deleteMiddle(self, head):

        # Edge case: single node
        if not head.next:
            return None

        slow = head
        fast = head
        prev = None

        # Find middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete middle node
        prev.next = slow.next

        return head
```

---

# Complexity

### Time

O(n)

### Space

O(1)

---

# 8. Step-by-Step Trace

## Input

```text id="cq7n4z"
1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
```

---

# Initial State

| slow | fast | prev |
| ---- | ---- | ---- |
| 1    | 1    | None |

---

# Iteration 1

| slow | fast | prev |
| ---- | ---- | ---- |
| 3    | 4    | 1    |

---

# Iteration 2

| slow | fast | prev |
| ---- | ---- | ---- |
| 4    | 1    | 3    |

---

# Iteration 3

| slow | fast | prev |
| ---- | ---- | ---- |
| 7    | 6    | 4    |

Fast cannot move further.

Middle = `7`

Prev = `4`

---

# Delete

```text id="4r25mq"
prev.next = slow.next
```

Becomes:

```text id="h0k7ck"
4 -> 1
```

Final list:

```text id="g6t4ul"
1 -> 3 -> 4 -> 1 -> 2 -> 6
```

---

# 9. Related Problems

## 1. Middle of the Linked List

Pure midpoint finding.

Foundation problem.

---

## 2. Remove Nth Node From End of List

Another important deletion + two pointer problem.

---

## 3. Linked List Cycle

Builds strong slow-fast pointer intuition.

---

## 4. Palindrome Linked List

Uses:

* midpoint
* reverse second half

Very closely related.

---

## 5. Reorder List

Advanced linked list manipulation using:

* midpoint
* reverse
* merge

Excellent follow-up question.
