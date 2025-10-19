my_dict1 = {"a" : 1 , "b" : 2 , "c" :3}
my_dict2 ={"d" : 4 ,"e" : 5}

modified_dict = my_dict1.copy()
modified_dict.update(my_dict2)

print("Updated Dict. :",modified_dict)

merged_pipe = my_dict1 | my_dict2
print("Merged using | operator:", merged_pipe)

merged_unpacking = {**my_dict1, **my_dict2}
print("Merged using unpacking:", merged_unpacking)