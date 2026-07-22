# 219. Contains Duplicate II

## 1. Problem Statement

Given an integer array `nums` and an integer `k`, return **true** if there exist **two distinct indices** `i` and `j` such that:

* `nums[i] == nums[j]`
* `|i - j| <= k`

Otherwise, return **false**.

### Constraints

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`
* `0 <= k <= 10^5`

Since `n` can be `10^5`, an **O(n²)** solution will timeout.

---

## 2. Diagram

Think of maintaining a **window of the last K elements**.

```
nums = [1,2,3,1,4]
k = 3

Initially

Window
[1]

Expand

Window
[1,2]

Expand

Window
[1,2,3]

Next element = 1

Window contains?
[1,2,3]

YES

Duplicate found within distance 3.
```

If the window grows beyond size `k`, remove the oldest element.

```
k = 2

nums = [1,2,3,1]

Step 1
Window = [1]

Step 2
Window = [1,2]

Step 3
Need size <=2

Remove 1

Window = [2,3]

Next element =1

1 not present

Answer = False
```

---

# 3. Example I/O

### Example 1

```
Input:
nums = [1,2,3,1]
k = 3

Output:
true
```

Explanation:

```
1 appears at indices 0 and 3

|3-0| = 3 <= k
```

---

### Example 2

```
Input:
nums = [1,0,1,1]
k = 1

Output:
true
```

Explanation:

```
Last two elements are both 1

distance = 1
```

---

### Edge Case

```
Input:
nums = [1,2,3,1]
k = 2

Output:
false
```

Because

```
distance = 3 > 2
```

---

# 4. Intuition & Pattern Recognition

### Signal 1

Question says

> "within distance K"

This immediately suggests

> **Sliding Window**

---

### Signal 2

Need to know quickly whether current value already exists inside window.

That suggests

> **HashSet**

---

### Pattern

Maintain a window containing **only the previous K elements**.

When processing current element:

```
Is current number already inside window?

YES -> duplicate within K

NO -> add it
```

If window becomes larger than `k`

```
Remove leftmost element
```

---

### Interview Thought Process

> "Distance ≤ K means I only care about the last K indices."

> "Checking duplicates inside a moving window is exactly Sliding Window + HashSet."

---

# 5. Simpler Version

### Simpler Problem

**217. Contains Duplicate**

Just determine whether any duplicate exists.

Solution:

```
HashSet

Seen before?

YES -> return true
```

---

### Difference

Here,

Not every duplicate counts.

Need

```
distance <= k
```

So instead of storing **all previous elements**, store only the **last K elements**.

---

### Thinking Progression

```
Contains Duplicate
      ↓

Need duplicate only in recent K indices

      ↓

Store only recent K elements

      ↓

Sliding Window + HashSet
```

---

### Related Simpler Problems

1. 217. Contains Duplicate
2. 387. First Unique Character in a String (HashMap)
3. Longest Substring Without Repeating Characters (Sliding Window + HashSet)

---

# 6. Brute Force

For every index,

check next K elements.

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, min(n, i + k + 1)):
                if nums[i] == nums[j]:
                    return True

        return False
```

### Complexity

Time

```
O(n*k)
```

Worst case

```
O(n²)
```

Space

```
O(1)
```

---

# 7. Optimal Solution (Sliding Window + HashSet)

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i in range(len(nums)):

            # If window exceeds size k, remove the element that is now too far away.
            if i > k:
                window.remove(nums[i - k - 1])

            # Duplicate found within the current window.
            if nums[i] in window:
                return True

            # Add current element to the window.
            window.add(nums[i])

        return False
```

---

### Why remove first?

At index `i`, valid previous indices are

```
[i-k ... i-1]
```

Element at

```
i-k-1
```

is now outside the allowed distance.

---

### Complexity

Time

```
O(n)
```

Each element is inserted once and removed once.

Space

```
O(k)
```

Window never stores more than `k` elements.

---

# 8. Step-by-Step Trace

Example

```
nums = [1,2,3,1]
k = 3
```

| i | Current | Window Before | Action          | Window After |
| - | ------- | ------------- | --------------- | ------------ |
| 0 | 1       | {}            | add             | {1}          |
| 1 | 2       | {1}           | add             | {1,2}        |
| 2 | 3       | {1,2}         | add             | {1,2,3}      |
| 3 | 1       | {1,2,3}       | found duplicate | Return True  |

---

Example 2

```
nums=[1,2,3,1]
k=2
```

| i | Current | Remove           | Window Before | Window After          |
| - | ------- | ---------------- | ------------- | --------------------- |
| 0 | 1       | -                | {}            | {1}                   |
| 1 | 2       | -                | {1}           | {1,2}                 |
| 2 | 3       | -                | {1,2}         | {1,2,3}               |
| 3 | 1       | remove nums[0]=1 | {2,3}         | 1 not found → {1,2,3} |

Finished

```
False
```

Notice that the earlier `1` was removed because it was more than `k` indices away.

---

# 9. Related Problems

| Problem                                               | Connection                                                                                               |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **217. Contains Duplicate**                           | Same HashSet idea without a window.                                                                      |
| **3. Longest Substring Without Repeating Characters** | Variable-size sliding window with a HashSet/HashMap to maintain uniqueness.                              |
| **220. Contains Duplicate III**                       | Adds a value-difference constraint (`abs(nums[i]-nums[j]) <= t`) along with index difference.            |
| **567. Permutation in String**                        | Fixed-size sliding window with frequency counting instead of a HashSet.                                  |
| **438. Find All Anagrams in a String**                | Another fixed-size window where the window content is compared using frequencies rather than membership. |
