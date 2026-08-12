# **1283. Find the Smallest Divisor Given a Threshold (Binary Search on Answer)**

---

# 1. Problem Statement

You are given an integer array `nums` and an integer `threshold`.

Choose a **positive integer divisor**.

For every element in `nums`, divide it by the divisor and **round up** the result.

Compute

[
\text{sum} = \sum \lceil nums[i] / divisor \rceil
]

Return the **smallest divisor** such that

```text
sum <= threshold
```

---

### Constraints

* `1 <= nums.length <= 5 × 10⁴`
* `1 <= nums[i] <= 10⁶`
* `nums.length <= threshold <= 10⁶`

The divisor can be very large, so trying every divisor is impossible.

---

## Example

```text
Input:
nums = [1,2,5,9]
threshold = 6

Output:
5
```

Explanation

```text
Divisor = 5

ceil(1/5)=1
ceil(2/5)=1
ceil(5/5)=1
ceil(9/5)=2

Total = 5

5 <= 6 ✅
```

Smaller divisors produce a larger sum.

---

# 2. Diagram

```text
Possible Divisors

1    2    3    4    5    6    7...
|----|----|----|----|----|----|

Computed Sum

17
10
7
7
5 ✅
5
4
...
```

Notice

```text
Divisor ↑

Sum ↓
```

Once a divisor works,

```text
False False False True True True
```

Perfect Binary Search.

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [1,2,5,9]
threshold = 6

Output:
5
```

Explanation

```text
Divisor 4

1+1+2+3 =7 ❌

Divisor 5

1+1+1+2 =5 ✅
```

---

### Example 2 (Edge Case)

```text
Input:
nums = [10]
threshold = 1

Output:
10
```

Need

```text
ceil(10/divisor)=1
```

Only possible when divisor ≥ 10.

---

# 4. Intuition & Pattern Recognition

### Signal 1

Question asks for

> **Smallest divisor**

This is a Binary Search clue.

---

### Signal 2

Suppose divisor = 8 works.

Then

```text
9 works
10 works
11 works
...
```

Larger divisor always decreases (or keeps) the sum.

Monotonic.

```text
False False False True True True
```

---

### Signal 3

We're not searching the array.

We're searching

```text
Divisor

1

↓

max(nums)
```

Binary Search on Answer.

---

### Interview Thinking

Ask:

> If I guess a divisor, can I verify it?

Yes.

Just calculate

```text
Σ ceil(num/divisor)
```

If

```text
sum <= threshold
```

it works.

---

# 5. Simpler Version

## Simplest Problem

Suppose

```text
nums = [12]

threshold = 3
```

Need

```text
ceil(12/divisor) <=3
```

Minimum divisor?

```text
divisor =4
```

---

Now multiple numbers.

Instead of checking one,

sum the ceiling divisions.

---

## Simpler LeetCode Problems

### 1. **374. Guess Number Higher or Lower**

Basic Binary Search.

---

### 2. **875. Koko Eating Bananas**

Guess speed.

Compute hours.

Exactly the same idea.

---

### 3. **1011. Capacity To Ship Packages**

Guess capacity.

Compute days.

Same Binary Search on Answer pattern.

---

### Thinking Progression

```text
Guess Number
      ↓
Binary Search

Koko
      ↓
Guess Speed

Smallest Divisor
      ↓
Guess Divisor

Capacity to Ship
      ↓
Guess Capacity
```

---

# 6. Brute Force

Try every divisor.

```text
1

↓

max(nums)
```

For every divisor,

compute the total sum.

Return the first valid divisor.

### Python

```python
class Solution:
    def smallestDivisor(self, nums, threshold):

        for divisor in range(1, max(nums) + 1):

            total = 0

            for num in nums:
                total += (num + divisor - 1) // divisor

            if total <= threshold:
                return divisor
```

### Complexity

Time

```text
O(max(nums) × n)
```

Too slow.

---

# 7. Optimal Solution

---

## Search Space

Smallest divisor

```text
1
```

Largest divisor

```text
max(nums)
```

No need to search beyond the largest number.

---

## Check Function

Given divisor,

calculate

```text
Σ ceil(num/divisor)
```

If

```text
sum <= threshold
```

Try a smaller divisor.

Else

Need a larger divisor.

---

## Python

```python
class Solution:
    def smallestDivisor(self, nums, threshold):

        left = 1
        right = max(nums)

        while left <= right:

            mid = (left + right) // 2

            total = 0

            # Calculate the sum after dividing by mid
            for num in nums:
                total += (num + mid - 1) // mid   # ceil(num / mid)

            if total <= threshold:
                # mid works, try a smaller divisor
                right = mid - 1
            else:
                # divisor too small
                left = mid + 1

        return left
```

---

### Why `(num + mid - 1) // mid`?

It computes

```text
ceil(num / mid)
```

Example

```text
num = 9

divisor =4

ceil(9/4)=3

Formula

(9+4-1)//4

12//4

3
```

---

### Complexity

Binary Search

```text
O(log(max(nums)))
```

Each check

```text
O(n)
```

Overall

```text
O(n log(max(nums)))
```

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,2,5,9]

threshold =6
```

Initial

```text
left=1

right=9
```

---

### Iteration 1

```text
mid=5
```

Compute

```text
1→1

2→1

5→1

9→2

Total=5
```

Works.

```text
right=4
```

---

### Iteration 2

```text
left=1

right=4

mid=2
```

Compute

```text
1→1

2→1

5→3

9→5

Total=10
```

Too large.

```text
left=3
```

---

### Iteration 3

```text
left=3

right=4

mid=3
```

Compute

```text
1→1

2→1

5→2

9→3

Total=7
```

Too large.

```text
left=4
```

---

### Iteration 4

```text
mid=4
```

Compute

```text
1→1

2→1

5→2

9→3

Total=7
```

Still too large.

```text
left=5
```

Loop ends.

Answer

```text
5
```

---

## Trace Table

| Left | Right | Mid | Computed Sum | Decision             |
| ---: | ----: | --: | -----------: | -------------------- |
|    1 |     9 |   5 |            5 | Works → Right = 4    |
|    1 |     4 |   2 |           10 | Too Small → Left = 3 |
|    3 |     4 |   3 |            7 | Too Small → Left = 4 |
|    4 |     4 |   4 |            7 | Too Small → Left = 5 |
| Stop |       |     |              | **Answer = 5**       |

---

# 9. Related Problems (Increasing Difficulty)

1. Koko Eating Bananas – Guess the minimum eating speed and check the total hours.

2. Capacity To Ship Packages Within D Days – Guess the minimum ship capacity and count required days.

3. Split Array Largest Sum – Guess the maximum subarray sum and count partitions.

4. Minimum Limit of Balls in a Bag – Guess the smallest allowed maximum bag size while counting operations.

5. Magnetic Force Between Two Balls – Binary search on the answer by maximizing the minimum feasible distance.

---

# Binary Search on Answer Cheat Sheet

| Problem                             | Search Space                  | Check Function                  |
| ----------------------------------- | ----------------------------- | ------------------------------- |
| **875. Koko Eating Bananas**        | `1 → max(piles)`              | Calculate total hours           |
| **1011. Capacity To Ship Packages** | `max(weights) → sum(weights)` | Calculate required days         |
| **1283. Smallest Divisor**          | `1 → max(nums)`               | Calculate `Σ ceil(num/divisor)` |
| **410. Split Array Largest Sum**    | `max(nums) → sum(nums)`       | Calculate required partitions   |

### Interview Recognition

Whenever you see:

* ✅ Find the **smallest/largest possible value**
* ✅ You can **guess** an answer
* ✅ You can **verify** the guess in **O(n)**
* ✅ Valid answers form a monotonic pattern (`False False ... True True`)

Think:

> **Binary Search on Answer**.

For this problem specifically:

* **Answer to guess:** `divisor`
* **Search range:** `1 → max(nums)`
* **Check function:** Compute `Σ ceil(num / divisor)` and verify `sum <= threshold`.
