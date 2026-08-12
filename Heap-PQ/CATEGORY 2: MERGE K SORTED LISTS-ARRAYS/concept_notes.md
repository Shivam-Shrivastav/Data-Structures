# Merge K Sorted Lists / Arrays — Heap & Priority Queue (DSA Revision)

---

# 1. Pattern in One Minute

### Core Idea

You have **K already sorted sequences**, and you need to produce **one globally sorted sequence**.

Instead of repeatedly scanning all K sequences to find the smallest element (**O(K)** each step), keep only the **current smallest candidate from each sequence** inside a **min-heap**.

Every time you remove the smallest element:

1. Output it.
2. Insert the next element from the same sequence into the heap.

The heap always contains at most **K elements**.

---

### Why does this pattern exist?

Because scanning all K lists for every output element gives:

> **O(NK)**

where **N = total elements**.

Using a heap reduces this to:

> **O(N log K)**

which is optimal.

---

### When should you immediately think of it?

Whenever you hear:

* Merge multiple sorted lists
* Merge K sorted arrays
* Merge K linked lists
* External sorting
* Streaming sorted data
* Multiple sorted inputs

---

# 2. Recognition Signals

## Strong clues

* "K sorted..."
* "Merge all..."
* "Return sorted order"
* Multiple sorted streams
* Sorted linked lists
* Sorted arrays

---

## Constraints

* K can be large
* Total elements can be huge
* Need efficient merging

If K > 2, don't repeatedly merge one by one unless asked.

---

## Common disguises

* Smallest element among many sorted streams
* Merge log files
* Merge timestamps
* Merge database shards
* Merge intervals coming from sorted sources

---

## When NOT to use it

❌ Arrays not sorted

❌ Need median

❌ Need Top-K only

❌ Need pair combinations

---

# 3. Mental Model

Imagine K conveyor belts.

Each conveyor belt exposes only its front item.

```
A: 1 4 8
B: 2 5 9
C: 3 6 7
```

Heap initially:

```
1
2
3
```

Take 1

Push 4

Heap

```
2
3
4
```

Take 2

Push 5

Continue...

The heap never stores the entire input.

Only:

> One active candidate per list.

---

Memory trick:

> **One representative from every list lives in the heap.**

---

# 4. Boilerplate Template (Python)

## Merge K Sorted Arrays

```python
import heapq

def merge(arrays):
    heap = []

    # Push first element from every array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
            # value, array_index, element_index

    ans = []

    while heap:
        value, arr_idx, idx = heapq.heappop(heap)
        ans.append(value)

        if idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(
                heap,
                (
                    arrays[arr_idx][idx + 1],
                    arr_idx,
                    idx + 1
                )
            )

    return ans
```

### Complexity

```
Heap size = K

Push = log K
Pop = log K

Total operations = N

Time = O(N log K)

Space = O(K)
```

---

## Merge K Sorted Linked Lists

```python
import heapq

class Solution:
    def mergeKLists(self, lists):

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        cur = dummy

        while heap:
            _, i, node = heapq.heappop(heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next
```

Why include `i`?

Python can't compare `ListNode` objects when values are equal. The list index acts as a tie-breaker.

---

# 5. Variations

| Variation                       | Change                                             |
| ------------------------------- | -------------------------------------------------- |
| Merge K arrays                  | Store `(value, array, index)`                      |
| Merge K linked lists            | Store `(value, list_id, node)`                     |
| Smallest range covering K lists | Maintain current maximum while popping minimum     |
| External Merge Sort             | Same idea, data comes from files instead of arrays |
| Merge sorted streams            | Push next streamed element after consuming one     |

---

# 6. Common Pitfalls

### ❌ Forgetting empty lists

Always check:

```python
if arr:
```

---

### ❌ Forgetting to push next element

After popping:

```
Push successor from same list
```

Otherwise elements disappear.

---

### ❌ Heap contains entire arrays

Wrong:

```
Push every element
```

Correct:

```
Only first element initially.
```

---

### ❌ Comparing ListNode directly

Need

```python
(value, index, node)
```

instead of

```python
(node)
```

---

### ❌ Confusing N and K

```
N = total elements

K = number of lists
```

Complexity depends on **log K**, **not log N**.

---

# 7. Interview Checklist

✅ Multiple sorted inputs

✅ Need globally sorted output

✅ K > 2

✅ Need smallest available repeatedly

✅ One candidate per list is enough

➡️ Use **Min Heap**.

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for Revision)

1. ⭐⭐ **LeetCode 23 — Merge k Sorted Lists** *(Medium)*
2. ⭐⭐ **LeetCode 373 — Find K Pairs with Smallest Sums** *(Medium, heap expansion variant)*
3. ⭐⭐ **LeetCode 632 — Smallest Range Covering Elements from K Lists** *(Hard)*

---

### Easy

* *(No canonical Easy problem for this exact pattern.)*

### Medium

* **LeetCode 23 — Merge k Sorted Lists** ⭐
* **LeetCode 373 — Find K Pairs with Smallest Sums** ⭐ *(related heap frontier pattern)*

### Hard

* **LeetCode 632 — Smallest Range Covering Elements from K Lists** ⭐

---

# 9. 30-Second Cheat Sheet

## Recognition

* K sorted arrays
* K sorted linked lists
* Merge sorted streams
* Global sorted output

---

## Core Idea

Maintain **one active element per list** in a **min-heap**.

Pop the smallest.

Push the next element from the same list.

Repeat until the heap is empty.

---

## Template

```python
Push first element of every list

while heap:
    smallest = pop()
    output.append(smallest)
    push next element from same list
```

---

## Complexity

```
Time : O(N log K)

Space : O(K)
```

---

## Common Variations

* Merge K arrays
* Merge K linked lists
* Smallest range from K lists
* External merge sort
* Merge streaming data

---

## Pitfalls

* Forget empty lists
* Forget to push successor
* Push entire arrays instead of one candidate
* Compare `ListNode` objects directly
* Mix up `N` (elements) and `K` (lists)

---

### 🧠 Memory Mnemonic

> **"One finger on every list."**
> Keep exactly **one current element from each sorted list** in the heap. Pop the smallest finger, then move only that finger forward. This invariant is the essence of every Merge K Sorted Lists/Arrays problem.
