# question2
# num = input("How many square numbers to generate? ")
# num_int =  int(num)
# square_list = []
# for i in range(0,num_int):
#     #get square
#     square = i**2
#     square_list.append(square)
# print("Here is a list of generated squares: {}".format(square_list))

#question3
#init a list
# int_list = []
# while True:
#     #get input
#     user_input = input("Enter an integer (enter QUIT to quit): ")
#     if(user_input == "QUIT"):
#         #quit
#         break
#     user_input_int = int(user_input)
#     int_list.append(user_input_int)
# print("You have entered: ",end="")
# for i in range (0,len(int_list)):
#     if (i==len(int_list)-1):
#         print(int_list[i], end=".")
#     else:
#         print(int_list[i], end=", ")

#question4
# numbers = input("How many Fibonacci numbers to generate? ")
# # init a list
# fibo_list = []
# for i in range(0,int(numbers)):
#     if i == 0:
#         fibo_list.append(0)
#     elif i == 1:
#         fibo_list.append(1)
#     else:
#         num1 = fibo_list[i-2]
#         num2 = fibo_list[i-1]
#         new_num = num1+num2
#         fibo_list.append(new_num)
# print("Here is a list of generated Fibonacci numbers: {}".format(fibo_list))

#question5
from queue import LifoQueue
def match_check(character):
    if character=="}":
        return "{"
    elif character=="]":
        return "["
    elif character==")":
        return "("
def math_expression_checking(expression):
    valid = False
    stack = LifoQueue()
    #for-each  character for the input
    for item in expression:
        if item == "{" or item == "[" or item == "(":
            stack.put(item)
        elif item == "}" or item == "]" or item == ")":
            #if stack is empty that means expression is wrong
            if stack.empty():
                return valid
            stack.get(match_check(item))
    #determine stack length
    if stack.empty():
        valid = True

    return valid

# print(math_expression_checking(expression="x+y"))

# print(math_expression_checking(expression="(x+y"))
#
# print(math_expression_checking(expression="(x+y)"))
#
# print(math_expression_checking(expression="x+y)"))
#
# print(math_expression_checking(expression="[(x+y) + z]*a"))
#
# print(math_expression_checking(expression="[(x+y) + z]* {a+b}"))
#
# print(math_expression_checking(expression="[[(x+y) + z]* {a+b}"))
#
# print(math_expression_checking(expression="[[(x+y) + z]* {a+b}] + 3"))