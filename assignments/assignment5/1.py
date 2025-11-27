#get input from user
records_number = int(input("Enter number of records: "))
#create an empty dictionary
item_map={}
#put user input into dictionary
for i in range(0,records_number):
    name = input("Enter name: ")
    quantity = int(input("Enter quantity: "))
    if quantity <0:
        quantity=0
    #check whether key is multipule
    all_key = item_map.keys();
    if all_key.__contains__ (name):
        old_quantity = item_map.get(name)
        item_map[name] = old_quantity+quantity
    else:
        item_map[name] = quantity
print()
queries_number = int(input("Enter number of queries: "))
#search in dictionary
for i in range(0,queries_number):
    name = input("Query name: ")
    quantity = item_map.get(name,0)
    print("{}: {}".format(name,quantity))
#calculate total
#get all keys
all_item = item_map.keys()
unique = 0
for key in all_item:
    #get item value
    item_quantity = item_map.get(key)
    if item_quantity != 0:
        unique += 1
#get all values
all_values = item_map.values()
total_quantity = 0
for value in all_values:
    total_quantity = total_quantity + value
print()
print("Total unique items: {}".format(unique))
print("Total quantity: {}".format(total_quantity))