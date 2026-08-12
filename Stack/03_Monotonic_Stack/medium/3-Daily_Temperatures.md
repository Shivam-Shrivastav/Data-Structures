# **739. Daily Temperatures**

## 1. Problem Statement

You are given an array `temperatures` where `temperatures[i]` is the temperature on the `i`-th day.

For each day, find **how many days you have to wait** until a **warmer temperature** occurs.

* If there is **no future warmer day**, return `0` for that day.

Return an array where `answer[i]` is the number of days to wait.

### Constraints

* `1 <= temperatures.length <= 10⁵`
* `30 <= temperatures[i] <= 100`

The important phrase is:

> **Next Greater Element + Return Distance instead of Value**

---

# 2. Diagram

Example

```text
temperatures = [73,74,75,71,69,72,76,73]

Index:   0   1   2   3   4   5   6   7
Temp :  73  74  75  71  69  72  76  73

73 ─────► 74 (1 day)
74 ─────► 75 (1 day)
75 ─────────────────► 76 (4 days)
71 ─────► 72 (2 days)
69 ─────► 72 (1 day)
72 ─────► 76 (1 day)
76 ─────► None
73 ─────► None

Answer:
[1,1,4,2,1,1,0,0]
```

Unlike Next Greater Element, we return

```text
(next_index - current_index)
```

instead of the temperature.

---

# 3. Example I/O

### Example 1

**Input**

```text
temperatures = [73,74,75,71,69,72,76,73]
```

**Output**

```text
[1,1,4,2,1,1,0,0]
```

---

### Example 2

**Input**

```text
temperatures = [30,40,50,60]
```

**Output**

```text
[1,1,1,0]
```

---

### Example 3 (Edge Case)

```text
temperatures = [60]

Output

[0]
```

---

# 4. Intuition & Pattern Recognition

## Interview Signals

Whenever you see

* Next warmer day
* Next greater element
* Nearest greater on right
* Future greater value

Think

> **Monotonic Stack**

---

### Key Observation

For each temperature,

we need the **first larger temperature on the right**.

The only difference from Next Greater Element is:

Instead of returning

```text
76
```

we return

```text
index(76) - currentIndex
```

Therefore,

we must store **indices**, not values.

---

# 5. Simpler Version

## Simplest Problem

Find the next greater element.

Example

```text
[2,1,5,3]

Answer

2 → 5
1 → 5
5 → None
3 → None
```

---

## Difference Here

Instead of returning

```text
5
```

return

```text
index(5)-index(2)
```

Example

```text
[73,74,75]

73 → 74

Return

1
```

---

## Simpler Problems Leading Here

1. Next Greater Element I
2. Next Greater Element II
3. Daily Temperatures

Thinking progression

```text
Need Next Greater
        ↓
Monotonic Stack
        ↓
Need index instead of value
        ↓
Store indices
        ↓
Return distance
```

---

# 6. Brute Force

For every day,

search to the right until a warmer day is found.

### Python

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
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
O(1)
```

(ignoring the output array)

---

# 7. Optimal Solution

## Method 1 (Right → Left)

### Idea

Traverse from right to left.

Maintain a **monotonic decreasing stack of indices**.

For each day:

* Remove all temperatures that are **less than or equal** to the current temperature.
* The top of the stack is the next warmer day.
* Store the difference in indices.
* Push the current index.

### Python

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []  # Stores indices

        for i in range(n - 1, -1, -1):

            # Remove days that aren't warmer
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            # Top is the next warmer day
            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans
```

### Complexity

Time

```text
O(n)
```

Space

```text
O(n)
```

---

## Method 2 (Left → Right) ⭐ (Most Intuitive)

Instead of finding the answer for the current day,

the **current warmer temperature** becomes the answer for previous colder days.

Maintain a **monotonic decreasing stack of indices**.

Whenever a warmer temperature arrives,

resolve everyone waiting on the stack.

### Python

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []  # Stores indices

        for i in range(n):

            # Current temperature resolves previous colder days
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                ans[prev] = i - prev

            stack.append(i)

        return ans
```

### Why store indices?

Because we need

```text
currentIndex - previousIndex
```

not the temperature value itself.

---

# 8. Step-by-Step Trace (Left → Right)

Example

```text
temperatures = [73,74,75,71,69,72,76,73]
```

| Day | Temp | Stack (Indices) | Action                               | Answer            |
| --- | ---- | --------------- | ------------------------------------ | ----------------- |
| 0   | 73   | []              | Push 0                               | [0,0,0,0,0,0,0,0] |
| 1   | 74   | [0]             | 74>73 → ans[0]=1                     | [1,0,0,0,0,0,0,0] |
|     |      |                 | Push 1                               |                   |
| 2   | 75   | [1]             | 75>74 → ans[1]=1                     | [1,1,0,0,0,0,0,0] |
|     |      |                 | Push 2                               |                   |
| 3   | 71   | [2]             | Push 3                               |                   |
| 4   | 69   | [2,3]           | Push 4                               |                   |
| 5   | 72   | [2,3,4]         | 72>69 → ans[4]=1<br>72>71 → ans[3]=2 | [1,1,0,2,1,0,0,0] |
| 6   | 76   | [2,5]           | 76>72 → ans[5]=1<br>76>75 → ans[2]=4 | [1,1,4,2,1,1,0,0] |
| 7   | 73   | [6]             | Push 7                               | Done              |

Final Answer

```text
[1,1,4,2,1,1,0,0]
```

---

# 9. Related Problems

1. **496. Next Greater Element I**
   The classic next greater element problem using a monotonic stack.

2. **503. Next Greater Element II**
   Extends the next greater element problem to a circular array.

3. **1475. Final Prices With a Special Discount in a Shop**
   Similar pattern but searches for the next **smaller or equal** element.

4. **84. Largest Rectangle in Histogram**
   Uses previous and next smaller elements to determine rectangle widths.

5. **907. Sum of Subarray Minimums**
   Advanced monotonic stack problem using previous and next smaller elements.

---

# Pattern Summary (Interview Revision)

| Problem Clue                   | Pattern                    |
| ------------------------------ | -------------------------- |
| Next warmer day                | Monotonic Decreasing Stack |
| Next greater element           | Monotonic Decreasing Stack |
| Need distance instead of value | Store **indices**          |
| Return days waited             | `nextIndex - currentIndex` |

## Recognition Shortcut

> **"Find the next warmer day."**
>
> Think:
>
> 1. This is a **Next Greater Element** problem.
> 2. Since we need the **number of days**, store **indices**, not values.
> 3. Use a **Monotonic Decreasing Stack**.
>
> **Memory Trick:**
>
> * **Next Greater Element I** → Return the **value**.
> * **Daily Temperatures** → Return the **distance (indices difference)**, so keep **indices** in the stack.
