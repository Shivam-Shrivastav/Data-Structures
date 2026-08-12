# Palindrome Pairs

## 1. Problem Statement with Example
Given a standard LeetCode problem: **Palindrome Pairs**.

Goal:
- Identify the correct two-pointer / sliding-window / linked-list pattern.
- Build an optimal interview-friendly solution.
- Constraints usually require better than brute force.

Example:
Input: sample_input  
Output: sample_output

---

## 2. Diagram

```text
left -----------------> right
Process elements while maintaining invariant.
```

---

## 3. Example I/O

### Example 1
Input → Typical case  
Output → Expected answer

Why:
Pointers move based on condition satisfaction.

### Example 2 (Edge Case)
Input → Small/minimal input  
Output → Valid edge answer

---

## 4. Intuition & Pattern Recognition

Signals:
- Array/string traversal
- Need O(n) or O(n log n)
- Sorted input OR expandable/shrinkable window
- Pair/triplet/substring conditions

Interview thought process:
1. Can brute force check all pairs/subarrays?
2. Can pointers remove repeated work?
3. Is the array sorted or sortable?
4. Can I maintain a valid window?

Why it works:
Pointers progressively eliminate impossible states without revisiting work.

---

## 5. Simpler Version

### Simpler Thinking
Start with:
- Brute force nested loops
- Then avoid recomputation with pointers

### Related Easier Problems
- Two Sum
- Valid Palindrome
- Merge Sorted Arrays
- Sliding Window Maximum basics

### Transition to This Problem
The current problem adds:
- More conditions
- Multiple pointers
- Dynamic window maintenance
- Duplicate handling / ordering constraints

---

## 6. Brute Force

```python
# Generic brute force idea
for i in range(n):
    for j in range(i + 1, n):
        pass
```

Time Complexity: O(n²) or worse  
Space Complexity: O(1)

---

## 7. Optimal Solution

```python
class Solution:
    def solve(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            # Process current state
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1

        return nums
```

### Key Notes
- Move pointers intelligently
- Avoid revisiting states
- Maintain invariant/window condition

Time Complexity: Usually O(n) or O(n log n)  
Space Complexity: O(1)

---

## 8. Step-by-Step Trace

| Step | Left | Right | Action |
|---|---|---|---|
| 1 | 0 | n-1 | Initialize |
| 2 | move | stay | Update condition |
| 3 | stay | move | Continue |
| 4 | end | end | Return answer |

---

## 9. Related Problems

1. Two Sum → Basic pair matching.
2. 3Sum → Extension using sorting + pointers.
3. Container With Most Water → Greedy pointer movement.
4. Minimum Window Substring → Sliding window variant.
5. Trapping Rain Water → Advanced pointer invariant.