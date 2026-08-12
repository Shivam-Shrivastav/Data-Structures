
# First Missing Positive

## 1. Problem Statement with Example
Given the problem **First Missing Positive**, solve it efficiently using the most suitable Array/Hashing pattern.

**Typical Constraints**
- Need better than brute force in most interview settings.
- Use hash maps/sets/two pointers/prefix sums depending on pattern.
- Aim for O(n) or O(n log n).

---

## 2. Diagram

```text
Input  -> Process using pattern -> Output
Array  -> HashMap/Set/Pointer   -> Answer
```

---

## 3. Example I/O

### Example 1
Input:
```text
nums = [1,2,3]
```

Output:
```text
Valid expected output based on problem logic
```

### Example 2 (Edge Case)
Input:
```text
[]
```

Output:
```text
Edge-case dependent answer
```

---

## 4. Intuition & Pattern Recognition

### Signals
- Arrays + lookup → Hash Map / Hash Set
- Pair finding → Two Sum style
- Continuous range → Sliding Window / Prefix Sum
- Frequency counting → Dictionary / Counter

### Interview Thought Process
> “Can I trade space for faster lookup?”

---

## 5. Simpler Version

### Simpler Thinking
1. Solve using nested loops.
2. Observe repeated lookups.
3. Store information in a hash map/set.
4. Reduce repeated work.

### Related Simpler Problems
- Two Sum
- Contains Duplicate
- Valid Anagram
- Prefix Sum basics

### Transition to Current Problem
The current problem extends the simpler idea by adding:
- ordering constraints,
- window constraints,
- frequency constraints,
- or matrix traversal logic.

---

## 6. Brute Force

```python
# Naive approach
for i in range(n):
    for j in range(i + 1, n):
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
        seen = set()

        for num in nums:
            # Fast lookup using hashing
            if num in seen:
                return True

            seen.add(num)

        return False
```

### Complexity
- Time: O(n)
- Space: O(n)

---

## 8. Step-by-Step Trace

| Step | Current Value | Data Structure | Result |
|------|----------------|----------------|--------|
| 1 | first element | add to set/map | continue |
| 2 | next element | lookup | update |
| 3 | repeated/final state | answer found | return |

---

## 9. Related Problems

1. Two Sum → hash map lookup.
2. Contains Duplicate → hash set existence check.
3. Group Anagrams → frequency grouping.
4. Longest Substring Without Repeating Characters → sliding window + hash map.
5. Minimum Window Substring → advanced variable window.

