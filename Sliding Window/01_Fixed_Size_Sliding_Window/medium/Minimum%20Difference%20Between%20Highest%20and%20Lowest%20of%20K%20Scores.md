
# Minimum Difference Between Highest and Lowest of K Scores

## Pattern
Sorting + Fixed Window

## Intuition
Sort the scores. Every valid group of k students becomes a contiguous window.

```
sorted = 1 4 7 9 10
         <---k--->
```

Difference = last-first.

## Brute Force
Try every combination.

## Optimal
```python
class Solution:
    def minimumDifference(self, nums, k):
        if k==1:
            return 0
        nums.sort()
        ans=float("inf")
        for i in range(len(nums)-k+1):
            ans=min(ans, nums[i+k-1]-nums[i])
        return ans
```

Time: O(n log n)
Space: O(1)
