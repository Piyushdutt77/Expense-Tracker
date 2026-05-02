def view_expense(expenses):
    if len(expenses)==0:
        print("No expenses")
        return

    print("Expenses:")
    for e in expenses:
        print(e["name"],e["amount"],e["category"])
    print()
