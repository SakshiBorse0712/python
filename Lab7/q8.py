def sample():
    x = 10
    s = "string"    

def count_local_variable(fun):
    return fun.__code__.co_nlocals


print(f"No. of local variables : ",count_local_variable(sample))