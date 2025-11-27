class Staff:#{
    def __init__(self,staff_number,first_name,last_name,email):#{
        self.staff_number = staff_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        #}
    def print_details(self, width):

    # {
        #display first line
        # write your code here
        length = len("| |")
        print("-" * width)
        # display second line
        print("| {0:{1}}|".format("Staff number: " + self.staff_number, width - length))
        # display third line
        name = self.first_name + " " + self.last_name
        print("| {0:{1}}|".format(name, width - length))
        # display forth line
        print("| {0:{1}}|".format(self.email, width - length))
        # display fifth line
        print("-" * width)
    # }

    #}
        #creat objects
        # staffObj1 = Staff(100001,"John","Lee","jl123@gmail.com")
        # staffObj2 = Staff(100002, "Mary", "Zheng", "maryz@gmail.com")
        # staffObj3 = Staff(100003, "Cindy", "Wilson", "cw456@hotmail.com")

staffObj = Staff("012345", "John", "Smith", "js@gmail.com")
staffObj.print_details(40)