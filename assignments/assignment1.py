#question1
# name = input("Enter a name: ")
# integer = input("Enter an integer: ")
# #print
# print()
# print("I am {}!".format(name))
# print("{} I am!".format(name))
# print("Here are some nerdy facts about {}.".format(integer))
# print("{} plus {} is {}.".format(integer,1,int(integer)+1))
# print("{} minus {} is {}.".format(integer,1,int(integer)-1))
# print("{} times {} is {}.".format(integer,integer,int(integer)*int(integer)))
# print("{} modulo {} is {}.".format(integer,2,int(integer)%2))
# print("{} modulo {} is {}.".format(integer,10,int(integer)%10))
# print("Good bye!")

#question2
# name = input("Please enter a name: ")
# friend = input("Enter a friend: ")
# #print
# print("0123456789012345678901234567890")
# print("|{:>10}|{:>10}| {:<7}".format(name,friend,"SHARK"))
# print("|{:>10}|{:>10}| {:<7}".format(friend,name,"SHARK"))
# print("|{:<10}|{:<10}| {:<7}".format(name,friend,"EMU"))
# print("|{:<10}|{:<10}| {:<7}".format(friend,name,"EMU"))
# print("0123456789012345678901234567890")
# print("Good bye!")


#quesiton3
# print("Ask user for string format pattern with index 0,1,2.")
# pattern = input("Enter a pattern: ")
# value1 = input("Enter value for {0}: ")
# value2 = input("Enter value for {1}: ")
# value3 = input("Enter value for {2}: ")
# #print output
# print("Here is the pattern {}".format(pattern))
# print("Apply string format we get: ")
# print(pattern.format(value1,value2,value3))

#question4
# name = input("Enter a name: ")
# number = input("Enter a number: ")
# #calculate
# add_number = int(number)+1
# mins_number = int(number)-1
# line1 = "{}{}+{}={}".format(name,number,1,add_number)
# line2 = "{}-{}={}{}".format(number,1,mins_number,name)
# line3=  "{}{}".format(name,number)
# #print
# print("0123456789012345678901234567890")
# print("|{0:>20}|".format(line1))
# print("|{0:<20}|".format(line2))
# print("|{0:^20}|".format(line3))
# print("0123456789012345678901234567890")


#question5
# print("Quantum Computer server booking.")
# name = input("Please enter computer name: ")
# user_name = input("Please enter your name: ")
# minutes = input("Enter number of minutes: ")
# #calculate
# hour = int(minutes)//60
# minute = int(minutes)%60
# print()
# #print output
# print("Here is the booking script:")
# print("{}.booking <<<".format(name))
# print("{:>2}register_name('{}');".format("",user_name))
# print("{:>2}booking_time(hour={}, minute={});".format("",hour,minute))
# print("{:>2}send_request();".format(""))
# print(">>>")