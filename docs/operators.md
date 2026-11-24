# Operators Across Programming Languages

Reference for common operators found in most languages (Python, C/C++, Java, JavaScript/TypeScript, Go, Rust, etc.) with notes on where they differ.

---

## 1. Arithmetic Operators

| Operator | Meaning | Example | Notes |
|----------|---------|---------|-------|
| `+` | Addition | `a + b` | Also string/list concatenation in some languages |
| `-` | Subtraction | `a - b` | Unary negation: `-a` |
| `*` | Multiplication | `a * b` | Also repetition in Python (`"ab" * 3`) |
| `/` | Division | `a / b` | Python 3: true division (float). C/Java: int division if both ints |
| `//` | Floor division | `a // b` | Python-specific; rounds toward negative infinity |
| `%` | Modulo / remainder | `a % b` | Sign of result varies by language (Python: sign of divisor; C: sign of dividend) |
| `**` | Exponentiation | `a ** b` | Python. C uses `pow(a, b)`; JavaScript uses `a ** b` |
| `^` | XOR (not power!) | `a ^ b` | **Careful:** `^` is bitwise XOR in C/Java/Python, not exponent |

### Integer division pitfalls
- Python 3: `7 / 2 = 3.5`, `7 // 2 = 3`, `-7 // 2 = -4`
- C/C++/Java: `7 / 2 = 3`, `-7 / 2 = -3` (truncates toward zero)

---

## 2. Assignment Operators

| Operator | Meaning | Equivalent |
|----------|---------|------------|
| `=` | Simple assignment | `a = b` |
| `+=` | Add and assign | `a = a + b` |
| `-=` | Subtract and assign | `a = a - b` |
| `*=` | Multiply and assign | `a = a * b` |
| `/=` | Divide and assign | `a = a / b` |
| `%=` | Modulo and assign | `a = a % b` |
| `//=` | Floor divide and assign (Python) | `a = a // b` |
| `**=` | Power and assign (Python/JS) | `a = a ** b` |
| `&=` | Bitwise AND and assign | `a = a & b` |
| `\|=` | Bitwise OR and assign | `a = a \| b` |
| `^=` | Bitwise XOR and assign | `a = a ^ b` |
| `<<=` | Left shift and assign | `a = a << b` |
| `>>=` | Right shift and assign | `a = a >> b` |

### Walrus operator (`:=`)
Python 3.8+ assignment expression: `if (n := len(nums)) > 0:`. Assigns and returns the value in one expression.

---

## 3. Comparison / Relational Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

### Equality vs identity
- `==` compares **values** (equality).
- `is` (Python) / `===` (JS strict) compares **identity** (same object in memory).

```python
a = [1, 2]
b = [1, 2]
a == b   # True  (same contents)
a is b   # False (different objects)
```

---

## 4. Logical Operators

| Operator | Meaning | Short-circuits? |
|----------|---------|-----------------|
| `and` / `&&` | Logical AND | Yes (stops at first falsy) |
| `or` / `\|\|` | Logical OR | Yes (stops at first truthy) |
| `not` / `!` | Logical NOT | N/A |

### Truthiness
- Python: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False` are falsy; everything else truthy.
- C/C++: `0` and `NULL` are false; non-zero is true.
- JavaScript: `0`, `""`, `null`, `undefined`, `NaN`, `false` are falsy.

---

## 5. Bitwise Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `&` | Bitwise AND | `5 & 3` → `1` |
| `\|` | Bitwise OR | `5 \| 3` → `7` |
| `^` | Bitwise XOR | `5 ^ 3` → `6` |
| `~` | Bitwise NOT (complement) | `~5` → `-6` (two's complement) |
| `<<` | Left shift | `5 << 1` → `10` |
| `>>` | Right shift | `5 >> 1` → `2` |
| `>>>` | Unsigned right shift | JavaScript only |

### Common bit tricks
- `x & 1` — check if `x` is odd (equivalent to `x % 2 != 0` for non-negative ints)
- `x & (x - 1)` — clears the lowest set bit
- `x & -x` — isolates the lowest set bit
- `1 << n` — `2^n`
- `x >> 1` — `x // 2` for non-negative ints
- `x ^ y` — swaps without temp (with three XORs), finds missing number in array

---

## 6. Membership & Identity Operators

| Operator | Meaning | Languages |
|----------|---------|-----------|
| `in` | Value is in container | Python |
| `not in` | Value is not in container | Python |
| `is` | Same object (identity) | Python |
| `is not` | Not same object | Python |

---

## 7. Ternary / Conditional Operators

| Language | Syntax | Example |
|----------|--------|---------|
| C / C++ / Java / JS | `cond ? a : b` | `x = a > b ? a : b` |
| Python | `a if cond else b` | `x = a if a > b else b` |
| Ruby | `cond ? a : b` | same as C |
| Go | No ternary | Use `if/else` |

---

## 8. Other Common Operators

| Operator | Meaning | Notes |
|----------|---------|-------|
| `.` | Member access | `obj.attr`, `obj.method()` |
| `[]` | Indexing / subscription | `arr[i]`, `dict[key]` |
| `()` | Function call / grouping | `foo()` |
| `?:` | Null coalescing (C# / TS / PHP) | `a ?? b` (use `b` if `a` is null) |
| `?.` | Optional chaining (TS / JS / C#) | `a?.b` (undefined if `a` is null) |
| `...` | Spread / rest (JS / TS / Python) | `[...arr]`, `def f(*args)` |
| `:` | Slicing (Python) | `arr[1:5]`, `arr[::-1]` |
| `->` | Return type annotation | Python type hints |
| `|` | Union type | `int \| None` (Python 3.10+) |
| `&` | Intersection type | TypeScript `A & B` |

---

## 9. Operator Precedence (High to Low)

Common order across most C-family languages and Python:

1. `()` — grouping / function call
2. `[]`, `.` — subscription / member access
3. `**` — exponentiation (right-associative)
4. `~`, `+`, `-` (unary) — bitwise NOT / unary plus/minus
5. `*`, `/`, `//`, `%` — multiplication/division
6. `+`, `-` — addition/subtraction
7. `<<`, `>>` — shifts
8. `&` — bitwise AND
9. `^` — bitwise XOR
10. `\|` — bitwise OR
11. `==`, `!=`, `>`, `<`, `>=`, `<=` — comparisons
12. `is`, `is not`, `in`, `not in` — identity/membership (Python)
13. `not` / `!` — logical NOT
14. `and` / `&&` — logical AND
15. `or` / `\|\|` — logical OR
16. `if-else` / `?:` — conditional (ternary)
17. `=`, `+=`, etc. — assignment (right-associative)

**When in doubt, use parentheses.** They make intent clear and prevent precedence bugs.

---

## 10. Language-Specific Gotchas

| Gotcha | Languages | Advice |
|--------|-----------|--------|
| `^` is XOR, not power | C, C++, Java, Python | Use `**` or `pow()` for exponentiation |
| `/` truncates integers | C, C++, Java, Go | Cast to float/double if you want real division |
| `%` with negatives | C vs Python differ | Python: `-7 % 3 = 2`; C: `-7 % 3 = -1` |
| `>>` arithmetic vs logical | C/Java vs JS `>>>` | Java's `>>` preserves sign bit; `>>>` is unsigned |
| `===` vs `==` | JavaScript | Always prefer `===` to avoid type coercion |
| `and`/`or` return operands, not booleans | Python | `[] or [1]` returns `[1]`; `[1] or [2]` returns `[1]` |
| `is` for integers | Python | Small ints are cached (`257 is 257` may be `False`); use `==` for value comparison |

---

## Quick Cheat Sheet

```python
# Arithmetic
a + b   a - b   a * b   a / b   a // b   a % b   a ** b

# Assignment
a += b   a %= b   (n := len(x))

# Comparison
a == b   a != b   a > b   a < b   a >= b   a <= b

# Logical
a and b   a or b   not a

# Bitwise
a & b   a \| b   a ^ b   ~a   a << b   a >> b

# Membership / Identity
x in lst   x not in lst   a is b   a is not b

# Ternary
y = a if cond else b     # Python
y = cond ? a : b         # C/Java/JS

# Types
int \| None              # Union (Python 3.10+)
```
