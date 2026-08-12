# **1751. Maximum Number of Events That Can Be Attended II (Binary Search + DP)**

---

# 1. Problem Statement

You are given `events`, where each event is represented as:

```
[startDay, endDay, value]
```

You can attend **at most `k` events**.

Rules:

* If you attend an event, you must attend it **from start to end**.
* You **cannot attend overlapping events**.
* Two events overlap if:

```
event1.endDay >= event2.startDay
```

So the next event must start **strictly after** the previous one ends.

Return the **maximum total value** obtainable.

### Constraints

* `1 <= k <= events.length`
* Up to `10^5` events
* O(n²) is impossible.

---

## Example

```
events =
[
 [1,2,4],
 [3,4,3],
 [2,3,1]
]

k = 2
```

Answer:

```
7
```

Attend

```
[1,2] value=4
[3,4] value=3

Total = 7
```

---

# 2. Diagram

Sort by starting day.

```
Index

0      1      2
|------|------|

[1,2,4]
      [2,3,1]
         [3,4,3]
```

If we choose

```
[1,2]
```

Next event must start

```
> 2
```

Binary Search directly jumps to

```
[3,4]
```

instead of checking every event.

---

# 3. Example I/O

### Example 1

Input

```
events =
[
 [1,2,4],
 [3,4,3],
 [2,3,1]
]

k=2
```

Output

```
7
```

Explanation

Choose

```
4 + 3 = 7
```

---

### Example 2 (Edge Case)

```
events =
[
 [1,5,10]
]

k=100
```

Output

```
10
```

Only one event exists.

---

# 4. Intuition & Pattern Recognition

This is a classic:

> **Weighted Interval Scheduling**

except now we may take **up to k intervals**.

Signals:

* intervals
* maximize profit/value
* intervals cannot overlap
* choose some, skip others

Whenever you see

> choose non-overlapping intervals maximizing value

think

```
Sort
+
Binary Search
+
DP
```

Interview thought process:

```
If I take this event,
where is the next compatible event?

Instead of scanning,
binary search can find it.

Then DP decides

Take
or
Skip
```

---

# 5. Simpler Version

## Simpler Problem

### LeetCode 435

Non-overlapping Intervals

Need maximum number of intervals.

No values.

No k.

Just greedy.

---

### Next Step

### LeetCode 1235

Maximum Profit in Job Scheduling

Exactly this problem without k.

State:

```
dp(i)
```

---

### Final Step

Now introduce

```
k choices
```

State becomes

```
dp(i, remainingEvents)
```

Transition remains identical.

Thinking evolution:

```
Greedy intervals
↓

Weighted intervals

↓

Binary Search

↓

DP

↓

DP + remaining k
```

---

# 6. Brute Force

At every event:

```
Take

Skip
```

Need to search next compatible event by scanning.

Complexity

```
Time:
O(2^n)

Space:
O(n)
```

Impossible.

---

# 7. Optimal Solution

## Idea

Sort events by

```
start time
```

State

```
dp(index, remaining)
```

Meaning

```
Maximum value obtainable
starting from index
with remaining events left.
```

Transition

### Skip

```
dp(index+1, remaining)
```

### Take

Need first event whose

```
start > currentEnd
```

Binary Search gives next index.

```
value +
dp(nextIndex, remaining-1)
```

Return max.

---

## Python Solution

```python
from functools import lru_cache
from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        # Sort events by start day
        events.sort()

        # Extract all start days for binary search
        starts = [event[0] for event in events]
        n = len(events)

        @lru_cache(None)
        def dp(index, remaining):
            # No events left or no selections remaining
            if index == n or remaining == 0:
                return 0

            # Option 1: Skip current event
            skip = dp(index + 1, remaining)

            # Find first event starting AFTER current event ends
            next_index = bisect_right(starts, events[index][1])

            # Option 2: Take current event
            take = events[index][2] + dp(next_index, remaining - 1)

            return max(skip, take)

        return dp(0, k)
```

---

## Complexity

Sorting

```
O(n log n)
```

Each state

```
n × k
```

Binary search

```
log n
```

Total

```
Time:
O(nk log n)

Space:
O(nk)
```

---

# 8. Step-by-Step Trace

Example

```
events =
[
[1,2,4],
[3,4,3],
[2,3,1]
]

k=2
```

Sorted

```
0 : [1,2,4]
1 : [2,3,1]
2 : [3,4,3]
```

Starts

```
[1,2,3]
```

---

### DP(0,2)

Current

```
[1,2,4]
```

Binary Search

```
first start >2

= index 2
```

Choices

Skip

```
dp(1,2)
```

Take

```
4 + dp(2,1)
```

---

### DP(2,1)

Current

```
[3,4,3]
```

Next index

```
3
```

Take

```
3
```

Skip

```
0
```

Answer

```
3
```

---

Back

Take

```
4+3=7
```

---

### DP(1,2)

Current

```
[2,3,1]
```

Next

```
3
```

Take

```
1
```

Skip

```
3
```

Answer

```
3
```

---

Final

```
max(
skip=3,
take=7
)

=7
```

---

# DP State Table

| State   | Result |
| ------- | ------ |
| dp(2,1) | 3      |
| dp(1,2) | 3      |
| dp(0,2) | 7      |

Answer

```
7
```

---

# 9. Related Problems

1. **121. Best Time to Buy and Sell Stock** — A simple DP on choices (buy/skip/sell) that introduces state-based optimization.

2. **435. Non-overlapping Intervals** — Greedy version of interval scheduling with no weights.

3. **646. Maximum Length of Pair Chain** — Similar interval compatibility, solved greedily or with DP.

4. **1235. Maximum Profit in Job Scheduling** — Weighted interval scheduling using Binary Search + DP, but with unlimited compatible selections.

5. **1751. Maximum Number of Events That Can Be Attended II** *(this problem)* — Extends weighted interval scheduling by adding a second DP dimension (`remaining events = k`), requiring `dp(index, remaining)` plus binary search for the next compatible event.
