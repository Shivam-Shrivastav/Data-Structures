# 876. Middle of the Linked List

## 1. Problem Statement with Example

Given the head of a singly linked list, return the **middle node**.

If there are **two middle nodes**, return the **second middle node**.

---

## Example

```text
Input:
1 → 2 → 3 → 4 → 5

Output:
3
```

---

## Even Length Example

```text
Input:
1 → 2 → 3 → 4 → 5 → 6

Output:
4
```

Because there are two middles:

* 3
* 4

We return the second one.

---

## Constraints

```text
1 <= number of nodes <= 100
```

Key observation:

* Need midpoint efficiently
* Single traversal preferred

---

# 2. Diagram

## Odd Length

```text
slow
 ↓
1 → 2 → 3 → 4 → 5
             ↑
            fast
```

Fast moves 2 steps.
Slow moves 1 step.

When fast reaches end:

* slow reaches middle.

---

## Even Length

```text
1 → 2 → 3 → 4 → 5 → 6
                ↑
              slow
```

Slow naturally lands on second middle.

---

# 3. Example I/O

## Example 1 (Odd Length)

### Input

```text
[1,2,3,4,5]
```

### Output

```text
[3,4,5]
```

### Why?

Middle node is `3`.

---

## Example 2 (Even Length)

### Input

```text
[1,2,3,4,5,6]
```

### Output

```text
[4,5,6]
```

### Why?

Two middles:

* 3
* 4

Return second middle (`4`).

---

## Example 3 (Edge Case)

### Input

```text
[1]
```

### Output

```text
[1]
```

Single node itself is middle.

---

# 4. Intuition & Pattern Recognition

## Biggest Clue

Whenever problem asks:

* middle
* midpoint
* half-way
* kth from end
* cycle

→ Think:

# Slow and Fast Pointer

---

## Core Idea

```text
slow moves 1 step
fast moves 2 steps
```

So:

```text
When fast finishes,
slow is halfway.
```

---

## Why Second Middle Automatically?

For even length:

```text
1 2 3 4 5 6
```

Fast becomes `None` after crossing end.

At that moment:

* slow is already at `4`.

Exactly what problem wants.

---

## Interview Recognition

If you see:

* “middle”
* “half”
* “single traversal preferred”

Immediately think:

# Tortoise and Hare Pattern

---

# 5. Simpler Version

## Simplest Approach

### Convert Linked List → Array

```python
arr = []
```

Store all nodes.

Return:

```python
arr[len(arr)//2]
```

Easy but extra space.

---

## Better Thinking

Can we avoid storing?

Need:

* one pointer for speed
* one pointer for position

Thus:

* fast pointer
* slow pointer

---

## Related Simpler Problems

### 1. Linked List Cycle

Introduces slow-fast movement.

---

### 2. Find kth Node From End

Uses pointer gap.

---

### 3. Happy Number

Hidden Floyd cycle detection.

---

## Thinking Evolution

```text
Store all nodes
      ↓
Need O(1) space
      ↓
Need midpoint tracking
      ↓
Fast/Slow pointers
```

---

# 6. Brute Force

## Idea

Store nodes in array.

Return middle index.

---

## Code

```python
class Solution:

    def middleNode(self, head):

        arr = []

        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        return arr[len(arr) // 2]
```

---

## Complexity

### Time

O(n)

### Space

O(n)

---

# 7. Optimal Solution

# Slow and Fast Pointer

---

## Core Idea

* slow → 1 step
* fast → 2 steps

When fast reaches end:

* slow reaches middle

---

## Code

```python
class Solution:

    def middleNode(self, head):

        slow = head
        fast = head

        # fast moves twice as fast
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow
```

---

## Why It Works

Suppose:

```text
slow speed = 1
fast speed = 2
```

If fast travels full list:

```text
slow travels half list
```

Thus slow reaches midpoint exactly.

---

## Complexity

### Time

O(n)

### Space

O(1)

---

# 8. Step-by-Step Trace

## Example

```text
1 → 2 → 3 → 4 → 5
```

---

| Step  | slow | fast |
| ----- | ---- | ---- |
| Start | 1    | 1    |
| 1     | 2    | 3    |
| 2     | 3    | 5    |

Next:

* fast.next = None

Loop stops.

Return:

```text
3
```

---

## Even Length Example

```text
1 → 2 → 3 → 4 → 5 → 6
```

---

| Step  | slow | fast |
| ----- | ---- | ---- |
| Start | 1    | 1    |
| 1     | 2    | 3    |
| 2     | 3    | 5    |
| 3     | 4    | None |

Return:

```text
4
```

(second middle)

---

# 9. Related Problems

## 1. Linked List Cycle

Classic fast/slow pointer problem.

---

## 2. Linked List Cycle II

Uses meeting point mathematics.

---

## 3. Palindrome Linked List

Uses middle finding + reverse.

---

## 4. Reorder List

Find middle before reversing second half.

---

## 5. Happy Number

Hidden cycle detection with fast/slow pointers.

---

# Interview One-Liner

> “Fast moves twice as quickly as slow, so when fast reaches the end, slow naturally reaches the middle.”
