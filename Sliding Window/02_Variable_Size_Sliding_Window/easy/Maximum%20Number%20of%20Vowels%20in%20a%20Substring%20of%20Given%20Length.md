
# Maximum Number of Vowels in a Substring of Given Length

## Pattern
Fixed Size Sliding Window

## Why in Variable Section?
Although the window length is fixed (`k`), it introduces maintaining a dynamic window count while sliding—often taught before harder variable-size problems.

## Idea
Maintain the vowel count in the current window.

When sliding:
- Remove outgoing vowel.
- Add incoming vowel.

Track the maximum.

## Optimal
```python
class Solution:
    def maxVowels(self, s, k):
        vowels=set("aeiou")
        cnt=sum(c in vowels for c in s[:k])
        ans=cnt

        for i in range(k,len(s)):
            if s[i] in vowels:
                cnt+=1
            if s[i-k] in vowels:
                cnt-=1
            ans=max(ans,cnt)
        return ans
```

Time: O(n)

Space: O(1)

## Related
- Maximum Average Subarray I
- Grumpy Bookstore Owner
