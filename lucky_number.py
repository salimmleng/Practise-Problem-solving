n = int(input("Enter a number: ").strip())

x = n // 10  
y = n % 10 

if x % y == 0 or y % x == 0:
    print("YES")
else:
    print("NO")

