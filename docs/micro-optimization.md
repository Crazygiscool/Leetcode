# Micro-Optimizations

Used after the most algorithmically optimized solution is found.

## Scope & Order of Operations

1. **Algorithm first.** Big-O wins every time. A O(n) solution with slight overhead beats an O(n²) micro-optimized solution.
2. **Profile then optimize.** Measure where time actually goes before changing code (e.g., `cProfile`, `timeit`, or LeetCode's runtime).
3. **Micro-optimize last.** These changes shave constant factors and interpreter overhead; they do not change complexity.

---

## Python-Specific Micro-Optimizations

### 1. Remove Type Hints on Hot Paths
Annotations like `nums: list[int]`, `seen: dict[int, int]`, and `-> list[int]` carry subscription and lookup cost. Strip them from performance-critical methods:

```python
# Before
def twoSum(self, nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

# After
def twoSum(self, nums, target):
    seen = {}
```

### 2. Prefer Local Variable Lookups
Local variables are faster than globals, builtins, attributes, and cell variables. Cache repeated lookups:

```python
# Slower
for i in range(len(nums)):
    if nums[i] in seen:   # nums and seen are looked up each iteration
        ...

# Faster
_nums = nums
_seen = seen
for i in range(len(_nums)):
    if _nums[i] in _seen:
        ...
```

### 3. Avoid `enumerate` Tuple Unpacking (Test Both)
`enumerate(nums)` creates and unpacks a tuple every iteration. On some Python versions, `range(len(...))` with direct indexing is faster; on others it's comparable. Benchmark your specific loop:

```python
# Option A
for i, num in enumerate(nums):
    ...

# Option B (often tighter in CPython)
for i in range(len(nums)):
    num = nums[i]
    ...
```

For leet code purposes, its usually faster and cleaner to use enumerate

### 4. Short Local Names
Shorter names don't change algorithmic speed, but they reduce bytecode length slightly and keep everything local:

```python
d = {}
n = nums[i]
c = target - n
if c in d:
    return [d[c], i]
```

### 5. `dict.setdefault` / `in` vs `try/except KeyError`
For membership checks, `key in dict` is fastest. Avoid `dict.get()` when you only need existence, and avoid `try/except KeyError` unless exceptions are truly rare (exception setup/teardown is expensive).

### 6. List Comprehensions vs `map` / Loops
List comprehensions run at near-C speed inside the interpreter and usually beat manual `for` loops with `.append()`:

```python
# Slower
res = []
for x in items:
    res.append(f(x))

# Faster
res = [f(x) for x in items]
```

For simple transformations, `map(f, items)` can be comparable or faster because it avoids the Python-level loop frame entirely, but materializing it (`list(map(...))`) adds cost.

### 7. Avoid Function Call Overhead in Tight Loops
Each Python function call creates a frame. Inline small helpers inside hot loops, or hoist them out so they're called once per outer iteration instead of once per element.

### 8. Use `@staticmethod` or Module-Level Functions
If the LeetCode template permits, `@staticmethod` avoids binding `self` and the bound-method lookup. Module-level functions are even faster (no `self` at all), but LeetCode's class template usually requires instance methods.

### 9. String Building: `"".join()` Over `+=`
For repeated concatenation in a loop, build a list and `"".join()` once. `+=` on strings creates a new object each time (O(n²)):

```python
# Slower
s = ""
for x in parts:
    s += x

# Faster
s = "".join(parts)
```

### 10. Prefer Builtins Implemented in C
`sorted()`, `sum()`, `max()`, `min()`, `any()`, `all()`, `set()`, and `dict` comprehensions run C loops and beat equivalent Python loops.

### 11. Integer / Bitwise Tricks
Where semantically valid:
- `x // 2` → `x >> 1`
- `x % 2` → `x & 1`
- `2 ** n` → `1 << n`

Only use these when they don't harm readability or correctness (e.g., with negative numbers, `>>` and `&` behave differently than `/` and `%`).

---

## Language-Agnostic Principles

| Principle | Why it helps |
|-----------|--------------|
| Hoist loop invariants | Compute outside the loop what doesn't change per iteration |
| Short-circuit evaluation | Order conditions so cheap/failing checks run first |
| Branch prediction | Sort hot branches so the common case is the `if` (Python doesn't have static branch hints, but ordering still matters for interpreter flow) |
| Avoid allocation in loops | Reuse containers instead of creating new objects each iteration |
| Cache-friendly access | Access memory linearly where possible (more relevant in C/C++/Rust than Python) |

---

## What Micro-Optimization Cannot Do

- **Cannot change Big-O.** If your algorithm is O(n²), micro-optimizing won't make it pass a large input.
- **Cannot guarantee LeetCode runtime < X ms.** LeetCode's reported time includes interpreter startup, harness overhead, and variance between runs. Python3 submissions for Two Sum typically land ~40–70 ms even when optimally written. Sub-17 ms usually requires a compiled language (C++, Rust, Go, etc.).

---

## Recommended Workflow

1. Write the cleanest algorithmically-optimal solution.
2. Submit and record runtime.
3. Profile locally if possible.
4. Apply one micro-optimization at a time; measure after each.
5. Stop when gains plateau or readability suffers unacceptably.
