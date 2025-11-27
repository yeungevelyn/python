# #question1
# #get user input
# word = input("Enter a word: ")
# integer1 = input("Enter an integer: ")
# option = input("Enter display option (next/pre): ")
# integer2 = 0
# #calcuate result
# if(option == "next"):
#     integer2 = int(integer1)+1;
# else:
#     integer2 = int(integer1) - 1;
# #output
# print("012345678901234567890123456789")
# print("|{:^15}|{:>5}|{:>5}|".format("word","int",option))
# print("|{:^15}|{:>5}|{:>5}|".format(word,integer1,integer2))
# print("012345678901234567890123456789")

#question2
# print("Product A: $10/per item")
# print("Product B: $15/per item")
# print("Discount $5 if buy >= $30")
# print()
# #get user input
# amount_of_A = input("How many product A? ")
# amount_of_B = input("How many product B? ")
# amount_of_A_int = int(amount_of_A)
# amount_of_B_int = int(amount_of_B)
# #calculate cost
# cost_of_A = amount_of_A_int*10
# cost_of_B = amount_of_B_int*15
# total_cost = cost_of_A+cost_of_B
# discount = 0
# payment = 0
# #calculate discount
# if total_cost>=30:
#     discount = 5
#     payment = total_cost-discount
# #print output
# print("Product A cost: {} x ${} = ${}".format(amount_of_A,"10",cost_of_A))
# print("Product B cost: {} x ${} = ${}".format(amount_of_B,"15",cost_of_B))
# print("Total cost: ${} + ${} = ${}".format(cost_of_A,cost_of_B,total_cost))
# print("Discount: ${} - ${} = {}".format(total_cost,discount,payment))
# print("Please pay ${}".format(payment))



# question3
multiplier = input("Enter multiplier: ")
start = input("From: ")
start_int = int(start)
end = input("To: ")
end_int = int(end)
print()
#print timestable
print("Here is timestable")
print("CAT1234567890123456DOG")
for i in range(start_int,end_int+1):
    #calculate result
    result = i * int(multiplier)
    formula = "{} x {} = {}".format(multiplier,i,result)
    # print(formula)
    print("{:3} {:>14} {:3}".format("CAT",formula,"DOG"))
print("CAT1234567890123456DOG")
