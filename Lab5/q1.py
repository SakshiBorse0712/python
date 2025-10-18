my_dict = {"Name":"Sakshi" , "Age":18 , "MIS":112415189}

print("Number of key-value pairs",len(my_dict))

for key,value in my_dict.items():
    print(f"Key: {key}")
    print(f"Hash value: {hash(key)}")
    print(f"Memory address of key: {id(key)}")
    print(f"Memory address of value: {id(value)}")
    print()