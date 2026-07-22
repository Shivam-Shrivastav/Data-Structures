
# Longest Substring Without Repeating Characters

## Pattern
Variable Size Sliding Window

## Problem
Find the length of the longest substring containing only unique characters.

## Diagram
```
abcabcbb

L     R
abc ✓

duplicate arrives
move L until duplicate removed
```

## Intuition
Expand the window while characters are unique.
If a duplicate appears, shrink from the left until it disappears.

## Brute Force
Check every substring and verify uniqueness.

**Time:** O(n²)

## Optimal
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        ans=0

        for right,ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left+=1
            seen.add(ch)
            ans=max(ans,right-left+1)
        return ans
```

**Time:** O(n)
**Space:** O(min(n,charset))

## Related
- Longest Repeating Character Replacement
- Fruit Into Baskets
- Minimum Window Substring
