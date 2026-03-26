# =============================================
#   Task 2: Generate and Print Number Patterns
#   Objective: Use loops to control structure
# =============================================

def pyramid_pattern(rows):
    print("=" * 30)
    print("   NUMBER PYRAMID PATTERN")
    print("=" * 30)
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        numbers = (str(i) + " ") * i
        print(spaces + numbers)
    print()

def right_triangle_pattern(rows):
    print("=" * 30)
    print("  RIGHT-ANGLED TRIANGLE PATTERN")
    print("=" * 30)
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()
    print()

def square_pattern(size):
    print("=" * 30)
    print("    NUMBER SQUARE PATTERN")
    print("=" * 30)
    num = 1
    for i in range(size):
        for j in range(size):
            print(f"{num:3}", end=" ")
            num += 1
        print()
    print()

# ----------- Run All Patterns -----------
print("\n*** NUMBER PATTERN GENERATOR ***\n")
pyramid_pattern(5)
right_triangle_pattern(5)
square_pattern(5)
print("*** All patterns generated successfully! ***")
