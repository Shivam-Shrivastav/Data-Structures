# Meeting Scheduler (LeetCode 1229)

**Pattern:** Two Pointers (Sorted Intervals)

---

# 1. Problem Statement

You are given the availability slots of two people:

* `slots1`
* `slots2`

Each slot is represented as:

```text
[start, end]
```

where the person is available from `start` to `end`.

You are also given an integer `duration`.

Find the **earliest time slot** where **both people are available for at least `duration` minutes**.

Return:

```text
[start, start + duration]
```

If no such slot exists, return:

```text
[]
```

### Constraints

* `1 <= slots1.length, slots2.length <= 10^4`
* `0 <= start < end <= 10^9`
* Slots within each list are non-overlapping.
* **The lists are NOT necessarily sorted.**

---

# 2. Diagram

Example

```text
slots1

[10---------50]      [60---120]      [140------210]

slots2

      [0-----15]     [60----70]
```

After sorting

```text
[10---------50]
[0-----15]

Overlap

[10----15]

Length = 5

Need duration = 8

Not enough

Move slot2
```

Next

```text
[60------120]
[60---70]

Overlap

[60---70]

Length = 10

Need = 8

Earliest answer

[60,68]
```

---

# 3. Example I/O

### Example 1

**Input**

```text
slots1 = [[10,50],[60,120],[140,210]]

slots2 = [[0,15],[60,70]]

duration = 8
```

**Output**

```text
[60,68]
```

---

### Example 2

**Input**

```text
slots1 = [[10,50]]

slots2 = [[60,120]]

duration = 5
```

**Output**

```text
[]
```

No overlapping slot.

---

### Example 3 (Edge Case)

**Input**

```text
slots1 = [[10,20]]

slots2 = [[15,30]]

duration = 5
```

**Output**

```text
[15,20]
```

Exactly 5 minutes overlap.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Two people's schedules
* Time intervals
* Earliest common meeting
* Sorted intervals

Think

> **Two Pointers on Intervals**

### Key Observation

Suppose

```text
A = [10,50]

B = [20,40]
```

Common availability is

```text
[max(10,20), min(50,40)]

↓

[20,40]
```

Its length is

```text
40 - 20 = 20
```

If

```text
20 >= duration
```

meeting is possible.

Otherwise,

move the interval that ends first.

---

### Why move the smaller ending interval?

Suppose

```text
A ends at 40

B ends at 80
```

A cannot overlap any future slot after 40.

So discard A.

---

### Interview Thinking

```text
Sort both schedules.

Compare one slot from each.

Compute overlap.

If overlap length ≥ duration,

return immediately.

Else,

move the slot that ends first.
```

---

# 5. Simpler Version

## Simpler Question 1

### Interval List Intersections (LeetCode 986)

Find every overlap.

No duration requirement.

---

## Simpler Question 2

### Merge Intervals (LeetCode 56)

Understand interval overlap.

---

## Current Question

Instead of returning **all overlaps**,

return the **first overlap whose length is at least `duration`**.

---

### Thinking Progression

```text
Understand overlap

↓

Interval List Intersections

↓

Measure overlap length

↓

Return first valid overlap

↓

Meeting Scheduler
```

---

# 6. Brute Force

Compare every slot from `slots1`
with every slot from `slots2`.

```python
for s1 in slots1:
    for s2 in slots2:
        overlap = ...
```

### Complexity

```text
Time : O(M × N)

Space : O(1)
```

---

# 7. Optimal Solution (Sorting + Two Pointers)

### Idea

1. Sort both slot lists by start time.
2. Compare one slot from each list.
3. Compute overlap:

   * `start = max(start1, start2)`
   * `end = min(end1, end2)`
4. If `end - start >= duration`, return `[start, start + duration]`.
5. Otherwise, move the interval that ends first.

### Python

```python
class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):

        # Sort by start time
        slots1.sort()
        slots2.sort()

        i = j = 0

        while i < len(slots1) and j < len(slots2):

            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])

            # Enough overlap for the meeting
            if end - start >= duration:
                return [start, start + duration]

            # Move the interval that finishes first
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1

        return []
```

### Complexity

```text
Sorting : O(M log M + N log N)

Two pointers : O(M + N)

Overall : O(M log M + N log N)

Space : O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
slots1

[10,50] [60,120] [140,210]

slots2

[0,15] [60,70]

duration = 8
```

| i | j | Overlap | Length | Action                  |
| - | - | ------- | ------ | ----------------------- |
| 0 | 0 | [10,15] | 5      | Move slot2 (ends first) |
| 0 | 1 | None    | 0      | Move slot1 (ends first) |
| 1 | 1 | [60,70] | 10     | Enough → Return         |

Answer

```text
[60,68]
```

---

# 9. Related Problems

| Problem                              | Connection                                                                                    |
| ------------------------------------ | --------------------------------------------------------------------------------------------- |
| **56. Merge Intervals**              | Basic interval overlap and merging.                                                           |
| **57. Insert Interval**              | Insert and merge intervals while maintaining order.                                           |
| **986. Interval List Intersections** | Finds all intersections; this problem returns the first one satisfying a duration constraint. |
| **252. Meeting Rooms**               | Checks whether meetings overlap.                                                              |
| **253. Meeting Rooms II**            | Counts the minimum number of meeting rooms needed using interval processing.                  |

---

# Key Interview Takeaways

* **Pattern:** Sorting + Two Pointers on Intervals.
* **Core Formula:**

  * `start = max(start1, start2)`
  * `end = min(end1, end2)`
* **Meeting Condition:** `end - start >= duration`.
* **Answer:** `[start, start + duration]` (the earliest possible meeting).
* **Pointer Rule:** Move the interval with the **smaller end time**, since it cannot contribute to future overlaps.
* **Complexity:** **O(M log M + N log N)** due to sorting, followed by a linear scan.
