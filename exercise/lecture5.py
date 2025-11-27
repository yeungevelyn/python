# for i in range (2,9):
#     print(i)

# for i in range (1,10):
#     print("{} x {} = {}".format(6,i,6*i))

# num = input("Enter a number: ")
# num_int = int(num)
# for i in range(1,10):
#     print("{} x {} = {}".format(num,i,num_int*i))

# for i in range (0,11):
#     print("{} + {} = {}".format(i,10-i,10))

# sum = 0
# for i in range(2,21):
#   sum = sum+i
# print("The sum of {} to {} is {}".format(2,20,sum))

# word = input("Enter a sentence: ")
# for item in word:
#     print(item)


username = input("Enter username: ")
#init psw
password =""
for i in range(0,len(username)):
    letter = username[i]
    if(letter == "i" or letter == "I"):
        password_letter= "1"
    elif(letter == "r" or letter == "R"):
        password_letter= "7"
    elif(letter == "s" or letter == "S"):
        password_letter = "5"
    elif(letter == "z" or letter =="Z"):
        password_letter="2"
    else:
        password_letter=letter
    #adding a character
    password = password + password_letter
print("Password is {}".format(password))


# for i in range(0,10):
#     flag = input("Would you like green eggs and ham? (Y/N): ")
#     if flag == "Y":
#         break

