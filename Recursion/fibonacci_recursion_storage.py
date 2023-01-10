# to store the first 'n' finonacci numbers

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

l = []

for i in range(int(input("Enter n : "))):
    l.append(fib(i))

print(l)