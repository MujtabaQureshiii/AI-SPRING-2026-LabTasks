def fibonacci_Series(n):
    fib_sequence = []
    a=0
    b=1
    while a <= n:
        fib_sequence.append(a)
        a, b =b, a + b      
    return fib_sequence

num = int(input("Enter a number: "))
print("Fibonacci sequence : ")
print(fibonacci_Series(num))
