# **1475. Final Prices With a Special Discount in a Shop**

## 1. Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of the `i`-th item in a shop.

For every item, find the **first item to its right** whose price is **less than or equal to** the current item's price.

* If such an item exists, subtract its price from the current item's price.
* Otherwise, the item's price remains unchanged.

Return the array of final prices.

### Constraints

* `1 <= prices.length <= 500`
* `1 <= prices[i] <= 1000`

The important part is **"first smaller or equal element on the right."**

---

## 2. Diagram

Example:

```
prices = [8,4,6,2,3]

Index:    0   1   2   3   4
Price:    8   4   6   2   3

8 ---> first <= 8 is 4
4 ---> first <= 4 is 2
6 ---> first <= 6 is 2
2 ---> none
3 ---> none

Final:
8-4 = 4
4-2 = 2
6-2 = 4
2
3

Output = [4,2,4,2,3]
```

This is exactly a **Next Smaller (or Equal) Element** problem.

---

# 3. Example I/O

### Example 1

**Input**

```
prices = [8,4,6,2,3]
```

**Output**

```
[4,2,4,2,3]
```

Explanation

```
8 gets discount 4
4 gets discount 2
6 gets discount 2
2 gets no discount
3 gets no discount
```

---

### Example 2 (Edge Case)

**Input**

```
prices = [5]
```

Output

```
[5]
```

Only one item exists.

---

### Example 3

```
Input:
prices = [10,1,1,6]

Output:
[9,0,1,6]
```

Explanation

```
10 -> first <=10 is 1
1 -> first <=1 is next 1
1 -> none
6 -> none
```

---

# 4. Intuition & Pattern Recognition

### Interview Signals

Whenever you see

* nearest element
* first smaller to right
* first greater to left
* next greater/smaller

Think immediately:

> **Monotonic Stack**

Here we need

> **First Smaller or Equal on Right**

A brute force scan works but is O(n²).

A stack lets us find that first qualifying element in O(n).

### Why a stack?

Suppose we're processing from **right → left**.

When standing at a number,

* elements larger than it can never become its discount
* remove them
* the remaining top is the first smaller/equal element

---

# 5. Simpler Version

### Simplest Problem

Find the **next smaller element** for every array element.

Example

```
[5,2,8,1]

Next Smaller

5 ->2
2 ->1
8 ->1
1 ->None
```

This is the classic **Next Smaller Element** problem.

---

### Difference Here

Instead of returning the next smaller element,

return

```
price - nextSmallerOrEqual
```

or

```
price
```

if none exists.

So this problem is simply

```
Next Smaller Element
+
Subtract Discount
```

---

### Simpler Problems Leading Here

1. Next Greater Element I
2. Next Smaller Element
3. Daily Temperatures
4. Stock Span
5. Final Prices (this problem)

Thinking progression:

```
Nearest Element
      ↓
Use Monotonic Stack
      ↓
Need smaller element
      ↓
Need first smaller/equal
      ↓
Subtract instead of returning
```

---

# 6. Brute Force

For every item,

scan towards the right until you find

```
prices[j] <= prices[i]
```

Then subtract it.

### Python

```python
class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        ans = prices[:]

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    ans[i] -= prices[j]
                    break

        return ans
```

### Complexity

Time:

```
O(n²)
```

Space:

```
O(n)
```

---

# 7. Optimal Solution (Monotonic Increasing Stack)

### Idea

Traverse **from right to left**.

Maintain a stack containing possible discounts.

For each price:

* Remove all larger prices (they can't be the first ≤ discount).
* If stack isn't empty, its top is the discount.
* Push current price.

### Python

```python
class Solution:
    def finalPrices(self, prices):
        stack = []              # Monotonic increasing stack (from top to bottom)
        ans = prices[:]

        # Traverse from right to left
        for i in range(len(prices) - 1, -1, -1):

            # Remove prices that are larger than current,
            # because they cannot be a valid discount.
            while stack and stack[-1] > prices[i]:
                stack.pop()

            # Top of stack is the first smaller or equal price.
            if stack:
                ans[i] = prices[i] - stack[-1]

            # Current price may serve as a discount for elements to its left.
            stack.append(prices[i])

        return ans
```

### Complexity

Time

```
O(n)
```

Each element is pushed and popped at most once.

Space

```
O(n)
```

---

# 8. Step-by-Step Trace

Example

```
prices = [8,4,6,2,3]
```

| Step | i | Price | Stack Before | Operation | Discount | Answer | Stack After |
| ---- | - | ----- | ------------ | --------- | -------- | ------ | ----------- |
| 1    | 4 | 3     | []           | Push      | None     | 3      | [3]         |
| 2    | 3 | 2     | [3]          | Pop 3     | None     | 2      | [2]         |
| 3    | 2 | 6     | [2]          | Top=2     | 6−2=4    | 4      | [2,6]       |
| 4    | 1 | 4     | [2,6]        | Pop 6     | Top=2    | 2      | [2,4]       |
| 5    | 0 | 8     | [2,4]        | Top=4     | 4        | 4      | [2,4,8]     |

Final answer

```
[4,2,4,2,3]
```

---

# 9. Related Problems

1. **496. Next Greater Element I**
   Learn the basic monotonic stack pattern for finding the next qualifying element.

2. **503. Next Greater Element II**
   Extends the same idea to circular arrays.

3. **739. Daily Temperatures**
   Uses a monotonic stack to find the next warmer day instead of the next greater element.

4. **84. Largest Rectangle in Histogram**
   Uses previous and next smaller elements to compute rectangle widths.

5. **907. Sum of Subarray Minimums**
   Advanced monotonic stack problem using previous/next smaller elements to calculate each element's contribution.

---

# Pattern Summary (Interview Revision)

| Clue in Problem                | Pattern                       |
| ------------------------------ | ----------------------------- |
| First smaller element on right | Monotonic Stack               |
| First greater element on right | Monotonic Stack               |
| Nearest greater/smaller        | Monotonic Stack               |
| Previous greater/smaller       | Monotonic Stack               |
| Discount = first smaller/equal | Next Smaller or Equal Element |

### Recognition Shortcut

> **"Find the first element to the right that is smaller (or smaller/equal)."**
> → Think **Monotonic Increasing Stack**.
> Traverse **right → left**, pop all larger elements, and the stack top (if any) is the answer.
