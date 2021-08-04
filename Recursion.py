def factorial_by_recursion(n):
    if n == 0:
        return 1
    return n * factorial_by_recursion(n-1)

def factorial_without_recursion(n):
    factorial = 1
    
    while n > 0:
        factorial = factorial * n
        n = n - 1
    return factorial


#run rabit run
print(f"With recursion {factorial_by_recursion(5)}")
print(f"without recursion {factorial_without_recursion(5)}")