numbers=[]
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in numbers:
    if prime(num):
        print(num,"is a Prime number")
    else:
        print(num,"is NOT a Prime number")
