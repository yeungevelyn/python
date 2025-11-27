# for i in range (1,11):
#     print("{:>2} + {:>2} = {:>2}".format(i,i,i+i))

# for i in range (1,11):
#     char=""
#     if i==10:
#         char = "."
#     else:
#         char = " - "
#     print(i,end=char)

# for i in range (1,11):
#     char =""
#     if i !=10:
#         char = " : "
#     print(i,end=char)

# for i in range (1,6):
#     char = ""
#     if i == 5:
#         char = "."
#     else:
#         char = ", "
#     print(2*i,end=char)


# for i in range (0,5):
#     char = ""
#     if i == 4:
#         char = "."
#     else:
#         char ="; "
#
#     print(2*i+1,end=char)



for i in range (1,10):
    for j in range (1,i+1):
        char = ""
        if j == i:
            char = None
        print(j,end=char)