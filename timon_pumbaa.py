a, b = map(int, input("Enter two numbers separated by space: ").split())
ans = a - b
if ans >= 0:
    print(ans)
else:
    print(0)