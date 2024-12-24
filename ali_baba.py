
a, b, c, d = map(int, input("Enter four numbers separated by spaces: ").split())

if (a + b - c == d or
    a - b + c == d or
    a * b - c == d or
    a * b + c == d or
    a + b * c == d or
    a - b * c == d):
    print("YES")
else:
    print("NO")