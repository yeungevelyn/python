# product_code = "377B"
# product_name = "Beef Liquid Stock"
# product_size = "250mL"
# product_price = 2.15

# print(product_code+": "+product_name+", "+product_size)

# print('"'+product_name+'", '+product_size)

# print(product_name+", "+product_size+", $"+str(product_price))

# Under 6: free
# 6 to 17: $7
# Adult: $20

# Welcome to Ocean World.
# How many tickets for children under 6? 2
# How many tickets for children age between 6-17? 3
# How many tickets for adults? 2
# Receipt:
# Number of tickets: 7
# Total cost $61

# print("Welcome to Ocean World. ")
# children_under_six = input("How many tickets for children under 6? ")
# children_between_six_and_seven = input("How many tickets for children age between 6-17? ")
# adults = input("How many tickets for adults? ")
# #calculate tickets and cost
# tickets_number = int(children_under_six)+int(children_between_six_and_seven)+int(adults)
# cost = int(children_between_six_and_seven)*7+int(adults)*20
# #print Receipt
# print("Receipt: ")
# print("Number of tickets: "+str(tickets_number))
# print("Total cost $"+str(cost))



# Enter the first integer: 10
# Enter the second integer: 1
# Enter the third integer: 2
# Here is the equation:
# 10x10 + 1x1 + 2x2 = 100 + 1 + 4 = 105

integer1 =input("Enter the first integer: ")
integer2 = input("Enter the second integer: ")
integer3 = input("Enter the third integer: ")
#calculate
integer1_square = int(integer1)*int(integer1)
integer2_square = int(integer2)*int(integer2)
integer3_square = int(integer3)*int(integer3)
total = integer1_square+integer2_square+integer3_square
#print
print("Here is the equation: ")
print(integer1+"x"+integer1+" + "+integer2+"x"+integer2+" + "+integer3+"x"+integer3,end=" = ")
print(str(integer1_square)+" + "+str(integer2_square)+" + "+str(integer3_square),end=" = ")
print(str(total))
