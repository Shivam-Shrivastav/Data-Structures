# **901. Online Stock Span**

## 1. Problem Statement

Design a class `StockSpanner` that collects daily stock prices and returns the **stock span** for each new price.

The **span** of today's stock price is the **number of consecutive days (including today)** for which the stock price was **less than or equal to today's price**.

Implement:

* `StockSpanner()` → Initializes the object.
* `next(int price)` → Returns the span of the current day's price.

### Constraints

* `1 <= price <= 10⁵`
* At most `10⁴` calls to `next()`.

The important phrase is:

> **Consecutive Previous Smaller (or Equal) Elements**

---

# 2. Diagram

Example

```text
Prices arrive one by one:

100, 80, 60, 70, 60, 75, 85
```

```text
Day:      1   2   3   4   5   6   7
Price:   100 80  60  70  60  75  85

100 → Span = 1

80
↑ stop (100 > 80)
Span = 1

60
↑ stop (80 > 60)
Span = 1

70
60 ≤ 70 ✓
80 > 70 stop

Span = 2

60
70 > 60 stop

Span = 1

75
60 ≤ 75 ✓
70 ≤ 75 ✓
80 > 75 stop

Span = 4

85
75 ≤ 85 ✓
80 ≤ 85 ✓
100 > 85 stop

Span = 6
```

Output

```text
[1,1,1,2,1,4,6]
```

---

# 3. Example I/O

### Example 1

```text
Input

["StockSpanner","next","next","next","next","next","next","next"]

[[],[100],[80],[60],[70],[60],[75],[85]]
```

Output

```text
[null,1,1,1,2,1,4,6]
```

---

### Example 2

```text
Prices

31
41
48
59
79
```

Output

```text
1
2
3
4
5
```

Every previous price is smaller.

---

### Edge Case

```text
Prices

100
90
80
70
```

Output

```text
1
1
1
1
```

---

# 4. Intuition & Pattern Recognition

## Interview Signals

Whenever you see

* Consecutive previous elements
* Previous greater/smaller
* Span
* Online queries (one value at a time)

Think

> **Monotonic Stack**

---

### Key Observation

Suppose prices arrive

```text
100
80
60
70
75
```

When **75** arrives,

do we ever need **60** or **70** individually again?

No.

Since **75** is greater than both,

they will never stop the span of any future larger price.

So we can safely remove them.

This is exactly why a stack works.

---

# 5. Simpler Version

## Simplest Problem

Given an array,

find the **Previous Greater Element**.

Example

```text
[100,80,60,70,75]

Previous Greater

100 → None
80 →100
60 →80
70 →80
75 →80
```

---

## Difference Here

Instead of returning the previous greater value,

we return

```text
distance from previous greater
```

because

```text
Span

=
Current Index
-
Previous Greater Index
```

---

### Simpler Problems Leading Here

1. Previous Greater Element
2. Next Greater Element
3. Daily Temperatures
4. Online Stock Span

Thinking progression

```text
Need Previous Greater
        ↓
Monotonic Stack
        ↓
Need distance
        ↓
Need online processing
        ↓
Store previous unresolved prices
```

---

# 6. Brute Force

For every new price,

keep scanning backwards until a greater price appears.

### Python

```python
class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)

        span = 1
        i = len(self.prices) - 2

        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1

        return span
```

### Complexity

Each query

```text
O(n)
```

Worst-case total

```text
O(n²)
```

---

# 7. Optimal Solution

## Method 1 (Store Price + Span) ⭐ Recommended

### Idea

Instead of storing every previous price,

store

```text
(price, span)
```

Whenever a larger price arrives,

merge all smaller spans.

### Python

```python
class StockSpanner:

    def __init__(self):
        self.stack = []   # (price, span)

    def next(self, price):
        span = 1

        # Merge spans of all smaller/equal prices
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))

        return span
```

---

### Why does this work?

Suppose stack

```text
(100,1)
(80,1)
(75,4)
```

New price

```text
85
```

Instead of counting

```text
75
70
60
```

again,

we already know

```text
75 represents span = 4
```

So

```text
span = 1 + 4
```

One pop handles multiple days.

---

### Complexity

Each price

* pushed once
* popped once

Time

```text
O(1) amortized
```

Total

```text
O(n)
```

Space

```text
O(n)
```

---

## Method 2 (Previous Greater Index)

Store indices.

Current span

```text
currentIndex - previousGreaterIndex
```

### Python

```python
class StockSpanner:

    def __init__(self):
        self.stack = []          # indices
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        i = len(self.prices) - 1

        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        if not self.stack:
            span = i + 1
        else:
            span = i - self.stack[-1]

        self.stack.append(i)

        return span
```

---

# 8. Step-by-Step Trace

Using **Method 1**

```text
Prices

100
80
60
70
60
75
85
```

| Price | Stack Before           | Operation | Returned Span                  | Stack After             |
| ----- | ---------------------- | --------- | ------------------------------ | ----------------------- |
| 100   | []                     | Push      | 1                              | [(100,1)]               |
| 80    | [(100,1)]              | Push      | 1                              | [(100,1),(80,1)]        |
| 60    | ...                    | Push      | 1                              | [(100,1),(80,1),(60,1)] |
| 70    | Pop (60,1)             | 1+1=2     | 2                              | [(100,1),(80,1),(70,2)] |
| 60    | Push                   | 1         | [(100,1),(80,1),(70,2),(60,1)] |                         |
| 75    | Pop (60,1), Pop (70,2) | 1+1+2=4   | 4                              | [(100,1),(80,1),(75,4)] |
| 85    | Pop (75,4), Pop (80,1) | 1+4+1=6   | 6                              | [(100,1),(85,6)]        |

Final outputs

```text
[1,1,1,2,1,4,6]
```

---

# 9. Related Problems

1. **496. Next Greater Element I**
   Finds the next greater element on the right using a monotonic stack.

2. **503. Next Greater Element II**
   Extends the next greater element problem to a circular array.

3. **739. Daily Temperatures**
   Finds the next warmer day and returns the distance instead of the value.

4. **84. Largest Rectangle in Histogram**
   Uses previous and next smaller elements to determine rectangle widths.

5. **1944. Number of Visible People in a Queue**
   Uses a monotonic stack to count visible people while processing one direction.

---

# Pattern Summary (Interview Revision)

| Problem Clue                       | Pattern                                           |
| ---------------------------------- | ------------------------------------------------- |
| Previous greater element           | Monotonic Decreasing Stack                        |
| Consecutive previous smaller/equal | Pop until previous greater remains                |
| Online processing                  | Maintain stack across queries                     |
| Need span                          | Store **(price, span)** or previous greater index |

## Recognition Shortcut

> **"Find the span of today's price."**
>
> Think:
>
> 1. We need the **Previous Greater Element**.
> 2. Maintain a **Monotonic Decreasing Stack**.
> 3. Since queries are **online**, preserve the stack between calls.
> 4. The cleanest solution stores **(price, span)**, allowing spans of popped elements to be merged in **O(1) amortized**.

---

# Comparison with Other Monotonic Stack Problems

| Problem                          | Looking For             | Direction        | Stack Stores      | Output                           |
| -------------------------------- | ----------------------- | ---------------- | ----------------- | -------------------------------- |
| **496. Next Greater Element I**  | Next Greater            | Right            | Values            | Next greater value               |
| **503. Next Greater Element II** | Next Greater (Circular) | Right (2 passes) | Indices           | Next greater value               |
| **739. Daily Temperatures**      | Next Warmer Day         | Right            | Indices           | Distance                         |
| **1475. Final Prices**           | Next Smaller or Equal   | Right            | Values/Indices    | Discounted price                 |
| **901. Online Stock Span**       | Previous Greater        | Left             | **(Price, Span)** | Span (count of consecutive days) |

### Memory Trick

* **Next Greater** → Look **right**.
* **Daily Temperatures** → Next Greater **+ distance**.
* **Final Prices** → Next **Smaller or Equal**.
* **Stock Span** → Look **left** (Previous Greater), process **online**, and store **(price, span)** for maximum efficiency.
