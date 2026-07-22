
# Check If a String Contains All Binary Codes of Size K

## Pattern
Fixed Size Sliding Window + Hash Set

## Problem
Given a binary string `s` and integer `k`, determine whether every possible binary code of length `k` appears as a substring.

## Diagram
```
s = 00110110, k=2

00 ✓
01 ✓
11 ✓
10 ✓
```

## Intuition
Slide a window of size `k` across the string and store each substring in a set.
If the set size becomes `2^k`, every code exists.

## Brute Force
Generate all `2^k` strings and search each one.

Time: O(2^k * n)

## Optimal
```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(len(s)-k+1):
            seen.add(s[i:i+k])
        return len(seen) == (1<<k)
```

Time: O(nk)
Space: O(2^k)

## Related
- Repeated DNA Sequences
- Find All Anagrams in a String
