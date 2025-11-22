def memoize_factorial():
    cache = {}   

    def factorial(n):
        if n in cache:
            return cache[n]        

        if n == 0 or n == 1:
            cache[n] = 1
        else:
            cache[n] = n * factorial(n - 1)  

        return cache[n]

    return factorial   


fact = memoize_factorial()

print(fact(5))   
print(fact(5))   
print(fact(6))   