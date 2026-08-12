## 347. Top K Frequent Elements
**Category:** **HEAP / KTH ELEMENT / HASH MAP**

**Problem:** Given an integer array `nums` and an integer `k`, return the **k most frequent** elements. You may return the answer in **any order**.

**Example:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time
```

```
Input: nums = [1], k = 1
Output: [1]
```

---

### **Relation to Kth Element Problems**
**Similar to:** **215. Kth Largest** but with **frequency** instead of value
**How it's different:**
1. **Kth Largest:** Compare element values directly
2. **Top K Frequent:** Need to count frequencies first, then find k largest frequencies
3. **Key Insight:** Problem reduces to "k largest" on frequencies

**Key Insight:** 
- Step 1: Count frequency of each element using hash map
- Step 2: Find top k elements by frequency
- Can use heap, bucket sort, or quickselect

---

### 1. Min-Heap (Optimal for k small)
```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    # Count frequencies
    freq = Counter(nums)
    
    # Min-heap of size k storing (frequency, element)
    heap = []
    
    for num, count in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, num))
        elif count > heap[0][0]:
            heapq.heapreplace(heap, (count, num))
    
    return [num for _, num in heap]
```
**TC:** O(n log k) | **SC:** O(n)

---

### 2. Max-Heap (Simpler but O(n log n))
```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    
    # Max-heap using negative frequencies
    heap = [(-count, num) for num, count in freq.items()]
    heapq.heapify(heap)
    
    # Extract k largest
    return [heapq.heappop(heap)[1] for _ in range(k)]
```
**TC:** O(n + k log n) | **SC:** O(n)

---

### 3. Bucket Sort (Optimal O(n))
```python
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    
    # Bucket: index = frequency, value = list of elements with that frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, count in freq.items():
        buckets[count].append(num)
    
    # Collect top k from highest frequencies
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result
```
**TC:** O(n) | **SC:** O(n)

---

### 4. QuickSelect (Hoare's Selection Algorithm)
```python
import random
from collections import Counter

def topKFrequent(nums, k):
    freq = list(Counter(nums).items())  # [(num, count), ...]
    
    def quick_select(left, right, k_smallest):
        if left == right:
            return
        
        # Random pivot
        pivot_idx = random.randint(left, right)
        pivot_freq = freq[pivot_idx][1]
        
        # Move pivot to end
        freq[pivot_idx], freq[right] = freq[right], freq[pivot_idx]
        
        # Partition: [< pivot] [pivot] [>= pivot]
        store_idx = left
        for i in range(left, right):
            if freq[i][1] < pivot_freq:
                freq[store_idx], freq[i] = freq[i], freq[store_idx]
                store_idx += 1
        
        # Move pivot to final position
        freq[store_idx], freq[right] = freq[right], freq[store_idx]
        
        # pivot is now at store_idx (kth smallest frequency)
        if k_smallest < store_idx:
            quick_select(left, store_idx - 1, k_smallest)
        elif k_smallest > store_idx:
            quick_select(store_idx + 1, right, k_smallest)
    
    n = len(freq)
    # We want k largest = (n-k)th smallest (0-indexed)
    quick_select(0, n - 1, n - k)
    
    return [num for num, _ in freq[n - k:]]
```
**TC:** O(n) average, O(n²) worst | **SC:** O(n)

---

### 5. Using heapq.nlargest (Pythonic)
```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
```
**TC:** O(n log k) | **SC:** O(n)

---

**Key Insight (Min-Heap):**
- Maintain a min-heap of size k containing the **k most frequent** elements seen so far
- Heap root = smallest frequency among top k = kth most frequent frequency
- When new element has higher frequency, replace the root

**Key Insight (Bucket Sort):**
- Create array where index = frequency
- Each bucket stores elements with that frequency
- Since frequency ≤ n, we can use direct indexing
- Collect from highest frequency downward

**Example Walkthrough (Bucket Sort):**
```
nums = [1,1,1,2,2,3], k=2

Step 1: Count frequencies
1:3, 2:2, 3:1

Step 2: Create buckets (size = n+1 = 7)
index: 0  1  2  3  4  5  6
       [] [] [] [] [] [] []

Step 3: Fill buckets
freq=3 → buckets[3] = [1]
freq=2 → buckets[2] = [2]
freq=1 → buckets[1] = [3]

buckets = [[], [3], [2], [1], [], [], []]

Step 4: Collect from highest frequency
i=6: []
i=5: []
i=4: []
i=3: [1] → result=[1], len=1
i=2: [2] → result=[1,2], len=2 → return [1,2]
```

**Example Walkthrough (Min-Heap):**
```
nums = [1,1,1,2,2,3], k=2
freq = {1:3, 2:2, 3:1}

heap = []

Process (1,3): heap=[(3,1)]
Process (2,2): heap=[(2,2), (3,1)] (min-heap, root=2)
Process (3,1): count=1 < heap[0][0]=2 → skip

Result: [2,1] (order may vary)
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**Min-Heap** | O(n log k) | O(n) | Good for k small | Not O(n) |
**Max-Heap** | O(n log n) | O(n) | Simple | O(n log n) |
**Bucket Sort** | O(n) | O(n) | Optimal time | Large memory if n large |
**QuickSelect** | O(n) avg | O(n) | Optimal average | O(n²) worst |
**nlargest** | O(n log k) | O(n) | Pythonic | Library dependent |

**Top K Family:**

| Problem | Key Difference |
|---------|---------------|
**347. Top K Frequent Elements** | Based on frequency |
**215. Kth Largest** | Based on value |
**973. K Closest Points** | Based on distance |
**692. Top K Frequent Words** | Frequency + lexicographic order |
**451. Sort Characters By Frequency** | Sort all by frequency |

**Edge Cases:**
- k = 0 → empty list
- k = number of distinct elements → all elements
- All elements same frequency → any order
- Single element → [element]

**Why Bucket Sort is Optimal:**
- Frequency is bounded by array length n
- Can use array indexing instead of comparison
- O(n) time, O(n) space
- Best when n is large and frequencies vary

**Space-Time Tradeoff:**
- **Min-Heap:** O(n log k) time, O(n) space - good for streaming
- **Bucket Sort:** O(n) time, O(n) space - optimal for static array
- **QuickSelect:** O(n) average - good when k is large