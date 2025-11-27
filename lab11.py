state_abb = {
  "NSW": "New South Wales",
  "ACT": "Australian Capital Territory",
  "NT": "Northern Territory",
  "QLD": "Queensland",
  "SA": "South Australia",
  "TAS": "Tasmania",
  "VIC": "Victoria",
  "WA": "Western Australia"
}

# write code to print out Queensland and Victoria.
# print(state_abb.get("QLD"))
# print(state_abb["VIC"])

city_code = input("Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: ")
print("The state you entered is {}".format(state_abb.get(city_code)))
