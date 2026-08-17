# Python Loops — Deep Dive Notes
**Date:** 2026-08-17
**Topics:** for, while, break, continue, for...else, nested loops, niche tricks

---

## 1. `range()` — the real mechanics

```python
range(a, b, step)
```

- `b` is **always exclusive** — `range(1, 5)` gives `1,2,3,4` not `5`
- `step` defaults to `1` if not given
- Negative step = reverse iteration

```python
for i in range(10, 0, -2):
    print(i)
# 10 8 6 4 2
```

**Niche thing most people miss:**
```python
range(5)         # 0,1,2,3,4
range(5, 5)      # empty — no iterations at all
range(5, 0)      # also empty — forgot the -1 step
range(5, 0, -1)  # 5,4,3,2,1 — this is what you wanted
```

That third one silently does nothing — no error, no output. Trips people up constantly.

---

## 2. `break` — exits the entire loop

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# 0 1 2 3 4
# loop dead after 5
```

**Key mental model:** `break` doesn't just skip — it **kills** the loop entirely. Everything after it in the loop body is also skipped for that iteration.

**Niche — break only exits the innermost loop:**
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break        # only kills inner loop
    print(i)             # outer loop keeps running
# 0 1 2
```

This catches people in nested loops. If you want to exit BOTH loops you need a flag:

```python
found = False
for i in range(3):
    for j in range(3):
        if j == 1:
            found = True
            break
    if found:
        break
```

---

## 3. `continue` — skips current iteration, loop keeps going

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
# 1 3 5
```

**Mental model:** `continue` teleports you to the **top of the loop** for the next iteration. Everything below it in the current iteration is skipped.

**Niche — `continue` in a `while` loop can cause infinite loop:**
```python
i = 0
while i < 5:
    if i == 3:
        continue     # ❌ i never increments — infinite loop
    print(i)
    i += 1
```

Fix — increment before continue:
```python
i = 0
while i < 5:
    if i == 3:
        i += 1
        continue     # ✅ now safe
    print(i)
    i += 1
```

This is one of the most common while loop bugs. Remember it.

---

## 4. `for...else` and `while...else` — the underused feature

The `else` block runs **only if the loop completed without hitting a `break`.**

```python
for i in range(5):
    if i == 10:      # never true
        break
else:
    print("Loop completed normally")
# prints: Loop completed normally
```

```python
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed normally")
# prints nothing — break was hit
```

**Real use case — search and report:**
```python
target = 7
numbers = [1, 4, 6, 9, 2]

for num in numbers:
    if num == target:
        print("Found it")
        break
else:
    print("Not found")   # only runs if break never triggered
# prints: Not found
```

Without `for...else` you'd need an extra flag variable. This is cleaner.

**Niche — most Python devs don't even know this exists.** Using it correctly in an interview or code review immediately signals you know the language deeply.

---

## 5. `while` — condition driven, not count driven

Use `while` when you don't know how many iterations you need:

```python
# sentinel pattern — keep going until user says stop
while True:
    val = input("Enter value (q to quit): ")
    if val == "q":
        break
    print(f"You entered: {val}")
```

`while True` with a `break` is the standard pattern for menus, input validation, game loops.

**Niche — `while` vs `for` decision rule:**
- Know the count upfront → `for`
- Waiting for a condition → `while`
- Infinite loop with exit condition → `while True` + `break`

---

## 6. Nested loops — the multiplication rule

```python
for i in range(3):       # runs 3 times
    for j in range(4):   # runs 4 times per outer
        print(i, j)
# total iterations = 3 × 4 = 12
```

**Niche — variable shadowing in nested loops:**
```python
for i in range(3):
    for i in range(5):   # ❌ reusing i — outer i gets destroyed
        print(i)
# outer loop still runs 3 times but i is now 0-4 each time
# confusing, never do this
```

Always use distinct names — `i, j, k` or descriptive names like `row, col`.

---

## 7. Rare things worth knowing

**`pass` — syntactic placeholder:**
```python
for i in range(5):
    pass    # does absolutely nothing, just satisfies syntax
```
Useful when stubbing out code you'll fill later.

---

**Loop variable leaks in Python (unlike C):**
```python
for i in range(5):
    x = i

print(x)   # prints 4 — x survives after loop ends
print(i)   # prints 4 — i also survives
```
In C, loop variables die after the loop. In Python they don't. Can cause subtle bugs if you reuse names.

---

**Iterating with index AND value — `enumerate()`:**
```python
fruits = ["apple", "banana", "mango"]
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
# 0 apple
# 1 banana
# 2 mango
```
Cleaner than `range(len(fruits))`. Use this whenever you need both index and value.

---

**Iterating two lists together — `zip()`:**
```python
names = ["Soham", "Tina", "Raj"]
scores = [95, 87, 76]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```
Stops at the shorter list. Clean, no index juggling.

---

## Quick Reference Card

| Tool | Use when |
|------|----------|
| `for` + `range` | Known count |
| `while` | Condition driven |
| `while True` + `break` | Sentinel/menu loop |
| `break` | Exit loop immediately |
| `continue` | Skip this iteration |
| `for...else` | Search + report not found |
| `enumerate` | Need index + value both |
| `zip` | Parallel list iteration |
| `pass` | Placeholder stub |

---

## The 3 things that will make you look sharp in interviews/reviews

1. **`for...else`** — most devs don't know it exists. Use it for search patterns.
2. **`continue` in `while` loops** — always increment before `continue`, never after.
3. **`break` only exits innermost loop** — use a flag to break out of nested loops.
