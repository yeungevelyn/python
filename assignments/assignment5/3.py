class Catalog:
    def __init__(self):
        self.price_map = {}

    def add_item(self,name,price):
        self.price_map[name] = price
        #print(self.price_map)

    def get_price(self,name):
        return self.price_map.get(name,"NA")

    def count(self):
        total_items = self.price_map.keys();
        return len(total_items)

    def average_price(self):
        all_prices = self.price_map.values()
        total_price = 0
        total_number = self.count()
        if total_number != 0 :
            for price in all_prices:
                total_price = total_price + price
            average_price = round(total_price/total_number,2)
            return average_price
        else:
            return 0

    def median_price(self):
        all_prices = self.price_map.values()
        all_prices_list = list(all_prices)
        #sort all prices
        all_prices_list.sort()
        #odd number
        if len(all_prices_list)%2 == 1:
            #get index
            index = (len(all_prices_list)-1)//2
            return round(all_prices_list[index],2)
        #even number
        elif len(all_prices_list)%2 == 0 and len(all_prices_list) >0 :
            index = len(all_prices_list)//2
            median = (all_prices_list[index-1] + all_prices_list[index])/2
            return round(median,2)
        elif len(all_prices_list) == 0:
            return 0.0

#MAIN
#get user input
item_number = int(input("Enter number of items: "))
#create an instance
catalog = Catalog()
for i in range (0,item_number):
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    catalog.add_item(name,price)

queries_number = int(input("Enter number of queries: "))
#query price of items
for i in range(0,queries_number):
    query_name = input("Query name: ")
    price = catalog.get_price(query_name)
    if(price != "NA"):
        print("{}: {:.2f}".format(query_name,price))
    else:
        print("{}: {}".format(query_name, price))

print()
#calculate total item
total = catalog.count()
print("Total items: {}".format(total))
#get average price
average_price = catalog.average_price()
print("Average price: {:.2f}".format(average_price))
#get median price
median_price = catalog.median_price()
print("Median price: {:.2f}".format(median_price))