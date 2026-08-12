
# Find Duplicate File in System

## 1. Problem Statement with Example

Solve **Find Duplicate File in System** using the best Array / Hashing / Heap / Sorting / Traversal strategy.

### Important Constraints
- Large datasets require efficient lookups.
- Heap/Bucket Sort may be needed for frequency ranking.
- In-place rearrangement often reduces extra space.
- Traversal problems require careful boundary handling.

---

## 2. Diagram

```text
Input
  ↓
Hashing / Heap / Traversal / Sorting
  ↓
Efficient Rearrangement or Query
  ↓
Output
```

---

## 3. Example I/O

### Example 1
Input:
```text
nums = [1,1,1,2,2,3]
k = 2
```

Output:
```text
[1,2]
```

Explanation:
Frequency-based processing identifies the most common elements.

### Example 2 (Edge Case)

Input:
```text
nums = [1]
```

Output:
```text
[1]
```

---

## 4. Intuition & Pattern Recognition

### Signals
- Need top frequencies → Heap / Bucket Sort
- Rearrangement in-place → Cyclic swaps / reverse operations
- Matrix traversal → Direction vectors + boundaries
- Consecutive elements → Hash Set sequence expansion
- Encoding/Decoding → Delimiter-based parsing or hashing

### Interview Thought Process
> “Can hashing reduce repeated searching to O(1)?”

---

## 5. Simpler Version

### Simpler Thinking
1. Solve using sorting or brute force.
2. Notice repeated scans.
3. Store frequencies/indices in hash maps.
4. Optimize traversal or extraction.

### Simpler LeetCode Problems
- Contains Duplicate
- Two Sum
- Running Sum
- Valid Anagram
- Rotate Array basics

### Transition to Current Problem
The current problem extends the simpler pattern by:
- requiring top-k extraction,
- handling matrices,
- encoding strings,
- or enforcing in-place operations.

---

## 6. Brute Force

```python
# Brute force idea
for i in range(n):
    for j in range(n):
        pass
```

### Complexity
- Time: O(n²)
- Space: O(1)

---

## 7. Optimal Solution

```python
from collections import Counter
import heapq

class Solution:
    def solve(self, nums, k):
        freq = Counter(nums)

        # Extract top k efficiently
        return heapq.nlargest(k, freq.keys(), key=freq.get)
```

### Complexity
- Time: O(n log k)
- Space: O(n)

---

## 8. Step-by-Step Trace

| Step | Current State | Data Structure | Action |
|------|----------------|----------------|--------|
| 1 | Read element | HashMap | count |
| 2 | Build frequency | Heap/Bucket | organize |
| 3 | Extract answer | Result list | return |

---

## 9. Related Problems

1. Top K Frequent Elements → heap + hashmap basics.
2. K Closest Points to Origin → top-k heap pattern.
3. Spiral Matrix → boundary traversal.
4. Longest Consecutive Sequence → hash set optimization.
5. Encode and Decode TinyURL → hashing for mapping systems.
