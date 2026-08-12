# **1552. Magnetic Force Between Two Balls (Binary Search on Answer)**

> **Pattern:** Binary Search on Answer + Greedy

---

# 1. Problem Statement

You are given an array `position`, where `position[i]` represents the location of a basket on a line.

You have `m` balls.

Place the `m` balls into different baskets such that the **minimum distance between any two balls** is as **large as possible**.

Return that **maximum possible minimum distance**.

---

### Constraints

* `2 <= position.length <= 10⁵`
* `1 <= position[i] <= 10⁹`
* All positions are unique.
* `2 <= m <= position.length`

---

## Example

```text
Input:

position = [1,2,3,4,7]

m = 3

Output:

3
```

Explanation

Place balls at

```text
1      4      7

Distance =

3
3
```

Minimum distance = **3**

No placement can achieve **4**.

---

# 2. Diagram

First sort

```text
1   2   3   4   7
```

Try minimum distance

```text
Distance = 3

●-------●-------●

1       4       7
```

Possible answers

```text
1    2    3    4
|----|----|----|

Possible?

Yes
Yes
Yes
No
```

```text
True True True False
```

We need the **largest valid distance**.

---

# 3. Example I/O

## Example 1

```text
Input

position = [1,2,3,4,7]

m = 3

Output

3
```

Explanation

```text
Put balls

1

4

7

Minimum distance

3
```

---

## Example 2

```text
Input

position = [5,4,3,2,1,1000000000]

m = 2

Output

999999999
```

Place balls

```text
1

1000000000
```

---

# 4. Intuition & Pattern Recognition

### Signal 1

Question asks

> **Maximum minimum distance**

This is a classic Binary Search on Answer problem.

---

### Signal 2

Suppose

```text
distance = 5
```

is possible.

Then

```text
4
3
2
1
```

must also be possible.

Smaller required distances are always easier.

Monotonic.

```text
True True True False False
```

---

### Signal 3

Need to answer

> Can we place all `m` balls if every pair is at least `mid` apart?

This can be checked greedily.

---

### Interview Thinking

Ask yourself

> If I guess a distance, can I verify it?

Yes.

Greedily place balls from left to right.

If all balls fit,

distance works.

---

# 5. Simpler Version

## Simplest Problem

Suppose

```text
position = [1,5]

m=2
```

Maximum minimum distance?

```text
4
```

---

Now

```text
1 2 4 8

m=3
```

Try

```text
distance=4
```

Greedy placement

```text
1

Next ≥5

8
```

Only

2 balls

Not enough.

---

## Why Greedy Works?

Always place the next ball in the **leftmost basket** that satisfies the required distance.

Why?

Placing earlier leaves **more room** for future balls.

Choosing a later basket can only reduce your options.

---

## Simpler LeetCode Problems

### 1. **875. Koko Eating Bananas**

Guess speed.

Check feasibility.

---

### 2. **1011. Capacity To Ship Packages**

Guess capacity.

Check feasibility.

---

### 3. **1283. Smallest Divisor**

Guess divisor.

Check feasibility.

---

### Thinking Progression

```text
Binary Search
      ↓
Guess Answer
      ↓
Check Function
      ↓
Greedy Verification
      ↓
Magnetic Force
```

---

# 6. Brute Force

Try every distance.

```text
1

↓

max(position)-min(position)
```

For every distance,

try placing balls greedily.

### Python

```python
class Solution:
    def maxDistance(self, position, m):

        position.sort()

        answer = 1

        for dist in range(1, position[-1] - position[0] + 1):

            balls = 1
            last = position[0]

            for p in position[1:]:

                if p - last >= dist:
                    balls += 1
                    last = p

            if balls >= m:
                answer = dist

        return answer
```

### Complexity

```text
O(range × n)
```

Too slow because positions go up to **10⁹**.

---

# 7. Optimal Solution

## Search Space

Minimum possible distance

```text
1
```

Maximum possible distance

```text
position[-1]-position[0]
```

---

## Check Function

For a guessed distance

```text
mid
```

Greedily place balls.

If

```text
balls >= m
```

distance works.

Try a larger distance.

Otherwise

reduce it.

---

## Python

```python
class Solution:
    def maxDistance(self, position, m):

        position.sort()

        left = 1
        right = position[-1] - position[0]

        # Check if we can place all balls
        # with at least 'dist' separation
        def canPlace(dist):

            balls = 1
            last_position = position[0]

            for current in position[1:]:

                if current - last_position >= dist:
                    balls += 1
                    last_position = current

            return balls >= m

        while left <= right:

            mid = (left + right) // 2

            if canPlace(mid):
                # Distance works, try larger
                left = mid + 1
            else:
                # Distance too large
                right = mid - 1

        return right
```

---

## Why Return `right`?

We are searching for the **largest valid** answer.

When

```text
mid works
```

we move

```text
left = mid + 1
```

Eventually

```text
left
```

becomes the first invalid distance.

So

```text
right
```

is the last valid distance.

---

## Complexity

Sorting

```text
O(n log n)
```

Binary Search

```text
O(log(maxDistance))
```

Each check

```text
O(n)
```

Overall

```text
O(n log n + n log(maxDistance))
```

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
position = [1,2,3,4,7]

m=3
```

Sorted

```text
1 2 3 4 7
```

Initial

```text
left=1

right=6
```

---

### Iteration 1

```text
mid=3
```

Greedy

```text
Place at 1

Next ≥4

Place at 4

Next ≥7

Place at 7
```

Placed

```text
3 balls
```

Works.

```text
left=4
```

---

### Iteration 2

```text
mid=5
```

Greedy

```text
1

Next ≥6

7
```

Only

2 balls.

Too large.

```text
right=4
```

---

### Iteration 3

```text
mid=4
```

Greedy

```text
1

Next ≥5

7
```

Only

2 balls.

Too large.

```text
right=3
```

Loop ends.

Answer

```text
3
```

---

## Dry Run Table

| Left | Right | Mid | Can Place? | Decision     |
| ---: | ----: | --: | ---------- | ------------ |
|    1 |     6 |   3 | Yes        | Left = 4     |
|    4 |     6 |   5 | No         | Right = 4    |
|    4 |     4 |   4 | No         | Right = 3    |
| Stop |       |     |            | **Return 3** |

---

# 9. Related Problems (Increasing Difficulty)

1. Aggressive Cows – The classic problem that inspired this LeetCode question. Same greedy + binary search approach.

2. Koko Eating Bananas – Binary search the minimum feasible eating speed.

3. Capacity To Ship Packages Within D Days – Binary search the minimum feasible ship capacity.

4. Split Array Largest Sum – Binary search the answer while checking feasibility through greedy partitioning.

5. Maximum Tastiness of Candy Basket – Very similar to this problem: maximize the minimum difference between chosen values using binary search and greedy placement.

---

# Binary Search on Answer Cheat Sheet

| Problem                       | Search Space                  | Check Function          | Return  |
| ----------------------------- | ----------------------------- | ----------------------- | ------- |
| **875. Koko Eating Bananas**  | `1 → max(piles)`              | Hours ≤ `h`             | `left`  |
| **1011. Ship Packages**       | `max(weights) → sum(weights)` | Days ≤ `D`              | `left`  |
| **1283. Smallest Divisor**    | `1 → max(nums)`               | Sum ≤ threshold         | `left`  |
| **1292. Maximum Side Length** | `0 → min(m,n)`                | Any valid square exists | `right` |
| **1552. Magnetic Force**      | `1 → maxPos-minPos`           | Can place all balls     | `right` |

## Interview Recognition

This problem differs from Koko/Shipping in one important way:

* **Koko/Shipping:** Find the **minimum** feasible value.

  * Pattern: `False False True True`
  * Move left when valid.
  * Return **`left`**.

* **Magnetic Force:** Find the **maximum** feasible value.

  * Pattern: `True True False False`
  * Move right when valid.
  * Return **`right`**.

A quick rule to remember:

* **Minimize a feasible answer** → return `left`.
* **Maximize a feasible answer** → return `right`.
