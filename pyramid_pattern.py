# Pattern 1: Number Pyramid
# A pyramid where each row contains the row number repeated

def pyramid_pattern(rows):
    print("=" * 30)
    print("   NUMBER PYRAMID PATTERN")
    print("=" * 30)
    for i in range(1, rows + 1):
        # Print leading spaces for pyramid shape
        spaces = " " * (rows - i)
        # Print numbers for current row
        numbers = (str(i) + " ") * i
        print(spaces + numbers)
    print()

pyramid_pattern(5)
