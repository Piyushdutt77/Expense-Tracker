def category_summary(expenses):
    summary={}

    for e in expenses:
        cat=e["category"]

        if cat in summary:
            summary[cat]=summary[cat]+e["amount"]
        else:
            summary[cat]=e["amount"]

    print("Category Summary:")
    for i in summary:
        print(i,summary[i])
    print()
