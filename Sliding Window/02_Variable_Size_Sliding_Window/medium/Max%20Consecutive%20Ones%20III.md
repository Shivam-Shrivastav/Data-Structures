# Max Consecutive Ones III

## Pattern
Variable Size Sliding Window

Keep at most **k zeros** inside the window. Expand right, shrink left whenever zeros exceed k.

```python
class Solution:
    def longestOnes(self, nums, k):
        left=zeros=0
        for right,x in enumerate(nums):
            if x==0: zeros+=1
            while zeros>k:
                if nums[left]==0: zeros-=1
                left+=1
        return right-left+1
```

Time: O(n)
Space: O(1)
