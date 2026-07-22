# **Substring with Concatenation of All Words (LeetCode 30)**

**Pattern:** Variable Size Sliding Window + HashMap + Fixed-Length Chunks

---

# 1. Problem Statement

You are given:

* A string `s`
* An array of strings `words`

Every word has the **same length**.

Return **all starting indices** of substrings in `s` that are a concatenation of every word in `words` **exactly once**, in any order, **without any extra characters**.

The words may repeat.

---

### Constraints

* `1 <= s.length <= 10^4`
* `1 <= words.length <= 5000`
* `1 <= words[i].length <= 30`
* All words have the **same length**
* Need better than checking every permutation.

---

# 2. Diagram

Example:

```text
s = "barfoothefoobarman"

words = ["foo","bar"]

wordLen = 3
windowLen = 6

Chunks of size 3

bar | foo | the | foo | bar | man
^^^^^^
bar + foo ✓

          foo | bar
          ^^^^^^
          foo + bar ✓

Answer = [0,9]
```

---

### Why process in chunks?

Instead of moving one character at a time,

```text
b a r f o o ...
```

we move by **word length**

```text
bar | foo | the | foo | bar
```

because every valid word starts on these boundaries.

---

# 3. Example I/O

### Example 1

```text
Input:
s = "barfoothefoobarman"

words = ["foo","bar"]

Output:
[0,9]
```

Explanation

```text
Index 0:
barfoo

Index 9:
foobar
```

---

### Example 2

```text
Input:
s = "wordgoodgoodgoodbestword"

words =
["word","good","best","word"]

Output:
[]
```

Need two "word"s, but only one fits in any valid window.

---

### Example 3 (Repeated Words)

```text
Input:
s = "barfoofoo"

words =
["foo","foo"]

Output:
[3]
```

Substring

```text
foofoo
```

contains both occurrences.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* List of words
* Every word has same length
* Need contiguous substring
* Need frequency matching

Think

> **Sliding Window on Fixed-Length Blocks**

---

### Why normal sliding window doesn't work?

Normally,

```text
abcde...
```

we move one character.

Here,

```text
foo
bar
cat
```

words have fixed length.

So move by

```text
wordLength
```

instead.

---

### Interview Thinking

Tell yourself:

```text
Every valid answer has exactly

numberOfWords × wordLength

characters.

Inside that window,
every chunk of size wordLength
must be one of the given words.

I'll slide over chunks,
maintain frequencies,
and shrink whenever a word
appears too many times.
```

---

# 5. Simpler Version

## Simpler Question 1

### Find All Anagrams in a String (LeetCode 438)

Need frequencies to match.

Uses sliding window + hashmap.

Difference:

```text
Character frequency
```

instead of

```text
Word frequency
```

---

## Simpler Question 2

### Permutation in String (LeetCode 567)

Need one permutation.

Window size fixed.

Frequency comparison.

---

## Simpler Question 3

### Longest Substring Without Repeating Characters

Shrink whenever invalid.

Introduces

```text
Expand

↓

Invalid

↓

Shrink
```

---

## Current Question

Now instead of characters,

our unit becomes

```text
Whole words
```

Window still expands and shrinks,

but by

```text
wordLength
```

instead of one character.

---

### Thinking Progression

```text
Character Window

↓

Frequency Map

↓

Fixed Window

↓

Word Frequency

↓

Jump by Word Length

↓

Substring with Concatenation of All Words
```

---

# 6. Brute Force

For every possible starting index

Generate substring of total length

```text
numberOfWords × wordLength
```

Split into chunks

Build frequency map

Compare with target.

```python
for each start:
    split substring
    count words
    compare maps
```

### Complexity

```text
Time  : O(N × M × L)

N = length of string
M = number of words
L = word length
```

Very slow.

---

# 7. Optimal Solution

## Idea

Create

```text
targetFreq
```

For every possible offset

```text
0
1
...
wordLength-1
```

Run sliding window.

Maintain

```text
left
right
currentFreq
matchedWords
```

If frequency exceeds,

shrink.

If matched words equals total words,

record answer.

---

### Python

```python
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        window_len = word_len * total_words

        target = Counter(words)
        ans = []

        # Try every possible alignment
        for offset in range(word_len):

            left = offset
            count = 0
            window = defaultdict(int)

            # Move in word-sized jumps
            for right in range(offset, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                if word in target:

                    window[word] += 1
                    count += 1

                    # Too many occurrences
                    while window[word] > target[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Perfect window
                    if count == total_words:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # Invalid word -> reset window
                    window.clear()
                    count = 0
                    left = right + word_len

        return ans
```

---

### Complexity

```text
Time  : O(N)

Space : O(M)

M = number of distinct words
```

Each word-sized chunk enters and leaves the window at most once.

---

# 8. Step-by-Step Trace

Example

```text
s = "barfoothefoobarman"

words = ["foo","bar"]
```

Target

```text
bar : 1
foo : 1
```

| Right Chunk | Window        | Action | Left | Count | Answer |
| ----------- | ------------- | ------ | ---- | ----- | ------ |
| bar         | {bar:1}       | Add    | 0    | 1     |        |
| foo         | {bar:1,foo:1} | Match  | 0    | 2     | 0      |
| the         | Invalid       | Reset  | 9    | 0     | 0      |
| foo         | {foo:1}       | Add    | 9    | 1     | 0      |
| bar         | {foo:1,bar:1} | Match  | 9    | 2     | 9      |

Final

```text
Answer = [0,9]
```

---

### Example with Duplicate Words

```text
words

foo
foo
```

Window

```text
foo
foo
```

Frequency

```text
foo : 2
```

If

```text
foo : 3
```

Shrink until

```text
foo : 2
```

Again valid.

---

# 9. Related Problems

| Problem                                               | Connection                                                                  |
| ----------------------------------------------------- | --------------------------------------------------------------------------- |
| **567. Permutation in String**                        | Fixed-size window with character frequency matching.                        |
| **438. Find All Anagrams in a String**                | Same frequency-map idea but on characters instead of words.                 |
| **76. Minimum Window Substring**                      | Variable sliding window with hashmap and shrink-until-valid logic.          |
| **3. Longest Substring Without Repeating Characters** | Variable window that maintains a validity condition.                        |
| **30. Substring with Concatenation of All Words**     | Extends sliding window to fixed-length word chunks with frequency matching. |

---

# Key Interview Takeaways

* **Pattern:** Variable Size Sliding Window on **fixed-length word chunks**.
* **Key Observation:** Since all words have the same length, move pointers by `wordLength` instead of one character.
* **Data Structure:** `Counter` for target frequencies and `defaultdict(int)` for the current window.
* **Invariant:** The window always contains only valid words, and no word exceeds its required frequency.
* **Optimization:** Process `wordLength` different starting offsets to cover every possible alignment.
* **Complexity:** **O(N)** time and **O(M)** space, where `M` is the number of distinct words.

---

This problem is the **word-level analogue of "Find All Anagrams in a String"**: instead of matching **character frequencies** in a fixed window, you match **word frequencies** in a fixed-length sequence of chunks. It builds directly on the variable sliding window concepts used in **Longest Substring Without Repeating Characters** and **Minimum Window Substring**. For reference, your earlier revision sheet on the sliding-window foundation problem is available in your uploaded notes. 
