# 142. Linked List Cycle II

## 1. Problem Statement with Example

Given the head of a singly linked list, determine if the list contains a cycle.

If there is a cycle, return the node where the cycle begins. Otherwise, return `null`.

You are **not allowed** to modify the linked list.

### Example

```text
Input:
3 → 2 → 0 → -4
    ↑       ↓
    ← ← ← ←

Output:
Node with value 2
```

The tail connects back to the node with value `2`, so the cycle starts there.

### Constraints

* Number of nodes: `[0, 10^4]`
* Node values: `-10^5 to 10^5`
* `pos` indicates cycle connection internally (not given directly)
* Must use **O(1)** extra space for optimal solution

---

# 2. Diagram

## Phase 1 — Detect Cycle

```text
slow moves 1 step
fast moves 2 steps

1 → 2 → 3 → 4 → 5
        ↑       ↓
        ← ← ← ←

Iteration:

slow: 1 -> 2 -> 3 -> 4
fast: 1 -> 3 -> 5 -> 4

Eventually:
slow == fast
```

---

## Phase 2 — Find Cycle Start

```text
head
 ↓
1 → 2 → 3 → 4 → 5
    ↑       ↓
    ← ← ← ←

meeting point = 4

Move:
ptr1 from head
ptr2 from meeting point

Both move 1 step:

ptr1: 1 -> 2
ptr2: 4 -> 5 -> 2

They meet at cycle start = 2
```

---

# 3. Example I/O

## Example 1 (Typical)

```text
Input:
head = [3,2,0,-4], pos = 1

Output:
Node with value 2
```

Explanation:
Tail connects back to index `1`.

---

## Example 2 (No Cycle)

```text
Input:
head = [1,2], pos = -1

Output:
null
```

Explanation:
No cycle exists.

---

## Example 3 (Single Node Cycle)

```text
Input:
head = [1], pos = 0

Output:
Node with value 1
```

Explanation:
The node points to itself.

---

# 4. Intuition & Pattern Recognition

This is the classic **Floyd’s Tortoise and Hare** problem.

### Signals for this pattern

* Linked list
* Need to detect cycle
* O(1) space restriction
* “Find where cycle begins”

These strongly hint toward:

* Two pointers
* Fast/slow movement

---

## Core Insight

If a cycle exists:

* Fast pointer eventually laps slow pointer
* They meet somewhere inside cycle

Then a mathematical property helps us locate the cycle start.

---

## Interview Recognition Thought Process

> “If I can detect the cycle using fast/slow pointers, maybe the meeting point contains information about the cycle entrance.”

That’s exactly the trick.

---

# 5. Simpler Version

## Simpler Problem

### Linked List Cycle

Only asks:

```text
Does a cycle exist?
Return true/false
```

Solution:

* Fast & slow pointers
* If they meet → cycle exists

---

## How This Problem Extends It

Now instead of:

```text
"Does cycle exist?"
```

We ask:

```text
"Where does cycle begin?"
```

So after detection, we need one extra mathematical step.

---

## Simpler Thinking → Full Thinking

### Step 1

Detect cycle.

```text
slow += 1
fast += 2
```

If they meet:

* cycle exists

---

### Step 2

Why resetting one pointer to head works?

Suppose:

```text
distance(head → cycleStart) = a
distance(cycleStart → meet) = b
cycle length = c
```

When they meet:

```text
fast traveled = 2 * slow
```

This eventually simplifies to:

```text
a = remaining distance to cycle start
```

Thus:

* One pointer from head
* One pointer from meeting point
* Move both 1 step
* They meet at cycle start

---

## Other Simpler Related Problems

1. Linked List Cycle
   Learn cycle detection.

2. Middle of the Linked List
   Learn fast/slow pointer movement.

3. Happy Number
   Same cycle detection idea but on numbers.

---

# 6. Brute Force

## Idea

Store visited nodes in a hash set.

If a node repeats:

* That node is cycle start.

---

## Python Code

```python
class Solution:
    def detectCycle(self, head):
        visited = set()

        curr = head

        while curr:
            if curr in visited:
                return curr

            visited.add(curr)
            curr = curr.next

        return None
```

---

## Complexity

* Time: `O(n)`
* Space: `O(n)`

---

# 7. Optimal Solution

## Floyd’s Cycle Detection Algorithm

### Steps

1. Detect meeting point
2. Reset one pointer to head
3. Move both one step
4. Meeting point becomes cycle start

---

## Python Code

```python
class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Phase 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                # Phase 2: Find cycle start
                ptr1 = head
                ptr2 = slow

                while ptr1 != ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next

                return ptr1

        return None
```

---

## Complexity

* Time: `O(n)`
* Space: `O(1)`

---

# 8. Step-by-Step Trace

## Input

```text
1 → 2 → 3 → 4 → 5
    ↑       ↓
    ← ← ← ←
```

Cycle starts at `2`.

---

# Phase 1 — Detect Meeting

| Step | slow | fast |
| ---- | ---- | ---- |
| 0    | 1    | 1    |
| 1    | 2    | 3    |
| 2    | 3    | 5    |
| 3    | 4    | 3    |
| 4    | 5    | 5    |

Meeting at node `5`.

---

# Phase 2 — Find Entry

```text
ptr1 = head = 1
ptr2 = meet = 5
```

| Step | ptr1 | ptr2 |
| ---- | ---- | ---- |
| 0    | 1    | 5    |
| 1    | 2    | 2    |

They meet at `2`.

Return node `2`.

---

# 9. Related Problems

1. Linked List Cycle
   Basic cycle detection using fast/slow pointers.

2. Happy Number
   Detect cycles in number transformations.

3. Find the Duplicate Number
   Converts array into linked-list-like cycle structure.

4. Middle of the Linked List
   Foundation for tortoise-hare movement.

5. Circular Array Loop
   Advanced cycle detection in arrays.
