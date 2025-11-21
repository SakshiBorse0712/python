n = 20

def fun():
    global n
    n = 10
    
print(n)
fun()
print(n)