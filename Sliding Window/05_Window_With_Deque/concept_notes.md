# Sliding Window with Deque

## 1. Pattern in One Minute

**Core idea:** Maintain a **monotonic deque of useful candidates** while a window moves across the array.

Think of it when you see:

> **Sliding window + need max/min efficiently**

Without a deque, finding the maximum of every window of size `k` can cost **O(k)** per window → **O(nk)**.

A monotonic deque keeps only elements that could still become the answer, giving **O(n)** overall.

**Mnemonic:**

> **Expire from front, dominate from back, answer from front.**

---

## 2. Recognition Signals

Strong clues:

* "Maximum/minimum in every subarray of size `k`"
* Window moves one position at a time
* Need the best value inside the **current window**
* `n` is large, so recomputing max/min is too expensive
* You need both:

  * efficient removal of expired elements
  * efficient knowledge of the current max/min

### Why deque?

Suppose:

```text
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
```

For maximum, maintain a **decreasing deque**:

```text
Window [1, 3, -1]

Deque values:
1
1 → see 3 → remove 1
3
3 → see -1
3, -1

max = 3
```

When `5` arrives later:

```text
deque = [3, -1, -3]

5 arrives

-3 < 5 → useless
-1 < 5 → useless
3  < 5 → useless

deque = [5]
```

Those smaller values can never become maximum before `5` leaves, because **5 is both newer and larger**.

### When NOT to use it

Don't reach for monotonic deque just because you see "sliding window."

For things like:

* longest substring without repeats → hash map/set
* at most `k` distinct → frequency map
* window sum/average → running sum
* arbitrary order statistics/median → heaps or balanced structure

Deque shines when the window needs an **extreme value or monotonic candidate optimization**.

---

# 3. Mental Model

For **Sliding Window Maximum**, maintain:

```text
deque = indices of candidates
values = decreasing
```

Example:

```text
nums = [8, 3, 5, 2]
```

Possible deque:

```text
indices: [0, 2, 3]
values:  [8, 5, 2]
```

Why isn't `3` there?

Because when `5` arrived:

```text
3 < 5
```

`3` became useless. `5` is:

```text
larger + newer
```

So `3` can never beat `5`.

The algorithm for every `right`:

```text
1. Remove expired indices from FRONT
2. Remove dominated values from BACK
3. Add current index to BACK
4. Once window reaches size k:
      answer = FRONT
```

### Front vs Back

This distinction is the entire pattern:

```text
FRONT → expiration + answer
BACK  → monotonic maintenance
```

For maximum:

```text
deque values: decreasing

[10, 8, 6, 2]
 ^
 maximum
```

For minimum:

```text
deque values: increasing

[1, 3, 7, 9]
 ^
 minimum
```

---

# 4. Boilerplate Template

### Sliding Window Maximum

```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()       # stores indices
    result = []

    for right, num in enumerate(nums):

        # 1. Remove indices outside the window
        while dq and dq[0] <= right - k:
            dq.popleft()

        # 2. Maintain decreasing values
        while dq and nums[dq[-1]] <= num:
            dq.pop()

        # 3. Add current index
        dq.append(right)

        # 4. Window is valid
        if right >= k - 1:
            result.append(nums[dq[0]])

    return result
```

### The part to memorize

```python
while dq and dq[0] <= right - k:
    dq.popleft()

while dq and nums[dq[-1]] <= nums[right]:
    dq.pop()

dq.append(right)

if right >= k - 1:
    ans.append(nums[dq[0]])
```

Notice we store **indices**, not values.

Why?

Because we need both:

```text
nums[dq[0]] → value
dq[0]       → position, to detect expiration
```

---

# 5. Variations

The most important variation is simply flipping the monotonic direction.

| Need           | Deque order | Remove from back |
| -------------- | ----------- | ---------------- |
| Window maximum | Decreasing  | smaller values   |
| Window minimum | Increasing  | larger values    |

For minimum:

```python
while dq and nums[dq[-1]] >= nums[right]:
    dq.pop()
```

A more advanced disguise is **Shortest Subarray with Sum at Least K**. Here the deque operates on **prefix sums**, not directly on window elements.

Another common family is **DP + bounded range maximum**, where a deque optimizes:

```text
dp[i] = nums[i] + max(dp[j])
                  j in [i-k, i-1]
```

Instead of scanning the previous `k` DP states, maintain their maximum with a deque.

---

# 6. Common Pitfalls

### Storing values instead of indices

Usually store:

```python
dq.append(right)
```

not:

```python
dq.append(nums[right])
```

Indices let you detect expired elements.

### Wrong monotonic direction

For maximum:

```text
decreasing deque
```

For minimum:

```text
increasing deque
```

A useful association:

> **Want max → max lives at front → decreasing.**

### Removing expired elements incorrectly

For window ending at `right`, valid indices are:

```text
[right - k + 1, ..., right]
```

Therefore:

```python
dq[0] <= right - k
```

means expired.

### Thinking nested `while` means O(n²)

It doesn't.

Each index enters the deque once and leaves at most once.

```text
push ≤ n
pop ≤ n
```

So:

**Time: O(n)**
**Space: O(k)**

---

# 7. Interview Checklist

✓ Fixed/bounded moving window?

✓ Need maximum/minimum repeatedly?

✓ Recomputing max/min would cost O(k) each time?

✓ Old elements expire as the window moves?

✓ Some candidates become permanently useless when a better, newer candidate arrives?

Then think:

> **Monotonic Deque**

And remember:

```text
front → expire
back  → dominate
front → answer
```

---

# 8. Must-Do Problems

**Top 3 for revision:**

1. ⭐ **LeetCode 239 — Sliding Window Maximum**
   The canonical monotonic deque problem.

2. ⭐ **LeetCode 862 — Shortest Subarray with Sum at Least K**
   Prefix sum + monotonic deque. Important advanced variation.

3. ⭐ **LeetCode 1696 — Jump Game VI**
   DP + sliding window maximum using deque.

Then do **LeetCode 1438 — Longest Continuous Subarray With Absolute Diff ≤ Limit** to learn the **two-deque** variation: one max deque + one min deque.

---

# 9. 30-Second Cheat Sheet

```text
SLIDING WINDOW + DEQUE

Recognition:
Window moves + repeatedly need max/min.

Core idea:
Keep only candidates that can still become the answer.

MAX:
    decreasing deque
    [9, 7, 5, 2]
     ↑ max

MIN:
    increasing deque
    [1, 3, 6, 8]
     ↑ min

Template:

for right in range(n):

    # expired
    while dq and dq[0] <= right - k:
        dq.popleft()

    # dominated
    while dq and nums[dq[-1]] <= nums[right]:
        dq.pop()

    dq.append(right)

    if right >= k - 1:
        ans.append(nums[dq[0]])

Remember:
FRONT = expiration + answer
BACK  = remove dominated candidates

MAX → decreasing
MIN → increasing

Store INDICES.

Complexity:
O(n) time
O(k) space

Mnemonic:
"Expire front, dominate back, answer front."
```

The key insight worth carrying into interviews is **not** merely "deque gives max in O(1)." It's:

> **When a newer element is better than an older element, the older one may never be useful again—delete it immediately.**
