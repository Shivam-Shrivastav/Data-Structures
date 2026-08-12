
# Grumpy Bookstore Owner

## Pattern
Fixed Size Sliding Window

## Idea
Customers are always satisfied when owner is not grumpy.

Window = secret technique used for X minutes.

Gain inside window =
sum(customers where grumpy==1)

Maximize this gain.

## Diagram
```
Always satisfied
+

Best gain window
```

## Optimal
```python
class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        base=sum(c for c,g in zip(customers,grumpy) if g==0)
        gain=sum(customers[i] for i in range(minutes) if grumpy[i])

        best=gain
        for i in range(minutes,len(customers)):
            if grumpy[i]:
                gain+=customers[i]
            if grumpy[i-minutes]:
                gain-=customers[i-minutes]
            best=max(best,gain)
        return base+best
```

Time: O(n)
Space: O(1)
