# Python + OOP Mega Drill — Phase 7
**Date:** 28-08-2026
**Format:** 2 Easy · 5 Medium · 3 Hard
**Topics:** OOP (classes, `__init__`, methods, instance/class attrs, inheritance, 
composition, `@property`/getters/setters) + Loops · Strings · Functions · Lists · 
Dicts · Sets · Tuples · Lambda

---

> **Rules**
> - Every solution must be wrapped in a class and/or function as the question requires
> - Test at least one adversarial input before marking done
> - No dunder/operator overloading yet (`__eq__`, `__lt__`, `__add__`, etc.) — that's 
> - next phase
> - No built-in shortcuts where logic is explicitly asked for

---

## 🟢 EASY (2 Questions)

### E1 — Grade Tracker (OOP + loops)
Create a class `GradeTracker` with `__init__(self, grades)` where `grades` is a 
list of ints.
Add `average()` returning the mean rounded to 2 decimals, and `highest()` 
returning the max.

```
Input:  GradeTracker([88, 92, 79, 95])
Output: average() -> 88.5
        highest() -> 95
```
> 💡 Adversarial: empty grades list — decide what `average()`/`highest()` 
should do (don't let it crash silently; be intentional).

---

### E2 — Common Interests (plain function, sets)
Write a function `common_interests(a, b)` that takes two lists and 
returns a **sorted list** of items present in both.

```
Input:  a = ["reading", "gaming", "coding"], 
        b = ["gaming", "coding", "cooking"]
Output: ["coding", "gaming"]
```
> 💡 Adversarial: no overlap at all. Identical lists.

---

## 🟡 MEDIUM (5 Questions)

### M1 — Library Shelf (OOP + composition + tuples)
Create a class `Book` with `__init__(self, title, author, year)`. 
Create a class `Shelf` with `__init__(self, books)` where `books` is a list 
of `Book` objects. Add `sorted_by_year()` returning a list of `(title, year)`
tuples, oldest first.

```
Input:  books = [Book("Dune", "Herbert", 1965), Book("Neuromancer", "Gibson", 1984),Book("1984", "Orwell", 1949)]
shelf = Shelf(books)
Output: shelf.sorted_by_year() -> [("1984", 1949),("Dune", 1965),("Neuromancer", 1984)]
```
> 💡 Adversarial: empty shelf. Two books published the same year — 
decide the tiebreak and be consistent about it.

---

### M2 — Validated Wallet (OOP + `@property`)
Create a class `Wallet` with `__init__(self, balance)` storing `self._balance`
Add a `balance` property with a setter that **raises `ValueError`** on 
a negative direct assignment. Add a method `spend(amount)` that 
reduces balance and **returns `True`/`False`** (not print) depending 
on whether funds were sufficient.

```
Input:  w = Wallet(1000)
        w.spend(200)
Output: w.spend(200) -> True,  w.balance -> 800
        w.spend(5000) -> False, w.balance unchanged -> 800
```
> 💡 Adversarial: `w.balance = -50` (direct assignment) should raise `ValueError` —
this is a different failure path than `spend()` returning `False`. 
Know which mechanism you're using and why.

---

### M3 — Word Frequency Rank (plain function, dict + lambda + sorted)
Write a function `rank_words(text)` returning the **top 3** `(word, count)`
tuples, sorted by count descending, ties broken alphabetically. 
Use `sorted()` with a lambda key — no manual max-tracking loop.

```
Input:  "the cat sat on the mat the cat ran"
Output: [("the", 3), ("cat", 2), ("mat", 1)]
```
> 💡 Adversarial: fewer than 3 unique words — return whatever's 
available, don't crash trying to slice past the end.

---

### M4 — Team Roster (OOP inheritance + composition, mixed)
Create a class `Person` with `__init__(self, name, age)`. 
Create `Coach(Person)` that inherits from it and adds a `specialty` 
attribute via `super()`. 
Create a class `Team` with __init__(self, name, coach, players)` 
where `coach` is a `Coach` object and `players` is a list of plain 
`Person` objects (composition, not inheritance). 
Add `roster_summary()` returning a 
  dict: `{"coach": coach.name, "specialty": coach.specialty, 
          "player_count": len(players)}`.

```
Input:  coach = Coach("Karan", 40, "Defense")
        players = [Person("Soham", 21), Person("Riya", 22)]
        team = Team("Alpha", coach, players)
Output: team.roster_summary() -> 
{"coach": "Karan", "specialty": "Defense", "player_count": 2}
```
> 💡 Adversarial: a team with zero players — 
`player_count` should just be `0`, not crash.

---

### M5 — Unique Merge (plain function, sets + tuples + dict)
Write a function `merge_unique(pairs)` that takes a list of `(category, item)` 
tuples and returns a dict mapping each category to a 
**sorted list of its unique items**. Use a set internally to dedupe before sorting.

```
Input:  [("fruit", "apple"), ("veg", "carrot"), ("fruit", "apple"), ("fruit", "banana")]
Output: {"fruit": ["apple", "banana"], "veg": ["carrot"]}
```
> 💡 Adversarial: empty input list should return an empty dict, not crash.

---

## 🔴 HARD (3 Questions)

### H1 — Library System (OOP composition + `@property` + aggregation)
Create a class `Book` with `__init__(self, title, author, copies)` 
storing `self._copies`, with a `copies` property whose setter 
rejects negative values.
Create a class `Library` with `__init__(self)` starting 
with an empty list of books. 
Add:
- `add_book(book)` — appends a `Book` object
- `total_copies()` — sum of `.copies` across every book in the library
- `find_by_author(author)` — returns a list of titles by that author (empty list if none, never `None`)

```
Input: 
lib = Library()
lib.add_book(Book("Dune", "Herbert", 3))
lib.add_book(Book("Children of Dune", "Herbert", 2))
lib.add_book(Book("1984", "Orwell", 5))
Output: lib.total_copies() -> 10
        lib.find_by_author("Herbert") -> ["Dune", "Children of Dune"]
        lib.find_by_author("Tolkien") -> []
```
> 💡 Adversarial: `find_by_author` on an author with zero matches must 
return `[]`, not `None` — check what your loop does when nothing matches.

---

### H2 — Polymorphic Shapes (OOP inheritance + polymorphism + lambda/sorted)
Create a base class `Shape` with a method `area()` returning `0` 
(placeholder — every subclass must override it). 
Create `Circle(radius)`, `Square(side)`, and `Rectangle(width, height)`, 
each correctly overriding `area()`. 
Write a **plain function** `total_area(shapes)` that takes a mixed list 
of shape objects and sums `.area()` across all of them — same method call, 
different underlying math, no `if isinstance()` branching.
Write a second plain function `largest_shape(shapes)` returning the 
object with the biggest area, using `sorted()` with a lambda key.

```
Input:  shapes = [Circle(3), Square(4), Rectangle(2, 5)]
Output: total_area(shapes) -> ~44.27  (28.27 + 16 + 10)
        largest_shape(shapes) -> the Circle object
```
> 💡 Adversarial: empty `shapes` list — `total_area([])` should return `0`, 
not crash. This is the actual point of the exercise: 
`total_area()` never needs to know or care which shape it's looking at — 
that's polymorphism doing its job.

---

### H3 — Student Report Pipeline (OOP + full mixed pipeline)
Create a class `Student` with `__init__(self, name, scores)` where `scores` 
is a list of ints, and a **read-only** `average` property computing the mean.
Write a **plain function** `process_students(students)` taking a list 
of `Student` objects and returning a report dict:
- `"roster"` → list of `(name, average)` tuples, sorted by average **descending**
- `"passed"` → set of names with average ≥ 50
- `"failed"` → set of names with average < 50
- `"topper"` → name of the highest-average student (tie → alphabetically first)

```
Input: [
    Student("Soham", [88, 92, 79]),
    Student("Riya", [95, 91]),
    Student("Arjun", [40, 45]),
    Student("Meera", [93, 93])   # ties Soham? no — check the numbers
]
Output: {
    "roster": [("Riya", 93.0), ("Meera", 93.0), ("Soham", 86.33), ("Arjun", 42.5)],
    "passed": {"Riya", "Meera", "Soham"},
    "failed": {"Arjun"},
    "topper": "Meera"
}
```
> 💡 Adversarial: this input has a genuine tie (Riya 93.0 vs Meera 93.0) — 
your `topper` logic and your `roster` sort order both need an explicit, 
deliberate tiebreak rule (alphabetical), not whatever order happens 
to fall out of `sorted()` by accident. Verify it, don't assume it.

---

## Log

## Log

| Q | Status | First Try? | Edge Case Tested | Notes |
|---|--------|------------|-------------------|-------|
| E1 | ✅ | Yes | Yes — empty list | Implicit `None` return on empty was a deliberate choice, not an oversight |
| E2 | ✅ | Yes | — | Clean |
| M1 | ✅ | Yes | — | Clean, tested with a different year than the spec (1969 instead of 1965) |
| M2 | ⚠️→✅ | No | Yes — insufficient funds path | Setter was missing `self._balance = value` on the valid path (removed while testing the error path, forgot to restore). Fixed. |
| M3 | ✅ | Yes | — | One harmless redundant `len < 3` check before slicing — slicing already handles it safely |
| M4 | ✅ | Yes | — | Correct logic; dict key spelled `"speciality"` instead of spec's `"specialty"` |
| M5 | ✅ | Yes | — | Clean set-based dedup |
| H1 | ✅ | Yes | Yes — author with no matches | Applied the M2 setter lesson immediately and correctly |
| H2 | ✅ | Yes | — | Code was correct — mentor's stated expected total (44.27) was wrong; correct sum is 54.27 |
| H3 | ✅ | Yes | Yes — tie between two students | Code was correct — mentor's stated roster order for the tie was inconsistent with the stated topper; his alphabetical tiebreak was the correct version |

*Phase 7 — mixed OOP (through getters/setters) + full prior topic set. Dunder/operator overloading picked back up next phase.*
