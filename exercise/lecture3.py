# quantity  = input("Enter the quantity: ")
# quantity_int = int(quantity)
# #calculate price
# price = 0
# postage = 0
# total = 0
# if quantity_int>=1 and quantity_int<=50:
#     price = 3
#     postage = 10
# else:
#     price = 2
# total = quantity_int * price + postage
# print("Total cost: ${}".format(total))

# mark = int(input("Please enter mark: "))
# grade = ""
# if 80<=mark<=100:
#     grade = "A"
# elif 60<=mark<=79 :
#     grade ="B"
# elif 40<=mark<=59:
#     grade = "C"
# elif 0<= mark <=39:
#     grade = "D"
# print("Mark {}, Grade {}".format(mark,grade))





integer1 = int(input("Enter the 1st integer: "))
integer2 = int(input("Enter the 2nd integer: "))
integer3 = int(input("Enter the 3rd integer: "))

#determine max
max = integer1
if integer2 > max:
    max = integer2
if integer3 > max:
    max = integer3
print("Max of {}, {}, {} is {}".format(integer1,integer2,integer3,max))