my_dict = { "a" : 1 , "b" : 2 , "c" : 3 ,"d" :4}

my_dict["e"] = 5
my_dict["f"] = 6
print("After insertion:", my_dict)

del my_dict["b"]
del my_dict["c"]
print("After deletion:", my_dict)

my_dict["b"] = 10
my_dict["c"] = 20
print("After re-insertion:", my_dict)