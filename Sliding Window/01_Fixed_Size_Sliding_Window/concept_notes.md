# Fixed Size Sliding Window (Revision)

---

# 1. Pattern in One Minute

### Core Idea

Maintain a **window of exactly `k` elements** while moving across the array/string.

Instead of recomputing the answer for every window from scratch (**O(nk)**), update the answer in **O(1)** when the window moves by:

* Removing the leftmost element
* Adding the new rightmost element

Overall complexity becomes **O(n)**.

### Why does this pattern exist?

Many interview problems ask about **every contiguous subarray of fixed length `k`**.

Without sliding window:

```
Window1 -> compute k elements
Window2 -> compute k elements
Window3 -> compute k elements
```

Lots of repeated work.

Sliding window reuses previous computation.

### Think of it immediately when

* Window size is fixed
* Every subarray/substring of size `k`
* "Average of K"
* "Maximum Sum of K"
* "First Negative in Every Window"
* "Distinct Count in Every Window"

---

# 2. Recognition Signals

## Strong Clues

### Keywords

* Fixed size k
* Window of size k
* Every k elements
* Every substring of length k
* Average of size k
* Maximum/minimum of size k

---

### Constraints

```
Find answer for every subarray of length k
```

or

```
Exactly k consecutive elements
```

---

### Problem Characteristics

* Contiguous
* Constant window size
* Left pointer moves only after window reaches size k

---

### Common Disguises

Instead of saying

> Window of size K

they may say

* Every group of K days
* K consecutive houses
* K consecutive temperatures
* Last K transactions
* Last K characters

---

## Don't use when

❌ Window size changes

Example:

```
Longest substring without repeating characters
```

That's **Variable Sliding Window**.

---

❌ Window depends on condition

```
Sum <= K
At most K distinct
Exactly K distinct
```

Again, Variable Window.

---

# 3. Mental Model

Think like a train moving.

```
[L.........R]
```

Train length never changes.

Every move:

```
remove left
add right
```

That's it.

Remember:

* Build first window
* Process answer
* Remove left
* Move both pointers
* Repeat

Visualization

```
k = 3

1 2 3 4 5 6

Window1

1 2 3

↓

Window2

2 3 4

↓

Window3

3 4 5

↓

Window4

4 5 6
```

Notice only **one element leaves and one enters**.

---

# 4. Boilerplate Template (Python)

```python
left = 0
window = 0

for right in range(len(nums)):
    # Add new element
    window += nums[right]

    # Window reached size k
    if right - left + 1 == k:
        # Process answer
        ans = max(ans, window)

        # Remove left element
        window -= nums[left]
        left += 1
```

### If maintaining frequency

```python
from collections import defaultdict

freq = defaultdict(int)
left = 0

for right in range(len(nums)):
    freq[nums[right]] += 1

    if right - left + 1 == k:
        # Use freq

        freq[nums[left]] -= 1
        if freq[nums[left]] == 0:
            del freq[nums[left]]

        left += 1
```

---

# 5. Variations

| Variation               | Window Data Structure         |
| ----------------------- | ----------------------------- |
| Maximum Sum             | Running Sum                   |
| Minimum Sum             | Running Sum                   |
| Average                 | Running Sum                   |
| Count Distinct          | HashMap                       |
| First Negative          | Queue                         |
| Sliding Window Maximum  | Monotonic Deque               |
| Median                  | Two Heaps / Ordered Structure |
| Frequency of Characters | HashMap                       |
| Maximum Vowels          | Counter                       |

---

# 6. Common Pitfalls

### ❌ Forgetting to remove left element

Window grows forever.

---

### ❌ Processing before window reaches size k

Wrong.

Correct:

```python
if right-left+1 == k:
```

---

### ❌ Removing before processing

Wrong order.

```
Add

↓

Process

↓

Remove

↓

Slide
```

---

### ❌ Off-by-one

Remember

```
Window Size

right-left+1
```

Not

```
right-left
```

---

### ❌ Forgetting to delete zero-frequency entries

Needed for problems involving distinct count.

---

# 7. Interview Checklist

✓ Is the array/string **contiguous**?

✓ Is the window size **exactly K**?

✓ Do I need an answer for **every window**?

✓ Can I update the answer by removing one element and adding one?

If yes → **Fixed Size Sliding Window**

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for Revision)

1. 🟢 **Maximum Average Subarray I** *(Easy)* ⭐
2. 🟟 **Maximum Number of Vowels in a Substring of Given Length** *(Medium)* ⭐
3. 🟟 **Sliding Window Maximum** *(Medium/Hard pattern with Monotonic Queue)* ⭐

---

## Easy

* Maximum Average Subarray I ⭐
* Contains Duplicate II
* Defuse the Bomb

---

## Medium

* Maximum Number of Vowels in a Substring of Given Length ⭐
* Find K-Length Substrings With No Repeated Characters
* Grumpy Bookstore Owner
* Number of Distinct Elements in Every Window (classic)

---

## Hard / Important Pattern Extension

* Sliding Window Maximum ⭐ *(introduces Monotonic Deque)*
* Sliding Window Median *(introduces Two Heaps / Ordered Set)*

---

# 9. 30-Second Cheat Sheet

### Recognition

* Exactly **K**
* Contiguous
* Every window of size K

---

### Core Idea

```
Add right

↓

Window == K

↓

Update answer

↓

Remove left

↓

Repeat
```

---

### Generic Template

```python
add(right)

if window == k:
    process()
    remove(left)
    left += 1
```

---

### Complexity

* Time: **O(n)**
* Space:

  * **O(1)** (running sum/counter)
  * **O(k)** (hash map, queue, deque)

---

### Common Variations

* Running Sum
* Frequency Map
* Queue
* Monotonic Deque
* Two Heaps

---

### Pitfalls

* ❌ Remove before processing
* ❌ Wrong window size check
* ❌ Forget to shrink
* ❌ Off-by-one (`right - left + 1`)
* ❌ Leave zero-frequency keys in the map

---

## 💡 Pattern Mnemonic

> **"Add → Reach K → Process → Remove → Slide"**

If the problem says **"every contiguous subarray/substring of exactly `k` elements"**, this should be your default mental flow.
