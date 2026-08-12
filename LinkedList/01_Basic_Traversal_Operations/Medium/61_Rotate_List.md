# 61. Rotate List

## 1. Problem Statement with Example

Given the `head` of a linked list, rotate the list to the right by `k` places.

Rotation means:

* take the last node
* move it to the front
* repeat `k` times

---

### Example

Input:

```text id="xw9q7z"
head = 1 → 2 → 3 → 4 → 5
k = 2
```

Output:

```text id="d5p38x"
4 → 5 → 1 → 2 → 3
```

Explanation:

```text id="u3jlwm"
After 1 rotation:
5 → 1 → 2 → 3 → 4

After 2 rotations:
4 → 5 → 1 → 2 → 3
```

---

### Constraints

* Number of nodes: `[0, 500]`
* `-100 <= Node.val <= 100`
* `0 <= k <= 2 * 10^9`

Key observation:

```text id="vfy12m"
k can be VERY large
```

So repeated rotation is too slow.

---

# 2. Diagram

Input:

```text id="08xjlwm"
1 → 2 → 3 → 4 → 5
```

Rotate by `k = 2`

---

### Core Idea

Make list circular first.

```text id="6ayfl0"
1 → 2 → 3 → 4 → 5
↑                 ↓
└─────────────────┘
```

Length = 5

Effective rotation:

```text id="xb62pl"
k = 2
```

New tail position:

```text id="0zjlwm"
length - k - 1
= 5 - 2 - 1
= 2
```

New tail:

```text id="s98f4v"
3
```

New head:

```text id="tq3v02"
4
```

Break circle:

```text id="9b1r2t"
4 → 5 → 1 → 2 → 3
```

---

# 3. Example I/O

## Example 1

Input:

```text id="wz9mkl"
head = [1,2,3,4,5]
k = 2
```

Output:

```text id="6lqmnx"
[4,5,1,2,3]
```

---

## Example 2

Input:

```text id="p4x92o"
head = [0,1,2]
k = 4
```

Output:

```text id="13mjq7"
[2,0,1]
```

Explanation:

```text id="u4smzq"
length = 3

k % length = 4 % 3 = 1
```

Only 1 effective rotation needed.

---

## Edge Case

Input:

```text id="9bx8zp"
head = []
k = 10
```

Output:

```text id="6dsyk2"
[]
```

---

# 4. Intuition & Pattern Recognition

## Key Pattern Signal

Whenever you see:

* linked list rotation
* moving tail to head repeatedly
* very large `k`

Think:

```text id="7aol9q"
Circular linked list trick
```

---

## Main Insight

Instead of rotating one-by-one:

```text id="c6mrkw"
1 → 2 → 3 → 4 → 5
```

Convert into:

```text id="m1j9cz"
1 → 2 → 3 → 4 → 5
↑                 ↓
└─────────────────┘
```

Now every node is reachable cyclically.

Then:

* locate new tail
* break circle

Done.

---

## Interview Thought Process

### Step 1

Brute force:

```text id="vd9n6k"
Move last node to front k times
```

Too slow.

---

### Step 2

Notice:

```text id="r2k7jlwm"
Rotations repeat every list length
```

So:

```python id="lyjlwm"
k = k % length
```

---

### Step 3

Instead of repeated movement:

```text id="r8mjlwm"
Connect tail to head
```

Now it becomes easy to cut at correct place.

---

# 5. Simpler Version

## Simplest Version

Rotate array by `k`.

Example:

```text id="1jlwmv"
[1,2,3,4,5]
→ [4,5,1,2,3]
```

In arrays:

* indexing helps directly

In linked lists:

* no backward movement
* need pointer manipulation

---

# Related Simpler Problems

## 1. Linked List Cycle

Teaches:

```text id="e5jlwm"
How circular linked lists work
```

---

## 2. Reverse Linked List

Teaches:

```text id="l2jlwm"
Pointer rewiring
```

---

## 3. Remove Nth Node From End

Teaches:

```text id="q8jlwm"
Finding node relative to end
```

This problem also depends on:

```text id="s7jlwm"
length-based positioning
```

---

# Thinking Progression

Basic:

```text id="d9jlwm"
Move last node to front
```

Optimization:

```text id="w4jlwm"
Rotations repeat after length
```

Advanced insight:

```text id="n6jlwm"
Convert list into circular list
```

Then:

```text id="f3jlwm"
Break at correct point
```

---

# 6. Brute Force

## Idea

Rotate one-by-one `k` times.

Each rotation:

1. find second-last node
2. move last node to front

---

## Code

```python id="h5jlwm"
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        for _ in range(k):
            prev = None
            curr = head

            # reach last node
            while curr.next:
                prev = curr
                curr = curr.next

            # already single node
            if not prev:
                return head

            prev.next = None
            curr.next = head
            head = curr

        return head
```

---

## Complexity

| Complexity | Value    |
| ---------- | -------- |
| Time       | O(k * n) |
| Space      | O(1)     |

Too slow for large `k`.

---

# 7. Optimal Solution

## Core Steps

1. Find length + tail
2. Make circular list
3. Reduce rotations:

   ```python
   k %= length
   ```
4. Find new tail
5. Break circle

---

## Optimal Code

```python id="m7jlwm"
class Solution:
    def rotateRight(self, head, k):
        # Empty list or single node
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Effective rotations
        k = k % length

        # No rotation needed
        if k == 0:
            return head

        # Make circular list
        tail.next = head

        # Find new tail
        steps = length - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # New head
        new_head = new_tail.next

        # Break circle
        new_tail.next = None

        return new_head
```

---

# 8. Step-by-Step Trace

Input:

```text id="x1jlwm"
1 → 2 → 3 → 4 → 5
k = 2
```

---

## Step 1: Find Length

| Node | Length |
| ---- | ------ |
| 1    | 1      |
| 2    | 2      |
| 3    | 3      |
| 4    | 4      |
| 5    | 5      |

```text id="o8jlwm"
length = 5
tail = 5
```

---

## Step 2: Reduce k

```python id="j6jlwm"
k = 2 % 5 = 2
```

---

## Step 3: Make Circular

```text id="r1jlwm"
1 → 2 → 3 → 4 → 5
↑                 ↓
└─────────────────┘
```

---

## Step 4: Find New Tail

```python id="u2jlwm"
steps = 5 - 2 - 1
      = 2
```

Move 2 steps from head:

| Step | Node |
| ---- | ---- |
| 0    | 1    |
| 1    | 2    |
| 2    | 3    |

New tail:

```text id="n5jlwm"
3
```

New head:

```text id="t8jlwm"
4
```

---

## Step 5: Break Circle

```text id="y7jlwm"
4 → 5 → 1 → 2 → 3
```

Done.

---

# 9. Related Problems

## 1. Linked List Cycle

Understanding circular linked lists.

---

## 2. Remove Nth Node From End of List

Pointer movement relative to list length.

---

## 3. Reverse Linked List II

Advanced pointer rewiring in linked lists.

---

## 4. Reorder List

Complex linked list restructuring.

---

## 5. Split Linked List in Parts

Length-based linked list partitioning.
