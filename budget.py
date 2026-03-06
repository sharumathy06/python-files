# Simple Budget Tracker

# Get total monthly budget
total_budget = float(input("Enter your total monthly budget: $"))

# Initialize expenses list
expenses = []

# Get expenses from user
print("\nEnter your expenses (type 'Done' when finished):")
expense_count = 1
while True:
    user_input = input(f"Expense {expense_count} (or 'Done' to finish): $")
    if user_input.lower() == "done":
        break
    try:
        expense = float(user_input)
        expenses.append(expense)
        expense_count += 1
    except ValueError:
        print("Invalid input. Please enter a valid amount or 'Done' to finish.")

# Calculate total expenses
total_expenses = sum(expenses)

# Calculate remaining balance
remaining_balance = total_budget - total_expenses

# Display results
print("\n" + "="*40)
print("BUDGET SUMMARY")
print("="*40)
print(f"Total Monthly Budget:  ${total_budget:.2f}")
print(f"\nExpenses:")
for i, expense in enumerate(expenses, 1):
    print(f"  Expense {i}:         ${expense:.2f}")
print(f"Total Expenses:        ${total_expenses:.2f}")
print("-"*40)
print(f"Remaining Balance:     ${remaining_balance:.2f}")
print("="*40)

# Display warning if overspent
if remaining_balance < 0:
    print(f"\nWARNING: You are over budget by ${abs(remaining_balance):.2f}")
elif remaining_balance < 500:
    print(f"\nWarning: Low Funds")
    print(f"You have ${remaining_balance:.2f} left in your budget")
else:
    print(f"\nYou have ${remaining_balance:.2f} left in your budget")
