## 703. Kth Largest Element in a Stream
**Category:** **HEAP / STREAM PROCESSING / KTH ELEMENT**

**Problem:** Design a class to find the **kth largest** element in a stream of numbers. The class should have:
- `KthLargest(k, nums)`: Initializes the object with integer `k` and an initial array `nums`
- `add(val)`: Appends `val` to the stream and returns the kth largest element

**Example:**
```
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4,5,8,2]], [3], [5], [10], [9], [4]]

Output:
[null, 4, 5, 5, 8, 8]

Explanation:
KthLargest(3, [4,5,8,2]) -> stream = [4,5,8,2]
add(3) -> stream = [4,5,8,2,3], sorted = [8,5,4,3,2] -> 3rd largest = 4
add(5) -> stream = [4,5,8,2,3,5], sorted = [8,5,5,4,3,2] -> 3rd largest = 5
add(10) -> stream = [...,10], sorted = [10,8,5,5,4,3,2] -> 3rd largest = 5
add(9) -> sorted = [10,9,8,5,5,4,3,2] -> 3rd largest = 8
add(4) -> sorted = [10,9,8,5,5,4,4,3,2] -> 3rd largest = 8
```

---

### **Relation to Kth Largest in Array**
**Similar to:** **215. Kth Largest Element** but **streaming** (continuous input)
**How it's different:**
1. **Static Array:** One-time computation
2. **Stream:** Need to handle `add()` efficiently (O(log k) per add)

**Key Insight:** 
- Maintain a **min-heap of size k** containing the k largest elements
- The smallest in that heap (root) is the kth largest
- When adding a new value, if it's larger than the smallest in heap, replace it

---

### 1. Min-Heap Implementation (Optimal)
```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # pop then push
        
        return self.heap[0]
```
**TC:** 
- `__init__`: O(n log n) or O(n + k log n) with heapify
- `add`: O(log k)
**SC:** O(k)

---

### 2. Max-Heap Implementation (Alternative)
```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        # Max-heap using negative values
        self.heap = []
        
        for num in nums:
            heapq.heappush(self.heap, -num)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        
        # Keep only k largest
        temp = []
        for _ in range(self.k):
            temp.append(-heapq.heappop(self.heap))
        
        # Restore heap
        for num in temp:
            heapq.heappush(self.heap, -num)
        
        return temp[-1]
```
**TC:** O(k log n) per add (inefficient) | **SC:** O(n)

---

### 3. Sorted List (Binary Search Insert)
```python
import bisect

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)
    
    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]
```
**TC:** 
- `__init__`: O(n log n)
- `add`: O(n) (insert shift)
**SC:** O(n)

---

### 4. With Counter for Duplicates (when k is large)
```python
from collections import Counter
import bisect

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)
    
    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]
```
(Similar to above, just more explicit)

---

### 5. Using heapq.nlargest (Less Efficient)
```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        return heapq.nlargest(self.k, self.nums)[-1]
```
**TC:** O(n log k) per add | **SC:** O(n)

---

**Key Insight (Min-Heap):**
- The heap always contains the **k largest** elements seen so far
- Heap root = minimum among k largest = kth largest
- When new element arrives:
  - If heap not full → push
  - If heap full and new element > heap root → replace root
  - Otherwise → ignore (not in top k)

**Example Walkthrough:**
```
k=3, initial nums=[4,5,8,2]

Heap after init: [4,5,8] (min-heap, root=4)

add(3):
  heap=[4,5,8], 3 < 4 → ignore
  heap remains [4,5,8]
  return 4

add(5):
  heap=[4,5,8], 5 > 4 → heapreplace → heap=[5,5,8]
  return 5

add(10):
  heap=[5,5,8], 10 > 5 → heapreplace → heap=[5,8,10]
  return 5

add(9):
  heap=[5,8,10], 9 > 5 → heapreplace → heap=[8,9,10]
  return 8

add(4):
  heap=[8,9,10], 4 > 8? No → ignore
  return 8
```

**Heap State Visualization:**
```
Initial:    [4,5,8]     → 4
add(3):     [4,5,8]     → 4
add(5):     [5,5,8]     → 5
add(10):    [5,8,10]    → 5
add(9):     [8,9,10]    → 8
add(4):     [8,9,10]    → 8
```

**Comparison Table:**

| Approach | Init Time | Add Time | Space | Pros | Cons |
|----------|-----------|----------|-------|------|------|
**Min-Heap** | O(n log k) | O(log k) | O(k) | Optimal, streaming | None |
**Sorted List** | O(n log n) | O(n) | O(n) | Simple | Slow adds |
**Max-Heap** | O(n) | O(k log n) | O(n) | Straightforward | Inefficient |
**nlargest** | O(1) | O(n log k) | O(n) | Easy | Slow adds |

**Stream Processing Family:**

| Problem | Key Difference |
|---------|---------------|
**703. Kth Largest in Stream** | Basic streaming, min-heap of size k |
**295. Find Median from Data Stream** | Median (two heaps) |
**480. Sliding Window Median** | Sliding window + median |
**1046. Last Stone Weight** | Max-heap for processing |
**23. Merge k Sorted Lists** | Min-heap for merging |

**Edge Cases:**
- k = 1 → keep largest element only (max-heap would work too)
- k = n → keep all elements (min-heap of size n)
- Initial array smaller than k → will fill up with adds
- Duplicate values → handled correctly

**Why Min-Heap Works:**
- To find kth largest, we only care about the k largest elements
- The smallest among these k is the kth largest
- Min-heap gives us O(1) access to the smallest element
- Heap size remains k, so space is bounded

**Common Pitfalls:**
- Forgetting to handle case when heap size < k
- Using max-heap incorrectly (needs negative values)
- Not using `heapreplace` (pop+push is less efficient)