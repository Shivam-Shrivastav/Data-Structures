# **1248. Count Number of Nice Subarrays (Sliding Window + Prefix Count / At Most K Trick)**

---

# 1. Problem Statement

You are given an integer array `nums` and an integer `k`.

A **nice subarray** is a contiguous subarray that contains **exactly `k` odd numbers**.

Return the number of nice subarrays.

### Constraints

* `1 <= nums.length <= 50,000`
* `1 <= nums[i] <= 10^5`
* `1 <= k <= nums.length`

These constraints eliminate brute force (`O(n²)`).

---

## Example

```text
nums = [1,1,2,1,1]
k = 3

Output = 2
```

The nice subarrays are:

```
[1,1,2,1]
[1,2,1,1]
```

---

# 2. Diagram

```
nums = [1, 1, 2, 1, 1]
         O  O  E  O  O

Need exactly 3 odds.

Window expands →

[1 1 2 1]      ✔
  [1 2 1 1]    ✔

Answer = 2
```

Another way to visualize:

```
Odd Count

1 -> 2 -> 2 -> 3 -> 4
```

We're interested in windows where odd count increases by exactly `k`.

---

# 3. Example I/O

### Example 1

```
Input:
nums = [1,1,2,1,1]
k = 3

Output:
2
```

Explanation:

```
[1,1,2,1]
[1,2,1,1]
```

---

### Example 2 (Edge Case)

```
nums = [2,4,6]
k = 1

Output:
0
```

No odd numbers exist.

---

### Example 3

```
nums = [2,2,1,2,2]
k = 1

Output = 9
```

Every subarray containing that single odd is valid.

---

# 4. Intuition & Pattern Recognition

### Signal 1

Problem asks:

> **Count subarrays**

Immediately think:

* Prefix Sum
* Sliding Window

---

### Signal 2

Condition is

```
Exactly K
```

Sliding window naturally solves

```
At Most K
```

Whenever you see

```
Exactly K
```

ask yourself:

```
Can I compute

Exactly(K)
=
AtMost(K)
-
AtMost(K-1)
```

This trick appears repeatedly.

---

### Signal 3

Odd numbers behave like binary values.

Convert mentally:

```
Odd  -> 1
Even -> 0
```

Example

```
1 1 2 1 1

↓

1 1 0 1 1
```

Now the problem becomes:

> Count binary subarrays having sum exactly K.

This is exactly the same idea as **Binary Subarrays With Sum**.

---

### Interview Thinking

> "I need exactly K odds.
>
> Sliding window can't directly maintain exactly.
>
> But it can maintain at most K.
>
> Therefore answer = AtMost(K)-AtMost(K-1)."

---

# 5. Simpler Version

## Simpler Problem 1

### Maximum Consecutive Ones III

Maintain

```
At most K zeros
```

Sliding window shrinks whenever zeros exceed K.

Same pattern:

```
Maintain a property
```

---

## Simpler Problem 2

### Binary Subarrays With Sum

Convert

```
odd → 1
even → 0
```

Then

```
Exactly K odds

↓

Exactly K ones
```

Literally identical.

---

## Simpler Problem 3

### Subarrays with K Different Integers

Again,

```
Exactly K

=

AtMost(K)
-
AtMost(K-1)
```

Same framework.

---

### Thinking Evolution

```
Longest valid window

↓

Count all windows with AtMost K

↓

Exactly K

=

AtMost(K)-AtMost(K-1)
```

---

# 6. Brute Force

Generate every subarray.

For every subarray:

* Count odd numbers.
* If odd count == k
  answer++

```python
class Solution:
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        ans = 0

        for i in range(n):
            odd = 0
            for j in range(i, n):
                if nums[j] % 2:
                    odd += 1

                if odd == k:
                    ans += 1

        return ans
```

### Complexity

Time:

```
O(n²)
```

Space:

```
O(1)
```

---

# 7. Optimal Solution (Sliding Window)

### Key Idea

Count

```
AtMost(K odds)
```

Then

```
Exactly(K)
=
AtMost(K)
-
AtMost(K-1)
```

---

```python
class Solution:

    def atMost(self, nums, k):
        if k < 0:
            return 0

        left = 0
        odd = 0
        ans = 0

        for right in range(len(nums)):

            # Add current element
            if nums[right] % 2:
                odd += 1

            # Shrink until window has at most k odds
            while odd > k:
                if nums[left] % 2:
                    odd -= 1
                left += 1

            # Every subarray ending at right is valid
            ans += right - left + 1

        return ans

    def numberOfSubarrays(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
```

---

### Complexity

Time

```
O(n)
```

Space

```
O(1)
```

---

## Alternative Optimal (Prefix Sum + Frequency Map)

### Intuition

Track the number of odd elements seen so far.

* Let `prefixOdd` = count of odd numbers from the start up to the current index.
* A subarray has exactly `k` odds if:

```
currentPrefixOdd - previousPrefixOdd = k
```

So for each position, count how many previous prefixes equal:

```
currentPrefixOdd - k
```

```python
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1

        prefixOdd = 0
        ans = 0

        for num in nums:
            if num % 2:
                prefixOdd += 1

            ans += freq[prefixOdd - k]
            freq[prefixOdd] += 1

        return ans
```

### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

This version follows the same pattern as **Subarray Sum Equals K**.

---

# 8. Step-by-Step Trace

Example

```
nums = [1,1,2,1]
k = 2
```

Need

```
AtMost(2)
```

| Right | Number | Odd Count | Left   | New Valid Subarrays | Answer |
| ----- | ------ | --------- | ------ | ------------------- | ------ |
| 0     | 1      | 1         | 0      | 1                   | 1      |
| 1     | 1      | 2         | 0      | 2                   | 3      |
| 2     | 2      | 2         | 0      | 3                   | 6      |
| 3     | 1      | 3         | Shrink | 2                   | 8      |

So

```
AtMost(2)=8
```

Now

```
AtMost(1)=5
```

Therefore

```
Exactly2

=
8-5

=3
```

Correct.

---

# 9. Related Problems

| Problem                                                  | Connection                                                                   |
| -------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Binary Subarrays With Sum**                            | Convert odd/even to 1/0. Identical problem.                                  |
| **Subarrays with K Different Integers**                  | Uses the same `AtMost(K) - AtMost(K-1)` trick.                               |
| **Max Consecutive Ones III**                             | Sliding window maintaining at most `K` constraint.                           |
| **Longest Substring with At Most K Distinct Characters** | Classic variable-size sliding window with an at-most condition.              |
| **Subarray Sum Equals K**                                | Uses the prefix-sum + frequency map technique for counting exact conditions. |

---

# Revision Notes (30 Seconds)

* **Exactly `K` constraint?** → Try `AtMost(K) - AtMost(K-1)`.
* **Treat odd numbers as `1` and even numbers as `0`** → Reduces to **Binary Subarrays With Sum**.
* **AtMost Sliding Window:** Maintain `odd <= K`; each step adds `right - left + 1` valid subarrays.
* **Alternative:** Prefix odd-count + hash map, identical to **Subarray Sum Equals K**.
