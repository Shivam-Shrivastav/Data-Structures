# Monotonic Stack

## 1. Pattern in One Minute

### Core Idea

Maintain a stack whose elements are **always increasing** or **always decreasing**. Whenever a new element violates that order, pop until the order is restored.

Each element is:

* Pushed **once**
* Popped **once**

→ Hence, **O(n)**.

### Why does this pattern exist?

Instead of repeatedly scanning left/right for the next greater/smaller element, we keep only the **useful candidates**.

The stack stores elements that are still waiting for an answer.

### Immediately think of Monotonic Stack when

> "For every element, find the nearest greater/smaller element."

or

> "How long until something bigger/smaller appears?"

or

> "Rectangle/span/boundary contribution."

---

# 2. Recognition Signals

## Strong Clues

### Keywords

* Next Greater Element
* Next Smaller Element
* Previous Greater
* Previous Smaller
* Nearest
* First greater
* First smaller
* Span
* Boundary
* Histogram
* Rectangle
* Daily temperatures

---

### Problem Characteristics

✓ Need nearest element satisfying some condition

✓ Need first greater/smaller on left/right

✓ Multiple repeated searches causing O(n²)

✓ Array only (usually)

✓ Linear solution expected

---

### Common Disguises

Instead of saying

> Find next greater

they may ask

* Days until warmer
* Stock span
* Building can see ocean
* Histogram width
* Trapping boundaries
* Collision simulation
* Remove digits
* Lexicographically smallest sequence

---

## Don't use Monotonic Stack when

* Need arbitrary queries
* Updates happen frequently
* Need all greater elements (not nearest)
* Binary Search / Heap / Segment Tree fits better

---

# 3. Mental Model

Think of people standing in a line.

Whenever a taller person arrives:

* everyone shorter behind him becomes useless
* remove them

Only useful candidates survive.

---

### Increasing Stack

Bottom → Top

```
1
3
5
8
```

Small → Large

Useful for

* Next Smaller
* Previous Smaller

---

### Decreasing Stack

```
9
7
5
2
```

Large → Small

Useful for

* Next Greater
* Previous Greater

---

### Important Rule

While current breaks monotonicity

```
while stack and condition:
    stack.pop()
```

then

```
answer
stack.append(current)
```

Everything is based on this.

---

### Store Indices, Not Values

Almost every interview problem needs

* distance
* width
* answer index

Hence

```
stack = []
stack.append(i)
```

instead of values.

---

# 4. Boilerplate Template

## Next Greater Element

```python
stack = []
ans = [-1] * len(nums)

for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        idx = stack.pop()
        ans[idx] = nums[i]

    stack.append(i)
```

---

## Previous Smaller

```python
stack = []

for i in range(len(nums)):
    while stack and nums[stack[-1]] >= nums[i]:
        stack.pop()

    prev = stack[-1] if stack else -1

    stack.append(i)
```

---

## Generic Template

```python
stack = []

for i in range(n):

    while stack and BAD(stack[-1], i):
        stack.pop()

    # process

    stack.append(i)
```

Only the **BAD()** condition changes.

---

# 5. Variations

| Variation                  | Change                                  |
| -------------------------- | --------------------------------------- |
| Next Greater               | Traverse left → right, decreasing stack |
| Next Smaller               | Traverse left → right, increasing stack |
| Previous Greater           | Answer before push                      |
| Previous Smaller           | Answer before push                      |
| Circular Array             | Traverse twice (`2n`)                   |
| Histogram                  | Add sentinel `0` at end                 |
| Stock Span                 | Previous Greater + distance             |
| Daily Temperatures         | Next Greater + index difference         |
| Trapping Rain Water        | Use boundaries                          |
| Remove K Digits            | Pop while current smaller               |
| Lexicographically Smallest | Greedy popping                          |
| Collision Problems         | Simulate using stack                    |

---

# 6. Common Pitfalls

### ❌ Store values instead of indices

Need width?

Impossible.

Store indices.

---

### ❌ Wrong comparison

```
>
>=
<
<=
```

This decides duplicate handling.

Always ask:

Should equal elements stay?

---

### ❌ Forget remaining stack

Remaining elements usually get

```
-1
```

or

```
n
```

depending on problem.

---

### ❌ Histogram width mistake

Width is

```
right - left - 1
```

NOT

```
right-left
```

---

### ❌ Circular traversal

Need

```
for i in range(2*n):
```

Use

```
i % n
```

---

### ❌ Missing Sentinel

Histogram often needs

```
heights.append(0)
```

to flush remaining bars.

---

# 7. Interview Checklist

Ask yourself:

✅ Need nearest greater/smaller?

✅ First element satisfying condition?

✅ Linear solution expected?

✅ Every element should be processed once?

✅ Boundary/span/width involved?

If yes →

**Monotonic Stack**

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for Revision)

1. ⭐ **Daily Temperatures** (Medium)
2. ⭐ **Largest Rectangle in Histogram** (Hard)
3. ⭐ **Next Greater Element II** (Medium)

These three cover almost every interview variation.

---

## Easy

* Next Greater Element I ⭐
* Final Prices With Discount
* Remove Outermost Parentheses (stack basics)

---

## Medium

* Daily Temperatures ⭐
* Next Greater Element II ⭐
* Online Stock Span
* Remove K Digits
* Asteroid Collision
* Sum of Subarray Minimums ⭐
* Maximum Width Ramp
* Beautiful Towers I/II

---

## Hard

* Largest Rectangle in Histogram ⭐
* Trapping Rain Water (Stack approach)
* Maximal Rectangle
* Sum of Subarray Ranges

---

# 9. 30-Second Cheat Sheet

### Recognition

* Next/Previous Greater or Smaller
* Nearest element
* Span
* Boundary
* Histogram
* Rectangle
* O(n) expected

---

### Core Idea

Maintain an increasing/decreasing stack by popping invalid candidates. Every element is pushed and popped at most once.

---

### Generic Template

```python
stack = []

for i in range(n):
    while stack and condition(nums[stack[-1]], nums[i]):
        stack.pop()

    # use stack if needed

    stack.append(i)
```

---

### Complexity

* **Time:** O(n)
* **Space:** O(n)

---

### Common Variations

* Next Greater
* Next Smaller
* Previous Greater
* Previous Smaller
* Circular Array
* Histogram
* Stock Span
* Daily Temperatures
* Sum of Subarray Minimums
* Remove K Digits

---

### Pitfalls

* Store **indices**, not values.
* Be careful with `>` vs `>=` (duplicate handling).
* Flush remaining elements (or use a sentinel when appropriate).
* For histogram, width = `right - left - 1`.
* For circular arrays, iterate `2 * n` with `i % n`.

---

## Mnemonic

Think in terms of **"Who becomes useless when the current element arrives?"**

* **Current is larger** → pop **smaller** elements → **decreasing stack** (Next Greater).
* **Current is smaller** → pop **larger** elements → **increasing stack** (Next Smaller).

This single question helps you derive the correct monotonic stack direction in most interview problems.
