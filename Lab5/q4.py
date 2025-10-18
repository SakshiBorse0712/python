my_dict = { "Name" : "Sakshi" , "Age" : 18 , "MIS" : 112415189}

keys = my_dict.keys()
value = my_dict.values()
item = my_dict.items()

print("Initial views:")
print("Keys:", keys)
print("Values:", value)
print("Items:", item)

my_dict["Name"] = "a"
my_dict["Age"] = 20
my_dict["MIS"] = 100000

print("After views:")
print("Keys:", keys)
print("Values:", value)
print("Items:", item)