# Variable Size Sliding Window (Sliding Window)

This is one of the **highest ROI interview patterns** because many seemingly different problems reduce to:

> **Expand the window until it satisfies some condition, then shrink it while maintaining the condition.**

Unlike Fixed Size Sliding Window, the window length is **not predetermined**.

---

# 1. Pattern in One Minute

### Core Idea

Maintain a window `[left...right]` whose size changes dynamically.

* Expand (`right++`) to include new elements.
* If the window violates or satisfies some condition, move `left` until the condition becomes valid again.
* Update the answer during expansion or shrinking depending on the problem.

---

### Why does this pattern exist?

Brute force checks every possible subarray.

```
O(n²)
```

Variable sliding window avoids restarting.

Each element:

* enters the window once
* leaves the window once

Therefore,

```
O(n)
```

---

### When should I immediately think of it?

Whenever the problem says

* subarray
* substring
* contiguous
* longest
* shortest
* at most
* at least
* exactly (sometimes)
* minimum window

---

# 2. Recognition Signals

### Strong clues

### Longest subarray

Examples

* Longest substring without repeating characters
* Longest repeating character replacement
* Max consecutive ones

---

### Smallest window

Examples

* Minimum window substring
* Minimum size subarray sum

---

### Constraints

```
sum >= target

at most K distinct

at most K zeros

frequency constraint

budget constraint

cost <= K
```

---

### Common disguises

Instead of saying "window", interviewers say

* operations
* replacements
* flips
* distinct characters
* unique elements
* budget
* edits
* frequency

---

### Don't use this when

❌ Window validity cannot be updated locally.

Example:

Need information from arbitrary positions outside the window.

Or

Need future information.

Then another pattern is needed.

---

# 3. Mental Model

Remember these steps.

### Step 1

Expand

```
right += 1
```

Include new element.

---

### Step 2

Update window state

Examples

```
sum += nums[right]

freq[s[right]] += 1

zeros += ...

distinct += ...
```

---

### Step 3

Check validity

Examples

```
while invalid:
    shrink
```

OR

```
while valid:
    update answer
    shrink
```

depends on the problem.

---

### Step 4

Shrink

```
remove nums[left]

left += 1
```

---

### Step 5

Update answer

Either

```
maximum length
```

or

```
minimum length
```

---

The whole algorithm becomes

```
Expand

Fix

Shrink

Repeat
```

---

# 4. Boilerplate Template

```python
left = 0

for right in range(len(nums)):

    # include right element
    add(nums[right])

    # shrink until window becomes valid
    while window_invalid():
        remove(nums[left])
        left += 1

    # current window is valid
    ans = update(ans, left, right)

return ans
```

---

## Minimum Window style

```python
left = 0

for right in range(len(s)):

    add(s[right])

    while window_valid():

        ans = min(ans, right - left + 1)

        remove(s[left])
        left += 1
```

Notice

Longest problems usually shrink while **invalid**.

Minimum problems shrink while **valid**.

That single difference is extremely important.

---

# 5. Variations

| Variation             | Change                                        |
| --------------------- | --------------------------------------------- |
| Longest valid window  | Update answer after shrinking invalid windows |
| Smallest valid window | Shrink while valid                            |
| At most K             | Keep shrinking when > K                       |
| Exactly K             | Solve(atMost(K)) − Solve(atMost(K−1))         |
| Budget problems       | Track cost instead of count                   |
| Frequency problems    | Maintain hashmap                              |
| Binary array          | Track zero count                              |

---

# 6. Common Pitfalls

### Mistake 1

Updating answer before fixing window.

Wrong.

Always restore validity first (unless problem specifically asks otherwise).

---

### Mistake 2

Forgetting to remove left element.

Very common.

Whenever

```
left += 1
```

you almost always need

```
remove(nums[left])
```

before moving.

---

### Mistake 3

Infinite while loop.

Condition never changes because state wasn't updated.

---

### Mistake 4

Using this pattern for "exactly K".

Most exactly-K questions are easier as:

```
Exactly(K)
=
AtMost(K)
-
AtMost(K-1)
```

---

### Mistake 5

Using a fixed window mindset.

Here,

```
right-left+1
```

changes continuously.

---

# 7. Interview Checklist

✓ Problem asks for contiguous array/string

✓ Window size isn't fixed

✓ Need longest or shortest

✓ Constraint depends only on current window

✓ Window can be repaired by moving left

→ Use Variable Sliding Window.

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for Revision)

### 1. Longest Substring Without Repeating Characters ⭐

Learn

* frequency map
* shrink while duplicate exists

---

### 2. Minimum Window Substring ⭐

Learn

* required frequency
* shrink while valid

---

### 3. Longest Repeating Character Replacement ⭐

Learn

* maintain max frequency
* budget constraint

---

## Easy

* Maximum Average Subarray I *(Fixed-size warm-up)*
* Max Consecutive Ones III
* Minimum Size Subarray Sum

---

## Medium

* Fruits Into Baskets
* Longest Substring with At Most K Distinct Characters
* Permutation in String
* Find All Anagrams in a String
* Frequency of the Most Frequent Element
* Get Equal Substrings Within Budget
* Subarrays with K Different Integers *(Exactly K trick)*

---

## Hard (High ROI)

* Minimum Window Substring
* Sliding Window Median *(uses additional data structures)*
* Count Vowel Substrings of a String *(advanced counting)*

---

# 9. 30-Second Cheat Sheet

### Recognition

* Contiguous array/string
* Longest/Shortest
* At most K
* Budget
* Frequency
* Distinct characters
* Minimum window

---

### Core Idea

```
Expand right

↓

Maintain window state

↓

Shrink left until condition holds

↓

Update answer
```

---

### Universal Template

```python
for right:

    add(right)

    while invalid:
        remove(left)
        left += 1

    update answer
```

For minimum-window problems:

```python
for right:

    add(right)

    while valid:
        update answer
        remove(left)
        left += 1
```

---

### Complexity

* Time: **O(n)** (each element enters and leaves the window at most once)
* Space: **O(1)** to **O(k)** or **O(alphabet size)**, depending on the state maintained (e.g., counters or hash maps)

---

### Common Variations

* Longest valid window
* Minimum valid window
* At Most K
* Exactly K = AtMost(K) − AtMost(K−1)
* Budget/Cost windows
* Frequency/Distinct-character windows

---

### Pitfalls

* ❌ Update answer before fixing the window
* ❌ Forget to remove the left element when shrinking
* ❌ Mishandle "Exactly K" (use the AtMost trick)
* ❌ Confuse "shrink while invalid" (longest) with "shrink while valid" (minimum)

---

## Pattern Map (Sliding Window)

Since you've already covered **Fixed Size Sliding Window**, your progression should be:

1. ✅ Fixed Size Sliding Window
2. ✅ Variable Size Sliding Window *(this pattern)*
3. Longest/Shortest Window Family
4. At Most K Pattern
5. Exactly K = AtMost(K) − AtMost(K−1)
6. Minimum Window Pattern
7. Monotonic Queue Sliding Window *(e.g., Sliding Window Maximum)*

Mastering these seven sub-patterns covers the vast majority of sliding-window interview questions.
