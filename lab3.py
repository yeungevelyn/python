# itmes = input("Enter the number of items: ")
# items_number = int(itmes)
# # calcualte price and postage
# postage = 0
# price = 0
# cost = 0
# total = 0
# if( items_number <= 50 and items_number >=1):
#     price = 3
#     postage = 10
#     # calcaulate price
#     cost = items_number * price
#     total = cost + 10
# elif(items_number>50):
#     price = 2
#     # calcaulate price
#     cost = items_number * price
#     total = cost
#
# print()
# #print receipt
# print("Receipt: ")
# print("{} items x ${} = ${}".format(itmes,price,cost))
# print("Postage: ${}".format(postage))
# print("Total: ${}".format(total))



# items = input("Enter the number of items: ")
# items_number = int(items)
# shipping_method = input("Enter shipping method (s/r/e): ")
# print()
# #calculate postage
# postage = 0
# post = ""
# if (items_number<=50 and items_number>=1 and shipping_method == "s"):
#     postage = 10
#     post = "Standard post"
# elif(items_number<=50 and items_number>=1 and shipping_method == "r"):
#     postage = 15
#     post = "Registered post"
# elif(items_number<=50 and items_number>=1 and shipping_method == "e"):
#     postage = 20
#     post = "Express post"
# elif(items_number>50 and shipping_method=="s" ):
#     postage = 0
#     post = "Standard post"
# elif(items_number>50 and shipping_method=="r"):
#     postage=10
#     post = "Registered post"
# elif(items_number>50 and shipping_method=="e"):
#     postage=17
#     post = "Express post"
# #calculate price
# total =0
# price =0
# amount_price = 0
# if(items_number<=50 and items_number>=1):
#     price = 3
#     amount_price
# else:
#     price = 2
# amount_price = items_number * price
# total = amount_price + postage
# #print recepit
# print("Receipt:")
#
# print("{} items x ${} = ${}".format(items,price,amount_price))
# print("{}: ${}".format(post,postage))
# print("Total: ${}".format(total))

integer1 = int(input("Enter the first integer: "))
integer2 = int(input("Enter the second integer: "))
integer3 = int(input("Enter the third integer: "))
integer4 = int(input("Enter the fourth integer: "))
#determine the minimum number
#assume integer1 is minimum number
#assume integer4 is maximum number
minimum = integer1
maximum = integer4
if integer2 < minimum:
    minimum = integer2
if integer3 < minimum:
    minimum = integer3
if integer4 < minimum:
    minimum = integer4

if integer1 > maximum:
    maximum = integer1
if integer2 >  maximum:
    maximum = integer2
if integer3> maximum:
    maximum = integer3
print()
print("The minimum number is {} and the maximum number is {}.".format(minimum,maximum))