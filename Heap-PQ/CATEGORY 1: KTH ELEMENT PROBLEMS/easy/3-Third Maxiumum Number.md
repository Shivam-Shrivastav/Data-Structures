## 414. Third Maximum Number
**Category:** **HEAP / KTH ELEMENT / DISTINCT ELEMENTS**

**Problem:** Given an integer array `nums`, return the **third distinct maximum** number in the array. If the third maximum does not exist, return the **maximum** number.

**Example:**
```
Input: nums = [3,2,1]
Output: 1
Explanation: Third maximum is 1
```

```
Input: nums = [1,2]
Output: 2
Explanation: Third maximum doesn't exist, return maximum (2)
```

```
Input: nums = [2,2,3,1]
Output: 1
Explanation: Distinct numbers: [3,2,1], third maximum is 1
```

---

### **Relation to Kth Largest Element**
**Similar to:** **215. Kth Largest** but with **distinct elements** and **k=3**
**How it's different:**
1. **Kth Largest:** Includes duplicates, k can be any value
2. **Third Maximum:** Only distinct elements, fixed k=3, special case when <3 distinct numbers

**Key Insight:** 
- Need to track **distinct** numbers only
- Maintain **top 3 distinct** elements seen so far
- Use min-heap of size 3 or simple variable tracking

---

### 1. Heap Solution (Min-Heap of size 3)
```python
import heapq

def thirdMax(nums):
    # Min-heap to store top 3 distinct numbers
    heap = []
    
    for num in nums:
        if num not in heap:  # Keep only distinct
            if len(heap) < 3:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heapreplace(heap, num)
    
    # If less than 3 distinct numbers, return max
    if len(heap) < 3:
        return max(heap) if heap else None
    
    return heap[0]  # Third maximum is the smallest in heap
```
**TC:** O(n × 3) = O(n) (heap operations are O(log 3) ≈ O(1)) | **SC:** O(3) = O(1)

---

### 2. Variable Tracking (Most Efficient)
```python
def thirdMax(nums):
    # Use None or -inf to track top 3 distinct
    first = second = third = None
    
    for num in nums:
        # Skip duplicates
        if num == first or num == second or num == third:
            continue
        
        # Update top 3
        if first is None or num > first:
            third = second
            second = first
            first = num
        elif second is None or num > second:
            third = second
            second = num
        elif third is None or num > third:
            third = num
    
    return third if third is not None else first
```
**TC:** O(n) | **SC:** O(1)

---

### 3. Set + Sorting (Simple)
```python
def thirdMax(nums):
    distinct = sorted(set(nums), reverse=True)
    
    if len(distinct) >= 3:
        return distinct[2]
    return distinct[0]
```
**TC:** O(n log n) | **SC:** O(n)

---

### 4. Set + Heap
```python
import heapq

def thirdMax(nums):
    distinct = list(set(nums))
    
    if len(distinct) < 3:
        return max(distinct)
    
    # Min-heap of size 3
    heap = distinct[:3]
    heapq.heapify(heap)
    
    for num in distinct[3:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]
```
**TC:** O(n) | **SC:** O(n)

---

### 5. Without Heap (Using -inf)
```python
def thirdMax(nums):
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')
    
    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif first > num > second:
            third = second
            second = num
        elif second > num > third:
            third = num
    
    return third if third != float('-inf') else first
```
**TC:** O(n) | **SC:** O(1)

---

**Key Insight (Variable Tracking):**
- Maintain `first`, `second`, `third` for top 3 distinct numbers
- Update order carefully when a new number arrives
- Skip duplicates by comparing with all three

**Example Walkthrough (Variable Tracking):**
```
nums = [2,2,3,1]

Initialize: first=None, second=None, third=None

num=2:
  first=2, second=None, third=None

num=2 (duplicate): skip

num=3:
  3 > first(2) → third=second(None), second=first(2), first=3
  Now: first=3, second=2, third=None

num=1:
  1 < second(2) but > third(None) → third=1
  Now: first=3, second=2, third=1

Result = third = 1
```

**Another Example:**
```
nums = [1,2]

first=1, second=None, third=None

num=2:
  2 > first(1) → third=second(None), second=first(1), first=2
  Now: first=2, second=1, third=None

Result: third is None → return first=2
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**Variable Tracking** | O(n) | O(1) | Most efficient, single pass | Manual update logic |
**Min-Heap (set)** | O(n) | O(1) | Clean, uses heap | Extra set conversion |
**Set + Sort** | O(n log n) | O(n) | Simple | Not optimal |
**Heap with distinct check** | O(n) | O(1) | Good for k=3 | Duplicate check O(3) |

**Kth Element Family:**

| Problem | Key Difference |
|---------|---------------|
**215. Kth Largest** | k can be any, includes duplicates |
**703. Kth Largest in Stream** | Streaming, min-heap of size k |
**414. Third Maximum** | k=3, distinct only, special case |
**378. Kth Smallest in Sorted Matrix** | 2D matrix, binary search |

**Edge Cases:**
- Less than 3 distinct numbers → return maximum
- All duplicates → return that number
- Negative numbers → works with comparison
- Very large numbers → fine with Python ints

**Why Variable Tracking is Best:**
- Only one pass through array
- No extra data structures
- Handles duplicates naturally
- O(1) space, O(n) time
- Simple to understand

**Common Pitfalls:**
- Forgetting to handle duplicates correctly
- Not updating in the right order (when num > first, shift first→second→third)
- Not handling the case when third doesn't exist