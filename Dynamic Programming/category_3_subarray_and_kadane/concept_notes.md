# Subarray & Kadane — DP

## 1. Pattern in One Minute

**Core idea:**
When the problem asks for the **best contiguous subarray**, think **Kadane's Algorithm**.

The key DP state:

> `dp[i] = best sum of a subarray that MUST end at index i`

At every element, you have only 2 choices:

```text
START a new subarray here
OR
EXTEND the previous subarray
```

So:

```python
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

And the overall answer is:

```python
max(dp)
```

### Immediately think Kadane when:

* "maximum subarray sum"
* "largest sum of a contiguous subarray"
* "best contiguous segment"
* Array contains **positive + negative numbers**
* Need an optimal contiguous range

Classic problem: **LeetCode 53 — Maximum Subarray**

---

## 2. Recognition Signals

### Strong signals

| Signal                                | Think                |
| ------------------------------------- | -------------------- |
| Contiguous subarray                   | Kadane candidate     |
| Maximum/minimum sum                   | Kadane               |
| Positive + negative values            | Kadane               |
| Need best segment/range               | Kadane               |
| Can choose where subarray starts/ends | Kadane               |
| O(n) expected                         | Strong Kadane signal |

### Common disguises

The problem may not literally say "maximum subarray."

Examples:

* Maximum subarray sum
* Maximum profit-like contiguous gain
* Maximum product subarray → **Kadane variation**
* Maximum circular subarray → **Kadane variation**
* Maximum sum after deleting one element → **two Kadane states**
* Maximum subarray with constraints → **modified DP**

### Don't use it when

The problem asks for:

* **Subsequence** rather than contiguous subarray
* Fixed-size window → Sliding Window
* Exact target sum → Prefix Sum / HashMap
* Number of subarrays → Prefix Sum / HashMap / DP depending on problem
* All subarrays → usually not plain Kadane

**Keyword to remember:**

> **Subarray = contiguous. Kadane exploits contiguity.**

---

# 3. Mental Model

Suppose:

```text
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

At every position ask:

> **"Is my previous subarray helping me, or should I start fresh?"**

### The 7-second thought process

1. I'm building the best subarray ending **here**.
2. Previous best ending at `i-1` is `current`.
3. I can append `nums[i]`.
4. Or abandon everything before it.
5. Therefore:

```python
current = max(nums[i], current + nums[i])
```

6. Keep the best `current` seen globally.
7. A negative running sum is effectively baggage.

### The important intuition

If:

```text
current = -10
nums[i] = 5
```

Then:

```text
-10 + 5 = -5
```

is worse than simply:

```text
5
```

So throw away the previous subarray.

**Mnemonic:**

> **"If my past hurts me, restart."**

---

# 4. Boilerplate Template

### Standard Kadane

```python
def maxSubArray(nums):
    current = nums[0]
    best = nums[0]

    for x in nums[1:]:
        current = max(x, current + x)
        best = max(best, current)

    return best
```

### DP-array version

```python
def maxSubArray(nums):
    n = len(nums)
    dp = [0] * n

    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])

    return max(dp)
```

### Interview version to remember

Don't memorize the whole code.

Memorize:

```text
current = max(x, current + x)
best = max(best, current)
```

That's basically Kadane.

**Complexity:** `O(n)` time, `O(1)` space.

---

# 5. Variations

### 1. Maximum Subarray

Standard:

```python
current = max(x, current + x)
best = max(best, current)
```

**Top 3:** ⭐ **LeetCode 53 — Maximum Subarray**

---

### 2. Maximum Product Subarray

Problem: **LeetCode 152**

You need both:

```text
max_so_far
min_so_far
```

Why?

Because:

```text
negative × negative = positive
```

So the previous minimum can become the new maximum.

Mental model:

> **Kadane + track both extremes.**

⭐ **Top 3**

---

### 3. Maximum Circular Subarray

Problem: **LeetCode 918**

Two possibilities:

```text
normal maximum subarray
OR
wrap-around maximum subarray
```

Use:

```text
max_subarray
```

and:

```text
total_sum - min_subarray
```

So:

```python
answer = max(max_sum, total_sum - min_sum)
```

Important edge case:

> If all numbers are negative, don't use `total_sum - min_sum`.

⭐ **Top 3**

---

### 4. Maximum Subarray Sum With One Deletion

Problem: **LeetCode 1186**

Maintain two states:

```text
no_delete = best sum ending here without deletion
one_delete = best sum ending here with one deletion
```

Transition:

```text
no_delete = max(x, no_delete + x)

one_delete = max(
    one_delete + x,   # deletion happened earlier
    no_delete_old     # delete current x
)
```

Mental model:

> **Kadane + one extra state for "already used my deletion".**

---

### 5. Maximum Subarray With Start/End Indices

Same Kadane, but when starting fresh:

```python
current = x
start = i
```

When finding a better answer:

```python
best = current
best_start = start
best_end = i
```

So Kadane can return the actual subarray, not just its sum.

---

# 6. Common Pitfalls

### ❌ Mistake 1: Resetting negative values manually

You may see:

```python
current += x

if current < 0:
    current = 0
```

This works for the **standard maximum subarray problem when there is at least one positive number**, but it can become awkward with all-negative arrays.

Safer interview template:

```python
current = max(x, current + x)
best = max(best, current)
```

---

### ❌ Mistake 2: Confusing subarray with subsequence

```text
[1, 2, 3, 4]
```

Subarray:

```text
[2, 3]
```

Subsequence:

```text
[1, 3, 4]
```

Kadane is fundamentally about **contiguous** elements.

---

### ❌ Mistake 3: Forgetting all-negative arrays

```text
[-5, -2, -8]
```

Answer:

```text
-2
```

Not `0`.

Therefore initialize with:

```python
current = best = nums[0]
```

---

### ❌ Mistake 4: Thinking `dp[i]` means "best answer in first i elements"

For standard Kadane:

```text
dp[i] = best sum of a subarray ENDING at i
```

That distinction is extremely important.

---

# 7. Interview Checklist

✓ Is it asking about a **contiguous subarray**?

✓ Is it asking for the **maximum/minimum sum/value**?

✓ Can I describe the decision as:

```text
extend previous
OR
start fresh
```

✓ Then:

```python
current = max(x, current + x)
```

✓ Maintain global:

```python
best = max(best, current)
```

✓ If product/circular/deletion appears → **Kadane variation**.

---

# 8. Must-Do Problems

### Easy

* **LeetCode 121 — Best Time to Buy and Sell Stock**

  * Kadane-like thinking with daily gains.
* **LeetCode 53 — Maximum Subarray** ⭐ **TOP 3**

### Medium

* **LeetCode 152 — Maximum Product Subarray** ⭐ **TOP 3**
* **LeetCode 918 — Maximum Sum Circular Subarray** ⭐ **TOP 3**
* **LeetCode 1191 — K-Concatenation Maximum Sum**
* **LeetCode 1186 — Maximum Subarray Sum with One Deletion**

### Hard

* **LeetCode 1749 — Maximum Absolute Sum of Any Subarray**
* More complex constrained subarray problems generally combine Kadane-style DP with another technique.

### For revision, these 3 are enough initially:

> **53 → 152 → 918**

They teach the three most important Kadane shapes:

```text
53   → basic Kadane
152  → multiple states
918  → Kadane + transformation
```

---

# 9. 30-Second Cheat Sheet

```text
KADANE
────────────────────────────────

Recognition:
Contiguous subarray + maximize/minimize sum/value

Core idea:
At each x:

    extend previous
        OR
    start fresh

Template:

current = max(x, current + x)
best = max(best, current)

DP meaning:
current = best subarray SUM ENDING HERE

Complexity:
Time  → O(n)
Space → O(1)

Variations:
Maximum Product
→ track max + min

Circular
→ max(normal_max, total - min_subarray)

One deletion
→ track 2 states:
   no_delete
   one_delete

Pitfalls:
→ subarray ≠ subsequence
→ handle all-negative arrays
→ don't confuse "ending here" with "overall best"

Mnemonic:
"If the past hurts me, restart."
```

**The one thing I'd make automatic in your head:**

> **Subarray optimization → "What is the best answer ending HERE?" → Extend or Restart.**
