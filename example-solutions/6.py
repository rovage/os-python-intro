# Part 1
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
            
fizzbuzz(16)

# Part 2

some_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print ([x for x in some_fib if (x % 2 == 0 or x % 5 == 0)])  
