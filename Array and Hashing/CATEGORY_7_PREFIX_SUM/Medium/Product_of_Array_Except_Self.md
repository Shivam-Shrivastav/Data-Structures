# 238. Product of Array Except Self

**Pattern:** Prefix & Suffix Products / Array

This is a key prefix-suffix problem: instead of recomputing the product for every index, precompute what comes **before** and **after** each position.

---

## 1. Problem Statement

Given an integer array `nums`, return an array `answer` where:

```text
answer[i] = product of every nums[j] where j != i
```

You **cannot use division**, and the intended solution runs in **O(N)** time.

### Constraints that matter

* `2 <= nums.length <= 10^5`
* `-30 <= nums[i] <= 30`
* Prefix/suffix products fit in a 32-bit integer.
* **Division is forbidden.**
* Target: **O(N)** time.

### Example

```text
nums = [1, 2, 3, 4]

answer = [24, 12, 8, 6]
```

Because:

```text
answer[0] = 2 × 3 × 4 = 24
answer[1] = 1 × 3 × 4 = 12
answer[2] = 1 × 2 × 4 = 8
answer[3] = 1 × 2 × 3 = 6
```

---

# 2. Diagram

For each index, split the array into:

```text
Everything LEFT of i   ×   Everything RIGHT of i
```

Example:

```text
nums = [1, 2, 3, 4]
             ↑
             i = 2

LEFT              RIGHT
[1, 2]      3      [4]

 1 × 2             4
   ↓                ↓
   2        ×       4 = 8
```

So:

```text
answer[i] = prefix_product_before_i × suffix_product_after_i
```

For the whole array:

```text
nums:       [ 1,  2,  3,  4 ]

left:       [ 1,  1,  2,  6 ]
              ↑
          product BEFORE i

right:      [24, 12,  4,  1 ]
                          ↑
                   product AFTER i

left*right: [24, 12,  8,  6]
```

Notice the important detail:

```text
left[i]  does NOT include nums[i]
right[i] does NOT include nums[i]
```

---

# 3. Example I/O

### Example 1 — Typical

```text
Input:
nums = [1, 2, 3, 4]

Output:
[24, 12, 8, 6]
```

For index `2`:

```text
1 × 2 × 4 = 8
```

### Example 2 — Zero + negatives

```text
Input:
nums = [-1, 1, 0, -3, 3]

Output:
[0, 0, 9, 0, 0]
```

At index `2`, we exclude the zero:

```text
(-1) × 1 × (-3) × 3 = 9
```

Every other index includes the zero, so its product is `0`.

This is one reason the prefix/suffix approach is cleaner than trying to work around division.

---

# 4. Intuition & Pattern Recognition

The key phrase is:

> **"Product of all elements except the current element."**

At index `i`, the elements we need naturally split into two groups:

```text
nums = [ ... left ... ] nums[i] [ ... right ... ]
```

Therefore:

```text
answer[i]
=
product(left side)
×
product(right side)
```

That should trigger:

> **Prefix + Suffix**

### Interview thinking

Say to yourself:

```text
I can't use division.

For every index I need information
from everything before it
and everything after it.

So I'll compute the product before i
with a left-to-right pass,

then multiply by the product after i
with a right-to-left pass.
```

### Why does it work?

Every element except `nums[i]` is either:

```text
index < i    → prefix
index > i    → suffix
```

There is nothing else.

Therefore:

```text
prefix[i] × suffix[i]
```

is exactly the product of every element except `nums[i]`.

---

# 5. Simpler Version

Before solving this problem, understand **Prefix Sum**.

## Simpler idea: Prefix Sum

Suppose:

```text
nums = [2, 3, 4, 5]
```

We can store cumulative sums:

```text
prefix = [2, 5, 9, 14]
```

Meaning:

```text
prefix[i] = nums[0] + ... + nums[i]
```

The same idea works with multiplication:

```text
nums   = [2, 3, 4, 5]

prefix product:
         2  6  24  120
```

### But this question needs something slightly different

We don't want:

```text
product up to i
```

We want:

```text
product BEFORE i
```

So:

```text
nums = [1, 2, 3, 4]

prefix-before:

i=0 → nothing before → 1
i=1 → 1              → 1
i=2 → 1×2            → 2
i=3 → 1×2×3          → 6

[1, 1, 2, 6]
```

Similarly from the right:

```text
suffix-after:

[24, 12, 4, 1]
```

Then:

```text
prefix-before × suffix-after
```

gives the answer.

### Simpler thinking → current thinking

```text
Running Sum
    ↓
Prefix Sum
    ↓
Running Product
    ↓
Prefix Product
    ↓
Need values after i too
    ↓
Suffix Product
    ↓
Prefix[i] × Suffix[i]
    ↓
Product of Array Except Self
```

A useful LeetCode stepping stone is **303. Range Sum Query - Immutable**: it teaches the core idea of preprocessing prefix information so repeated range computations do not require rescanning the array.

---

# 6. Brute Force

For every index `i`, loop through the entire array and multiply everything except `nums[i]`.

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(n):
            product = 1

            for j in range(n):
                if i != j:
                    product *= nums[j]

            answer[i] = product

        return answer
```

### Complexity

```text
Time  : O(N²)
Space : O(1) auxiliary
```

The output array itself requires `O(N)` space.

---

# 7. Optimal Solution

We could create separate `left[]` and `right[]` arrays, but we don't need to.

Use the output array itself to store prefix products.

### Pass 1: Left → Right

```text
answer[i] = product of everything LEFT of i
```

### Pass 2: Right → Left

Maintain one variable:

```text
suffix = product of everything RIGHT of i
```

Then:

```text
answer[i] *= suffix
```

### Python

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1

        # answer[i] = product of all elements before i
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Multiply by product of all elements after i
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
```

### Complexity

```text
Time  : O(N)

Auxiliary Space : O(1)
Output Space    : O(N)
```

LeetCode does not count the returned `answer` array as extra space for this problem.

---

# 8. Step-by-Step Trace

```text
nums = [1, 2, 3, 4]
```

## Pass 1 — Prefix

Start:

```text
answer = [1, 1, 1, 1]
prefix = 1
```

|  i | nums[i] | answer[i] gets | prefix after multiplication | answer      |
| -: | ------: | -------------: | --------------------------: | ----------- |
|  0 |       1 |              1 |                           1 | `[1,1,1,1]` |
|  1 |       2 |              1 |                           2 | `[1,1,1,1]` |
|  2 |       3 |              2 |                           6 | `[1,1,2,1]` |
|  3 |       4 |              6 |                          24 | `[1,1,2,6]` |

Now:

```text
answer = [1, 1, 2, 6]

Meaning:

answer[0] = product before index 0 = 1
answer[1] = product before index 1 = 1
answer[2] = product before index 2 = 2
answer[3] = product before index 3 = 6
```

## Pass 2 — Suffix

Start:

```text
suffix = 1
answer = [1, 1, 2, 6]
```

|  i | nums[i] | suffix before | answer[i] after `*= suffix` | suffix after |
| -: | ------: | ------------: | --------------------------: | -----------: |
|  3 |       4 |             1 |                           6 |            4 |
|  2 |       3 |             4 |                           8 |           12 |
|  1 |       2 |            12 |                          12 |           24 |
|  0 |       1 |            24 |                          24 |           24 |

Final:

```text
answer = [24, 12, 8, 6]
```

### The subtle part

Order matters:

```python
answer[i] *= suffix
suffix *= nums[i]
```

and **not**:

```python
suffix *= nums[i]
answer[i] *= suffix
```

Why?

Because `suffix` should contain elements **after** `i`, not `nums[i]` itself.

Same idea during the prefix pass:

```python
answer[i] = prefix
prefix *= nums[i]
```

Store first, then include the current number.

---

# 9. Related Problems

| Problem                               | Connection                                                                         |
| ------------------------------------- | ---------------------------------------------------------------------------------- |
| **1480. Running Sum of 1d Array**     | Simplest introduction to accumulating information from the left.                   |
| **303. Range Sum Query - Immutable**  | Introduces prefix preprocessing to avoid repeated work.                            |
| **724. Find Pivot Index**             | Uses left and right aggregate information around each index.                       |
| **238. Product of Array Except Self** | Prefix and suffix products combined without division.                              |
| **42. Trapping Rain Water**           | A harder application of information from both the left and right of each position. |

## Revision takeaway

```text
"Except self"
     +
"Can't use division"
     ↓
Split around i

LEFT of i × RIGHT of i
     ↓
Prefix × Suffix
     ↓
Two passes 
     ↓
O(N) time + O(1) auxiliary space
```

The most important implementation pattern to remember is:

```python
prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]

suffix = 1

for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= nums[i]
```

This follows the same quick-revision structure as your uploaded DSA revision material. 
