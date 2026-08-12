# 219. Contains Duplicate II

**Pattern:** Fixed-Size Sliding Window + HashSet
**Difficulty:** Easy

This is a useful bridge from basic duplicate detection to sliding window. It also leads naturally into **Longest Substring Without Repeating Characters**, where the window size becomes variable. 

---

## 1. Problem Statement

Given an integer array `nums` and an integer `k`, return `True` if there exist **two different indices** `i` and `j` such that:

```text
nums[i] == nums[j]
and
|i - j| <= k
```

Otherwise return `False`.

In simpler words:

> Find whether the same value occurs twice **within `k` indices** of each other.

### Constraints

```text
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
```

The `10^5` array size suggests we should avoid comparing every pair.

---

## 2. Diagram

Example:

```text
nums = [1, 2, 3, 1]
k = 3

indices:
        0  1  2  3
nums:  [1, 2, 3, 1]
        ↑        ↑
        i        j

Distance = 3 - 0 = 3

3 <= k

→ True
```

Think of maintaining the **previous `k` elements**:

```text
right = 0
[1]
 ↑
window = {1}


right = 1
[1, 2]
 ↑  ↑
window = {1,2}


right = 2
[1, 2, 3]
window = {1,2,3}


right = 3
[1, 2, 3, 1]
             ↑

1 already exists in previous k elements

→ duplicate nearby → True
```

The HashSet answers:

> **Have I seen this value among the previous `k` positions?**

---

## 3. Example I/O

### Example 1 — Typical

```text
Input:
nums = [1,2,3,1]
k = 3

Output:
True
```

Because:

```text
nums[0] == nums[3] == 1

|0 - 3| = 3 <= k
```

### Example 2 — Duplicate too far away

```text
Input:
nums = [1,2,3,1,2,3]
k = 2

Output:
False
```

For value `1`:

```text
indices = 0, 3
distance = 3 > 2
```

Same for `2` and `3`.

### Edge Case

```text
Input:
nums = [1,1]
k = 0

Output:
False
```

Two **different indices** can never have distance `<= 0`.

---

# 4. Intuition & Pattern Recognition

The obvious clue is:

```text
|i - j| <= k
```

We don't care whether a duplicate exists **anywhere**.

We care whether it exists **nearby**.

So when processing index `right`, only these previous indices matter:

```text
right-k ... right-2, right-1
```

Anything older can be forgotten.

That gives us:

```text
array
+ nearby distance constraint
+ duplicate lookup
        ↓
Fixed-size sliding window + HashSet
```

### Interview thinking

Tell yourself:

> "For each element, I only need to know whether the same value appeared among the previous `k` elements."

A HashSet gives `O(1)` average duplicate lookup.

The window tells us **which elements are still close enough to matter**.

---

# 5. Simpler Version

## Step 1: Contains Duplicate — LeetCode 217

The simpler problem asks:

> Does any duplicate exist anywhere?

```text
nums = [1,2,3,1]

seen = {}

1 → add
2 → add
3 → add
1 → already exists → True
```

Solution:

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

The set remembers **everything we've seen**.

---

## Step 2: Contains Duplicate II

Now add:

```text
|i-j| <= k
```

The old solution doesn't work directly because:

```text
nums = [1,2,3,1]
k = 2
```

A global set sees duplicate `1`:

```text
{1,2,3}
```

but their distance is:

```text
3 > 2
```

So we need to **forget old elements**.

```text
Contains Duplicate

Set contains ALL previous elements
            ↓
Add distance constraint
            ↓
Only previous k elements matter
            ↓
Remove elements that become too old
            ↓
Sliding Window + HashSet
```

### Simpler → Current thinking

```text
217. Contains Duplicate
        ↓
"I need fast duplicate detection"
        ↓
HashSet

219. Contains Duplicate II
        ↓
"I need fast duplicate detection,
but only among nearby elements"
        ↓
HashSet + Sliding Window
```

This removal idea is important because it later becomes the basis of variable-size sliding windows such as **Longest Substring Without Repeating Characters**.

---

# 6. Brute Force

For each index `i`, compare it with nearby indices up to `i + k`.

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, min(n, i + k + 1)):
                if nums[i] == nums[j]:
                    return True

        return False
```

### Complexity

At most `k` comparisons for each element:

```text
Time:  O(N × min(N, K))
       worst case O(N²)

Space: O(1)
```

No optimization: simply check all valid pairs.

---

# 7. Optimal Solution

Maintain a HashSet containing at most the **previous `k` elements**.

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for right in range(len(nums)):

            # Keep only the previous k elements.
            if right > k:
                window.remove(nums[right - k - 1])

            # Same value appeared within distance k.
            if nums[right] in window:
                return True

            # Current value can affect future indices.
            window.add(nums[right])

        return False
```

### Why remove `right - k - 1`?

Suppose:

```text
right = 4
k = 2
```

For index `4`, valid previous indices are:

```text
2, 3

|4-2| = 2 ✓
|4-3| = 1 ✓
```

Index `1` is too far:

```text
|4-1| = 3 > 2
```

The expired index is therefore:

```text
right - k - 1

4 - 2 - 1 = 1
```

### Complexity

```text
Time:  O(N)
Space: O(min(N, K))
```

Each element enters the set once and leaves at most once.

---

# 8. Step-by-Step Trace

Take:

```text
nums = [1,2,3,1]
k = 3
```

| `right` | Current | Window before check | Duplicate? | Window after  |
| ------: | ------: | ------------------- | ---------- | ------------- |
|       0 |       1 | `{}`                | No         | `{1}`         |
|       1 |       2 | `{1}`               | No         | `{1,2}`       |
|       2 |       3 | `{1,2}`             | No         | `{1,2,3}`     |
|       3 |       1 | `{1,2,3}`           | **Yes**    | Return `True` |

At `right = 3`:

```text
current = 1

window = {1,2,3}

1 in window
↓
There exists previous 1
within the last k=3 indices
↓
True
```

### Trace where removal matters

```text
nums = [1,2,3,1]
k = 2
```

Before processing index `3`:

```text
right = 3
k = 2

expired index
= right - k - 1
= 3 - 2 - 1
= 0

remove nums[0] = 1

window:
{1,2,3}
   ↓
{2,3}
```

Now:

```text
nums[3] = 1

1 not in {2,3}

→ no nearby duplicate
```

Exactly correct because:

```text
3 - 0 = 3 > k
```

---

# 9. Related Problems

| Problem                                               | Progression                                                                                          |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **217. Contains Duplicate**                           | Simplest version: HashSet detects duplicates anywhere.                                               |
| **219. Contains Duplicate II**                        | Adds index-distance constraint → bounded HashSet window.                                             |
| **3. Longest Substring Without Repeating Characters** | Same set + removal idea, but window size becomes variable based on duplicates.                       |
| **904. Fruit Into Baskets**                           | Variable window using frequencies; maintain at most two distinct values.                             |
| **220. Contains Duplicate III**                       | Adds both index-distance and value-distance constraints, requiring a more advanced window structure. |

## Quick Revision

```text
Signal:
|i-j| <= k + duplicate

Think:
"Only previous k elements matter."

Pattern:
Fixed/bounded Sliding Window + HashSet

Algorithm:
for each right:
    remove expired element
    check nums[right] in window
    add nums[right]

Invariant:
window contains only previous elements
close enough to current index.

Time  = O(N)
Space = O(K)
```

The key progression to remember is:

```text
Contains Duplicate
      ↓
HashSet

Contains Duplicate II
      ↓
HashSet + remove old values

Longest Substring Without Repeating Characters
      ↓
HashSet + shrink until valid
```
