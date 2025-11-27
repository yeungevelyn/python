# num = input("Enter an integer: ")
# try:
#     num_int = int(num)
#     print("You have entered {}".format(num_int))
# except ValueError as e:
#     print("You have entered an invalid input")
#

# try:
#     try:
#         # get first integer
#         num1 = input("Enter the 1st integer: ")
#         num1_int = int(num1)
#         # get second integer
#         num2 = input("Enter the 2nd integer: ")
#         num2_int = int(num2)
#     except: raise ValueError("You have entered an invalid input")
#
#     if (num2_int==0):
#         raise ValueError("The second number must be non-zero")
#     result = num1_int / num2_int
#     print("{} / {} = {}".format(num1_int,num2_int,result))
# except ValueError as e:
#     print(str(e))

# try:
#     num = input("Enter a positive integer: ")
#     try:
#         num_int = int(num)
#     except:
#         raise ValueError("You have entered an invalid input")
#     if num_int <0:
#         raise ValueError("You must enter a positive integer")
#     print("You have entered {}".format(num_int))
# except ValueError as e:
#     print(str(e))

while True:
    #get input
    try:
        num = input("Enter a positive integer: ")
        #valiad the value
        try:
            num_int = int(num)
        except:
            raise ValueError ("Input is not an integer")
        if(num_int <=0 ):
            raise ValueError("Input is not a positive integer")
        #when input is a positive integer
        print("You have entered {}".format(num_int))
        break
    except ValueError as e:
        print(str(e))


