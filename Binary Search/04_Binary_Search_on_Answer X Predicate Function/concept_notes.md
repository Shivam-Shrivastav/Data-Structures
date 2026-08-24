# Binary Search on Answer + Predicate Function (Parametric Search)

---

# 1. Pattern in One Minute

### Core Idea

Instead of binary searching **an element in an array**, binary search **the answer itself**.

You guess an answer `mid` and ask:

> **"Can this answer work?"**

This is checked using a **predicate function**.

The predicate always returns

* True (possible)
* False (not possible)

Binary search works because the answers form a **monotonic transition**.

```
False False False True True True
                 ^
            first valid answer
```

or

```
True True True False False
          ^
     last valid answer
```

---

### Why does this pattern exist?

Many optimization problems ask

* minimum possible...
* maximum possible...
* smallest...
* largest...

where checking one answer is much easier than constructing the answer directly.

Instead of searching the solution space linearly,

Binary Search reduces

```
O(N * AnswerRange)
↓

O(N log AnswerRange)
```

---

### Immediately think of it when

The problem asks

* minimize something
* maximize something
* smallest valid
* largest valid
* answer isn't directly searchable
* feasibility can be checked

---

# 2. Recognition Signals

## Keywords

* Minimum capacity
* Maximum minimum
* Smallest distance
* Largest value
* Minimize X
* Maximize Y
* At least K
* At most K

---

## Constraints

Usually

```
N = 10^5

Answer range = 10^9
```

Linear search impossible.

---

## Problem Characteristics

You can answer

> "Can answer = X?"

efficiently.

Examples

```
Can we finish within D days?

Can we place cows 5 units apart?

Can Koko eat at speed 8?

Can ship capacity be 20?
```

---

## Common disguises

Instead of

> Find minimum capacity

they ask

> What's the smallest speed?

or

> Largest minimum distance

or

> Earliest possible day

---

## Don't use when

* Predicate isn't monotonic.
* Feasibility check is harder than solving directly.
* Answer space is tiny.

---

# 3. Mental Model

* Binary search doesn't require arrays.
* Search any ordered answer space.
* Guess middle answer.
* Validate with predicate.
* Predicate must be monotonic.
* True/False boundary is the answer.
* Shrink search space based on predicate.
* Never build the answer directly.
* Design the predicate first.
* Binary search is only a wrapper around the predicate.

---

# 4. Boilerplate Template

```python
def predicate(mid):
    # Can answer = mid work?
    pass

left = minimum_possible_answer
right = maximum_possible_answer

while left <= right:
    mid = left + (right - left) // 2

    if predicate(mid):
        answer = mid      # valid answer
        right = mid - 1   # try better (smaller)
    else:
        left = mid + 1

return answer
```

---

## If maximizing instead

```python
while left <= right:

    mid = (left + right) // 2

    if predicate(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
```

---

# 5. Variations

| Variation              | Binary Search Goal                    |
| ---------------------- | ------------------------------------- |
| Smallest valid answer  | First True                            |
| Largest valid answer   | Last True                             |
| Minimize maximum       | First True                            |
| Maximize minimum       | Last True                             |
| Floating-point answers | Binary search on doubles with epsilon |
| Continuous search      | Precision-based binary search         |

---

# 6. Common Pitfalls

### Forgetting monotonicity

```
False True False
```

Binary Search breaks.

---

### Wrong search range

Example

```
Capacity

left = max(weights)
right = sum(weights)
```

Not

```
1...
10^9
```

Use the tightest possible bounds.

---

### Predicate solves the whole problem

Predicate should only answer

```
Possible?

YES / NO
```

Not compute the optimal answer.

---

### Wrong direction

For minimum answer

```
True

↓

Search left
```

For maximum answer

```
True

↓

Search right
```

---

### Infinite loop

Always update

```
left = mid + 1

or

right = mid - 1
```

---

# 7. Interview Checklist

✅ Problem asks

* smallest
* largest
* minimum
* maximum

---

✅ Huge answer range

```
10^9
```

---

✅ Can write

```
can(mid)
```

---

✅ Predicate is monotonic

```
False False False True True
```

or

```
True True False False
```

---

✅ Binary search over answers instead of array.

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for Revision)

1. **875. Koko Eating Bananas** ⭐⭐⭐
2. **1011. Capacity To Ship Packages Within D Days** ⭐⭐⭐
3. **1552. Magnetic Force Between Two Balls** ⭐⭐⭐

---

## Easy

* 69. Sqrt(x)
* 367. Valid Perfect Square

---

## Medium

* 875. Koko Eating Bananas ⭐
* 1011. Capacity To Ship Packages ⭐
* 1552. Magnetic Force Between Two Balls ⭐
* 1283. Find the Smallest Divisor Given a Threshold
* 1482. Minimum Number of Days to Make m Bouquets
* 1891. Cutting Ribbons
* 2064. Minimized Maximum of Products Distributed to Any Store
* 2187. Minimum Time to Complete Trips
* 2226. Maximum Candies Allocated to K Children

---

## Hard (High ROI)

* 410. Split Array Largest Sum
* 1231. Divide Chocolate
* 774. Minimize Max Distance to Gas Station (floating-point binary search)

---

# 9. 30-Second Cheat Sheet

### Recognition

* Smallest valid answer
* Largest valid answer
* Minimize/Maximize
* Huge answer range
* Feasibility check possible

---

### Core Idea

Binary search **the answer**, not the data.

Design

```
can(mid)
```

then binary search over possible answers.

---

### Template

```python
while left <= right:
    mid = (left + right) // 2

    if can(mid):
        ans = mid
        right = mid - 1   # first true
    else:
        left = mid + 1
```

For maximum answer:

```python
if can(mid):
    ans = mid
    left = mid + 1
else:
    right = mid - 1
```

---

### Complexity

* Predicate: **O(f(n))**
* Binary Search: **O(log AnswerRange)**
* Total: **O(f(n) · log AnswerRange)**

---

### Common Variations

* Smallest valid value
* Largest valid value
* Minimize maximum
* Maximize minimum
* Floating-point binary search

---

### Pitfalls

* ❌ Non-monotonic predicate
* ❌ Wrong search bounds
* ❌ Moving in the wrong direction after a valid `mid`
* ❌ Predicate computes the answer instead of just checking feasibility
