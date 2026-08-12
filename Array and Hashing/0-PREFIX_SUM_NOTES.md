# Prefix Sum — DSA Pattern Revision

## 1. Pattern in One Minute

**Core idea:** preprocess cumulative sums so that repeated **range-sum queries** become O(1).

For:

```text
nums = [2, 4, 1, 3, 5]
```

Build:

```text
prefix = [0, 2, 6, 7, 10, 15]
          ↑
       sum of 0 elements
```

Here:

```text
prefix[i] = sum(nums[0:i])
```

So sum from index `L` through `R` is:

```text
range_sum(L, R) = prefix[R + 1] - prefix[L]
```

**Mnemonic:**

> **Sum until R − Sum before L**

Think **Prefix Sum** when you see **subarray + sum/count + repeated ranges**, or when a subarray condition can be transformed using two prefix sums.

---

# 2. Recognition Signals

### Strong signals

* "Sum of elements from index `L` to `R`"
* Many **range sum queries**
* "Number of subarrays whose sum equals `K`"
* "Subarray sum divisible by K"
* "Equal number of 0s and 1s"
* "Pivot/equilibrium index"
* Need left sum / right sum at every position
* 2D rectangle-region sums

### The deeper signal

For a subarray `[i ... j]`:

```text
sum(i...j) = prefix[j + 1] - prefix[i]
```

Therefore:

```text
sum(i...j) == k

prefix[j + 1] - prefix[i] == k

prefix[i] == prefix[j + 1] - k
```

This leads to the extremely common pattern:

> **Prefix Sum + HashMap**

### When NOT to use it

If the array changes frequently, normal prefix sums become expensive to maintain. Think **Fenwick Tree / Segment Tree** instead.

For a simple one-pass maximum/minimum subarray problem, another pattern such as Kadane's algorithm may be cleaner.

---

# 3. Mental Model

Think of prefix sum as **checkpoints of everything accumulated before me**.

Given:

```text
nums:    [3,  2,  5,  1]
index:    0   1   2   3

prefix: [0,  3,  5, 10, 11]
```

Want `[1...3]`:

```text
          [3, 2, 5, 1]
               └──────┘
               2 + 5 + 1

prefix[4] = 3 + 2 + 5 + 1 = 11
prefix[1] = 3             =  3
                               -
                               8
```

So:

```python
prefix[R + 1] - prefix[L]
```

The leading `0` is extremely useful because it removes special handling for ranges starting at index `0`.

The more powerful mental model is:

```text
subarray = difference between two prefix states
```

So many subarray problems become:

> "Have I seen the prefix state I need earlier?"

That is why prefix sums frequently pair with a `dict` or `set`.

---

# 4. Boilerplate Templates

### A. Classic Range Sum

```python
def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)

    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x

    return prefix


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

**Complexity:** preprocessing O(n), each query O(1), space O(n).

---

### B. Prefix Sum + HashMap

For **number of subarrays with sum `k`**:

```python
def subarraySum(nums, k):
    freq = {0: 1}
    prefix = 0
    ans = 0

    for x in nums:
        prefix += x

        ans += freq.get(prefix - k, 0)

        freq[prefix] = freq.get(prefix, 0) + 1

    return ans
```

Why `prefix - k`?

```text
currentPrefix - oldPrefix = k

oldPrefix = currentPrefix - k
```

Why `{0: 1}`?

It represents the empty prefix before the array starts, allowing subarrays beginning at index `0` to be counted naturally.

---

# 5. Variations

| Variation                   | Key change                                     |
| --------------------------- | ---------------------------------------------- |
| Range Sum Query             | Build prefix array                             |
| Subarray Sum = K            | Prefix + frequency map                         |
| Subarray Sum divisible by K | Store `prefix % k` frequencies                 |
| Equal 0s and 1s             | Convert `0 → -1`, find equal prefix sums       |
| Pivot Index                 | `left_sum == total - left_sum - nums[i]`       |
| Product Except Self         | Prefix product + suffix product                |
| 2D Matrix Region Sum        | 2D prefix sum                                  |
| Range updates               | Difference array, essentially the inverse idea |

### Prefix remainder trick

If:

```text
prefix[j] % k == prefix[i] % k
```

then:

```text
(prefix[j] - prefix[i]) % k == 0
```

So equal remainders indicate a subarray divisible by `k`.

---

# 6. Common Pitfalls

**Off-by-one errors** are the biggest problem.

Prefer:

```python
prefix = [0] * (n + 1)
```

and memorize:

```python
sum(L...R) = prefix[R + 1] - prefix[L]
```

Another common mistake is using a `set` when duplicates matter. For **counting subarrays**, you need frequencies:

```python
freq[prefix] += 1
```

not merely whether the prefix exists.

Also, don't assume sliding window can replace prefix sums for arbitrary subarray-sum problems. With **negative numbers**, expanding the window does not necessarily increase the sum, so classic sliding-window logic breaks. Prefix Sum + HashMap still works.

---

# 7. Interview Checklist

✓ Is the problem about **contiguous subarrays/ranges**?

✓ Do I repeatedly need **sum/count from L to R**?

✓ Can the condition be expressed as:

```text
prefix[j] - prefix[i] = something
```

✓ Do I need to know whether an earlier prefix existed?
→ **Prefix + Set**

✓ Do I need to know how many times it existed?
→ **Prefix + HashMap frequency**

✓ Is divisibility involved?
→ Think **prefix remainder**

✓ Are there many static range queries?
→ Precompute prefix array.

---

# 8. Must-Do Problems

### Easy

**⭐ Top 3 — 303. Range Sum Query - Immutable**
Pure prefix-sum fundamentals.

724. Find Pivot Index
     Great for total sum + running prefix.

725. Running Sum of 1d Array
     Basic prefix construction.

### Medium

**⭐ Top 3 — 560. Subarray Sum Equals K**
The canonical **Prefix Sum + HashMap** problem.

**⭐ Top 3 — 525. Contiguous Array**
Excellent transformation: `0 → -1`, then repeated prefix states.

523. Continuous Subarray Sum
     Prefix remainder / divisibility pattern.

524. Subarray Sums Divisible by K
     Frequency-map version of prefix remainder.

### Hard

1074. Number of Submatrices That Sum to Target
      Important extension of prefix sum into 2D + hashmap thinking.

For revision, prioritize **303 → 560 → 525**.

---

# 9. 30-Second Cheat Sheet

```text
PREFIX SUM

Recognition:
    range/subarray + sum/count
    repeated range queries
    subarray sum = K
    divisibility / equal counts

Core:
    prefix[i] = sum of nums before i

    prefix = [0, ...]

Range:
    sum(L...R)
    = prefix[R + 1] - prefix[L]

Subarray Sum = K:
    current - previous = k
    previous = current - k

    freq = {0: 1}

    for x in nums:
        prefix += x
        ans += freq[prefix - k]
        freq[prefix] += 1

Divisible by K:
    track prefix % k
    same remainder => difference divisible by k

Equal 0/1:
    convert 0 → -1
    equal prefix => balanced subarray

Complexity:
    Build prefix: O(n)
    Range query: O(1)
    Prefix + HashMap: O(n)
    Space: O(n)

Pitfalls:
    off-by-one
    forget {0: 1}
    set vs frequency map
    sliding window fails with negatives

MEMORY:
    "Subarray = difference of two prefixes."
```
