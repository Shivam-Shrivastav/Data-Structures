# Fruit Into Baskets

## Pattern
Variable Size Sliding Window + HashMap

Maintain a window containing at most **2 distinct fruits**.

```python
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        freq=defaultdict(int)
        left=ans=0
        for right,x in enumerate(fruits):
            freq[x]+=1
            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans
```

Time: O(n)
Space: O(1)
