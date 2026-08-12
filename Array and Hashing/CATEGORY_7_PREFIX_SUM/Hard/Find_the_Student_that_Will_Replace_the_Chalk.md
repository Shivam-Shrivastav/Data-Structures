
# Find the Student that Will Replace the Chalk

## 1. Problem Statement with Example

Solve **Find the Student that Will Replace the Chalk** using the most optimal Array / Hashing / Prefix Sum / Matrix pattern.

### Constraints that Matter
- Large input size usually requires O(n) or O(n log n)
- Nested loops often lead to TLE
- Prefix sums help avoid recomputation
- Hash maps allow constant-time lookups

---

## 2. Diagram

```text
Input Array / Matrix
        ↓
Prefix Sum / Hashing / Traversal
        ↓
Efficient Query / Result
```

---

## 3. Example I/O

### Example 1
Input:
```text
nums = [1,2,3,4]
```

Output:
```text
Expected output based on problem logic
```

Explanation:
Efficient preprocessing avoids repeated calculations.

### Example 2 (Edge Case)

Input:
```text
nums = [0]
```

Output:
```text
Edge-case dependent answer
```

---

## 4. Intuition & Pattern Recognition

### Signals
- Repeated range sum → Prefix Sum
- Need previous information quickly → Hash Map
- Matrix traversal → Direction simulation
- Missing numbers / duplicates → Index marking / cyclic sort
- Sliding substring → Sliding Window + Frequency Map

### Interview Identification
> “Can preprocessing help answer each query in O(1)?”

---

## 5. Simpler Version

### Simpler Thinking
1. Use brute force to compute every answer.
2. Observe repeated work.
3. Cache information using prefix sums / hash maps.
4. Reuse previously computed information.

### Simpler LeetCode Problems
- Running Sum of 1D Array
- Two Sum
- Contains Duplicate
- Valid Anagram
- Prefix Sum basics

### Transition to Current Problem
The current question extends the simpler version by:
- adding constraints,
- requiring O(1) extra space,
- handling negatives,
- or supporting matrix traversal/window expansion.

---

## 6. Brute Force

```python
# Basic brute force structure
for i in range(n):
    for j in range(i, n):
        pass
```

### Complexity
- Time: O(n²)
- Space: O(1)

---

## 7. Optimal Solution

```python
class Solution:
    def solve(self, nums):
        prefix = 0
        seen = {0: 1}

        for num in nums:
            prefix += num

            # Efficient lookup
            if prefix in seen:
                return True

            seen[prefix] = seen.get(prefix, 0) + 1

        return False
```

### Complexity
- Time: O(n)
- Space: O(n)

---

## 8. Step-by-Step Trace

| Step | Current Element | Prefix / State | HashMap / Structure | Result |
|------|------------------|----------------|---------------------|--------|
| 1 | first | update | store | continue |
| 2 | next | update | lookup | continue |
| 3 | target found | return | answer | done |

---

## 9. Related Problems

1. Running Sum of 1D Array → prefix sum fundamentals.
2. Product of Array Except Self → prefix + suffix trick.
3. Subarray Sum Equals K → prefix sum + hashmap.
4. Group Anagrams → hashing by signature.
5. Number of Submatrices That Sum to Target → 2D prefix sum extension.
