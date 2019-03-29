def fibonacci(n):
    first = 0
    second = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 0:
        print(first)
    elif n == 1:
        print(second)
    else:
        print(first, ",", second, end=", ")
        for i in range(2,n):
            next = first + second
            print(next, end =", ")
            first = second
            second = next
num = int(input("Enter the value of N : "))
print("Fibonacci Series till ",num, "digits : ")
fibonacci(num)
