# 347. Top K Frequent Elements

**Pattern:** Frequency Counting + Heap / Bucket Sort
**Difficulty:** Medium

---

## 1. Problem Statement

Given an integer array `nums` and an integer `k`, return the **`k` most frequent elements**.

The answer can be returned in any order.

### Example

```text
nums = [1,1,1,2,2,3]
k = 2

Frequency:
1 → 3
2 → 2
3 → 1

Top 2 frequencies:
1 → 3
2 → 2

Output = [1,2]
```

### Constraints

```text
1 <= nums.length <= 10^5
1 <= k <= number of unique elements

Answer is guaranteed to be unique.
```

The important requirement is that the intended solution should be **better than O(N log N)** sorting of all elements.

---

# 2. Diagram

```text
nums = [1,1,1,2,2,3]
k = 2

Step 1: Frequency Map

        ┌───────┬──────┐
        │ Value │ Freq │
        ├───────┼──────┤
        │   1   │  3   │
        │   2   │  2   │
        │   3   │  1   │
        └───────┴──────┘

Step 2: Group by frequency

frequency
    3  → [1]
    2  → [2]
    1  → [3]

Step 3: Walk from HIGH → LOW

    3 → take 1
    2 → take 2

We have k = 2 elements.

Answer = [1, 2]
```

This reversed viewpoint is extremely useful:

```text
Normal map:

element → frequency

1 → 3
2 → 2
3 → 1

Bucket representation:

frequency → elements

3 → [1]
2 → [2]
1 → [3]
```

---

# 3. Example I/O

### Example 1 — Typical

```text
Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
[1,2]
```

Because `1` occurs 3 times and `2` occurs 2 times.

### Example 2

```text
Input:
nums = [4,4,4,4,5,5,5,6,6,7]
k = 2

Output:
[4,5]
```

```text
4 → 4
5 → 3
6 → 2
7 → 1
```

### Edge Case

```text
Input:
nums = [1]
k = 1

Output:
[1]
```

There is only one unique element.

---

# 4. Intuition & Pattern Recognition

The key phrase is:

> **"K most frequent"**

Break that into two subproblems:

```text
"frequent" → Frequency Map

"Top K"    → Heap / Bucket Sort
```

So your interview thought process should be:

> "First count occurrences. Then I don't need everything sorted — I only need the K highest frequencies."

This distinction matters.

If the problem said:

> Sort all elements by frequency

then sorting makes sense.

But here:

> Give me only the **Top K**.

That should immediately make you think about **selection techniques**:

```text
Top K
  ↓
Heap
or
Bucket Sort
```

### Pattern recognition shortcut

```text
Top/Bottom K + ranking metric
           ↓
         Heap

Frequency bounded by N
           ↓
       Bucket Sort
```

---

# 5. Simpler Version

This problem combines several simpler ideas.

## Simpler 1 — Contains Duplicate

**217. Contains Duplicate**

```text
nums = [1,2,3,1]
```

You learn:

> Hash-based structures let us efficiently track values.

But we only care whether something repeats.

---

## Simpler 2 — Valid Anagram

**242. Valid Anagram**

Now we need actual counts:

```text
a → 3
n → 1
g → 1
...
```

This introduces:

```python
freq[num] += 1
```

---

## Simpler 3 — Sort Characters By Frequency

**451. Sort Characters By Frequency**

You already know:

```text
Count
  ↓
Rank by frequency
```

Example:

```text
tree

e → 2
t → 1
r → 1

↓ frequency descending

e, t, r
```

But that problem wants **all characters** arranged.

---

## Current Question

Now:

```text
Count
  ↓
Rank by frequency
  ↓
STOP after K elements
```

So the progression is:

```text
Contains Duplicate
       ↓
Does frequency exist?

Valid Anagram
       ↓
Count frequency

Sort Characters By Frequency
       ↓
Order by frequency

Top K Frequent Elements
       ↓
Only retrieve K highest frequencies
```

That last step introduces the classic **Top K pattern**.

---

# 6. Brute Force — Count + Sort

The simplest solution is:

1. Count frequencies.
2. Sort unique elements by frequency descending.
3. Return first `k`.

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        elements = sorted(
            freq.keys(),
            key=lambda x: freq[x],
            reverse=True
        )

        return elements[:k]
```

For:

```text
nums = [1,1,1,2,2,3]
```

we get:

```text
freq = {
    1: 3,
    2: 2,
    3: 1
}

sort ↓

[1, 2, 3]

take first k=2

[1, 2]
```

Let `U` = number of unique elements.

```text
Counting → O(N)
Sorting  → O(U log U)

Time  → O(N + U log U)
Space → O(U)
```

Worst case `U = N`, so:

**O(N log N)**.

Works, but we can do better.

---

# 7. Optimal Solution — Bucket Sort

The crucial observation is:

> An element's frequency can never exceed `N`.

For an array of length 6:

```text
Possible frequencies:

1, 2, 3, 4, 5, 6
```

Therefore, create buckets where:

```text
bucket[f] = elements occurring f times
```

### Python

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        # Maximum possible frequency is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Put each number into its frequency bucket
        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        # Visit highest frequencies first
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)

                # Stop once we collect k elements
                if len(result) == k:
                    return result
```

### Why `len(nums) + 1`?

Suppose:

```text
nums = [5,5,5,5]
N = 4
```

`5` has frequency `4`.

We need:

```text
buckets[4]
```

So valid indices must be:

```text
0, 1, 2, 3, 4
```

Hence:

```python
buckets = [[] for _ in range(len(nums) + 1)]
```

Bucket `0` simply remains unused.

### Complexity

```text
Frequency map     → O(N)
Build buckets     → O(U)
Traverse buckets  → O(N)
Build result      → O(K)

Time  → O(N)
Space → O(N)
```

This beats sorting and satisfies the intended requirement.

---

# 8. Step-by-Step Trace

Take:

```text
nums = [1,1,1,2,2,3]
k = 2
```

### Step 1 — Count

| Read | Frequency Map     |
| ---- | ----------------- |
| `1`  | `{1:1}`           |
| `1`  | `{1:2}`           |
| `1`  | `{1:3}`           |
| `2`  | `{1:3, 2:1}`      |
| `2`  | `{1:3, 2:2}`      |
| `3`  | `{1:3, 2:2, 3:1}` |

Final:

```text
1 → 3
2 → 2
3 → 1
```

### Step 2 — Create buckets

`N = 6`, so:

```text
index:
0   1   2   3   4   5   6

[ ] [ ] [ ] [ ] [ ] [ ] [ ]
```

Process `1 → 3`:

```text
bucket[3] = [1]
```

Process `2 → 2`:

```text
bucket[2] = [2]
```

Process `3 → 1`:

```text
bucket[1] = [3]
```

Final:

```text
0 → []
1 → [3]
2 → [2]
3 → [1]
4 → []
5 → []
6 → []
```

### Step 3 — Traverse backwards

Start:

```text
result = []
k = 2
```

`count = 6, 5, 4`

```text
empty → skip
```

`count = 3`

```text
bucket[3] = [1]

result = [1]
```

Not enough yet.

`count = 2`

```text
bucket[2] = [2]

result = [1,2]
```

Now:

```text
len(result) == k
```

Return:

```text
[1,2]
```

---

# 9. Heap Solution — Important for Top K Pattern

Bucket sort is excellent here because frequency is bounded by `N`.

But for general **Top K** interview problems, you should also know the **min-heap of size K** approach.

Maintain:

```text
heap = K best elements seen so far
```

For every `(num, frequency)`:

```text
push into heap

if heap size > k:
    remove smallest frequency
```

So the heap never stores more than `K` elements.

```python
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]
```

Let `U` be unique elements.

```text
Counting     → O(N)
Each heap op → O(log K)
U elements   → O(U log K)

Time  → O(N + U log K)
Space → O(U + K)
```

### Why min-heap, not max-heap?

This is one of the most important Top K ideas.

We want to keep the **K largest** frequencies.

The element we need to quickly throw away is:

> the **smallest among our current K candidates**.

Therefore:

```text
        Min Heap

          2       ← weakest candidate
         / \
        5   4

New frequency = 7

push 7

          2
         / \
        5   4
       /
      7

size > K

remove minimum → 2

Remaining:
4, 5, 7
```

So remember:

```text
Top K largest  → Min Heap size K
Top K smallest → Max Heap size K
```

The root represents the **worst candidate currently allowed into the Top K**.

---

# 10. Bucket Sort vs Heap

| Approach    |             Time | When to think of it         |
| ----------- | ---------------: | --------------------------- |
| Sort        | `O(N + U log U)` | Simplest first solution     |
| Min Heap    | `O(N + U log K)` | General Top K pattern       |
| Bucket Sort |         **O(N)** | Frequency is bounded by `N` |

For **this exact problem**, bucket sort is the clean optimal answer.

For building interview pattern recognition, the **heap solution is more transferable** to other Top K problems.

---

# 11. Related Problems

| Problem                                  | Connection                                                           |
| ---------------------------------------- | -------------------------------------------------------------------- |
| **451. Sort Characters By Frequency**    | Count frequencies and rank all characters by frequency.              |
| **703. Kth Largest Element in a Stream** | Classic min-heap of size `K`; root is the Kth largest.               |
| **215. Kth Largest Element in an Array** | Same Top K selection idea, but asks only for the Kth element.        |
| **692. Top K Frequent Words**            | Same frequency + Top K pattern, with lexicographical tie-breaking.   |
| **973. K Closest Points to Origin**      | Replace "frequency" with "distance"; same Top K selection structure. |

# Quick Revision

```text
347. Top K Frequent Elements

Signal:
"Top K" + "frequent"

Step 1:
Count frequencies

num → count

Step 2:
Need K highest counts

Choices:

Sort:
O(N log N)

Min Heap size K:
O(N + U log K)

Bucket Sort:
O(N) ← optimal here

Bucket idea:

frequency → elements

1 → [3]
2 → [2]
3 → [1]

Traverse backwards:

3 → [1]
2 → [2]

k = 2
Answer = [1,2]
```

### Interview memory hook

**Frequency problem? → HashMap.**

**Top K? → Heap.**

**Frequency is bounded by N? → Bucket Sort can eliminate sorting.**
