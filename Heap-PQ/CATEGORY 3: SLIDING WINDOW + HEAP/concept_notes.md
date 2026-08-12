# Sliding Window + Heap (Heap and Priority Queue)

> **Pattern goal:** Maintain the **best (min/max)** element inside a **moving window** when elements are continuously entering and leaving.

---

# 1. Pattern in One Minute

### Core Idea

A sliding window efficiently processes contiguous subarrays, but sometimes you also need to know:

* maximum
* minimum
* top K
* median
* highest priority

while the window keeps changing.

A heap gives fast access to the current extreme.

Since heaps **cannot delete arbitrary elements efficiently**, we use **lazy deletion**.

---

### Why does this pattern exist?

Normal sliding window tells us **which elements are inside**.

Heap tells us **which element is best**.

Together:

```
Window controls validity.
Heap controls priority.
```

---

### Immediately think of this when

> "Among every window..."
>
> "Need max/min continuously..."
>
> "Window moves one element at a time."

---

# 2. Recognition Signals

## Strong clues

* Sliding window
* Every subarray/window
* Maximum inside window
* Minimum inside window
* Top element while window changes
* Largest score in current range
* Dynamic range queries

---

## Common disguises

Instead of saying

> maximum

they may say

* strongest
* highest profit
* most frequent
* earliest deadline
* smallest cost
* best candidate

---

## Constraints

Usually

```
O(n²) ❌

Need O(n log n)
```

---

## Don't use when

* Need only window sum
* Need only frequency counts
* Monotonic Queue solves max/min in O(n)
* Window isn't contiguous

---

# 3. Mental Model

Think of two structures.

```
Window
```

decides

```
Which elements are alive?
```

Heap decides

```
Which alive element is best?
```

---

Remember:

* Push every new element.
* Never remove immediately.
* Remove only when it reaches heap top.
* Ignore stale elements.

Think:

```
Window expires elements.

Heap cleans lazily.
```

---

Example

```
nums

5 2 7 1 8

window size = 3

Window

5 2 7

Heap

7
5
2

Slide

2 7 1

Heap still contains

7
5
2
1

5 is expired.

Do nothing.

Later if 5 reaches top

remove it.
```

---

# 4. Boilerplate Template (Python)

```python
import heapq

heap = []

left = 0

for right in range(len(nums)):

    # Push current element
    heapq.heappush(heap, (-nums[right], right))   # max heap

    # Maintain window
    while right - left + 1 > k:
        left += 1

    # Remove expired elements
    while heap and heap[0][1] < left:
        heapq.heappop(heap)

    # Heap top is current answer
    if right >= k - 1:
        ans.append(-heap[0][0])
```

---

## Template Breakdown

Store

```
(value, index)
```

Index tells whether the element is still inside the window.

For max heap

```
(-value, index)
```

For min heap

```
(value, index)
```

---

# 5. Variations

| Variation                  | Change               |
| -------------------------- | -------------------- |
| Sliding Window Maximum     | Max heap             |
| Sliding Window Minimum     | Min heap             |
| Max score in window        | Max heap             |
| Smallest element in window | Min heap             |
| Median in window           | Two heaps            |
| Top K inside window        | Heap + lazy deletion |
| Dynamic interval problems  | Heap + index cleanup |

---

# 6. Common Pitfalls

## ❌ Forgetting indices

Wrong

```python
heap.push(value)
```

Correct

```python
heap.push((value, index))
```

Without index you cannot know if it expired.

---

## ❌ Removing expired immediately

Heap can't delete arbitrary elements efficiently.

Instead

```
Lazy deletion.
```

---

## ❌ Cleaning only once

Wrong

```python
if heap[0].index < left:
    pop()
```

Correct

```python
while heap and heap[0][1] < left:
    heapq.heappop(heap)
```

Multiple stale elements can accumulate.

---

## ❌ Building max heap incorrectly

Python only supports min heap.

Need

```python
-value
```

---

## ❌ Window update order

Correct sequence

```
Push

Move window

Remove stale

Answer
```

---

# 7. Interview Checklist

✅ Window moves continuously

✅ Need maximum/minimum while moving

✅ Elements expire

✅ Need fast access to best element

✅ Heap stores (value, index)

✅ Lazy deletion removes expired values

→ **Sliding Window + Heap**

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for revision)

1. 🔥 **239. Sliding Window Maximum** ⭐⭐⭐
2. 🔥 **480. Sliding Window Median** ⭐⭐⭐
3. 🔥 **1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit** *(know both heap and deque solutions)* ⭐⭐⭐

---

## Easy

* None (this pattern is rarely tested in Easy problems)

---

## Medium

* **239. Sliding Window Maximum**
* **1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit**
* **2461. Maximum Sum of Distinct Subarrays With Length K** *(heap not required, good contrast)*

---

## Hard

* **480. Sliding Window Median**
* **295. Find Median from Data Stream** *(foundation for sliding median)*
* **632. Smallest Range Covering Elements from K Lists** *(heap + moving pointers, closely related)*

---

# 9. 30-Second Cheat Sheet

### Recognition

* Moving window
* Need max/min continuously
* Elements expire
* O(n²) not allowed

---

### Core Idea

```
Sliding Window
        +
Heap
        +
Lazy Deletion
```

---

### Template

```
Push (value, index)

Move window

While heap top expired:
    Pop

Heap top = answer
```

---

### Complexity

* Insert → **O(log n)**
* Pop → **O(log n)**
* Overall → **O(n log n)**
* Space → **O(n)** (heap may temporarily hold stale elements until they reach the top)

---

### Common Variations

* Sliding Maximum
* Sliding Minimum
* Sliding Median (two heaps)
* Dynamic range problems
* Top-K in a moving window

---

### Pitfalls

* ❌ Don't store only values.
* ❌ Always store indices.
* ❌ Use **lazy deletion** (`while heap top is expired: pop`).
* ❌ Remember Python's heap is a min-heap (`-value` for max-heap).

## Pattern Comparison

| Pattern                              | Best Use Case                                                              | Time           | Key Idea                                 |
| ------------------------------------ | -------------------------------------------------------------------------- | -------------- | ---------------------------------------- |
| **Sliding Window + Heap**            | Need max/min/priority in a moving window, or more complex order statistics | **O(n log n)** | Heap + lazy deletion                     |
| **Sliding Window + Monotonic Deque** | Only need window maximum/minimum                                           | **O(n)**       | Maintain a monotonic deque of candidates |

**Interview tip:** If the problem only asks for the **maximum or minimum of each sliding window**, think of a **monotonic deque first** because it's optimal (**O(n)**). Reach for the **heap** when the required statistic is more complex (e.g., median, top-K, arbitrary priorities) or when a heap-based approach is simpler to generalize.
