# 25. Reverse Nodes in k-Group

**Pattern:** Linked List Reversal + Group Processing

---

# 1. Problem Statement with Example

Given the head of a linked list, reverse the nodes of the list `k` at a time and return the modified list.

* If the number of nodes is not a multiple of `k`, leave the remaining nodes as-is.
* You may not change node values.
* Only pointers can be modified.

---

## Example

Input:

```text id="2gk9aa"
head = 1 -> 2 -> 3 -> 4 -> 5
k = 2
```

Output:

```text id="m4b06x"
2 -> 1 -> 4 -> 3 -> 5
```

---

## Another Example

Input:

```text id="0hnn7g"
head = 1 -> 2 -> 3 -> 4 -> 5
k = 3
```

Output:

```text id="u9op7r"
3 -> 2 -> 1 -> 4 -> 5
```

Because:

* first 3 nodes reversed
* remaining 2 nodes stay unchanged

---

## Constraints

* `1 <= k <= n <= 5000`

This strongly hints:

* iterative pointer manipulation
* `O(1)` extra space expected

---

# 2. Diagram

## Original

```text id="8xntmx"
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

---

## k = 2

Reverse every pair:

```text id="l7t5mx"
(1 2) (3 4) (5 6)
```

becomes:

```text id="5d7fj6"
2 -> 1 -> 4 -> 3 -> 6 -> 5
```

---

## k = 3

```text id="8a8olw"
(1 2 3) (4 5 6)
```

becomes:

```text id="vr8k5q"
3 -> 2 -> 1 -> 6 -> 5 -> 4
```

---

# 3. Example I/O

## Example 1

Input:

```text id="6a4t8q"
head = [1,2,3,4,5]
k = 2
```

Output:

```text id="3u2f3n"
[2,1,4,3,5]
```

---

## Example 2

Input:

```text id="m2e08f"
head = [1,2,3,4,5]
k = 3
```

Output:

```text id="44qj6t"
[3,2,1,4,5]
```

Explanation:
Last 2 nodes are not enough for a group of 3.

---

## Example 3 (Edge Case)

Input:

```text id="1obon9"
head = [1]
k = 1
```

Output:

```text id="wt1j8o"
[1]
```

Nothing changes.

---

# 4. Intuition & Pattern Recognition

## Key Signal

Problem says:

```text id="k47qti"
reverse every k nodes
```

This means:

* repeatedly apply linked list reversal
* but only on fixed-size chunks

---

# Mental Breakdown

Instead of:

```text id="e4t60n"
reverse whole list once
```

Think:

```text id="3wn5p0"
reverse small windows repeatedly
```

---

# Core Observation

Before reversing:

* must verify group contains exactly `k` nodes

Otherwise:

* leave remaining nodes unchanged

---

# Interview Recognition Pattern

If you hear:

* “group”
* “batch”
* “every k nodes”
* “chunk reversal”

Think:

```text id="s8i2wy"
Find group
→ reverse group
→ reconnect
→ move forward
```

---

# 5. Simpler Version

---

# Simpler Question 1

### Reverse Linked List

Reverse entire linked list.

Core operation:

```python id="r5t0r7"
curr.next = prev
```

---

# Simpler Question 2

### Reverse Linked List II

Reverse a sublist between positions.

Now instead of one sublist:

* repeat reversal many times

---

# Simpler Question 3

### Swap Nodes in Pairs

This is actually:

```text id="o6i3dx"
k = 2
```

version of current problem.

---

# Simpler Thinking → Full Problem

## Start

Reverse once:

```text id="8b2kp9"
1 2 3
→
3 2 1
```

---

## Then

Reverse only part:

```text id="k58l8z"
1 [2 3 4] 5
```

---

## Finally

Reverse repeatedly:

```text id="jywt1h"
[1 2 3] [4 5 6]
```

Each group handled independently.

---

# 6. Brute Force

## Idea

* Store nodes in array
* Reverse every k segment
* Reconnect list

---

## Brute Force Code

```python id="h6a5a7"
class Solution:
    def reverseKGroup(self, head, k):

        arr = []

        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        n = len(arr)

        for i in range(0, n, k):

            if i + k <= n:
                arr[i:i+k] = reversed(arr[i:i+k])

        for i in range(n - 1):
            arr[i].next = arr[i + 1]

        arr[-1].next = None

        return arr[0]
```

---

## Complexity

* Time: `O(n)`
* Space: `O(n)`

---

# 7. Optimal Solution

# Core Idea

For each group:

1. Check if k nodes exist
2. Reverse k nodes
3. Connect previous group
4. Continue

---

# Important Pointer Roles

| Pointer     | Purpose                    |
| ----------- | -------------------------- |
| `groupPrev` | node before current group  |
| `kth`       | last node of current group |
| `groupNext` | node after group           |
| `prev/curr` | used for reversal          |

---

# Optimal Code (Python)

```python id="c2bdp6"
class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            # Find kth node
            kth = groupPrev

            for _ in range(k):

                kth = kth.next

                if not kth:
                    return dummy.next

            groupNext = kth.next

            # Reverse group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:

                temp = curr.next

                curr.next = prev

                prev = curr

                curr = temp

            # Reconnect group
            temp = groupPrev.next

            groupPrev.next = kth

            groupPrev = temp
```

---

# Why `prev = groupNext`?

Very important trick.

Suppose:

```text id="7kdb6l"
1 -> 2 -> 3 -> 4
```

Reversing:

```text id="ztuvq0"
1 2 3
```

Need:

```text id="dn5m3y"
3 -> 2 -> 1 -> 4
```

So during reversal:

```text id="4p0khr"
1.next must finally point to 4
```

That is why:

```python id="pn9w4x"
prev = groupNext
```

before reversal starts.

---

# 8. Step-by-Step Trace

Input:

```text id="y9u7u8"
1 -> 2 -> 3 -> 4 -> 5
k = 2
```

---

# Group 1

Nodes:

```text id="5j33s8"
1 -> 2
```

Reverse:

```text id="byr5dn"
2 -> 1
```

List becomes:

```text id="mjlwmu"
2 -> 1 -> 3 -> 4 -> 5
```

---

# Group 2

Nodes:

```text id="46mbqm"
3 -> 4
```

Reverse:

```text id="9d6yz7"
4 -> 3
```

List becomes:

```text id="8n74ip"
2 -> 1 -> 4 -> 3 -> 5
```

---

# Remaining

Only:

```text id="9zfybk"
5
```

Less than `k`.

Stop.

---

# Final Answer

```text id="nfyz8l"
2 -> 1 -> 4 -> 3 -> 5
```

---

# 9. Related Problems

1. Reverse Linked List
   Basic linked list reversal.

2. Swap Nodes in Pairs
   Special case where `k = 2`.

3. Reverse Linked List II
   Reverse a single sublist.

4. Rotate List
   Another heavy pointer manipulation problem.

5. Reorder List
   Multiple linked list transformations combined.
