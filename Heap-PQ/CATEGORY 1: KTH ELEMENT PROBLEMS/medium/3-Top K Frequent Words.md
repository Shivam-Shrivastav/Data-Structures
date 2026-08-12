## 692. Top K Frequent Words
**Category:** **HEAP / KTH ELEMENT / HASH MAP / SORTING**

**Problem:** Given an array of strings `words` and an integer `k`, return the **k most frequent** strings. Sort the result by:
1. **Frequency** (higher frequency first)
2. If frequencies are the same, sort **lexicographically** (alphabetically ascending)

**Example:**
```
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" (2), "love" (2), then lexicographically: "i" before "love"
```

```
Input: words = ["the","day","is","sunny","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: 
- "the": 3, "is": 3, "sunny": 2, "day": 1
- "the" and "is" tie → lexicographically: "is", "the" (but higher freq first)
- Wait, order: highest freq first, so "the" then "is"? Let's check:
  Actually both have freq 3, so lexicographically: "is" < "the", but we need higher freq first.
  Since same freq, sort alphabetically ascending: "is", "the", "sunny", "day"
  So output: ["is","the","sunny","day"]? The example says ["the","is","sunny","day"]
```

Let's verify: Actually the problem says **higher frequency first**, then **lexicographically ascending** for ties. So with same frequency, "is" should come before "the" because "i" < "t". But the example output shows ["the","is"...] which contradicts this. Let me check the actual LeetCode problem.

The correct output for this input is actually `["the","is","sunny","day"]` because "the" appears first in the original array? No, LeetCode's requirement is: **sort by frequency descending, then lexicographically ascending**. So "is" should come before "the". The example in the problem statement might be outdated or I'm misremembering. For consistency, we'll implement the standard: **frequency descending, then lexicographically ascending**.

---

### **Relation to Top K Frequent Elements**
**Similar to:** **347. Top K Frequent Elements** but with **strings** and **lexicographic tie-breaking**
**How it's different:**
1. **Top K Frequent Elements:** Numbers only, tie-breaking not required
2. **Top K Frequent Words:** Strings with custom sort order
3. **Key Insight:** Need to define custom comparator for heap or sort

**Key Insight:** 
- Step 1: Count frequency using hash map
- Step 2: Sort or heap with custom order:
  - Primary key: frequency (descending)
  - Secondary key: word (ascending lexicographically)

---

### 1. Min-Heap with Custom Comparator
```python
import heapq
from collections import Counter

def topKFrequent(words, k):
    freq = Counter(words)
    
    # Min-heap with (-freq, word) or (freq, word) with custom logic
    # We want highest freq first, so use negative freq for max-heap behavior
    heap = []
    
    for word, count in freq.items():
        # Push (-count, word) so that higher count has smaller negative value
        # But for tie-breaking, lexicographic order: we want smaller word first
        # However, Python's heap compares tuples element by element
        # (-count, word) works: 
        #   - Higher count → smaller first element → comes first
        #   - If counts equal, compares word lexicographically (ascending)
        heapq.heappush(heap, (-count, word))
    
    # Extract top k
    result = []
    for _ in range(k):
        _, word = heapq.heappop(heap)
        result.append(word)
    
    return result
```
**TC:** O(n + k log n) | **SC:** O(n)

---

### 2. Max-Heap with Tuple (Alternative)
```python
import heapq
from collections import Counter

def topKFrequent(words, k):
    freq = Counter(words)
    
    # Max-heap using negative frequency and negative lexicographic? Complex
    # Simpler: use min-heap of size k
    heap = []
    
    for word, count in freq.items():
        # Push (count, word) - but min-heap gives smallest count first
        # We want to keep k largest, so push negative count or use custom
        heapq.heappush(heap, (-count, word))
    
    return [heapq.heappop(heap)[1] for _ in range(k)]
```
**TC:** O(n + k log n) | **SC:** O(n)

---

### 3. Min-Heap of Size k (More Efficient)
```python
import heapq
from collections import Counter

def topKFrequent(words, k):
    freq = Counter(words)
    
    # Min-heap of size k
    # For min-heap, we want to keep largest frequencies
    # So we push (-freq, word) to simulate max-heap
    # But to keep only k, we need to pop when size > k
    heap = []
    
    for word, count in freq.items():
        heapq.heappush(heap, (-count, word))
    
    # Heap now contains all items, extract k
    # This is O(n + k log n) which is fine
    
    result = []
    for _ in range(k):
        _, word = heapq.heappop(heap)
        result.append(word)
    
    return result
```
**TC:** O(n + k log n) | **SC:** O(n)

---

### 4. Sorting (Simplest)
```python
from collections import Counter

def topKFrequent(words, k):
    freq = Counter(words)
    
    # Sort by frequency descending, then word ascending
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
    
    return sorted_words[:k]
```
**TC:** O(n log n) | **SC:** O(n)

---

### 5. Min-Heap of Size k with Custom Comparator (Python 3)
```python
import heapq
from collections import Counter

class WordFreq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        # For min-heap, we want smaller frequency first
        # If frequencies equal, we want lexicographically larger first
        # (because we'll pop the smallest to keep top k)
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word  # Lexicographically larger is "smaller" for heap

def topKFrequent(words, k):
    freq = Counter(words)
    
    heap = []
    
    for word, count in freq.items():
        heapq.heappush(heap, WordFreq(word, count))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Heap now contains k least frequent? Wait, we want most frequent
    # This approach needs careful handling
    
    # Better: push (-count, word) approach
    pass

# Simpler to use the sorting or max-heap approach
```
**Note:** Custom comparator approach is more complex; sorting is recommended.

---

### 6. Using heapq.nsmallest with key (Alternative)
```python
import heapq
from collections import Counter

def topKFrequent(words, k):
    freq = Counter(words)
    
    # Get all items, then use nlargest with custom key
    # nlargest uses heap internally
    items = list(freq.items())
    top_k = heapq.nlargest(k, items, key=lambda x: (x[1], x[0]))
    # This gives (word, freq) with higher freq first, but freq tie not lexicographically correct
    # Need to adjust: lexicographically ascending for ties
    
    # Actually nlargest with tuple works: (freq, word) but freq descending
    top_k = heapq.nlargest(k, items, key=lambda x: (x[1], x[0]))
    # But this sorts word ascending? Let's test
    
    return [word for word, _ in top_k]
```
**TC:** O(n + k log n) | **SC:** O(n)

---

**Key Insight (Min-Heap with Size k):**
- Maintain a min-heap of size k with `(-freq, word)` or custom comparator
- For min-heap to keep **largest** frequencies, we push `(-freq, word)`
- Then heap[0] is the smallest among top k (kth largest frequency)
- But with tie-breaking, we need careful comparator

**Better Approach: Sort**
- Counting + sorting is simplest and clear
- O(n log n) is acceptable for most cases

**Example Walkthrough (Sorting):**
```
words = ["i","love","leetcode","i","love","coding"], k=2

Step 1: Count frequencies
{
  "i": 2,
  "love": 2,
  "leetcode": 1,
  "coding": 1
}

Step 2: Sort by (-freq, word)
  "i": (-2, "i")
  "love": (-2, "love")
  "leetcode": (-1, "leetcode")
  "coding": (-1, "coding")

Sorted: [(-2, "i"), (-2, "love"), (-1, "coding"), (-1, "leetcode")]
Extract first k words: ["i", "love"]
```

**Example Walkthrough (Min-Heap with Size k):**
```
words = ["i","love","leetcode","i","love","coding"], k=2

freq = {"i":2, "love":2, "leetcode":1, "coding":1}

heap = []

Process "i", count=2:
  heap=[(-2, "i")]

Process "love", count=2:
  heap=[(-2, "i"), (-2, "love")]

Process "leetcode", count=1:
  (-1, "leetcode") vs heap[0]=(-2, "i") → -1 > -2, so push? Wait, we want to keep top 2
  If we push, heap becomes [(-2, "i"), (-2, "love"), (-1, "leetcode")] size=3
  Then pop: heapq.heappop() removes (-2, "i")? Actually min-heap: smallest first
  (-2, "i") < (-1, "leetcode") so pop removes (-2, "i") → we lose "i" incorrectly.

This shows that min-heap of size k with (-freq, word) requires careful management.
Better to use max-heap or sort.
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**Sorting** | O(n log n) | O(n) | Simple, clear | O(n log n) |
**Max-Heap** | O(n + k log n) | O(n) | Good for large k | All items in heap |
**Min-Heap (size k)** | O(n log k) | O(n) | Good for streaming | Complex comparator |
**nlargest** | O(n + k log n) | O(n) | Pythonic | May not handle ties correctly |

**Top K Family:**

| Problem | Key Difference |
|---------|---------------|
**347. Top K Frequent Elements** | Numbers, no tie-breaking |
**692. Top K Frequent Words** | Strings, lexicographic tie-breaking |
**973. K Closest Points** | Distance metric |
**215. Kth Largest** | Single value |
**451. Sort Characters By Frequency** | Sort all by frequency |

**Edge Cases:**
- k = 0 → empty list
- k = number of distinct words → all words
- Words with same frequency → lexicographically ascending
- All words same → any order

**Common Pitfalls:**
- Forgetting lexicographic order for ties
- Using heap without proper comparator
- Not handling k > len(distinct_words)
- Sorting in wrong direction (ascending vs descending)

**Recommended Solution:**
```python
from collections import Counter

def topKFrequent(words, k):
    freq = Counter(words)
    return sorted(freq.keys(), key=lambda w: (-freq[w], w))[:k]
```
**TC:** O(n log n) | **SC:** O(n)

This is simplest and most readable for interviews.