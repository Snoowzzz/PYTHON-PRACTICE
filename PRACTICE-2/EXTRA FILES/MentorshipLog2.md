# Python Mentorship — Master Log (Complete)
**Started:** 17-08-2026 | **Last Updated:** 22-08-2026
**Student:** Soham | BTech CSE Sem 5, MIT WPU
**Mentor:** Claude

---

## OVERALL PROGRESS SNAPSHOT

| Phase | Topic | Score | Status |
|-------|-------|-------|--------|
| Days 1-2 | Loops + Strings | 14/15 + 2 bonus | ✅ Complete |
| Session 1 | Functions + Lists (intro level) | 9/10 | ✅ Complete |
| Session 2 | Functions + Lists (elevated) | 10/10 | ✅ Complete |
| Drill Round 1 | Dict, Set, Tuple syntax | 10/10 | ✅ Complete |
| Drill Round 2 | Dict, Set, Tuple mixed | 6/7 | ✅ Complete |
| Lambda | map, filter, sorted | 6/6 | ✅ Complete |
| Session 3 | Functions + Lists (boss tier) | 0/10 | ⏳ Pending |
| OOP | Classes, objects, __init__ | — | ⏳ Pending |
| File Handling | read, write, append | — | ⏳ Pending |

---

## DETAILED QUESTION LOG

### Days 1–2 — Loops + Strings (17–18 Aug)

| Q | Problem | Status | Notes |
|---|---------|--------|-------|
| 1 | Sum of N | ✅ | First try |
| 2 | Index + char print | ✅ | First try |
| 3 | Print evens | ✅ | First try |
| 4 | Countdown | ✅ | First try |
| 5 | Reverse string | ✅ | First try |
| 6 | Sum of positives | ✅ | Flagged: fragile on multi-digit input |
| 7 | Char-repeat pattern | ✅ | First try |
| 8 | Largest digit | ✅ | First try |
| 9 | First multiple of 15 | ✅ | First try |
| 10 | Contains-digit check | ✅ | First try |
| 11 | Factorial + parity | ✅ | First try |
| 12 | Nested triangular sums | ✅ | First self-built nested loop pattern |
| 13 | RLE | ⚠️ | Had correct solution, overthought it, abandoned. Redeemed in Session 2 H1 |
| 14 | Mini multiplication table | ✅ | Nested loops |
| 15 | Balanced parentheses | ✅ | Missed negative-dip edge case, corrected after counterexample |
| B1 | Decreasing triangle | ✅ | Bonus |
| B2 | Diamond pattern | ✅ | Bonus — correctly generalized spacing formula |

**Score: 14/15 + 2 bonus**

---

### Session 1 — Functions + Lists Intro (19 Aug)

| Q | Problem | Status | Notes |
|---|---------|--------|-------|
| E1 | Remove Negatives | ✅ | Added count extension himself. Minor: unnecessary `pass`, count via math cleaner |
| E2 | Count Vowels | ✅ | Clean. Minor: return only `count` not `new_word` |
| E3 | Squares List | ✅ | Works. Cleaner with `range(1, n+1)` |
| E4 | First Even Index | ✅ | Used `enumerate` + `for-else` — strongest easy of session |
| M1 | Unique Ordered | ✅ | 2-3 mins. Arrived at seen-tracker naturally without hints |
| M2 | Rotate String | ✅ | Creative `insert` approach. Self-caught hardcoded `6` bug |
| M3 | Categorize Scores | ✅ | Clean boundary logic. Caught mentor's question error |
| M4 | Compress Spaces | ✅ | Solved on pen and paper in college. Self-debugged 15 min character-skip bug |
| H1 | List Flattener | ✅ | V1 broke on multi-digit. Built V2 tokenizer independently. Recursion shown and understood |
| H2 | Scoreboard | ❌ | Dict syntax gap. Logic direction correct. Pending redo |

**Score: 9/10**

---

### Session 2 — Functions + Lists Elevated (20 Aug)

| Q | Problem | Status | Notes |
|---|---------|--------|-------|
| E1 | Merge Alternating | ✅ | All edge cases correct. Learned `min()` collapse after |
| E2 | Palindrome (no slicing) | ✅ | All 6 adversarial cases correct |
| M1 | Running Maximum | ✅ | Caught descending trap. Key insight: compare against `newlst[-1]` |
| M2 | Word Reverser | ✅ | `for` loop bug self-identified, rebuilt with `while`. Logic was right all along |
| M3 | Chunk Splitter | ✅ | All edge cases correct. Built manual version then saw slicing shortcut |
| M4 | List Rotator | ✅ | Transferred insert logic from Session 1. Derived slicing version independently |
| M5 | Frequency Counter | ✅ | Used `set()` to deduplicate tuples, `sorted()` with lambda — clean pipeline |
| H1 | RLE Upgraded | ✅ | RLE redemption arc complete. Fixed last group flush + removed replace hack |
| H2 | Matrix Operations | ✅ | Transpose nested loop logic clean first try. Non-square matrix handled |
| H3 | Caesar Cipher | ✅ | ASCII boundaries + case preservation handled independently. Wrap and k>26 both correct |

**Score: 10/10 — Clean sweep**

---

### Dict, Set, Tuple Drill Round 1 (21 Aug)

| Q | Problem | Status | Notes |
|---|---------|--------|-------|
| Q1 | Build Profile | ✅ | Clean |
| Q2 | Update Score | ✅ | Used `d.update()` — learned `d[k]=v` cleaner for single key |
| Q3 | Word Count | ✅ | `split()` + `count()` — efficient |
| Q4 | Dict Flip | ✅ | Clean `for k,v in d.items()`. Observed duplicate value overwrite independently |
| Q5 | Unique + Common Elements | ✅ | Set operations clean first try |
| Q6 | Set Report | ✅ | All three operations correct |
| Q7 | MinMax Tuple | ✅ | Initialized with `nums[0]` — remembered H2 matrix bug fix |
| Q8 | Swap Pairs | ✅ | Direct tuple unpacking in loop header — Pythonic |
| Q9 | Group by Length | ⚠️ | Struggled with list-inside-dict. Clicked after hint |
| Q10 | Analyse (all three) | ✅ | All four output types correct. Clean pipeline |

**Score: 10/10**

---

### Dict, Set, Tuple Drill Round 2 (22 Aug)

| Q | Problem | Status | Notes |
|---|---------|--------|-------|
| Q1 | Filter Passing | ✅ | Clean |
| Q2 | Who Left | ✅ | Set difference, one line |
| Q3 | Sort by Score | ✅ | Skipped initially, attempted anyway. Independently built selection sort. Bug: name vs tuple membership — fixed with `used_names` tracker |
| Q4 | Merge Dicts | ✅ | Nested loop had empty dict bug. Learned foundation-first pattern |
| Q5 | Char Freq Dict | ✅ | Self-fixed `newstr` → `seen` before being told |
| Q6 | Top Students | ✅ | Self-fixed `dict_keys` → `set()` before being told |
| Q7 | Class Report | ✅ | All four output types correct first try. One loop handled set + dict + max together |

**Score: 6/7 (Q3 attempted and solved despite being marked skip)**

---

### Lambda Functions (22 Aug)

Theory: what lambda is, why it exists, when to use vs `def`. Tools covered: `map()`, `filter()`, `sorted()` with key.

| Q | Problem | Status | Notes |
|---|---------|--------|-------|
| Q1 | Celsius → Fahrenheit with `map()` | ✅ | Clean |
| Q2 | Bonus descending sort | ✅ | Applied `(-x[1], x[0])` unprompted from drill memory |
| Q3 | Filter strings by length | ✅ | Clean |
| Q4 | Sort by last character | ✅ | `x[-1]` as key |
| Q5 | Name → (name, length) tuple | ✅ | Clean |
| Q6 | Chain `filter()` + `map()` | ✅ | Copilot assisted on structure. Filter condition overcomplicated |

**Score: 6/6**

---

## KEY BREAKTHROUGHS

| Date | Breakthrough |
|------|-------------|
| 17 Aug | First self-built nested loop pattern |
| 18 Aug | Balanced parentheses negative-dip edge case |
| 19 Aug | Seen-tracker for deduplication — arrived without hints |
| 19 Aug | Derived `(i+t)%k` rotation formula independently |
| 19 Aug | Self-debugged M4 space-compression bug on paper, no IDE |
| 19 Aug | Built string tokenizer for multi-digit flattener — two versions |
| 19 Aug | Understood recursion on first encounter without formal teaching |
| 20 Aug | Derived list slicing rotation `lst[k-p:] + lst[0:k-p]` independently |
| 20 Aug | Used `set()` on tuple list for deduplication — lateral thinking |
| 20 Aug | 10/10 clean sweep including Caesar cipher and matrix transpose |
| 21 Aug | Recognized stack pattern needed for Leetcode 2390 without knowing stacks |
| 22 Aug | Independently built selection sort without knowing the algorithm exists |
| 22 Aug | Self-corrected return types and variable naming before being told |

---

## RECURRING GAPS

| Gap | Status |
|-----|--------|
| Edge case discipline | 🔄 Improving, not yet habitual |
| Return scope — returning more than promised | 🔄 Self-correcting now |
| Unnecessary intermediate variables | 🔄 Improving |
| Dict — list inside dict pattern | ✅ Clicked 22 Aug |
| Completing solutions when fix is known | ⚠️ Still occasional |

---

## PENDING

### Immediate
- [ ] Session 3 — 4 medium, 6 hard (boss tier)
- [ ] Session 1 H2 Scoreboard redo

### After Session 3
- [ ] OOP — classes, objects, `__init__`, methods, inheritance
- [ ] File Handling — read, write, append, CSV, JSON

### Later
- [ ] Sorting algorithms — bubble, selection, merge
- [ ] Stack, Queue data structures
- [ ] Connect Python to AWS — cloud automation scripts

---

## QUICK SYNTAX REFERENCE

### Dict
```python
d = {"name": "Soham", "score": 91}
d["name"]               # access
d["score"] = 95         # update
d["city"] = "Pune"      # add new key
del d["city"]           # delete
"name" in d             # check key
d.get("age", 0)         # safe access with fallback
for k, v in d.items()   # loop key-value pairs
```

### Set
```python
s = {1, 2, 3}
s.add(4)
s.remove(3)
s.discard(10)
s1 | s2       # union
s1 & s2       # intersection
s1 - s2       # difference
```

### Tuple
```python
t = (1, 2, 3)
t[0]           # access
a, b, c = t    # unpack
# t[0] = 5 → ERROR, immutable
```

### Lambda
```python
lambda x: x**2
sorted(data, key=lambda x: x[1])
sorted(data, key=lambda x: (-x[1], x[0]))
list(map(lambda x: x**2, nums))
list(filter(lambda x: x > 0, nums))
```

---

*Log maintained by Claude. Updated after every session.*
