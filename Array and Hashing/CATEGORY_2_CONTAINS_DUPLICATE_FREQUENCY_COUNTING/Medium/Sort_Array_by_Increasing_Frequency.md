# 1636. Sort Array by Increasing Frequency

**Pattern:** Frequency Counting + Custom Sorting
**Difficulty:** Easy

---

## 1. Problem Statement

Given an integer array `nums`, sort it according to these rules:

1. Elements with **lower frequency come first**.
2. If two elements have the **same frequency**, the **larger value comes first**.

Return the sorted array.

### Example

```text
nums = [1,1,2,2,2,3]

Frequency:
1 → 2
2 → 3
3 → 1

Sort by frequency ↑:
3, 1,1, 2,2,2

Answer = [3,1,1,2,2,2]
```

### Constraints

```text
1 <= nums.length <= 100
-100 <= nums[i] <= 100
```

The constraints are small, so sorting the array directly with a custom key is ideal.

---

# 2. Diagram

Consider:

```text
nums = [2,3,1,3,2]

Step 1: Count

Value       1    2    3
Frequency   1    2    2

Step 2: Decide order

1 → freq 1
3 → freq 2
2 → freq 2
     ↑
same frequency:
larger number first

So:

1 → 3 → 2

Result:

[1, 3,3, 2,2]
```

The key idea is:

```text
Primary sorting rule   → frequency ascending
Secondary sorting rule → value descending
```

---

# 3. Example I/O

### Example 1 — Typical

```text
Input:
nums = [1,1,2,2,2,3]

Output:
[3,1,1,2,2,2]
```

Because:

```text
3 → 1 time
1 → 2 times
2 → 3 times
```

---

### Example 2 — Tie in frequency

```text
Input:
nums = [2,3,1,3,2]

Output:
[1,3,3,2,2]
```

`2` and `3` both occur twice, so larger value `3` comes first.

---

### Edge Case

```text
Input:
nums = [-1,1,-6,4,5,-6,1,4,1]

Output:
[5,-1,4,4,-6,-6,1,1,1]
```

Notice that descending value order also applies correctly to negative numbers.

---

# 4. Intuition & Pattern Recognition

The important signal is:

> **Sort elements based on how many times they occur.**

Whenever the ordering depends on frequency, immediately think:

```text
Frequency Counting
       ↓
HashMap / Counter
       ↓
Custom Sorting
```

The problem gives us **two sorting conditions**:

```text
1. frequency ↑
2. value ↓ when frequencies tie
```

So each number can conceptually be represented as:

```text
number → (frequency, value)

1 → (2, 1)
2 → (3, 2)
3 → (1, 3)
```

We need to sort using:

```text
(frequency ascending, value descending)
```

In Python, ascending sorting is the default, so we can convert descending value into ascending `-value`:

```text
(freq[x], -x)
```

### Interview recognition

Say to yourself:

> "Ordering depends on frequency, so first build a frequency map. Then sort using frequency as the primary key and value as the tie-breaker."

That is essentially the whole problem.

---

# 5. Simpler Version

This problem becomes easy if you separate the two ideas.

### Simpler idea 1: Count frequencies

Think of **Contains Duplicate** / **Valid Anagram** style problems.

```python
freq[x] += 1
```

For:

```text
[1,1,2,2,2,3]

freq = {
    1: 2,
    2: 3,
    3: 1
}
```

Now every element knows its frequency.

### Simpler idea 2: Sort by one property

Suppose the question only said:

> Sort numbers by increasing frequency.

Then:

```python
nums.sort(key=lambda x: freq[x])
```

Done.

### Current problem adds a tie-breaker

Now:

> If frequency is equal, larger number comes first.

So instead of one sorting key:

```text
frequency
```

we need two:

```text
(frequency, -value)
```

Therefore:

```python
nums.sort(key=lambda x: (freq[x], -x))
```

### Thinking progression

```text
Contains Duplicate
       ↓
Learn frequency counting

Valid Anagram
       ↓
Frequency maps represent occurrence counts

Sort by frequency
       ↓
key = freq[x]

Need tie-breaking
       ↓
key = (freq[x], -x)

       ↓

Sort Array by Increasing Frequency
```

This is less about a sophisticated algorithm and more about **frequency map + multi-condition sorting**.

---

# 6. Brute Force

For every number, scan the entire array to calculate its frequency during sorting.

Conceptually:

```python
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:

        def frequency(x):
            count = 0

            for num in nums:
                if num == x:
                    count += 1

            return count

        return sorted(nums, key=lambda x: (frequency(x), -x))
```

The problem is that frequency is repeatedly calculated.

With `N` elements, each frequency lookup can cost `O(N)`, and sorting performs many comparisons/key evaluations depending on implementation.

A straightforward brute-force framing is roughly:

```text
Time:  O(N² + N log N)
Space: O(N)
```

We can eliminate the repeated frequency calculation with a hash map.

---

# 7. Optimal Solution

```python
from collections import Counter

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:

        # Count occurrence of every number
        freq = Counter(nums)

        # Lower frequency first.
        # For equal frequency, larger value first.
        nums.sort(key=lambda x: (freq[x], -x))

        return nums
```

The most important line is:

```python
nums.sort(key=lambda x: (freq[x], -x))
```

Understand it as:

```text
               primary     secondary
                   ↓           ↓
key(x) =      (freq[x],       -x)
                   ↑           ↑
              ascending    descending
```

### Why does `-x` give descending order?

Suppose:

```text
x = 2, 3, 5
```

Their sorting keys become:

```text
2 → -2
3 → -3
5 → -5
```

Ascending order:

```text
-5 < -3 < -2
```

therefore original values become:

```text
5, 3, 2
```

### Complexity

Counting:

```text
O(N)
```

Sorting:

```text
O(N log N)
```

Overall:

```text
Time  : O(N log N)
Space : O(N)
```

`Counter` can contain up to `N` distinct values.

---

# 8. Step-by-Step Trace

Take:

```text
nums = [2,3,1,3,2]
```

First build:

```text
freq = {
    2: 2,
    3: 2,
    1: 1
}
```

Now calculate each element's sorting key:

|  x | freq[x] | -x | Sort Key |
| -: | ------: | -: | -------: |
|  2 |       2 | -2 | `(2,-2)` |
|  3 |       2 | -3 | `(2,-3)` |
|  1 |       1 | -1 | `(1,-1)` |
|  3 |       2 | -3 | `(2,-3)` |
|  2 |       2 | -2 | `(2,-2)` |

Python compares tuples from left to right.

First:

```text
(1,-1)
```

comes before all `(2, ...)` because:

```text
1 < 2
```

So `1` comes first.

For `2` and `3`:

```text
2 → (2,-2)
3 → (2,-3)
```

Frequencies tie, so compare:

```text
-3 < -2
```

Therefore:

```text
3 before 2
```

Final:

```text
[1,3,3,2,2]
```

---

# 9. Related Problems

| Problem                               | Connection                                                                 |
| ------------------------------------- | -------------------------------------------------------------------------- |
| **217. Contains Duplicate**           | Basic HashSet introduction for detecting repeated values.                  |
| **242. Valid Anagram**                | Basic frequency counting with HashMap/Counter.                             |
| **347. Top K Frequent Elements**      | Frequency counting followed by ranking elements based on frequency.        |
| **451. Sort Characters By Frequency** | Very close pattern, but characters are sorted by **decreasing** frequency. |
| **692. Top K Frequent Words**         | Frequency counting plus an important custom tie-breaking rule.             |

---

## Quick Revision

```text
Sort Array by Increasing Frequency

Pattern:
Frequency Counting + Custom Sort

1. Count frequencies
   freq = Counter(nums)

2. Sort using:
   frequency ↑
   value ↓

3. Python trick:
   key = (freq[x], -x)

Code:
freq = Counter(nums)
nums.sort(key=lambda x: (freq[x], -x))

Time  = O(N log N)
Space = O(N)
```

The key interview takeaway is **multi-condition sorting**: represent the priority rules as a tuple in priority order.

This builds naturally on the frequency-counting ideas from your earlier revision material; the uploaded sheet shows the same general use of hash-based state for efficient decisions. 
