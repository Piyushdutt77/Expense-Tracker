def add_expense(expenses):
    name=input("Enter name: ")
    amount=float(input("Enter amount: "))
    category=input("Enter category: ")

    expense={"name":name,"amount":amount,"category":category}
    expenses.append(expense)

    print("Added\n")