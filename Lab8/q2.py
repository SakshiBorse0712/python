def create_pipeline(functions):
    def pipeline(value):
        for func in functions:
            value = func(value)  
        return value
    return pipeline

def add2(x):
    return x + 2

def multiply3(x):
    return x * 3

def subtract1(x):
    return x - 1

pipeline = create_pipeline([add2, multiply3, subtract1])

print(pipeline(5))  