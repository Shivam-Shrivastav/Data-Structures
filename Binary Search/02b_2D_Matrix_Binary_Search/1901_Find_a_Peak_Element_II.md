
# 1901 Find a Peak Element II (Hard)

## 1. Problem Statement with Example
Given a problem related to **peak finding**, use binary search to optimize searching or decision making.

### Constraints that matter
- Input size can be large → `O(n log n)` or `O(log n)` preferred.
- Array may be sorted / partially sorted / monotonic.
- Direct linear scan may timeout.

---

## 2. Diagram

```text
low ---------------- mid ---------------- high
```

Binary search shrinks the search space every iteration.

---

## 3. Example I/O

### Example 1
Input:
```text
nums = [1,2,3,4,5]
target = 4
```

Output:
```text
3
```

Explanation:
Binary search keeps halving the array until target is found.

### Example 2 (Edge Case)
Input:
```text
nums = [1]
target = 2
```

Output:
```text
-1 / insertion index depending on question
```

---

## 4. Intuition & Pattern Recognition

### Signals
- Sorted array
- Need faster than linear search
- Need minimum / maximum valid answer
- Monotonic predicate exists

### Interview Thought Process
> “If the answer space is monotonic, I can binary search it.”

Binary search works because one half can always be discarded safely.

---

## 5. Simpler Version

### Simplest Form
Classic binary search on sorted array:
- Compare `mid` with target
- Move left or right

### Related Easier Problems
- 704. Binary Search
- 35. Search Insert Position
- 69. Sqrt(x)

### Transition to This Problem
The current problem adds:
- Rotation
- Predicate checking
- Matrix mapping
- Peak logic
- Answer space search

Core idea remains:
> eliminate half the search space every step.

---

## 6. Brute Force

### Idea
Check every possibility linearly.

### Complexity
- Time: `O(n)` or worse
- Space: `O(1)`

---

## 7. Optimal Solution

```python
class Solution:
    def binarySearch(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # target found
            if nums[mid] == target:
                return mid

            # discard left half
            elif nums[mid] < target:
                low = mid + 1

            # discard right half
            else:
                high = mid - 1

        return -1
```

### Complexity
- Time: `O(log n)`
- Space: `O(1)`

---

## 8. Step-by-Step Trace

Target = 4

| low | high | mid | nums[mid] | action |
|---|---|---|---|---|
| 0 | 4 | 2 | 3 | move right |
| 3 | 4 | 3 | 4 | found |

---

## 9. Related Problems

1. **704. Binary Search** → base binary search.
2. **33. Search in Rotated Sorted Array** → binary search with conditions.
3. **153. Find Minimum in Rotated Sorted Array** → identify sorted half.
4. **875. Koko Eating Bananas** → binary search on answer.
5. **410. Split Array Largest Sum** → advanced predicate binary search.
