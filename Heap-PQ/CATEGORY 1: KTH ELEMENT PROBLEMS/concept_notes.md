# Kth Element Problems - Heap & Priority Queue

---

# 1. Pattern in One Minute

### Core Idea

Instead of sorting the entire dataset (**O(n log n)**), maintain only the **K most relevant elements** using a heap.

The heap always represents the current answer.

---

### Why does this pattern exist?

Many interview problems ask:

* Kth largest
* Kth smallest
* Top K
* Closest K
* Merge K things

Sorting everything is unnecessary because you only care about **K elements**, not all **N**.

Heap reduces unnecessary work.

---

### Immediately think of this pattern when

* "Kth Largest"
* "K Closest"
* "Top K Frequent"
* "Merge K Sorted Lists"
* Need continuous access to current minimum/maximum while processing data.

---

# 2. Recognition Signals

## Strong clues

### Keywords

* Kth Largest
* Kth Smallest
* Top K
* Closest K
* Highest Priority
* Lowest Cost
* Merge K
* Running Median

---

### Constraints

```
n = 100000+

k << n
```

Sorting feels wasteful.

---

### Problem characteristics

You're processing elements one by one while keeping only the best K.

---

### Common disguises

Instead of

> Find K largest

they ask

* Return top K scores
* K closest points
* K weakest rows
* K nearest numbers
* Smallest pairs
* Schedule tasks by priority

---

## Don't use Heap when

* Need complete ordering → Sort
* Need binary search over sorted array
* K ≈ N (sorting is often simpler)

---

# 3. Mental Model

Think of the heap as a **waiting room with only K seats**.

For every new candidate:

* Is there space?

  * Add it.
* Room full?

  * Compare with weakest candidate.
  * Better candidate enters.
  * Weakest leaves.

Eventually only the K best survive.

---

Quick intuition

* Min Heap → Keep K Largest
* Max Heap → Keep K Smallest

Reason:

The root should always be the **worst among the current answer**, so it can be removed quickly.

---

Remember

> Heap root = candidate to kick out.

---

# 4. Boilerplate Templates (Python)

## Pattern 1 — K Largest (Min Heap)

```python
import heapq

heap = []

for num in nums:
    heapq.heappush(heap, num)

    if len(heap) > k:
        heapq.heappop(heap)

return heap[0]          # kth largest
```

Complexity

```
Time:
O(n log k)

Space:
O(k)
```

---

## Pattern 2 — K Smallest (Max Heap)

Python has no max heap.

Store negatives.

```python
import heapq

heap = []

for num in nums:
    heapq.heappush(heap, -num)

    if len(heap) > k:
        heapq.heappop(heap)

return -heap[0]
```

---

## Pattern 3 — Top K Frequent

```python
freq = Counter(nums)

heap = []

for num, count in freq.items():

    heapq.heappush(heap, (count, num))

    if len(heap) > k:
        heapq.heappop(heap)

return [num for count, num in heap]
```

Heap stores frequency first because tuples compare lexicographically.

---

## Pattern 4 — K Closest

Store distance.

```python
dist = x*x + y*y

heapq.heappush(heap, (-dist, point))

if len(heap) > k:
    heapq.heappop(heap)
```

---

# 5. Variations

| Problem               | Heap Used             | One-line change                      |
| --------------------- | --------------------- | ------------------------------------ |
| Kth Largest           | Min Heap              | Remove smallest                      |
| Kth Smallest          | Max Heap              | Remove largest                       |
| Top K Frequent        | Min Heap by frequency | Store `(freq, value)`                |
| K Closest Points      | Max Heap by distance  | Store `(-distance, point)`           |
| Merge K Lists         | Min Heap              | Store node value                     |
| Merge K Arrays        | Min Heap              | Store value + array index            |
| K Smallest Pairs      | Min Heap              | Push pair sums                       |
| Running Median        | Two Heaps             | One min + one max                    |
| IPO / Maximum Capital | Two Heaps             | One sorted by capital, one by profit |

---

# 6. Common Pitfalls

### ❌ Using wrong heap

Remember

```
Want K Largest

↓

Need Min Heap
```

Because smallest among K should leave first.

---

### ❌ Forgetting heap size

Always

```python
if len(heap) > k:
    heapq.heappop(heap)
```

---

### ❌ Negating wrong values

Python only supports min heap.

Use negatives only when simulating max heap.

---

### ❌ Sorting after heap

If only kth element is required

Don't sort.

Heap already has answer.

---

### ❌ Forgetting tuple ordering

Python compares tuples like

```
(freq, value)
```

Frequency compared first.

---

# 7. Interview Checklist

✅ Problem mentions **K**

✅ Need only partial ordering

✅ K much smaller than N

✅ Continuously maintain best candidates

✅ Need insert/remove efficiently

→ Think **Heap**

---

Quick mapping

```
Largest
↓

Min Heap


Smallest
↓

Max Heap


Top Frequency
↓

Heap on frequency


Closest
↓

Heap on distance


Merge K
↓

Heap on current minimum
```

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for Revision)

1. **215. Kth Largest Element in an Array** ⭐⭐⭐
2. **347. Top K Frequent Elements** ⭐⭐⭐
3. **23. Merge K Sorted Lists** ⭐⭐⭐

Master these and you'll recognize most heap interview patterns.

---

## Easy

* 703. Kth Largest Element in a Stream
* 1046. Last Stone Weight

---

## Medium

* 215. Kth Largest Element in an Array ⭐
* 347. Top K Frequent Elements ⭐
* 973. K Closest Points to Origin
* 373. Find K Pairs with Smallest Sums
* 378. Kth Smallest Element in a Sorted Matrix
* 692. Top K Frequent Words
* 658. Find K Closest Elements
* 621. Task Scheduler (heap variant)

---

## Hard

* 23. Merge K Sorted Lists ⭐
* 295. Find Median from Data Stream
* 480. Sliding Window Median
* 502. IPO
* 632. Smallest Range Covering Elements from K Lists

---

# 9. 30-Second Cheat Sheet

## Recognition

* Kth Largest
* Kth Smallest
* Top K
* Closest K
* Merge K
* Running priorities

---

## Core Idea

Keep only the **K candidates** in a heap.

Root is always the **next element to remove**.

---

## Templates

**K Largest**

```python
push
if len > k:
    pop
```

**K Smallest**

```python
Use negative values
```

**Top K Frequent**

```python
(freq, value)
```

**Merge K**

```python
(value, list_index, node)
```

---

## Complexity

| Operation       | Complexity |
| --------------- | ---------: |
| Push            |   O(log k) |
| Pop             |   O(log k) |
| Process N items | O(n log k) |
| Space           |       O(k) |

---

## Common Variations

* Kth Largest → Min Heap
* Kth Smallest → Max Heap
* Top K Frequent → Frequency Heap
* K Closest → Distance Heap
* Merge K Lists → Min Heap
* Running Median → Two Heaps
* IPO → Two Heaps

---

## Pitfalls

* ❌ Wrong heap type
* ❌ Forgetting to cap heap size at `k`
* ❌ Incorrect use of negatives for max heap
* ❌ Sorting unnecessarily after heap
* ❌ Storing tuples in the wrong order

### Mnemonic

> **"Keep only what matters."**

If the problem only asks for **K** elements or the **Kth** answer, don't manage all `N` elements. Let the heap continuously discard the candidates that can no longer be part of the final answer. This is the core intuition behind almost every K-element heap problem.
