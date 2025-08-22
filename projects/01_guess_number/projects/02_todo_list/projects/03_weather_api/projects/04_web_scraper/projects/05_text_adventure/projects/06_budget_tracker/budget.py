income = 0
expenses = []

def add_income(amount):
    global income
    income += amount
    print(f"💰 Income added: {amount}")

def add_expense(name, amount):
    expenses.append((name, amount))
    print(f"📉 Expense added: {name} - {amount}")

def summary():
    total_expense = sum(x[1] for x in expenses)
    balance = income - total_expense
    print("\n📊 Budget Summary:")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Balance: {balance}")

def main():
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. View Summary\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            add_income(amount)
        elif choice == "2":
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            add_expense(name, amount)
        elif choice == "3":
            summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
