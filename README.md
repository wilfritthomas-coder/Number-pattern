# 🔢 Number Pattern Generator

**Task 2 – Cognifyz | Generate and Print Simple Number Patterns**

> Objective: Utilize loops to control the structure of number patterns.

---

## 📁 Project Structure

```
number_patterns/
├── main.py               # Runs all 3 patterns at once
├── pyramid_pattern.py    # Pattern 1: Number Pyramid
├── triangle_pattern.py   # Pattern 2: Right-Angled Triangle
├── square_pattern.py     # Pattern 3: Number Square
└── README.md             # Project documentation
```

---

## ▶️ How to Run

### Run all patterns at once:
```bash
python3 main.py
```

### Run individual patterns:
```bash
python3 pyramid_pattern.py
python3 triangle_pattern.py
python3 square_pattern.py
```

---

## 🔷 Pattern 1: Number Pyramid (`pyramid_pattern.py`)

Each row prints the row number repeated, centered to form a pyramid shape.

**Code Logic:**
- Outer loop controls the number of rows
- Leading spaces `(rows - i)` create the centering effect
- Row number `i` is repeated `i` times per row

**Sample Output (5 rows):**
```
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 
```

---

## 🔷 Pattern 2: Right-Angled Triangle (`triangle_pattern.py`)

Sequential numbers are printed row by row, forming a right-angled triangle.

**Code Logic:**
- Outer loop controls the number of rows
- Inner loop prints numbers for each column in that row
- A running counter `num` increments continuously across all rows

**Sample Output (5 rows):**
```
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
```

---

## 🔷 Pattern 3: Number Square (`square_pattern.py`)

Sequential numbers fill a square grid with aligned columns.

**Code Logic:**
- Outer loop controls rows, inner loop controls columns
- `f"{num:3}"` formats numbers with fixed width for neat alignment
- Counter increments with each cell

**Sample Output (5×5):**
```
  1   2   3   4   5 
  6   7   8   9  10 
 11  12  13  14  15 
 16  17  18  19  20 
 21  22  23  24  25 
```

---

## 🛠️ Requirements

- Python 3.x (no external libraries needed)

---

## 📌 Key Concepts Used

| Concept | Usage |
|---|---|
| `for` loop | Controls rows and columns |
| Nested loops | Builds 2D pattern structure |
| String multiplication | Repeats numbers in pyramid |
| `end=" "` in print | Keeps output on the same line |
| f-string formatting | Aligns numbers in the square |
| Running counter | Sequential numbering in triangle & square |

---

*Cognifyz Internship Task 2 – Number Pattern Generator*
