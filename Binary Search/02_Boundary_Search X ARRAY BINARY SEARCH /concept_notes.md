# Find First and Last Position + Find Peak (Binary Search)

---

# 1. Pattern in One Minute

### Core Idea

Not every binary search is about finding an exact element.

Sometimes you're searching for:

* the **first occurrence**
* the **last occurrence**
* a **boundary**
* or a **peak**

The key is that **one half of the search space can still be discarded every iteration**, even though the target isn't directly identified.

Think of this as:

> **Binary Search on Properties instead of Values.**

---

### Why does this pattern exist?

Duplicates and local properties (like peaks) break the standard binary search.

Instead of stopping when `nums[mid] == target`, you keep searching one side.

---

### Immediately think of it when

* Need first/last occurrence
* Sorted array with duplicates
* Need insertion position
* Looking for transition/boundary
* Need local maximum (peak)

---

# 2. Recognition Signals

### Strong clues

### Find First/Last Position

* Sorted array
* Duplicates exist
* "Return first occurrence"
* "Return last occurrence"
* "Range of target"

Examples:

* Find First and Last Position
* First Bad Version
* Search Insert Position
* Lower Bound
* Upper Bound

---

### Find Peak

Keywords:

* Peak element
* Local maximum
* Neighbor comparison
* Array isn't sorted
* O(log n)

---

### Common disguises

Instead of saying

> Find first 5

They ask

> Find smallest index satisfying condition.

---

### Don't use this when

* Array unsorted (unless peak problem)
* Need all occurrences
* Can't eliminate half

---

# 3. Mental Model

## A. First/Last Position

Imagine duplicates:

```
1 2 2 2 2 3
    ^
```

Binary search lands somewhere inside.

Now ask:

> Can answer exist on the left?

If yes

→ continue left.

Similarly,

Last occurrence:

> Can answer exist on right?

---

Keep current answer.

Continue searching.

---

## B. Peak Element

Instead of comparing with target,

Compare

```
nums[mid]
nums[mid+1]
```

If

```
mid < mid+1
```

you're climbing.

Peak lies right.

Else

Peak lies left (including mid).

This is identical to climbing a mountain.

---

# 4. Boilerplate Template

## A. First Position

```python
def first(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            right = mid - 1      # keep searching left

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

---

## B. Last Position

```python
def last(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            left = mid + 1       # keep searching right

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

---

## C. Peak Element

```python
def findPeak(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1      # peak on right
        else:
            right = mid         # peak on left (or mid)

    return left
```

---

# 5. Variations

| Problem                | Change                                  |
| ---------------------- | --------------------------------------- |
| First Position         | move right = mid-1 after finding target |
| Last Position          | move left = mid+1 after finding target  |
| Lower Bound            | first index ≥ target                    |
| Upper Bound            | first index > target                    |
| Search Insert Position | return lower bound                      |
| First Bad Version      | predicate instead of equality           |
| Peak Element           | compare neighbors instead of target     |

---

# 6. Common Pitfalls

### First/Last Position

❌ Return immediately after finding target

Need boundary.

---

❌ Forget storing answer

Always

```python
ans = mid
```

before continuing.

---

❌ Wrong side movement

First occurrence

```
right = mid - 1
```

Last occurrence

```
left = mid + 1
```

---

### Peak

❌ Comparing with both neighbors unnecessarily

Only compare

```
nums[mid]
nums[mid+1]
```

---

❌ Using

```
while left <= right
```

Peak template uses

```
while left < right
```

---

# 7. Interview Checklist

### ✓ First/Last Position

* Sorted array
* Duplicates
* Boundary search
* Need first/last index

→ Binary Search with answer variable.

---

### ✓ Peak

* Local maximum
* Neighbor comparisons
* O(log n)
* Not necessarily sorted

→ Binary Search on slope.

---

# 8. Must-Do Problems

## ⭐ Top 3

1. **LC 34 — Find First and Last Position of Element in Sorted Array** ⭐
2. **LC 162 — Find Peak Element** ⭐
3. **LC 35 — Search Insert Position** ⭐

---

## Easy

* LC 35 Search Insert Position
* LC 704 Binary Search

---

## Medium

* LC 34 Find First and Last Position ⭐
* LC 162 Find Peak Element ⭐
* LC 278 First Bad Version (if available in your environment)
* LC 852 Peak Index in a Mountain Array

---

## Hard (only if important)

* LC 1095 Find in Mountain Array

---

# 9. 30-Second Cheat Sheet

### Recognition

* Sorted + duplicates → First/Last Position
* Boundary search → Lower/Upper Bound
* Local maximum → Peak
* Neighbor comparison → Peak Binary Search

---

### Core Idea

* Don't stop when found.
* Keep searching toward the required boundary.
* For peaks, follow the uphill slope.

---

### Templates

**First Position**

```python
ans = mid
right = mid - 1
```

**Last Position**

```python
ans = mid
left = mid + 1
```

**Peak**

```python
if nums[mid] < nums[mid + 1]:
    left = mid + 1
else:
    right = mid
```

---

### Complexity

* Time: **O(log n)**
* Space: **O(1)**

---

### Common Variations

* First Occurrence
* Last Occurrence
* Lower Bound
* Upper Bound
* Search Insert Position
* First Bad Version
* Peak Index in Mountain Array
* Find Peak Element

---

### Pitfalls

* Don't return on the first match.
* Save the candidate answer before moving.
* Move toward the boundary you want.
* For peak search, use `while left < right` and compare `nums[mid]` with `nums[mid + 1]`.
