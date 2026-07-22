
# Longest Substring Without Repeating Characters

## 1. Problem Statement with Example
Given an input related to **Longest Substring Without Repeating Characters**, solve it efficiently using the Sliding Window pattern.

### Key Constraints
- Input size is usually large (`10^5` range)
- Brute force often becomes `O(n^2)`
- Window expansion/contraction is required

---

## 2. Diagram

```text
Window Movement

L                R
v                v
[a, b, c, d, e, f]

Expand R ->
Shrink L when condition breaks
```

---

## 3. Example I/O

### Example 1
Input:
```text
nums = [1,2,3,4]
k = 2
```

Output:
```text
Expected result based on sliding window logic
```

Explanation:
- Build window
- Maintain condition
- Update answer

### Edge Case
Input:
```text
nums = [1]
```

Output:
```text
1
```

---

## 4. Intuition & Pattern Recognition

Signals:
- Subarray / substring
- Contiguous region
- "Longest", "minimum", "maximum"
- Condition changes while moving

Interview Thinking:
> "Can I reuse previous window work instead of recalculating everything?"

Sliding window works because:
- Each element enters once
- Each element leaves once
- Gives near `O(n)` complexity

---

## 5. Simpler Version

### Simpler Problems
1. Two Sum → maintain state
2. Maximum Sum Subarray of Size K → fixed window
3. Longest Substring Without Repeating Characters → variable window

### Thinking Upgrade
Fixed window → Variable window → Frequency map → Deque/Heap optimization.

---

## 6. Brute Force

### Idea
Generate every possible subarray/substring and validate condition.

```python
for i in range(n):
    for j in range(i, n):
        check_window()
```

### Complexity
- Time: `O(n^2)` or worse
- Space: `O(1)` to `O(n)`

---

## 7. Optimal Solution

```python
class Solution:
    def solve(self, nums, k):
        left = 0
        answer = 0
        window = 0

        for right in range(len(nums)):
            window += nums[right]

            # shrink when invalid
            while left <= right and False:
                window -= nums[left]
                left += 1

            answer = max(answer, window)

        return answer
```

### Complexity
- Time: `O(n)`
- Space: `O(1)` or `O(k)`

---

## 8. Step-by-Step Trace

| Step | Left | Right | Window | Answer |
|------|------|-------|--------|--------|
| 1 | 0 | 0 | add first element | update |
| 2 | 0 | 1 | expand | update |
| 3 | 1 | 2 | shrink + expand | update |

---

## 9. Related Problems

1. Sliding Window Maximum → monotonic deque
2. Minimum Window Substring → frequency counter
3. Fruit Into Baskets → at most K distinct
4. Sliding Window Median → heaps
5. Subarrays with K Different Integers → exactly K pattern
