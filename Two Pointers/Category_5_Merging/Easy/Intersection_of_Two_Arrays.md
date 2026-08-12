# Intersection of Two Arrays (LeetCode 349)

**Pattern:** Hash Set / Two Pointers (if arrays are sorted)

---

# 1. Problem Statement

Given two integer arrays `nums1` and `nums2`, return **an array of their intersection**.

Each element in the result:

* Must be **unique**.
* Can be returned in **any order**.

### Constraints

* `1 <= nums1.length, nums2.length <= 1000`
* `0 <= nums[i] <= 1000`

---

# 2. Diagram

Example:

```text
nums1 = [1,2,2,1]
nums2 = [2,2]

Create Set1

{1,2}

Traverse nums2

2  -> present -> answer = {2}

2  -> already added

Final

[2]
```

Visualization

```text
nums1 Set
+---------+
| 1 | 2   |
+---------+

nums2

2  ✓

2  already taken

Answer

{2}
```

---

# 3. Example I/O

### Example 1

**Input**

```text
nums1 = [1,2,2,1]
nums2 = [2,2]
```

**Output**

```text
[2]
```

Explanation

Only `2` appears in both arrays.

---

### Example 2

**Input**

```text
nums1 = [4,9,5]

nums2 = [9,4,9,8,4]
```

**Output**

```text
[4,9]
```

Explanation

Both `4` and `9` appear in both arrays.

---

### Example 3 (Edge Case)

**Input**

```text
nums1 = [1]

nums2 = [2]
```

**Output**

```text
[]
```

No common element.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Common elements
* Unique elements
* Fast lookup

Think

> **Hash Set**

HashSet provides

```text
Insert : O(1)

Search : O(1)
```

### Interview Thinking

```text
Need common elements.

Duplicates don't matter.

Store one array in a set.

Traverse the other array.

If element exists,

add it to answer set.

Finally return answer.
```

---

# 5. Simpler Version

## Simpler Question 1

### Contains Duplicate (LeetCode 217)

```text
Need fast lookup.

Use HashSet.
```

Introduces the concept of constant-time membership checking.

---

## Simpler Question 2

### Two Sum (LeetCode 1)

```text
Store seen values.

Lookup complement.
```

Further strengthens HashMap/HashSet lookup.

---

## Current Question

Now instead of finding duplicates **within one array**,

find common elements **between two arrays**.

---

### Thinking Progression

```text
HashSet lookup

↓

Contains Duplicate

↓

Two Sum

↓

Common elements

↓

Intersection of Two Arrays
```

---

# 6. Brute Force

Compare every element of `nums1` with every element of `nums2`.

```python
answer = set()

for a in nums1:
    for b in nums2:
        if a == b:
            answer.add(a)

return list(answer)
```

### Complexity

```text
Time : O(m × n)

Space : O(min(m,n))
```

---

# 7. Optimal Solution (Hash Set)

### Idea

* Store all elements of `nums1` in a set.
* Traverse `nums2`.
* If an element exists in the first set, add it to another set (to avoid duplicates).

### Python

```python
class Solution:
    def intersection(self, nums1, nums2):

        seen = set(nums1)
        ans = set()

        for num in nums2:
            if num in seen:
                ans.add(num)

        return list(ans)
```

### Complexity

```text
Time  : O(m+n)

Space : O(m+n)
```

---

## Alternative: Two Pointers (Sorted Arrays)

If sorting is allowed,

1. Sort both arrays.
2. Move two pointers.
3. Skip duplicates.

```python
class Solution:
    def intersection(self, nums1, nums2):

        nums1.sort()
        nums2.sort()

        i = j = 0
        ans = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:

                # Add only unique values
                if not ans or ans[-1] != nums1[i]:
                    ans.append(nums1[i])

                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return ans
```

### Complexity

```text
Time  : O(m log m + n log n)

Space : O(1) (excluding sorting)
```

---

# 8. Step-by-Step Trace

Example

```text
nums1 = [4,9,5]

nums2 = [9,4,9,8,4]
```

Create set

```text
seen = {4,5,9}
```

| Current | In seen?       | Answer |
| ------- | -------------- | ------ |
| 9       | Yes            | {9}    |
| 4       | Yes            | {4,9}  |
| 9       | Already exists | {4,9}  |
| 8       | No             | {4,9}  |
| 4       | Already exists | {4,9}  |

Return

```text
[4,9]
```

---

# 9. Related Problems

| Problem                                | Connection                                                              |
| -------------------------------------- | ----------------------------------------------------------------------- |
| **217. Contains Duplicate**            | Basic HashSet lookup.                                                   |
| **1. Two Sum**                         | Uses HashMap for constant-time lookup.                                  |
| **350. Intersection of Two Arrays II** | Similar problem but duplicates must be preserved using a frequency map. |
| **349. Intersection of Two Arrays**    | Current problem focusing on unique intersection.                        |
| **454. 4Sum II**                       | Uses HashMap to efficiently count combinations across arrays.           |

---

# Key Interview Takeaways

* **Pattern:** Hash Set (Fast Lookup).
* **Data Structure:** One set for membership checking and another set for unique answers.
* **Rule:** Store one array in a set, scan the other array, and collect common elements.
* **Alternative:** If arrays are sorted (or sorting is allowed), solve using the Two Pointers pattern.
* **Complexity:** **O(m+n)** time and **O(m+n)** space with the HashSet approach.
