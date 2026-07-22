# Pancake Sorting (LeetCode 969)

**Pattern:** Greedy + Array Reversal (Two Pointers)

---

# 1. Problem Statement

Given an integer array `arr`, sort the array using only **pancake flips**.

A **pancake flip** consists of choosing an integer `k` (`1 <= k <= arr.length`) and **reversing the first `k` elements** of the array.

Return a sequence of pancake flips that sorts the array. Any valid sequence is acceptable.

### Constraints

* `1 <= arr.length <= 100`
* `1 <= arr[i] <= arr.length`
* All elements are unique.
* Need to sort using only prefix reversals.

---

# 2. Diagram

Example

```text id="8v2mqw"
arr = [3,2,4,1]

Goal:
[1,2,3,4]

----------------------------

Largest = 4

Bring 4 to front

Flip(3)

3 2 4 1

↓

4 2 3 1

----------------------------

Move 4 to its correct position

Flip(4)

4 2 3 1

↓

1 3 2 4

----------------------------

Now ignore last position

Repeat for 3...
```

Visualization

```text id="w7lw2t"
Unsorted Part

[3 2 4 1]

↓

Place largest at end

[1 3 2 |4]

↓

Place second largest

[1 2 |3 4]

↓

Place second smallest

[1|2 3 4]
```

---

# 3. Example I/O

### Example 1

```text id="c4e3qo"
Input:
arr = [3,2,4,1]

Output:
[3,4,2,3,2]
```

One valid sequence:

```text id="8o0tr7"
Flip 3

↓

Flip 4

↓

Flip 2

↓

Flip 3

↓

Flip 2
```

Final array:

```text id="dkjhl4"
[1,2,3,4]
```

---

### Example 2

```text id="qzjewb"
Input:
arr = [1,2,3]

Output:
[]
```

Already sorted.

---

### Edge Case

```text id="uxg2ix"
Input:
arr = [1]

Output:
[]
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Only one allowed operation (reverse prefix)
* Need in-place sorting
* Repeatedly place largest/smallest element

Think:

> **Greedy**

At every step:

Place the largest remaining element into its final position.

### Key Observation

Suppose we want to place `5`.

If it's not already at the front:

1. Flip it to the front.
2. Flip the whole unsorted part.

Now `5` reaches its correct position.

Repeat.

### Interview Thinking

Tell yourself:

```text id="pbh6a3"
Sorting isn't free.

The only operation allowed is reversing
a prefix.

So first bring the largest element
to the front.

Then flip the whole unsorted section.

Now the largest element is fixed forever.

Repeat.
```

---

# 5. Simpler Version

## Simpler Question 1

### Reverse String (LeetCode 344)

Reverse an array using two pointers.

Introduces in-place reversal.

---

## Simpler Question 2

### Next Permutation

Reverse only the suffix.

Shows how reversal changes order efficiently.

---

## Simpler Question 3

### Selection Sort

Find the maximum element.

Place it at the end.

Current question uses the same idea, but instead of swapping directly, we use **two flips**.

---

## Current Question

Instead of

```text id="4z52rh"
Swap maximum with end
```

Do

```text id="bhx1na"
Flip maximum to front

↓

Flip front to end
```

---

### Thinking Progression

```text id="8sqcfm"
Reverse Array

↓

Selection Sort

↓

Need only prefix reversals

↓

Bring max to front

↓

Bring max to end

↓

Pancake Sorting
```

---

# 6. Brute Force

Try every possible pancake flip recursively until the array becomes sorted.

### Complexity

```text id="l6j6gk"
Time  : Exponential

Space : Exponential
```

Clearly impractical.

---

# 7. Optimal Solution (Greedy)

### Algorithm

For every position from the end towards the beginning:

1. Find the maximum element in the unsorted part.
2. If already in correct place → continue.
3. Otherwise:

   * Flip it to the front.
   * Flip it to its final position.

Repeat.

---

### Python

```python
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        ans = []
        n = len(arr)

        for size in range(n, 1, -1):

            # Find index of current maximum
            max_idx = arr.index(size)

            # Already at correct position
            if max_idx == size - 1:
                continue

            # Bring maximum to front
            if max_idx != 0:
                arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
                ans.append(max_idx + 1)

            # Move maximum to its final position
            arr[:size] = reversed(arr[:size])
            ans.append(size)

        return ans
```

---

### Complexity

```text id="9jzjnb"
Finding maximum : O(N)

Done N times

Time  : O(N²)

Space : O(1)
```

*(Ignoring the output list of flips.)*

---

# 8. Step-by-Step Trace

Example

```text id="b71jml"
arr = [3,2,4,1]
```

### Place 4

```text id="gux3xw"
Flip(3)

[4,2,3,1]

Flip(4)

[1,3,2,4]
```

---

### Place 3

```text id="0d7bqy"
Flip(2)

[3,1,2,4]

Flip(3)

[2,1,3,4]
```

---

### Place 2

```text id="j5rq74"
Flip(2)

[1,2,3,4]
```

---

Final

```text id="mptgkp"
Sorted!

Flips = [3,4,2,3,2]
```

---

# 9. Related Problems

| Problem                  | Connection                                                                                                |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| **344. Reverse String**  | Basic two-pointer reversal used for every pancake flip.                                                   |
| **31. Next Permutation** | Uses reversal of a suffix to achieve the next lexicographical order.                                      |
| **969. Pancake Sorting** | Classic greedy sorting using only prefix reversals.                                                       |
| **75. Sort Colors**      | In-place array sorting with restricted operations and pointers.                                           |
| **912. Sort an Array**   | General-purpose sorting (Merge Sort/Quick Sort/Heap Sort), contrasting with restricted-operation sorting. |

---

# Key Interview Takeaways

* **Pattern:** Greedy + Array Reversal.
* **Core Insight:** Repeatedly place the largest remaining element into its final position.
* **Allowed Operation:** Reverse only a **prefix** of the array.
* **Algorithm:**

  1. Find the largest element in the unsorted prefix.
  2. Flip it to the front (if needed).
  3. Flip the entire unsorted prefix to move it to the end.
  4. Shrink the unsorted region and repeat.
* **Why It Works:** After each iteration, the largest remaining element is fixed in its final position and never moves again.
* **Complexity:** **O(N²)** time and **O(1)** extra space (excluding the returned list of flips).

Reference style followed from your sliding window revision notes. 
