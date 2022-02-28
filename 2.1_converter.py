answ = "yes"
test_list = ["yes","no"]

print("Hello!")
print("This program converts kilometres into miles.")
print()

while answ == "yes":
    km = float(input(("Enter the number of kilometres: ")))
    print(km,"km =",km*0.621371,"miles")
    print()
    answ_test = input("Do you want to do another conversion? ")
    while answ_test not in test_list:
        answ_test = input("Please enter 'yes' or 'no': ")
    answ = answ_test
    print()

print("Good bye!")
