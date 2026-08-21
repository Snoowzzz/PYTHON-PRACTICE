# Python Practice Log — Functions + Lists
**Session 2 of 3** | Date: 20-08-2026
**Topics:** Functions · Lists · Loops · Strings (mixed)
**Format:** 2 Easy · 5 Medium · 3 Hard

---

> **Level Warning**
> Easy here = Session 1 Medium level. Medium here = harder than anything in Session 1.
> Every function must have at least one adversarial input tested before you mark it done.
> No dicts, no sets, no tuples — pure functions + lists + strings + loops.

---

## 🟢 EASY (2 Questions)
*These are not warm-ups. Think before you type.*

---

### E1 — Two-List Merger
Write a function `merge_alternating(a, b)` that merges two lists by alternating elements.
If one list is longer, append the remaining elements at the end.

```
Input:  a = [1, 2, 3], b = [10, 20]
Output: [1, 10, 2, 20, 3]

Input:  a = [1], b = [10, 20, 30]
Output: [1, 10, 20, 30]
```
> 💡 Adversarial: both empty. One empty, one has 5 elements.

---

### E2 — Palindrome Checker
Write a function `is_palindrome(s)` that returns `True` if the string is a palindrome, 
ignoring spaces and case. Do **not** use slicing reversal `[::-1]` — use a loop.

```
Input:  "Race Car"    → True
Input:  "Cloud"       → False
Input:  "A man a plan a canal Panama"  → True
```
> 💡 Adversarial: single character. Empty string. All spaces.

---

## 🟡 MEDIUM (5 Questions)
*Every one of these has a non-obvious edge. Don't rush.*

---

### M1 — Running Maximum
Write a function `running_max(nums)` that returns a new list where each element is the 
**maximum value seen so far** from the beginning of the list up to that index.

```
Input:  [3, 1, 4, 1, 5, 9, 2, 6]
Output: [3, 3, 4, 4, 5, 9, 9, 9]
```
> 💡 Adversarial: single element list. All same numbers. Descending list `[9,7,5,3]`.

---

### M2 — Word Reverser
Write a function `reverse_words(sentence)` that reverses the **order of words** in a 
sentence but keeps each word's characters intact. Handle multiple spaces between words.

```
Input:  "Cloud Computing is fun"
Output: "fun is Computing Cloud"

Input:  "  hello   world  "
Output: "world hello"
```
> 💡 Do NOT use `split()` and `reverse()` together as a one-liner. 
Build the word list manually with a loop, then reconstruct. Adversarial: 
single word. All spaces.

---

### M3 — Chunk Splitter
Write a function `chunk_list(lst, size)` that splits a list into chunks of a given size. 
The last chunk may be smaller if the list doesn't divide evenly.

```
Input:  lst = [1,2,3,4,5,6,7], size = 3
Output: [[1,2,3], [4,5,6], [7]]

Input:  lst = [1,2,3,4], size = 2
Output: [[1,2], [3,4]]
```
> 💡 Adversarial: `size > len(lst)`. `size = 1`. Empty list.

---

### M4 — List Rotator
Write a function `rotate_list(lst, k)` that rotates a list to the **right** by `k`. 
positions Do **not** use string slicing tricks — work with the list directly 
using a loop or index math.

```
Input:  lst = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input:  lst = [1,2,3], k = 5
Output: [2,3,1]   ← k > len(lst), handle it
```
> 💡 This is the list version of M2 from Session 1. The math insight is the same —
find it.

---

### M5 — Frequency Counter
Write a function `char_frequency(s)` that returns a list of tuples `(character, count)` 
sorted by count **descending**, then alphabetically for ties. Ignore spaces. 
Do not use dicts.

```
Input:  "hello world"
Output: [('l', 3), ('o', 2), ('d', 1), ('e', 1), ('h', 1), ('r', 1), ('w', 1)]
```
> 💡 This is a genuine challenge without dicts. Think about what structures you DO have.
 Adversarial: single character repeated. All unique characters.

---

## 🔴 HARD (3 Questions)
*Plan on paper before you code. Seriously.*

---

### H1 — String Compression (RLE Upgraded)
Write a function `compress(s)` that performs Run-Length Encoding but with a twist — if a 
character appears only once, do **not** write the count. Only write the count when it's 
greater than 1.

```
Input:  "aaabbccddddef"
Output: "3a2b2c4def"

Input:  "abcd"
Output: "abcd"   ← no counts since all are 1
```

**Extension:** Write `decompress(s)` that reverses this — takes `"3a2b2c4def"` and 
returns `"aaabbccdddddef"`. Both functions must work together as a pair.

> 💡 Adversarial: single character `"a"` → `"a"`. Empty string. `"aaaaaa"` → `"6a"`.

---

### H2 — Matrix Row Operations
Write three functions that operate on a **list of lists** (2D matrix):

```python
def row_sum(matrix, r):
    # Returns sum of all elements in row r

def col_max(matrix, c):
    # Returns the maximum element in column c

def transpose(matrix):
    # Returns a new matrix where rows become columns
    # [[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]
```

Test with:
```python
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(row_sum(m, 1))    # → 15
print(col_max(m, 2))    # → 9
print(transpose(m))     # → [[1,4,7],[2,5,8],[3,6,9]]
```

> 💡 Transpose is the real challenge here. Think about what `matrix[row][col]` becoming 
`matrix[col][row]` means structurally. Adversarial: 1x1 matrix. 
Non-square matrix (2 rows, 3 cols).

---

### H3 — The Cipher
Write a function `caesar_cipher(text, shift, mode)` where:
- `mode = "encode"` → shifts each letter forward by `shift` positions in the alphabet
- `mode = "decode"` → shifts each letter backward by `shift`
- Non-letter characters (spaces, numbers, punctuation) stay unchanged
- Case is preserved — uppercase stays uppercase, lowercase stays lowercase

```
Input:  caesar_cipher("Hello, World!", 3, "encode")
Output: "Khoor, Zruog!"

Input:  caesar_cipher("Khoor, Zruog!", 3, "decode")
Output: "Hello, World!"
```

> 💡 The alphabet wraps — `Z` shifted by 1 becomes `A`. Think modulo. `ord()` and 
`chr()` are allowed — they convert characters to ASCII numbers and back. 
That's all you need.

---
Q	Status	First Try?	Edge Case Tested	Notes
E1	✅ Solved	✅ Yes	✅ Both empty, one empty	Learned min() collapse after
E2	✅ Solved	✅ Yes	✅ Single char, empty, all spaces	Clean, no slicing used
M1	✅ Solved	✅ Yes	✅ Descending, all same, single element	Key insight: compare against newlst[-1]
M2	✅ Solved	❌ No	✅ Multiple spaces, single word	for loop bug caught, rebuilt with while
M3	✅ Solved	✅ Yes	✅ size > len, size=1, empty	Manual version first, then saw slicing shortcut
M4	✅ Solved	✅ Yes	✅ k > len, k=0, k=len	Transferred Session 1 insert logic, then derived slicing independently
M5	✅ Solved	✅ Yes	✅ All same, all unique	Smart use of set() on tuple list for dedup
H1	✅ Solved	❌ No	✅ Single char, all same, all unique	V1 had missing last group + replace hack, fixed both cleanly
H2	✅ Solved	✅ Yes	✅ Non-square matrix, negative numbers	Transpose nested loop logic was clean first try
H3	✅ Solved	✅ Yes	✅ Wrap (XYZ→ABC), k>26	Handled ASCII boundaries + case preservation independently

10/10 — Clean sweep. Session 2 done. 🫡

*Session 3 is the final boss — 4 medium 6 hard, same elevated level. 
Lock Session 2 in first.*
