def total_expense(expenses):
    total=0

    for e in expenses:
        total=total+e["amount"]

    print("Total:",total,"\n")