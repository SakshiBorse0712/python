def append_items(item,item_list = None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

print(append_items(10))
print(append_items(20))
print(append_items(30))
print(append_items(40))
print(append_items(50))