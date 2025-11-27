import random
class Order: #{
    #initialize static attributes
    count = 0
    # initialize attributes
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
        # count how many objects have been created
        Order.count += 1

    @staticmethod
    def clamp_percent(x):
        #get the min number between x and 100
        num = min(x,100)
        #get the max number between x and 0
        num = max(0,num)
        return float(num)

    @staticmethod
    def bounded_quantity(x,max_q=100):
        str_x = str(x)
        # get index of point
        index = str_x.find(".")
        #determine the range of x
        if index == -1:
            return int(x)

        if 0 < x < max_q:
            quantity = str_x[:index]
            return int(quantity)
        elif x < 0 :
            quantity = str_x[1:index]
            return int(quantity)
        else:
            return max_q

    def total_with_vat(self,rate):
        # calculate total amount
        total_amout = quantity * price
        print("{} - {} @ {:.2f} = {:.2f}".format(item, quantity, price, total_amout))
        # calculate vat amount
        #if vat more than 100%, it should be calculated as 100%
        rate = Order.clamp_percent(rate)
        vat_amout = rate/100 * total_amout
        print("VAT amount: {:.2f}".format(vat_amout))
        return vat_amout


#}
#main program
# get input
vat = int(input("Enter VAT (%): "))
order_number = int(input("Enter number of orders: "))
# initialize total vat
total_vat = 0
# get every vat of items
for i in range(0, order_number):
    item = input("Enter item: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    # the max of quantity should be 1000
    quantity = Order.bounded_quantity(quantity)
    order = Order(item, price, quantity)
    amount = order.total_with_vat(vat)
    total_vat = total_vat + amount
# print out
print()
print("Total orders: {}".format(order_number))
print("Total VAT: {:.2f}".format(total_vat))



