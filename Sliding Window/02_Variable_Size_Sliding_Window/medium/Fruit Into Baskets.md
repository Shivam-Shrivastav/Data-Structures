# 904. Fruit Into Baskets

**Pattern:** Variable Size Sliding Window + HashMap (Frequency Count)

This problem is one of the most important follow-ups to **Longest Substring Without Repeating Characters**. Instead of requiring **all unique elements**, you're now allowed **at most 2 distinct elements** in the window. 

---

# 1. Problem Statement

You are given an integer array `fruits`, where each number represents a fruit type growing on a tree.

You have **2 baskets**, and each basket can hold **only one type of fruit**, but an unlimited quantity of that type.

Starting from any tree, move **only to the right**, picking exactly one fruit from every tree until you encounter a third fruit type that cannot fit into your two baskets.

Return the **maximum number of fruits** you can collect.

### Constraints

* `1 <= fruits.length <= 10^5`
* `0 <= fruits[i] < fruits.length`
* Need an **O(N)** solution.

---

# 2. Diagram

Example:

```text
fruits = [1,2,1,2,3,2,2]

                R
1  2  1  2  3  2  2
L

Window = [1,2,1,2]
Distinct = {1,2}

--------------------------

Next fruit = 3

1  2  1  2  3  2  2
L           R

Window = [1,2,1,2,3]
Distinct = {1,2,3} ❌

Shrink from left

Remove 1
Remove 2
Remove 1

Window becomes

2 3

Distinct = {2,3} ✅
```

**Invariant:** The window always contains **at most 2 distinct fruit types**.

---

# 3. Example I/O

### Example 1

```text
Input:
fruits = [1,2,1]

Output:
3
```

Explanation:

```text
Window = [1,2,1]

Only 2 fruit types.

Answer = 3
```

---

### Example 2

```text
Input:
fruits = [0,1,2,2]

Output:
3
```

Explanation

```text
Longest valid window

[1,2,2]

Length = 3
```

---

### Example 3

```text
Input:
fruits = [1,2,3,2,2]

Output:
4
```

Explanation

```text
Longest window

[2,3,2,2]
```

---

### Edge Case

```text
Input:
[5]

Output:
1
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Longest contiguous subarray
* At most K distinct values
* Need maximum length
* Constraint = 100k

Think immediately:

> **Variable Size Sliding Window**

Unlike **Longest Substring Without Repeating Characters**:

```text
Unique characters only

↓

HashSet
```

Here we need

```text
Know how many of each fruit exist

↓

HashMap (frequency)
```

because removing one fruit doesn't necessarily remove that fruit type from the window.

---

### Interview Thinking

```text
Expand the window.

Keep frequency of every fruit.

If there are more than 2 fruit types,

keep shrinking until only 2 remain.

Track the maximum window size.
```

---

# 5. Simpler Version

## Simpler Question 1

### Longest Substring Without Repeating Characters (LeetCode 3)

Window rule:

```text
No duplicate characters allowed.
```

Uses

```text
HashSet
```

---

## Simpler Question 2

### Longest Substring with At Most 2 Distinct Characters (LeetCode 159)

This is literally the **string version** of Fruit Into Baskets.

Characters ↔ Fruit types.

---

## Simpler Question 3

### Longest Substring with At Most K Distinct Characters (LeetCode 340)

Generalization.

Replace

```text
2 baskets

↓

K baskets
```

Same exact algorithm.

---

### Thinking Progression

```text
Unique characters

↓

At most 2 distinct

↓

At most K distinct

↓

Fruit Into Baskets
```

The only new idea is replacing a `HashSet` with a **frequency HashMap**.

---

# 6. Brute Force

Try every starting position.

Keep collecting fruits until a third fruit appears.

```python
for i:
    basket = {}
    for j:
        add fruit
        if >2 types:
            break
```

### Complexity

```text
Time  : O(N²)

Space : O(2)
```

---

# 7. Optimal Solution

### Idea

Maintain

```text
left
right
frequency map
```

Expand with `right`.

If distinct fruits become more than 2,

shrink from `left`.

Whenever frequency becomes zero,

remove that fruit from the map.

---

### Python

```python
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        freq = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(fruits)):

            # Include current fruit
            freq[fruits[right]] += 1

            # Too many fruit types -> shrink
            while len(freq) > 2:
                freq[fruits[left]] -= 1

                # Remove fruit type completely
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left += 1

            # Update maximum valid window
            ans = max(ans, right - left + 1)

        return ans
```

### Complexity

```text
Time  : O(N)

Space : O(3) ≈ O(1)
```

Each fruit enters and leaves the window at most once.

---

# 8. Step-by-Step Trace

Example

```text
fruits = [1,2,3,2,2]
```

|  Right | Fruit | Frequency Map        | Left | Window    | Max |
| -----: | ----: | -------------------- | ---: | --------- | --: |
|      0 |     1 | {1:1}                |    0 | [1]       |   1 |
|      1 |     2 | {1:1,2:1}            |    0 | [1,2]     |   2 |
|      2 |     3 | {1:1,2:1,3:1}        |    0 | Invalid   |   - |
| Shrink |     - | Remove 1 → {2:1,3:1} |    1 | [2,3]     |   2 |
|      3 |     2 | {2:2,3:1}            |    1 | [2,3,2]   |   3 |
|      4 |     2 | {2:3,3:1}            |    1 | [2,3,2,2] |   4 |

Final Answer

```text
4
```

---

### Visual Shrinking

```text
Window

1 2 3
^

Three fruit types

Remove 1

↓

2 3

Now only 2 types remain.
```

---

# 9. Related Problems

| Problem                                                         | Connection                                                                                                            |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **3. Longest Substring Without Repeating Characters**           | Window must contain only unique elements; uses a `HashSet` instead of a frequency map.                                |
| **159. Longest Substring with At Most Two Distinct Characters** | Exact same logic on strings instead of arrays.                                                                        |
| **340. Longest Substring with At Most K Distinct Characters**   | Generalization of this problem from 2 baskets to K baskets.                                                           |
| **992. Subarrays with K Different Integers**                    | Uses the same "at most K distinct" sliding window as a building block to count exactly K distinct subarrays.          |
| **76. Minimum Window Substring**                                | Also uses a frequency map and shrink/expand window, but minimizes the window while satisfying character requirements. |

---

# Key Interview Takeaways

* **Pattern:** Variable Size Sliding Window
* **Data Structure:** Frequency HashMap
* **Invariant:** Window always contains **at most 2 distinct fruit types**.
* **Rule:** Expand with `right`; if distinct fruit types exceed 2, shrink from `left` until the window is valid again.
* **HashSet vs HashMap:**

  * **Unique elements required** → `HashSet`
  * **At most K distinct elements** → `HashMap` (because duplicates matter)
* **Generalization:** Replace `2` with `K` and you get **Longest Substring with At Most K Distinct Characters (LeetCode 340)**, a very common interview pattern.
