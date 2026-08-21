# Python Strings — Complete Guide

## 1. What a String Actually Is

A string is an **immutable sequence of characters**. Immutable means once created, it can never be changed in place — every "modification" (`.replace()`, `.upper()`, slicing, etc.) returns a **brand new string** and leaves the original untouched.

```python
s = "hello"
s.upper()
print(s)          # still "hello" — original untouched
s = s.upper()      # you must reassign to actually keep the change
```

This matters for performance: building a string with repeated `+=` in a loop creates a new string object every single iteration (O(n²) behavior). For heavy concatenation, use `''.join(list_of_pieces)` instead — O(n).

---

## 2. Creating Strings

```python
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple quotes — spans
multiple lines'''
s4 = "It's fine"        # use double quotes to avoid escaping '
s5 = 'She said "hi"'    # use single quotes to avoid escaping "
s6 = "Escaped: \" and \'"
raw = r"C:\new\test"     # raw string — backslashes are literal, no escape processing
```

---

## 3. Indexing & Slicing

Strings are indexed like arrays — `0` to `len-1` forward, `-1` to `-len` backward.

```python
s = "Python"
s[0]      # 'P'
s[-1]     # 'n'
s[2:5]    # 'tho'   (start inclusive, end exclusive)
s[:3]     # 'Pyt'
s[3:]     # 'hon'
s[::-1]   # 'nohtyP'  — reverse trick, step = -1
s[::2]    # 'Pto'     — every 2nd character
```

**Key rule:** slicing never throws an IndexError even if the range is out of bounds — it just returns what's available (or empty). Direct indexing (`s[10]` on a 6-char string) **does** throw.

---

## 4. Core Methods (organized by purpose)

### Case
| Method | Effect |
|---|---|
| `.upper()` | `"abc"` → `"ABC"` |
| `.lower()` | `"ABC"` → `"abc"` |
| `.title()` | `"hello world"` → `"Hello World"` |
| `.capitalize()` | `"hello world"` → `"Hello world"` |
| `.swapcase()` | `"AbC"` → `"aBc"` |

### Whitespace / Cleaning
| Method | Effect |
|---|---|
| `.strip()` | removes leading+trailing whitespace (or given chars) |
| `.lstrip()` / `.rstrip()` | left-only / right-only strip (covered last session) |
        "-42".lstrip('-')      # → "42"
        "---42".lstrip('-')    # → "42"   (removes ALL leading '-', not just one)
        "42-".lstrip('-')      # → "42-"  (only strips from the LEFT, so trailing '-' stays)
        "42".lstrip('-')       # → "42"   (nothing to strip, no error)
        The Family: strip, lstrip, rstrip
Method	Strips from	Example
    strip()	Both ends	"  hi  ".strip() → "hi"
    lstrip()	Left only	"  hi  ".lstrip() → "hi  "
    rstrip()	Right only	"  hi  ".rstrip() → "  hi"

No argument → defaults to stripping whitespace (spaces, tabs, newlines). This is why strip() with no args is the classic tool for cleaning up input() values that might have accidental trailing spaces.
### Searching
| Method | Returns |
|---|---|
| `.find(sub)` | index of first match, or `-1` if not found (never crashes) |
| `.index(sub)` | same as find, but **raises ValueError** if not found |
| `.count(sub)` | number of non-overlapping occurrences |
| `in` keyword | `"py" in "python"` → `True` (preferred for existence checks) |

### Checking (the `is*` family)
`isdigit()`, `isalpha()`, `isalnum()`, `isspace()`, `isupper()`, `islower()` — all covered last session. Rule of thumb: they all return `False` on an empty string.

### Splitting & Joining
```python
"a,b,c".split(",")            # ['a', 'b', 'c']
"hello world".split()          # ['hello', 'world']  — default splits on any whitespace
",".join(['a', 'b', 'c'])       # "a,b,c"  — join is called ON the separator
"line1\nline2".splitlines()    # ['line1', 'line2']
```

### Replacing
```python
"3.1.4".replace('.', '', 1)    # "31.4" — max-count replace (last session's Q5 trick)
```

### Padding / Alignment
```python
"7".zfill(3)          # "007"
"hi".ljust(5, '-')     # "hi---"
"hi".rjust(5, '-')     # "---hi"
"hi".center(6, '*')    # "**hi**"
```

### Checking start/end
```python
"filename.py".endswith(".py")     # True
"https://x.com".startswith("https")  # True
```

---

## 5. String Formatting (3 ways — know all 3, you'll see all 3 in real code)

```python
name, age = "Soham", 20

# 1. f-strings (modern, preferred, Python 3.6+)
f"{name} is {age}"

# 2. .format()
"{} is {}".format(name, age)

# 3. % operator (old-style, still shows up in legacy code)
"%s is %d" % (name, age)
```

**f-string extras worth knowing:**
```python
f"{3.14159:.2f}"     # "3.14"     — round to 2 decimal places
f"{42:05d}"           # "00042"    — zero-pad to width 5
f"{name!r}"           # "'Soham'"  — repr instead of str
f"{age = }"           # "age = 20" — debug shortcut (3.8+), prints var name AND value
```

---

## 6. Strings Are Immutable — Common Trap

```python
s = "hello"
s[0] = "H"     # TypeError: 'str' object does not support item assignment
```
To "change" a character, you must build a new string:
```python
s = "H" + s[1:]     # "Hello"
```

---

## 7. Escape Sequences

| Sequence | Meaning |
|---|---|
| `\n` | newline |
| `\t` | tab |
| `\\` | literal backslash |
| `\'` `\"` | literal quote |
| `\r` | carriage return |

---

## 8. Extra Practice Angle (beyond last session)

Things to specifically stress-test yourself on, given your track record on Q3/Q4 last time:
- What happens with an **empty string** input to your parsing logic?
- What happens with a string that's **all whitespace**?
- Multi-digit / multi-word cases (you already know this bites you from the swap problem)
- Unicode / non-ASCII input (not core syllabus, but good to know `len()` counts characters, not bytes)

---

## Session Log — for continuity next time

**Date:** 2026-08-15
**Topic completed:** Topic 1 — Variables, Data Types & Type Casting (5/5 questions attempted)
- Q1 (easy): correct, minor formatting nitpick (missing period)
- Q2 (medium): logic correct but left commented out + label mismatch — needs a clean re-run
- Q3 (medium): integer/decimal parts correct; sign logic was buggy (fixed via `.startswith('-')` + boolean indexing)
- Q4 (medium): working swap via string-concat trick, but fragile for multi-digit differences — reinforced with the robust `a+b / a-b / a-b` arithmetic swap
- Q5 (hard): initial idea (`type(input())`) was a common misconception — `input()` always returns `str`; resolved with `.lstrip('-').isdigit()` / `.replace('.','',1)` pattern

**Extra ground covered:** `.lstrip()`/`.rstrip()`/`.strip()` mechanics, the `is*` string-check family, `.replace()`'s count argument.

**Next up:** Topic 2 — Operators & Expressions (5 questions: 1 easy / 3 medium / 1 hard), same one-at-a-time format. Strings topic (Topic 5) partially front-loaded via this guide — can move faster through it when we get there.
