from add import add_expense
from view import view_expense
from total import total_expense
from category import category_summary

def main():
    expenses=[]

    while True:
        print("1 Add")
        print("2 View")
        print("3 Total")
        print("4 Category")
        print("5 Exit")

        choice=input("Choice: ")

        if choice=="1":
            add_expense(expenses)

        elif choice=="2":
            view_expense(expenses)

        elif choice=="3":
            total_expense(expenses)

        elif choice=="4":
            category_summary(expenses)

        elif choice=="5":
            break

        else:
            print("Invalid\n")

main()