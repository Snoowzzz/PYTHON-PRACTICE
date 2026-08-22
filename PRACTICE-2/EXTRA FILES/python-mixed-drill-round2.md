# Python Mixed Drill — Dicts, Sets, Tuples (Round 2)
**Date:** 22-08-2026
**Format:** 7 questions, mixed difficulty, all three data structures combined

---

> **Goal:** By Q7 the syntax should feel automatic. No reference needed.

---

### Q1 — Dict Filter
Write a function `filter_passing(grades)` that takes a dict of `{name: score}` and returns a new dict with only students who scored 50 or above.

```
Input:  {"Soham": 91, "Riya": 45, "Arjun": 72, "Meera": 38}
Output: {"Soham": 91, "Arjun": 72}
```

---

### Q2 — Set Difference Report
Write a function `who_left(batch1, batch2)` that takes two sets of student names. Return a set of students who were in batch1 but did NOT continue to batch2.

```
batch1 = {"Soham", "Riya", "Arjun", "Meera"}
batch2 = {"Soham", "Riya", "Karan"}
Output: {"Arjun", "Meera"}
```

---

### Q3 — Tuple Sorter
Write a function `sort_by_score(data)` that takes a list of `(name, score)` tuples and returns them sorted by score descending. No built-in `sorted` with lambda — use your own logic to sort.

```
Input:  [("Soham", 91),("Riya", 95),("Arjun", 72)]
Output: [("Riya", 95),("Soham", 91),("Arjun", 72)]

> 💡 Think: bubble sort or selection sort. You know loops. Apply them to tuples.

---

### Q4 — Dict Merger
Write a function `merge_dicts(d1, d2)` that merges two dicts. If a key exists in both, keep the higher value.

```
d1 = {"a": 10, "b": 5, "c": 8}
d2 = {"b": 12, "c": 3, "d": 7}
Output: {"a": 10, "b": 12, "c": 8, "d": 7}
```

---

### Q5 — Frequency Dict
Write a function `char_freq_dict(s)` that returns a dict of character frequencies, ignoring spaces. Then return only characters that appear more than once.

```
Input:  "hello world"
Output: {"l": 3, "o": 2}   ← only chars with count > 1
```

---

### Q6 — Invert and Filter
Write a function `top_students(grade_dict, threshold)` that:
1. Takes a dict of `{name: score}`
2. Returns a **set** of names who scored above the threshold

```
Input:  {"Soham": 91, "Riya": 95, "Arjun": 72}, threshold=90
Output: {"Soham", "Riya"}
```

---

### Q7 — Full Pipeline
Write a function `class_report(data)` that takes a list of `(name, score)` tuples and returns a dict with:
- `"passed"` → set of names with score >= 50
- `"failed"` → set of names with score < 50
- `"top_scorer"` → tuple of (name, score) of the highest scorer
- `"score_map"` → dict of {name: score} for ALL students

```
Input: [("Soham", 91), ("Riya", 45), ("Arjun", 72), ("Meera", 38)]
Output: {
    "passed": {"Soham", "Arjun"},
    "failed": {"Riya", "Meera"},
    "top_scorer": ("Soham", 91),
    "score_map": {"Soham": 91, "Riya": 45, "Arjun": 72, "Meera": 38}
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
