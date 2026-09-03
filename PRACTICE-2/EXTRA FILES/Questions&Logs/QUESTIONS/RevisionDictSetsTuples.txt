# Python Syntax Drill — Dicts, Sets, Tuples
**Date:** 21-08-2026
**Format:** 10 questions, no difficulty labels, pure syntax muscle memory

---

> **Rules**
> - No timer pressure. This is about getting comfortable, not speed.
> - Every question is solvable with the syntax reference above.
> - Test at least one edge case per question.

---

### Q1 — Dict Builder
Write a function `build_profile(name, age, city)` that returns a dictionary with those 
three keys.

```
Input:  "Soham", 20, "Pune"
Output: {"name": "Soham", "age": 20, "city": "Pune"}
```

---

### Q2 — Dict Updater
Write a function `update_score(d, name, score)` that takes a dict of `{name: score}` 
pairs. 
If the name exists, update only if new score is higher. If name doesn't exist, add it.

```
d = {"Soham": 88, "Riya": 95}
update_score(d, "Soham", 91)   # updates → {"Soham": 91, "Riya": 95}
update_score(d, "Soham", 80)   # no change → {"Soham": 91, "Riya": 95}
update_score(d, "Arjun", 72)   # adds → {"Soham": 91, "Riya": 95, "Arjun": 72}
```

---

### Q3 — Dict Counter
Write a function `word_count(sentence)` that returns a dict where each key is a word and 
value is how many times it appears.

```
Input:  "the cat sat on the mat the cat"
Output: {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}
```

---

### Q4 — Dict Flip
Write a function `flip_dict(d)` that swaps keys and values.

```
Input:  {"a": 1, "b": 2, "c": 3}
Output: {1: "a", 2: "b", 3: "c"}
```
> Edge case: what if two keys have the same value? Note what happens — 
don't need to fix it, just observe.

---

### Q5 — Set Basics
Write a function `unique_elements(lst)` that returns a set of unique elements from a list.
Then write a second function `common_elements(lst1, lst2)` that returns elements present
in both lists.

```
unique_elements([1,2,2,3,3,3])     → {1, 2, 3}
common_elements([1,2,3], [2,3,4])  → {2, 3}
```

---

### Q6 — Set Operations
Write a function `set_report(a, b)` that takes two lists and prints:
- Elements in both (intersection)
- Elements only in a (difference)
- All unique elements combined (union)

```
a = [1,2,3,4]
b = [3,4,5,6]

Both:     {3, 4}
Only in a: {1, 2}
All:      {1, 2, 3, 4, 5, 6}
```

---

### Q7 — Tuple Basics
Write a function `minmax(nums)` that returns a tuple of `(minimum, maximum)` from a list 
without using `min()` or `max()`.

```
Input:  [3, 1, 4, 1, 5, 9, 2, 6]
Output: (1, 9)
```

---

### Q8 — Tuple Unpacking
Write a function `swap_pairs(lst)` that takes a list of tuples and swaps each pair.

```
Input:  [(1,2), (3,4), (5,6)]
Output: [(2,1), (4,3), (6,5)]
```

---

### Q9 — Dict + List Combined
Write a function `group_by_length(words)` that takes a list of words and returns a dict 
where keys are word lengths and values are lists of words with that length.

```
Input:  ["cat", "dog", "elephant", "ant", "ox", "bee"]
Output: {3: ["cat", "dog", "ant", "bee"], 8: ["elephant"], 2: ["ox"]}
```

---

### Q10 — All Three Together
Write a function `analyse(data)` that takes a list of `(name, score)` tuples and returns 
a dict with:
- `"highest"` → name of the person with highest score
- `"unique_scores"` → a set of all unique scores
- `"average"` → average score rounded to 2 decimal places

```
Input:  [("Soham", 91), ("Riya", 95), ("Arjun", 72), ("Soham", 91)]
Output: {
    "highest": "Riya",
    "unique_scores": {91, 95, 72},
    "average": 87.25
}
```

---

## Log

| Q | Done? | Notes |
|---|-------|-------|
| Q1 | | |
| Q2 | | |
| Q3 | | |
| Q4 | | |
| Q5 | | |
| Q6 | | |
| Q7 | | |
| Q8 | | |
| Q9 | | |
| Q10 | | |