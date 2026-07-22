# 904. Fruit Into Baskets

## 1. Problem Statement

You are given an integer array `fruits`, where `fruits[i]` represents the type of fruit on the `i-th` tree.

You have **two baskets**, and each basket can hold **only one type of fruit**, but an unlimited quantity of that type.

Starting from **any tree**, you must pick **exactly one fruit from every consecutive tree** while moving to the right.

You must stop when you encounter a tree whose fruit cannot fit into either basket.

Return the **maximum number of fruits** you can collect.

### Constraints

* `1 <= fruits.length <= 10^5`
* `0 <= fruits[i] < fruits.length`

Since `n` can be `10^5`, an **O(n²)** solution will timeout.

---

# 2. Diagram

You can keep **at most two fruit types** in your baskets.

```text
fruits = [1,2,1,2,3]

Window
[1,2,1,2]

Basket 1 → Fruit 1
Basket 2 → Fruit 2

Distinct Types = 2 ✅
Length = 4
```

Next fruit:

```text
[1,2,1,2,3]

Fruit types:

1
2
3

Distinct = 3 ❌
```

Shrink from the left until only **2 types** remain.

```text
Remove 1

[2,1,2,3]

Still 3 types

Remove 2

[1,2,3]

Still 3

Remove 1

[2,3]

Now only 2 types ✅
```

---

# 3. Example I/O

### Example 1

```text
Input:
fruits = [1,2,1]

Output:
3
```

Explanation

```text
Collect all fruits.

Types = {1,2}
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
Best window

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
Best window

[2,3,2,2]

Length = 4
```

---

### Edge Case

```text
Input:
fruits = [1,1,1]

Output:
3
```

Only one fruit type exists.

---

# 4. Intuition & Pattern Recognition

## Signal 1

Question asks for the

> Maximum consecutive fruits

This immediately suggests

> **Sliding Window**

---

## Signal 2

Only

> Two fruit types

Need to know how many distinct fruit types exist in the window.

Use a

> **HashMap (frequency map)**

---

## Pattern

Expand the window.

```text
Add current fruit.
Increase its count.
```

If

```text
Distinct > 2
```

Shrink from the left until

```text
Distinct <= 2
```

Update the maximum window length.

---

### Interview Thought Process

> "Maximum valid subarray."

> "Validity = at most two distinct values."

> "Expand while valid."

> "Shrink when invalid."

---

# 5. Simpler Version

## Simpler Problem

### Longest Substring with At Most K Distinct Characters (340)

There,

```text
At most K distinct characters
```

Here,

```text
At most 2 distinct fruit types
```

It is literally

```text
K = 2
```

---

### Thinking Progression

```text
Longest window

↓

Window validity

↓

Distinct elements

↓

Maintain frequencies

↓

Shrink when
distinct > 2
```

---

### Related Simpler Problems

* 340. Longest Substring with At Most K Distinct Characters
* 159. Longest Substring with At Most Two Distinct Characters
* 3. Longest Substring Without Repeating Characters

---

# 6. Brute Force

Start from every index.

Keep extending until more than two fruit types appear.

```python
class Solution:
    def totalFruit(self, fruits):
        n = len(fruits)
        ans = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                freq[fruits[j]] = freq.get(fruits[j], 0) + 1

                if len(freq) <= 2:
                    ans = max(ans, j - i + 1)
                else:
                    break

        return ans
```

### Complexity

Time

```text
O(n²)
```

Space

```text
O(2)
```

---

# 7. Optimal Solution (Sliding Window + Frequency Map)

```python
class Solution:
    def totalFruit(self, fruits):
        freq = {}
        left = 0
        ans = 0

        for right in range(len(fruits)):

            # Include current fruit.
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1

            # More than two fruit types? Shrink window.
            while len(freq) > 2:
                freq[fruits[left]] -= 1

                # Remove fruit type completely if its count becomes 0.
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left += 1

            # Current window is valid.
            ans = max(ans, right - left + 1)

        return ans
```

---

### Complexity

Time

```text
O(n)
```

Each fruit enters and leaves the window once.

Space

```text
O(2)
```

The map contains at most **2 fruit types** (temporarily 3 before shrinking).

---

# 8. Step-by-Step Trace

Example

```text
fruits = [1,2,3,2,2]
```

| Right | Fruit | Window    | Frequency     | Distinct | Action | Answer |
| ----- | ----- | --------- | ------------- | -------- | ------ | ------ |
| 0     | 1     | [1]       | {1:1}         | 1        | Valid  | 1      |
| 1     | 2     | [1,2]     | {1:1,2:1}     | 2        | Valid  | 2      |
| 2     | 3     | [1,2,3]   | {1:1,2:1,3:1} | 3        | Shrink | 2      |
|       |       | [2,3]     | {2:1,3:1}     | 2        | Valid  | 2      |
| 3     | 2     | [2,3,2]   | {2:2,3:1}     | 2        | Valid  | 3      |
| 4     | 2     | [2,3,2,2] | {2:3,3:1}     | 2        | Valid  | 4      |

Final Answer

```text
4
```

---

# 9. Related Problems (Increasing Difficulty)

| Problem                                                         | Connection                                                                                                         |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **159. Longest Substring with At Most Two Distinct Characters** | Identical problem on strings instead of arrays.                                                                    |
| **340. Longest Substring with At Most K Distinct Characters**   | Generalization where the allowed number of distinct elements is `k` instead of `2`.                                |
| **1004. Max Consecutive Ones III**                              | Variable-size sliding window where the validity depends on the number of zeros instead of distinct values.         |
| **424. Longest Repeating Character Replacement**                | Sliding window with a frequency map, but the validity rule uses the most frequent character.                       |
| **76. Minimum Window Substring**                                | Uses the same expand/shrink window framework but searches for the **minimum** valid window instead of the maximum. |
