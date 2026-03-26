# Pattern 3: Number Square
# A square grid filled with sequential numbers

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

square_pattern(5)
