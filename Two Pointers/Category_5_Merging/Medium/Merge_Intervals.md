# 56. Merge Intervals (LeetCode 56)

**Pattern:** Sorting + Greedy (Intervals)

---

# 1. Problem Statement

You are given an array of intervals where `intervals[i] = [start_i, end_i]`.

Merge all overlapping intervals and return an array of the **non-overlapping intervals** that cover all the intervals.

An overlap exists if:

```text
next.start <= current.end
```

Intervals that just touch (e.g., `[1,4]` and `[4,5]`) are also considered overlapping.

### Constraints

* `1 <= intervals.length <= 10^4`
* `intervals[i].length == 2`
* `0 <= start <= end <= 10^4`

Need an efficient **O(N log N)** solution because of sorting.

---

# 2. Diagram

Example:

```text
Input:

[1,3]   [2,6]      [8,10]    [15,18]

Timeline:

1-----3
   2--------6

                8------10

                             15------18


Merge first two

1-----------6

                8------10

                             15------18

Answer:

[[1,6],[8,10],[15,18]]
```

Another example:

```text
[1,4]
    [4,5]

1---------5

Because 4 touches 4,
they overlap.
```

---

# 3. Example I/O

### Example 1

```text
Input:
intervals = [[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]
```

Explanation

```text
[1,3] overlaps with [2,6]

Merged → [1,6]
```

---

### Example 2

```text
Input:
intervals = [[1,4],[4,5]]

Output:
[[1,5]]
```

Explanation

```text
4 touches 4

Still considered overlap.
```

---

### Edge Case

```text
Input:
[[1,2]]

Output:
[[1,2]]
```

Only one interval.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Merge overlapping intervals
* Meeting schedules
* Calendar events
* Ranges
* Time intervals

Immediately think:

> **Sort by starting time**

Why?

After sorting:

* Every future interval starts after the previous one.
* You only need to compare with the **last merged interval**.

Without sorting you'd have to compare every interval with every other one.

### Interview Thinking

Tell yourself:

```text
If intervals are sorted,

then overlap can only happen
with the previously merged interval.

No need to compare with everything.

Just keep extending the current interval.
```

---

# 5. Simpler Version

## Simpler Question 1

### Sort Numbers

```text
Sort

1 5 2 8

↓

1 2 5 8
```

Sorting organizes data.

---

## Simpler Question 2

### Check if Two Intervals Overlap

```text
A = [1,5]
B = [4,7]

4 <= 5

Overlap
```

---

## Current Question

Now combine both ideas.

```text
Sort

↓

Compare adjacent intervals

↓

Merge if overlap

↓

Else push current answer
```

---

### Thinking Progression

```text
Sort numbers

↓

Understand interval overlap

↓

Sort intervals

↓

Merge adjacent overlaps

↓

Merge Intervals
```

---

# 6. Brute Force

Compare every interval with every other interval repeatedly until no merge is possible.

```text
for every interval

    compare with all intervals

        merge if overlap
```

### Complexity

```text
Time : O(N²)

Space: O(N)
```

Too slow for 10,000 intervals.

---

# 7. Optimal Solution (Sorting + Greedy)

### Idea

1. Sort intervals by start.
2. Add first interval.
3. For each remaining interval:

   * If overlapping → extend last merged interval.
   * Otherwise → append as a new interval.

### Python

```python
class Solution:
    def merge(self, intervals):
        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:

            # First interval or no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                # Extend the previous interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
```

### Complexity

```text
Sorting : O(N log N)

Scanning : O(N)

Total : O(N log N)

Space : O(N)
```

---

# 8. Step-by-Step Trace

Example

```text
intervals =
[[1,3],[2,6],[8,10],[15,18]]
```

Already sorted.

| Current Interval | Last Merged | Overlap? | Result                 |
| ---------------- | ----------- | -------- | ---------------------- |
| [1,3]            | None        | —        | [[1,3]]                |
| [2,6]            | [1,3]       | Yes      | [[1,6]]                |
| [8,10]           | [1,6]       | No       | [[1,6],[8,10]]         |
| [15,18]          | [8,10]      | No       | [[1,6],[8,10],[15,18]] |

Final Answer

```text
[[1,6],[8,10],[15,18]]
```

---

### Example 2 Trace

```text
Input

[1,4]
[4,5]
```

| Interval | Last  | Action        |
| -------- | ----- | ------------- |
| [1,4]    | —     | Add           |
| [4,5]    | [1,4] | Merge → [1,5] |

Result

```text
[[1,5]]
```

---

# 9. Related Problems

| Problem                              | Connection                                                           |
| ------------------------------------ | -------------------------------------------------------------------- |
| **252. Meeting Rooms**               | Check if any intervals overlap after sorting.                        |
| **253. Meeting Rooms II**            | Count minimum meeting rooms using intervals and heaps.               |
| **57. Insert Interval**              | Insert one interval into sorted intervals and merge where necessary. |
| **986. Interval List Intersections** | Use two pointers to find intersections between two interval lists.   |
| **759. Employee Free Time**          | Merge intervals from multiple employees to find gaps.                |

---

# Key Interview Takeaways

* **Pattern:** Sorting + Greedy
* **Core Insight:** After sorting by start time, an interval can only overlap with the **last merged interval**.
* **Overlap Condition:** `current.start <= lastMerged.end`
* **No Overlap Condition:** `current.start > lastMerged.end`
* **Merge Rule:** Update the end as `max(lastMerged.end, current.end)`.
* **Time Complexity:** **O(N log N)** (sorting dominates).
* **Space Complexity:** **O(N)** for the output list.

This follows the same structured revision style as your previous sheets. 
