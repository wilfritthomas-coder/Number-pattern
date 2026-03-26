# Pattern 2: Right-Angled Triangle
# Numbers printed sequentially row by row

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

right_triangle_pattern(5)
