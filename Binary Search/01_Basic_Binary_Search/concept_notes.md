# Basic Binary Search Pattern (Revision)

---

# 1. Pattern in One Minute

### Core Idea

Binary Search repeatedly eliminates **half of the search space** by checking a middle element.

Instead of searching linearly (`O(n)`), it exploits the fact that the search space is **monotonic (ordered)** to achieve **`O(log n)`**.

### Why does this pattern exist?

Whenever the answer lies in a **sorted structure**, or there exists a **true/false boundary**, binary search lets you discard half of the possibilities each iteration.

### Think Binary Search immediately when

* Array is sorted.
* Search space is ordered.
* Need `O(log n)`.
* Looking for first/last occurrence.
* Need insertion position.
* Need boundary where condition changes.

---

# 2. Recognition Signals

### Strong Clues

### Keywords

* sorted array
* ascending/descending
* search
* index
* insert position
* first occurrence
* last occurrence
* lower bound
* upper bound

### Constraints

* `n ≤ 10^5`
* `n ≤ 10^6`
* Expected `O(log n)`

### Problem Characteristics

* Data already sorted
* Can discard half every step
* One unique answer

### Common Disguises

* Search in rotated array (modified BS)
* Peak element
* Find boundary
* Search insert position

---

### Do NOT use when

* Unsorted data
* Need all occurrences (unless first find one occurrence)
* No monotonicity
* Frequent insert/delete (BST/HashMap may be better)

---

# 3. Mental Model

* Imagine a phone book.
* Check the middle.
* If target is smaller → ignore right half.
* If target is larger → ignore left half.
* Keep shrinking until one element remains.
* Every comparison removes **50%**.
* Loop invariant: target can only exist inside `[left, right]`.
* Stop when interval becomes empty.

---

# 4. Boilerplate Template

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

### Complexity

* Time: **O(log n)**
* Space: **O(1)**

---

# 5. Variations

| Variation              | Change                                        |
| ---------------------- | --------------------------------------------- |
| Exact Search           | Return when found                             |
| First Occurrence       | Continue searching left after finding target  |
| Last Occurrence        | Continue searching right after finding target |
| Search Insert Position | Return `left` after loop                      |
| Lower Bound            | First element ≥ target                        |
| Upper Bound            | First element > target                        |
| Descending Array       | Reverse comparisons                           |
| Rotated Array          | Identify sorted half first                    |

---

# 6. Common Pitfalls

### ❌ Overflow in mid

Don't write

```python
mid = (left + right) // 2
```

Prefer

```python
mid = left + (right - left) // 2
```

(important in languages like Java/C++)

---

### ❌ Wrong loop condition

Use

```python
while left <= right
```

for normal binary search.

---

### ❌ Infinite loop

Always move beyond mid

```python
left = mid + 1
right = mid - 1
```

Never

```python
left = mid
right = mid
```

---

### ❌ Forgetting sorted order

Binary Search only works because ordering lets you discard half.

---

# 7. Interview Checklist

✅ Array is sorted

✅ Need fast search (`O(log n)`)

✅ Only one answer exists

✅ Can eliminate half after every comparison

✅ Search space is ordered

➡️ Use **Basic Binary Search**

---

# 8. Must-Do Problems

### ⭐ Top 3 (Enough for Revision)

1. **704. Binary Search** ⭐⭐⭐
2. **35. Search Insert Position** ⭐⭐⭐
3. **744. Find Smallest Letter Greater Than Target** ⭐⭐⭐

### Easy

* 704. Binary Search ⭐
* 35. Search Insert Position ⭐
* 744. Find Smallest Letter Greater Than Target ⭐

### Medium

* 33. Search in Rotated Sorted Array *(modified BS)*
* 81. Search in Rotated Sorted Array II
* 34. Find First and Last Position of Element in Sorted Array *(boundary search)*

### Hard (important)

* 4. Median of Two Sorted Arrays *(advanced binary search on partitions)*

---

# 9. 30-Second Cheat Sheet

### Recognition

* Sorted array
* Search
* `O(log n)`
* First/last position
* Insert position

### Core Idea

Keep eliminating **half** of the search space using the middle element.

### Template

```python
while left <= right:
    mid = left + (right-left)//2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### Complexity

* **Time:** `O(log n)`
* **Space:** `O(1)`

### Common Variations

* Exact search
* First occurrence
* Last occurrence
* Lower bound
* Upper bound
* Insert position
* Descending array
* Rotated array

### Pitfalls

* Wrong loop condition (`<=` vs `<`)
* Infinite loop (`left = mid`)
* Wrong mid calculation
* Applying to unsorted data
