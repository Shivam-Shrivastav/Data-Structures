
# Minimum Size Subarray Sum

## Pattern
Variable Size Sliding Window

## Problem
Return the minimum length of a contiguous subarray whose sum is at least `target`.

## Diagram
```
Expand ---> until sum >= target

Then

Shrink <--- while condition still holds
```

## Intuition
Grow window until valid.
Once valid, shrink as much as possible while maintaining validity.

## Brute Force
Try every subarray.

Time: O(n²)

## Optimal
```python
class Solution:
    def minSubArrayLen(self, target, nums):
        left=0
        total=0
        ans=float("inf")

        for right,x in enumerate(nums):
            total+=x
            while total>=target:
                ans=min(ans,right-left+1)
                total-=nums[left]
                left+=1
        return 0 if ans==float("inf") else ans
```

Time: O(n)
Space: O(1)

## Related
- Longest Substring Without Repeating Characters
- Minimum Window Substring
