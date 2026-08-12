# 220. Contains Duplicate III

**Pattern:** Sliding Window + Ordered Set / Bucketization
**Difficulty:** Hard

---

## 1. Problem Statement

Given an integer array `nums` and two integers `indexDiff` and `valueDiff`, return `True` if there exist two **different indices** `i` and `j` such that:

```text
|i - j| <= indexDiff
AND
|nums[i] - nums[j]| <= valueDiff
```

Otherwise return `False`.

### Example

```text
nums      = [1, 2, 3, 1]
indexDiff = 3
valueDiff = 0

Output: True
```

Choose:

```text
i = 0, j = 3

|0 - 3| = 3 <= 3       ✓
|1 - 1| = 0 <= 0       ✓
```

### Constraints affecting the approach

`nums` can be large, so checking every pair is too expensive.

Notice there are **two constraints**:

```text
index distance <= indexDiff
value distance <= valueDiff
```

This is what makes it harder than **Contains Duplicate II**.

---

# 2. Diagram

Suppose:

```text
nums = [1, 5, 9, 1]
indexDiff = 3
valueDiff = 3
```

At `right = 3`:

```text
Indices:    0   1   2   3
            ↓           ↓
nums =     [1,  5,  9,  1]
            └───────────┘

Index difference:
3 - 0 = 3 ✓

Value difference:
|1 - 1| = 0 ✓

Answer = True
```

The index condition tells us which elements are relevant:

```text
              right
                ↓
... [ x  x  x  CURRENT ]
     └─────┘
     previous at most indexDiff elements
```

So maintain a **sliding window of previous `indexDiff` elements**.

Inside that window, we need to efficiently ask:

> Is there some value close enough to `nums[right]`?

---

# 3. Example I/O

### Example 1 — True

```text
Input:
nums = [1, 2, 3, 1]
indexDiff = 3
valueDiff = 0

Output:
True
```

Because:

```text
nums[0] = nums[3] = 1

index difference = 3
value difference = 0
```

Both conditions hold.

### Example 2 — False

```text
Input:
nums = [1, 5, 9, 1, 5, 9]
indexDiff = 2
valueDiff = 3

Output:
False
```

The repeated values are too far apart:

```text
1 ... 1
index difference = 3 > 2
```

And elements that are close enough in index differ by more than `3` in value.

---

# 4. Intuition & Pattern Recognition

The condition is:

```text
|i-j| <= indexDiff
```

This immediately suggests:

> **Sliding Window**

For current index `j`, we only care about:

```text
j-indexDiff ... j-1
```

Older elements can be discarded.

But now comes the second condition:

```text
|nums[i] - nums[j]| <= valueDiff
```

For current value `x`, we need some previous value `y` satisfying:

```text
|x-y| <= valueDiff
```

Rewrite:

```text
-valueDiff <= x-y <= valueDiff
```

Therefore:

```text
x-valueDiff <= y <= x+valueDiff
```

So we're really asking:

> Does my current sliding window contain **any number inside a value range**?

```text
[x - valueDiff, x + valueDiff]
```

That's the core problem.

### Interview thinking

```text
Index constraint
    → sliding window

Value constraint
    → need efficient "nearby value" lookup

Therefore:

Sliding Window
+
Ordered Set

OR

Sliding Window
+
Buckets
```

---

# 5. Simpler Version

This problem becomes much easier when you remove one condition at a time.

## Step 1 — Contains Duplicate

**217. Contains Duplicate**

Question:

```text
Does nums contain equal values anywhere?
```

Condition:

```text
nums[i] == nums[j]
```

Use:

```text
HashSet
```

---

## Step 2 — Contains Duplicate II

**219. Contains Duplicate II**

Now add:

```text
|i-j| <= k
```

Question becomes:

```text
Are equal values close in index?
```

Maintain only the last `k` elements:

```text
Sliding Window + HashSet
```

```text
Contains Duplicate

equal values
     ↓
HashSet

        +

Contains Duplicate II

equal values
+ index distance
     ↓
Sliding Window + HashSet
```

---

## Step 3 — Contains Duplicate III

Now equality becomes **near equality**:

```text
Contains Duplicate II:

nums[i] == nums[j]


Contains Duplicate III:

|nums[i] - nums[j]| <= valueDiff
```

This changes everything.

A normal HashSet efficiently answers:

```text
Does 10 exist?
```

But now we need:

```text
Does anything from
[7, 13]
exist?
```

when:

```text
x = 10
valueDiff = 3
```

HashSet cannot efficiently perform range queries.

So:

```text
Contains Duplicate
       ↓
HashSet

Contains Duplicate II
       ↓
Sliding Window + HashSet

Contains Duplicate III
       ↓
Sliding Window
+
Ordered Set / Buckets
```

That's the progression worth remembering.

---

# 6. Brute Force

For every element, compare it with every relevant previous element.

```python
class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums: list[int],
        indexDiff: int,
        valueDiff: int
    ) -> bool:

        for i in range(len(nums)):
            # Only indices within indexDiff can qualify
            for j in range(i + 1, min(len(nums), i + indexDiff + 1)):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True

        return False
```

### Complexity

Worst case:

```text
Time:  O(N × indexDiff)
Space: O(1)
```

If `indexDiff ≈ N`:

```text
O(N²)
```

Too expensive.

---

# 7. Optimal Solution — Bucketization

For interviews, bucketization gives an **O(N)** expected-time solution using a HashMap.

The clever idea is to divide numbers into buckets of width:

```text
valueDiff + 1
```

Let:

```text
w = valueDiff + 1
bucket_id = x // w
```

### Why `valueDiff + 1`?

Suppose:

```text
valueDiff = 3
w = 4
```

Buckets conceptually look like:

```text
Bucket 0: [0,1,2,3]
Bucket 1: [4,5,6,7]
Bucket 2: [8,9,10,11]
...
```

Any two values in the **same bucket** differ by at most `3`.

So if current `x` lands in an already occupied bucket:

```text
return True
```

But valid values can also cross bucket boundaries.

Example:

```text
3 and 4

|3 - 4| = 1 <= 3
```

Yet they're in neighboring buckets.

Therefore check:

```text
same bucket
left neighbor
right neighbor
```

For neighboring buckets, verify the actual absolute difference.

---

## Python

```python
class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums: list[int],
        indexDiff: int,
        valueDiff: int
    ) -> bool:

        if indexDiff <= 0 or valueDiff < 0:
            return False

        width = valueDiff + 1
        buckets = {}

        for i, x in enumerate(nums):
            bucket = x // width

            # Same bucket guarantees difference <= valueDiff
            if bucket in buckets:
                return True

            # Neighboring buckets may contain a close enough value
            if bucket - 1 in buckets:
                if abs(x - buckets[bucket - 1]) <= valueDiff:
                    return True

            if bucket + 1 in buckets:
                if abs(x - buckets[bucket + 1]) <= valueDiff:
                    return True

            buckets[bucket] = x

            # Keep only the previous indexDiff elements
            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_bucket = old // width
                del buckets[old_bucket]

        return False
```

### Complexity

```text
Time:  O(N) expected
Space: O(indexDiff)
```

Each element performs constant expected-time HashMap operations.

---

# 8. Step-by-Step Trace

Consider:

```text
nums      = [1, 5, 9, 1]
indexDiff = 3
valueDiff = 3

width = 3 + 1 = 4
```

Buckets:

```text
bucket 0 → [0..3]
bucket 1 → [4..7]
bucket 2 → [8..11]
```

### `i = 0`, `x = 1`

```text
bucket = 1 // 4 = 0

buckets = {}

same bucket? No
neighbor?    No

insert:

0 → 1
```

### `i = 1`, `x = 5`

```text
bucket = 5 // 4 = 1

buckets:
0 → 1
```

Neighbor bucket `0` contains `1`.

Check:

```text
|5 - 1| = 4

4 > 3
```

Not valid.

Insert:

```text
0 → 1
1 → 5
```

### `i = 2`, `x = 9`

```text
bucket = 9 // 4 = 2
```

Neighbor bucket `1` contains `5`:

```text
|9 - 5| = 4 > 3
```

Not valid.

Now:

```text
0 → 1
1 → 5
2 → 9
```

### `i = 3`, `x = 1`

```text
bucket = 1 // 4 = 0
```

Bucket `0` already exists:

```text
bucket 0 → 1
```

Therefore:

```text
|1 - 1| = 0 <= 3
|3 - 0| = 3 <= 3

return True
```

---

# 9. Related Problems

| Problem                         | Why it's related                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **217. Contains Duplicate**     | Basic HashSet duplicate detection without distance constraints.                                                    |
| **219. Contains Duplicate II**  | Adds the index-distance constraint, introducing a sliding window.                                                  |
| **220. Contains Duplicate III** | Adds value-distance constraint, requiring ordered lookup or buckets.                                               |
| **729. My Calendar I**          | Introduces efficient reasoning about values/ranges and neighboring intervals.                                      |
| **239. Sliding Window Maximum** | Another case where sliding window alone isn't enough; requires an additional data structure for efficient queries. |

## Quick Revision

```text
Contains Duplicate III

Need i,j such that:

|i-j| <= indexDiff
       +
|nums[i]-nums[j]| <= valueDiff


Index condition
      ↓
Sliding Window

Value condition
      ↓
Nearby-value search

      ↓

Bucket width = valueDiff + 1

For current x:
    ↓
check same bucket
    ↓
check left bucket
    ↓
check right bucket
    ↓
insert x
    ↓
remove element outside indexDiff
```

The key progression is:

```text
217 Contains Duplicate
    HashSet
       ↓
219 Contains Duplicate II
    Sliding Window + HashSet
       ↓
220 Contains Duplicate III
    Sliding Window + Buckets
```

**Most important insight:** `indexDiff` controls **which elements remain in the window**, while `valueDiff` controls **which values are considered close enough**.
