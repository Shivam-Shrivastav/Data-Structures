# 155. Min Stack (Stack)

## 1. Problem Statement

Design a stack that supports the following operations, all in **O(1)** time:

* `push(val)` → Push an element onto the stack.
* `pop()` → Remove the top element.
* `top()` → Return the top element.
* `getMin()` → Return the minimum element currently in the stack.

### Constraints

* Number of operations ≤ 3 × 10⁴
* Values can be negative.
* Every operation must run in **O(1)** time.

---

## Example

```text
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]

[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]
```

Explanation

```text
push(-2)
Stack: [-2]
Min = -2

push(0)
Stack: [-2, 0]
Min = -2

push(-3)
Stack: [-2, 0, -3]
Min = -3

getMin() → -3

pop()
Stack: [-2,0]

top() → 0

getMin() → -2
```

---

# 2. Diagram

Instead of storing only values, store:

```
(value, minimum_so_far)
```

Example:

```
push(-2)

Stack
┌──────────┐
│(-2,-2)   │
└──────────┘


push(0)

Stack
┌──────────┐
│(0,-2)    │
├──────────┤
│(-2,-2)   │
└──────────┘


push(-3)

Stack
┌──────────┐
│(-3,-3)   │
├──────────┤
│(0,-2)    │
├──────────┤
│(-2,-2)   │
└──────────┘
```

Notice every element remembers:

> **"What was the minimum when I was inserted?"**

When popping, the previous minimum automatically comes back.

---

# 3. Example I/O

### Example 1

```
Input
push(-2)
push(0)
push(-3)

getMin()

Output
-3
```

Explanation

Minimum after inserting is **-3**.

---

### Example 2 (Edge Case)

```
push(5)

getMin()

Output
5
```

Single element itself is minimum.

---

# 4. Intuition & Pattern Recognition

### Interview Hint

Whenever you hear:

> "Support min/max in O(1)"

Think immediately:

> **Store extra information along with each element.**

A normal stack forgets previous minimums.

Instead, every node stores:

```
(value, current minimum)
```

So when we remove an element, we instantly know what the previous minimum was.

### Recognition Pattern

Questions asking:

* Current minimum
* Current maximum
* Running information
* O(1) retrieval

usually require:

* Auxiliary stack
* Extra metadata
* Prefix information

---

# 5. Simpler Version

### Simpler Problem

Implement only:

```
push()
pop()
top()
```

This is **LeetCode 225 — Implement Stack using Queues** (or a standard stack implementation).

---

Now add:

```
getMin()
```

Without extra storage you'd scan the stack.

```
O(n)
```

Too slow.

---

### Better Thinking

Store the minimum till every position.

Example

```
Stack

5
2
4
1
```

Store

```
Value   Min

5       5
2       2
4       2
1       1
```

Now minimum is always on top.

---

### Simpler Questions Leading Here

1. Implement Stack
2. Design Browser History
3. Valid Parentheses
4. Daily Temperatures (uses stack)
5. Min Stack ← add metadata

---

# 6. Brute Force

Keep one stack.

```
push -> O(1)

pop -> O(1)

top -> O(1)

getMin -> Scan stack
```

### Python

```python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)
```

### Complexity

* Push : O(1)
* Pop : O(1)
* Top : O(1)
* getMin : **O(n)**

Space:

```
O(n)
```

---

# 7. Optimal Solution

### Idea

Each element stores

```
(value, minimum till now)
```

### Python

```python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # First element, so it is the minimum
        if not self.stack:
            self.stack.append((val, val))
        else:
            # Current minimum is the smaller of
            # current value and previous minimum
            curr_min = min(val, self.stack[-1][1])
            self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        # Return only the value
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return stored minimum
        return self.stack[-1][1]
```

---

### Complexity

| Operation | Time |
| --------- | ---- |
| push      | O(1) |
| pop       | O(1) |
| top       | O(1) |
| getMin    | O(1) |

Space

```
O(n)
```

---

# Alternative Optimal (Two Stacks)

One stack stores values.

Another stack stores minimums.

```
Main Stack

5
2
4
1

Min Stack

5
2
2
1
```

Whenever minimum changes (or stays the same), push onto min stack too.

This is another common interview solution.

---

# 8. Step-by-Step Trace

Operations

```
push(-2)

push(0)

push(-3)

getMin()

pop()

top()

getMin()
```

| Operation | Stack (value,min)        | Return |
| --------- | ------------------------ | ------ |
| push(-2)  | [(-2,-2)]                |        |
| push(0)   | [(-2,-2),(0,-2)]         |        |
| push(-3)  | [(-2,-2),(0,-2),(-3,-3)] |        |
| getMin    | same                     | **-3** |
| pop       | [(-2,-2),(0,-2)]         |        |
| top       | same                     | **0**  |
| getMin    | same                     | **-2** |

---

# 9. Related Problems

| Problem                               | Connection                                                         |
| ------------------------------------- | ------------------------------------------------------------------ |
| **20. Valid Parentheses**             | Basic stack operations.                                            |
| **225. Implement Stack using Queues** | Stack implementation fundamentals.                                 |
| **155. Min Stack**                    | Stack with extra metadata (minimum tracking).                      |
| **901. Online Stock Span**            | Monotonic stack storing additional information.                    |
| **739. Daily Temperatures**           | Classic monotonic stack pattern for next greater/smaller elements. |

---

# Interview Takeaway

Whenever you see:

> **"Design a data structure that returns minimum/maximum in O(1)"**

Think:

* **Store extra information with every element**, or
* **Maintain an auxiliary stack**.

For **Min Stack**, the simplest and most interview-friendly solution is storing each element as:

```text
(value, minimum_so_far)
```

This guarantees **all four operations (`push`, `pop`, `top`, `getMin`) run in O(1) time**.
