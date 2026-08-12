# Merging Problems — Two Pointers

## 1. Pattern in One Minute

**Core idea:** When you have **two sorted sequences**, keep one pointer on each and repeatedly process whichever pointed element should come next.

```text
A = [1, 4, 7]
     i
B = [2, 3, 8]
     j

Compare A[i] and B[j]
→ process the appropriate one
→ move only that pointer
→ repeat
```

Think of **merging two sorted lists in Merge Sort**.

### When should it click?

> **Two sorted sequences + need to combine/compare them efficiently → Two Pointers**

The important insight is that sorted order makes discarded elements irrelevant. You never need to move backward.

**Typical complexity:** `O(n + m)` time, often `O(1)` extra space if modifying in-place.

---

# 2. Recognition Signals

Strong signals:

* Two **sorted arrays/lists/interval lists**
* "Merge two sorted..."
* "Intersection of two sorted..."
* "Find common elements"
* "Compare two sorted sequences"
* "Combine while maintaining sorted order"
* Two ordered streams that need to be synchronized

### Common disguises

It isn't always literally called "merge."

```text
Array A ──i──►
Array B ──j──►
              Compare
                ↓
       advance i / j / both
```

For example:

* **Merge Sorted Array** → copy the smaller/larger value
* **Intersection** → advance the pointer with smaller value
* **Interval List Intersections** → process overlap, advance interval that ends first
* **Meeting Scheduler** → find overlap large enough, advance interval ending first

### Don't use it when

If the sequences are **unsorted**, two-pointer merging usually loses its advantage. Sorting may help, but if you only need membership/intersection, a hash set may be better.

---

# 3. Mental Model

Remember:

> **Compare → Process → Advance**

1. Put `i` on the first sequence and `j` on the second.
2. Compare `A[i]` and `B[j]`.
3. Decide what that comparison means for the problem.
4. Process the current element(s).
5. Advance the pointer whose current element is "finished."
6. Sometimes advance **both** when they match.
7. Never move pointers backward.
8. Continue until one sequence is exhausted.
9. Handle leftovers if the problem requires them.

The key interview question is:

> **Which pointer can I safely advance without losing a future answer?**

For normal merging:

```text
A[i] < B[j]  → A[i] comes next → i++
A[i] > B[j]  → B[j] comes next → j++
A[i] == B[j] → problem decides whether one/both advance
```

---

# 4. Boilerplate Template

### Generic two-sequence merge

```python
def merge(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # One side may still contain elements
    result.extend(a[i:])
    result.extend(b[j:])

    return result
```

**Time:** `O(n + m)`
**Space:** `O(n + m)` for output.

### The reusable skeleton

For many interview problems, remember this rather than the exact merge code:

```python
i = j = 0

while i < len(a) and j < len(b):

    if condition_1:
        # process
        i += 1

    elif condition_2:
        # process
        j += 1

    else:
        # process relationship/match
        i += 1
        j += 1
```

The **conditions and pointer movement** are what change across problems.

---

# 5. Variations

### A. Merge two sorted arrays

Take the smaller element and advance its pointer.

```text
A[i] < B[j] → take A[i], i++
else         → take B[j], j++
```

### B. Intersection of sorted arrays

Advance whichever value is smaller.

```text
A[i] < B[j] → i++
A[i] > B[j] → j++
A[i] == B[j] → record match, both++
```

Why? If `A[i] < B[j]`, then `A[i]` cannot match `B[j]` or anything after it.

### C. Merge Sorted Array in-place

If the first array has empty space at the end:

> **Merge backwards.**

```text
nums1 = [1, 3, 7, _, _, _]
nums2 = [2, 5, 8]

               i
                     write
nums2             j
```

Compare the **largest** remaining elements and write from the end.

Mnemonic:

> **Empty space at end → start from end.**

This avoids overwriting unprocessed elements in `nums1`.

### D. Interval intersection

Given sorted, non-overlapping interval lists:

```python
start = max(a_start, b_start)
end = min(a_end, b_end)

if start <= end:
    # overlap exists
```

Then:

> **Advance the interval that ends first.**

Because that interval cannot overlap anything further without first being replaced.

### E. Meeting Scheduler

Same interval-intersection idea, but additionally check:

```python
if end - start >= duration:
    return [start, start + duration]
```

---

# 6. Common Pitfalls

### Advancing the wrong pointer

The most important part of merging problems isn't initializing two pointers; it's proving **which pointer is safe to discard**.

For intersection:

```python
if a[i] < b[j]:
    i += 1
```

Don't advance `j`: `b[j]` might match some later element in `a`.

### Forgetting leftovers

For actual merging:

```python
result.extend(a[i:])
result.extend(b[j:])
```

Once one side is exhausted, the other side may still matter.

### Overwriting during in-place merge

Don't merge from the front when `nums1` contains the source elements and destination space.

```text
Merge from front  → overwrite risk
Merge from back   → safe
```

### Mishandling duplicates

For set-like intersection:

```text
[1, 1, 2]
[1, 1, 3]
```

Ask whether the result should be `[1]` or `[1, 1]`. Pointer movement changes accordingly.

### Using binary search unnecessarily

You could search each element of one array in another:

`O(n log m)`

But two sorted sequences can usually be processed together:

`O(n + m)`.

---

# 7. Interview Checklist

✓ Are there **two sorted sequences**?

✓ Do I need to merge, intersect, compare, or synchronize them?

✓ Can I put one pointer on each sequence?

✓ After comparing current elements, can I prove one pointer is safe to advance?

✓ Is each pointer moving only forward?

→ **Think merging two pointers: `O(n + m)`.**

For intervals:

> **Overlap → process it → advance the one ending first.**

For in-place merge:

> **Free space at end → merge backwards.**

---

# 8. Must-Do Problems

### Easy

**⭐ Top 3 — Merge Sorted Array (LC 88)**
The essential **backward merge** problem.

**⭐ Top 3 — Intersection of Two Arrays II (LC 350)**
Excellent for learning compare + advance/both.

**Merge Two Sorted Lists (LC 21)**
Same pattern on linked lists.

### Medium

**⭐ Top 3 — Interval List Intersections (LC 986)**
One of the best extensions of the merging pattern.

**Meeting Scheduler (LC 1229)**
Interval overlap + advance whichever ends first.

**Sort Transformed Array (LC 360)**
A useful variation combining sorted input and two-pointer placement.

For revision, **88 + 350 + 986** cover most of the important reasoning.

---

# 9. 30-Second Cheat Sheet

```text
MERGING — TWO POINTERS

Recognition:
Two sorted sequences
+ merge / intersection / comparison / synchronization

Core:
i → sequence A
j → sequence B

Compare A[i], B[j]
        ↓
Process current relationship
        ↓
Advance pointer that is safe to discard


NORMAL MERGE
A[i] < B[j] → take A[i], i++
else         → take B[j], j++

INTERSECTION
A[i] < B[j] → i++
A[i] > B[j] → j++
equal        → record, i++, j++

INTERVALS
overlap = [max(starts), min(ends)]
advance interval with smaller end

IN-PLACE MERGE
Free space at end → MERGE BACKWARDS

Complexity:
Time  → O(n + m)
Space → O(1) possible in-place

Mnemonic:
COMPARE → PROCESS → ADVANCE

Key question:
"Which pointer can I safely move without
losing a possible future answer?"
```
