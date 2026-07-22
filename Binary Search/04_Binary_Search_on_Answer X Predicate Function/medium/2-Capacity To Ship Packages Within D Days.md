# **Binary Search on Answer Template**

Koko Eating Bananas and Capacity To Ship Packages are almost the **same problem**.

The only thing that changes is the **check function**.

| Problem                   | Guess         | Check Function           |
| ------------------------- | ------------- | ------------------------ |
| Koko Eating Bananas       | Eating Speed  | Calculate hours required |
| Capacity To Ship Packages | Ship Capacity | Calculate days required  |

---

# **1011. Capacity To Ship Packages Within D Days (Binary Search)**

---

# 1. Problem Statement

You are given an array `weights`, where `weights[i]` is the weight of the `iᵗʰ` package.

A ship has a fixed carrying capacity.

Packages **must be shipped in the same order** they appear.

Each day:

* Load packages one by one.
* If adding the next package exceeds the ship's capacity, stop for that day.
* Continue from the next package on the following day.

Return the **minimum ship capacity** required to ship all packages within `days`.

### Constraints

* `1 <= weights.length <= 5 × 10⁴`
* `1 <= weights[i] <= 500`
* `1 <= days <= weights.length`

The large constraints immediately suggest **Binary Search**, not brute force.

---

## Example

```text
Input:
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

Output:
15
```

Explanation

```text
Capacity = 15

Day 1 : 1 + 2 + 3 + 4 + 5 = 15
Day 2 : 6 + 7 = 13
Day 3 : 8
Day 4 : 9
Day 5 : 10
```

Capacity 14 would require **6 days**, so the answer is **15**.

---

# 2. Diagram

```
Possible Capacities

10   11   12   13   14   15   16   17
 |----|----|----|----|----|----|----|

Days Required

10 → 10 days
11 → 9
12 → 8
13 → 7
14 → 6
15 → 5 ✅
16 → 5
17 → 4
```

Notice

```
Capacity ↑

Days Needed ↓
```

Once a capacity works,

```
False False False False True True True
```

This monotonic property is why Binary Search works.

---

# 3. Example I/O

### Example 1

```
Input:
weights = [3,2,2,4,1,4]
days = 3

Output:
6
```

Explanation

```
Capacity = 6

Day1 : 3 + 2 = 5

Day2 : 2 + 4 = 6

Day3 : 1 + 4 = 5
```

Exactly 3 days.

---

### Example 2 (Edge Case)

```
Input:
weights = [5]

days = 1

Output:
5
```

Only one package.

Capacity must be at least **5**.

---

# 4. Intuition & Pattern Recognition

### Signal 1

The problem asks for

> **Minimum capacity**

Whenever you see **minimum/maximum possible value**, think:

> **Binary Search on Answer**

---

### Signal 2

Suppose capacity **20** works.

Then

```
21 works
22 works
23 works
...
```

Increasing capacity can never increase the number of days.

So we get

```
False False False True True True
```

Perfect Binary Search pattern.

---

### Signal 3

We're not searching inside the array.

We're searching over

```
Capacity

max(weights)
↓

sum(weights)
```

---

### Interview Thinking

Ask yourself:

> If I guess a capacity, can I verify whether it works?

Yes.

Just simulate shipping once.

Since verification is **O(n)**,

Binary Search becomes

```
O(n log(sum(weights)))
```

---

# 5. Simpler Version

## Simpler Problem

Suppose

```
weights = [10]

days = 1
```

Minimum capacity?

```
10
```

---

Now

```
weights = [3,5]

days = 1
```

Need

```
3 + 5 = 8
```

---

Now multiple days.

Instead of shipping everything today,

keep loading packages until capacity is exceeded.

Start the next day.

That's the only additional logic.

---

## Simpler LeetCode Problems

### 1. **374. Guess Number Higher or Lower**

Basic Binary Search.

---

### 2. **875. Koko Eating Bananas**

Guess speed.

Calculate hours.

Same Binary Search on Answer idea.

---

### 3. **1283. Find the Smallest Divisor Given a Threshold**

Guess divisor.

Calculate threshold.

Same check function pattern.

---

### 4. **410. Split Array Largest Sum**

Guess largest allowed subarray sum.

Count partitions.

Almost identical to this problem.

---

### Thinking Progression

```
Binary Search
      ↓
Guess Answer
      ↓
Can I verify it?
      ↓
Koko Eating Bananas
      ↓
Capacity To Ship Packages
      ↓
Split Array Largest Sum
```

---

# 6. Brute Force

Try every possible capacity.

```
capacity

=

max(weights)

to

sum(weights)
```

For every capacity,

simulate shipping.

Return the first valid capacity.

### Python

```python
class Solution:
    def shipWithinDays(self, weights, days):

        for capacity in range(max(weights), sum(weights) + 1):

            required_days = 1
            current = 0

            for weight in weights:

                if current + weight > capacity:
                    required_days += 1
                    current = 0

                current += weight

            if required_days <= days:
                return capacity
```

### Complexity

Time

```
O(sum(weights) × n)
```

Space

```
O(1)
```

Too slow.

---

# 7. Optimal Solution

## Step 1 : Search Space

The minimum possible capacity is

```
max(weights)
```

because every package must fit individually.

The maximum possible capacity is

```
sum(weights)
```

Ship everything in one day.

---

## Step 2 : Check Function

For a guessed capacity,

count how many days are needed.

If

```
required_days <= days
```

capacity works.

Try smaller.

Otherwise,

increase capacity.

---

## Python

```python
class Solution:
    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        while left <= right:

            mid = (left + right) // 2

            required_days = 1
            current_weight = 0

            # Calculate how many days are needed
            for weight in weights:

                # Current package doesn't fit today
                if current_weight + weight > mid:
                    required_days += 1
                    current_weight = 0

                current_weight += weight

            if required_days <= days:
                # Capacity works, try smaller
                right = mid - 1
            else:
                # Capacity too small
                left = mid + 1

        return left
```

---

### Complexity

Binary Search

```
O(log(sum(weights)))
```

Each validation

```
O(n)
```

Overall

```
O(n log(sum(weights)))
```

Space

```
O(1)
```

---

# 8. Step-by-Step Trace

Example

```
weights = [3,2,2,4,1,4]

days = 3
```

Initial

```
left = 4
right = 16
```

---

### Iteration 1

```
mid = 10
```

Simulation

```
Day1

3+2+2 =7

Next package =4

7+4 =11 >10

Ship Day1
```

```
Day2

4+1+4=9
```

Total

```
Days =2
```

Works.

```
right = 9
```

---

### Iteration 2

```
left=4

right=9

mid=6
```

Simulation

```
Day1

3+2=5

Next=2

7>6

Ship
```

```
Day2

2+4=6
```

```
Day3

1+4=5
```

Days

```
3
```

Works.

```
right=5
```

---

### Iteration 3

```
left=4

right=5

mid=4
```

Simulation

```
Day1 :3

Day2 :2+2

Day3 :4

Day4 :1

Day5 :4
```

Need

```
5 days
```

Too many.

```
left=5
```

---

### Iteration 4

```
mid=5
```

Simulation

```
Day1 :3+2

Day2 :2

Day3 :4+1

Day4 :4
```

Need

```
4 days
```

Still too many.

```
left=6
```

Loop ends.

Answer

```
6
```

---

## Dry Run Table

| Left | Right | Mid | Days Needed | Decision             |
| ---- | ----- | --- | ----------- | -------------------- |
| 4    | 16    | 10  | 2           | Works → Right = 9    |
| 4    | 9     | 6   | 3           | Works → Right = 5    |
| 4    | 5     | 4   | 5           | Too Small → Left = 5 |
| 5    | 5     | 5   | 4           | Too Small → Left = 6 |
| Stop |       |     |             | **Answer = 6**       |

---

# 9. Related Problems (Increasing Difficulty)

1. Koko Eating Bananas – Guess the minimum eating speed and verify whether all bananas can be finished within `h` hours.

2. Find the Smallest Divisor Given a Threshold – Guess the divisor and compute the resulting sum using a check function.

3. Split Array Largest Sum – Guess the largest allowed partition sum and count how many partitions are required. This is the closest follow-up to this problem.

4. Minimum Limit of Balls in a Bag – Binary search the smallest feasible maximum bag size while counting split operations.

5. Magnetic Force Between Two Balls – Reverse the idea by maximizing the minimum feasible distance, using binary search on the answer.

---

# Binary Search on Answer Cheat Sheet

| Problem                             | Search Space                  | Check Function               |
| ----------------------------------- | ----------------------------- | ---------------------------- |
| **875. Koko Eating Bananas**        | `1 → max(piles)`              | Compute total hours          |
| **1011. Capacity To Ship Packages** | `max(weights) → sum(weights)` | Compute total days           |
| **1283. Smallest Divisor**          | `1 → max(nums)`               | Compute threshold sum        |
| **410. Split Array Largest Sum**    | `max(nums) → sum(nums)`       | Compute number of partitions |

## Interview Recognition

Whenever you see:

* ✅ Find the **minimum/maximum possible value**
* ✅ You can **guess** an answer
* ✅ You can **verify** that guess in **O(n)**
* ✅ The answers are monotonic (`False False ... True True`)

Immediately think:

> **Binary Search on Answer**.
