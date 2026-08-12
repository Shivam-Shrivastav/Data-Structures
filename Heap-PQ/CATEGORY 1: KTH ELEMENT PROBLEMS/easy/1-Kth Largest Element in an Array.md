## 215. Kth Largest Element in an Array
**Category:** **HEAP / QUICKSELECT / KTH ELEMENT**

**Problem:** Given an integer array `nums` and an integer `k`, return the **kth largest** element in the array.

**Note:** It is the kth largest element in sorted order, not the kth distinct element.

**Example:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: Sorted descending: [6,5,4,3,2,1], 2nd largest = 5
```

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Explanation: Sorted descending: [6,5,5,4,3,3,2,2,1], 4th largest = 4
```

---

### **Relation to Kth Element Problems**
**Similar to:** **Kth Smallest** and **Top K Frequent** problems
**Key Insight:** 
- Can solve with:
  1. **Min-Heap** of size k
  2. **QuickSelect** (Hoare's selection algorithm)
  3. **Sorting** (simplest but not optimal)

---

### 1. Sorting (Simplest)
```python
def findKthLargest(nums, k):
    return sorted(nums, reverse=True)[k-1]
```
**TC:** O(n log n) | **SC:** O(1) if in-place, O(n) otherwise

---

### 2. Min-Heap (Optimal for streaming)
```python
import heapq

def findKthLargest(nums, k):
    # Min-heap of size k
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]
```
**TC:** O(n log k) | **SC:** O(k)

---

### 3. Max-Heap (Convert to max-heap)
```python
import heapq

def findKthLargest(nums, k):
    # Convert to max-heap by negating values
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    # Pop k-1 largest elements
    for _ in range(k-1):
        heapq.heappop(max_heap)
    
    return -max_heap[0]
```
**TC:** O(n + k log n) | **SC:** O(n)

---

### 4. QuickSelect (Hoare's Selection Algorithm)
```python
import random

def findKthLargest(nums, k):
    # Convert to kth smallest index
    k = len(nums) - k
    
    def quick_select(left, right):
        pivot = nums[random.randint(left, right)]
        l, r = left, right
        
        # Partition: [小于pivot] [pivot] [大于pivot]
        while l <= r:
            while nums[l] < pivot:
                l += 1
            while nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # After partition, left..r < pivot, l..right > pivot
        if k <= r:
            return quick_select(left, r)
        elif k >= l:
            return quick_select(l, right)
        else:
            return nums[k]
    
    return quick_select(0, len(nums)-1)
```
**TC:** O(n) average, O(n²) worst | **SC:** O(log n) recursion

---

### 5. QuickSelect with Index Return (Alternative)
```python
import random

def findKthLargest(nums, k):
    def quick_select(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        # Random pivot
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]
        
        # Move pivot to end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        # Partition
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        
        # Move pivot to final position
        nums[store_idx], nums[right] = nums[right], nums[store_idx]
        
        # pivot is now at store_idx
        if k_smallest == store_idx:
            return nums[store_idx]
        elif k_smallest < store_idx:
            return quick_select(left, store_idx - 1, k_smallest)
        else:
            return quick_select(store_idx + 1, right, k_smallest)
    
    # kth largest = (n-k)th smallest (0-indexed)
    return quick_select(0, len(nums)-1, len(nums)-k)
```
**TC:** O(n) average | **SC:** O(log n) recursion

---

### 6. Counting Sort (When values are in a limited range)
```python
def findKthLargest(nums, k):
    if not nums:
        return -1
    
    min_val, max_val = min(nums), max(nums)
    offset = -min_val
    freq = [0] * (max_val - min_val + 1)
    
    for num in nums:
        freq[num + offset] += 1
    
    count = 0
    for i in range(len(freq)-1, -1, -1):
        count += freq[i]
        if count >= k:
            return i - offset
    
    return -1
```
**TC:** O(n + range) | **SC:** O(range)

---

**Key Insight (Min-Heap):**
- Maintain a min-heap of size k
- Heap stores the k largest elements seen so far
- The smallest among them (heap[0]) is the kth largest

**Key Insight (QuickSelect):**
- Based on QuickSort's partition
- Find kth smallest by partitioning around pivot
- kth largest = (n-k)th smallest

**Example Walkthrough (Min-Heap):**
```
nums = [3,2,1,5,6,4], k=2

heap = []
num=3: heap=[3]
num=2: heap=[2,3]
num=1: heap=[1,2,3] → len>2 → pop → heap=[2,3]
num=5: heap=[2,3,5] → pop → heap=[3,5]
num=6: heap=[3,5,6] → pop → heap=[5,6]
num=4: heap=[4,5,6] → pop → heap=[5,6]

heap[0] = 5
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**Sorting** | O(n log n) | O(1) | Simple | Not optimal for large n |
**Min-Heap** | O(n log k) | O(k) | Good for streaming | k can be large |
**Max-Heap** | O(n + k log n) | O(n) | Simple heap | Extra space |
**QuickSelect** | O(n) avg | O(log n) | Optimal average | O(n²) worst case |
**Counting Sort** | O(n+range) | O(range) | Linear if range small | Range dependent |

**Kth Element Problems Family:**

| Problem | Key Difference |
|---------|---------------|
**215. Kth Largest** | Basic kth largest |
**703. Kth Largest in Stream** | Streaming, maintain heap |
**973. K Closest Points to Origin** | K closest, not largest |
**347. Top K Frequent Elements** | Frequency based |
**378. Kth Smallest in Sorted Matrix** | 2D matrix, binary search |

**Edge Cases:**
- k = 1 → largest element
- k = n → smallest element
- Duplicate values → handled correctly
- Single element → return that element

**When to Use Each:**
- **Sorting:** Quick and simple for small arrays
- **Min-Heap:** Best for streaming or when k is small
- **QuickSelect:** Best for large n when you need optimal average time
- **Counting Sort:** When values are within a small range (e.g., 1-100)