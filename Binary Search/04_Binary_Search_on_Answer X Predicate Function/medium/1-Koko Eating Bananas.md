# **875. Koko Eating Bananas (Binary Search)**

---

# 1. Problem Statement

Koko loves bananas. There are `n` piles of bananas, where `piles[i]` is the number of bananas in the `iᵗʰ` pile.

The guards will return in exactly `h` hours.

Koko chooses an eating speed `k` (bananas/hour).

Every hour:

* She chooses **one pile**.
* Eats **up to `k` bananas** from that pile.
* If the pile has fewer than `k`, she eats the whole pile.
* She **cannot switch to another pile in the same hour.**

Return the **minimum integer eating speed `k`** so that she finishes all bananas within `h` hours.

### Constraints

* `1 <= piles.length <= 10⁴`
* `piles.length <= h <= 10⁹`
* `1 <= piles[i] <= 10⁹`

The large constraints immediately rule out simulation.

---

# Example

```
Input:
piles = [3,6,7,11]
h = 8

Output:
4
```

Explanation

```
Speed = 4

Pile 3  -> 1 hour
Pile 6  -> 2 hours
Pile 7  -> 2 hours
Pile 11 -> 3 hours

Total = 8 hours
```

---

# 2. Diagram

```
Possible Speeds

1    2    3    4    5    6   ...   11
|----|----|----|----|----|---------|

Hours Needed

speed=1  -> 27 hours
speed=2  -> 15 hours
speed=3  -> 10 hours
speed=4  ->  8 hours ✅
speed=5  ->  8 hours
speed=6  ->  6 hours
...
speed=11 ->  4 hours

Need the FIRST speed
whose hours <= h
```

This is exactly a **Binary Search on Answer**.

---

# 3. Example I/O

## Example 1

```
Input:
piles = [3,6,7,11]
h = 8

Output:
4
```

Why?

```
Speed 3 → 10 hours ❌

Speed 4 → 8 hours ✅

Minimum possible = 4
```

---

## Example 2 (Edge Case)

```
Input:
piles = [30]
h = 30

Output:
1
```

Explanation

```
Eat 1 banana/hour

30 bananas
30 hours

Done.
```

---

# 4. Intuition & Pattern Recognition

### Signal 1

Question asks for

> **minimum value satisfying a condition**

Very strong Binary Search clue.

---

### Signal 2

If a speed works,

```
speed = 8

Then

9 works
10 works
11 works
...
```

Once a speed becomes valid,

**every larger speed is also valid.**

This gives

```
False False False True True True
```

Binary Search works on monotonic functions.

---

### Signal 3

Search space isn't the array.

We're searching

```
Eating Speed

1
2
3
...
max(piles)
```

This is Binary Search on Answer.

---

### Interview Thinking

Ask yourself:

> Can I check whether a given answer is valid?

Here,

Given speed = k,

Can I calculate hours needed?

YES.

So Binary Search.

---

# 5. Simpler Version

## Simpler Problem

Suppose

```
Only one pile

30 bananas

h = 6
```

Need minimum speed.

Obviously

```
30/6 = 5 bananas/hour
```

---

Now multiple piles.

Need

```
hours =
ceil(pile1/speed)
+
ceil(pile2/speed)
+
...
```

Everything becomes the same except summing hours.

---

## Related Simpler LeetCode Problems

### 1. **69. Sqrt(x)**

Search smallest number satisfying

```
mid² >= x
```

Same Binary Search on Answer idea.

---

### 2. **374. Guess Number Higher or Lower**

Binary Search over answers.

---

### 3. **1283. Find the Smallest Divisor Given a Threshold**

Almost identical.

Instead of

```
hours
```

we calculate

```
sum(ceil(num/divisor))
```

Exactly the same pattern.

---

### Thinking Progression

```
Guess Number
      ↓
Binary Search

Sqrt(x)
      ↓
Binary Search on values

Smallest Divisor
      ↓
Check function

Koko Eating Bananas
      ↓
Guess speed
Compute hours
Binary Search
```

---

# 6. Brute Force

Try every possible speed.

```
for speed = 1 to max(piles)

    calculate total hours

    first valid speed
```

### Python

```python
class Solution:
    def minEatingSpeed(self, piles, h):

        max_speed = max(piles)

        for speed in range(1, max_speed + 1):

            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            if hours <= h:
                return speed
```

### Complexity

Time

```
O(maxPile × n)
```

Space

```
O(1)
```

Too slow because

```
maxPile = 10^9
```

---

# 7. Optimal Solution (Binary Search)

### Idea

Search speed between

```
left = 1

right = max(piles)
```

For every mid

Compute

```
hours =
Σ ceil(pile/mid)
```

If

```
hours <= h
```

Try smaller speed.

Else

Need faster eating.

---

### Python

```python
class Solution:
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        while left <= right:

            mid = (left + right) // 2

            hours = 0

            # Calculate hours needed at speed = mid
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                # mid works, try finding a smaller valid speed
                right = mid - 1
            else:
                # Too slow, increase speed
                left = mid + 1

        # left is the minimum valid speed
        return left
```

### Why `(pile + mid - 1) // mid`?

It computes:

```
ceil(pile / mid)
```

Example

```
7 bananas

speed = 3

Need

ceil(7/3)=3 hours

Formula

(7+3-1)//3

=9//3

=3
```

---

### Complexity

Time

```
Binary Search : log(maxPile)

Checking each speed : O(n)

Total

O(n log(maxPile))
```

Space

```
O(1)
```

---

# 8. Step-by-Step Trace

Example

```
piles = [3,6,7,11]

h = 8
```

Initial

```
left = 1

right = 11
```

---

### Iteration 1

```
mid = 6
```

Hours

```
3 →1

6 →1

7 →2

11→2

Total = 6
```

```
6 <= 8

Try smaller

right = 5
```

---

### Iteration 2

```
left=1

right=5

mid=3
```

Hours

```
3→1

6→2

7→3

11→4

Total =10
```

```
Too many hours

left = 4
```

---

### Iteration 3

```
left=4

right=5

mid=4
```

Hours

```
3→1

6→2

7→2

11→3

Total=8
```

Valid

```
right=3
```

---

Loop ends

```
left=4

right=3
```

Answer

```
4
```

---

## Trace Table

| Left | Right | Mid | Hours | Action       |
| ---: | ----: | --: | ----: | ------------ |
|    1 |    11 |   6 |     6 | Right = 5    |
|    1 |     5 |   3 |    10 | Left = 4     |
|    4 |     5 |   4 |     8 | Right = 3    |
| Stop |       |     |       | Return **4** |

---

# 9. Related Problems (Increasing Difficulty)

1. Binary Search (Concept) – Learn the basic binary search template on a sorted search space.

2. Search Insert Position – Find the first valid position in a sorted array, introducing the "first true" binary search pattern.

3. Find the Smallest Divisor Given a Threshold – Nearly identical to Koko; binary search on the answer with `ceil(value/divisor)` as the check function.

4. Capacity To Ship Packages Within D Days – Binary search the minimum ship capacity that satisfies a day limit.

5. Split Array Largest Sum – A harder binary-search-on-answer problem where you minimize the largest subarray sum while respecting the number of partitions.

---

# Recognition Checklist (Interview)

Whenever you see:

* ✅ "Minimum/maximum value"
* ✅ "Such that..." (a condition)
* ✅ You can **check** whether a candidate answer is valid in `O(n)`
* ✅ The valid/invalid answers form a monotonic pattern (`False False ... True True`)

Think:

> **Binary Search on Answer**
