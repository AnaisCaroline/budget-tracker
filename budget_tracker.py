import json
# File to store budget data 
BUDGET_FILE = "budget_data.json"
def load_budget():
	""" Load budget data from a file."""
	try: 
		with open (BUDGET_FILE,"r") as file:
			return json.load (file)
	except (FileNotFoundError, json.JSONDecodeError):
		return {"income": 0, "expenses":[]}
def save_budget(data): 
	""" Save budget data to file."""
	with open(BUDGET_FILE, "w")	as file:
		json.dump(data, file, indent=4)
def add_income():
	"""Add income to the budget."""
	data = load_budget ()
	try:
		income = float(input("Enter your total monthly income: $"))
		data ["income"] = income 
		save_budget(data)
		print(f"Income of ${income} recorded succesfully!")
	except ValueError:
		print ("Invalid input! Please enter a valid number.")
def add_expense():
	"""Add an expense to the budget."""	
	data = load_budget()
	try:
		category = input("Enter expense category (e.g., rent, groceries) ").strip()
		amount = float(input("Enter expense amount: $"))
		data["expenses"].append({"category": category, "amount": amount})
		save_budget(data)
		print(f"Expense of $ {amount} for {category} added successfully!")
	except ValueError:
		print("Invalid input! Please enter a valid number.")
def view_budget():
	"""Display the budget summary."""	
	data = load_budget()
	print("\n--- Budget Summary ---")
	print(f"Total Income: ${data['income']:.2f}")
	total_expenses = sum(exp["amount"]for exp in data["expenses"])
	print(f"Total Expenses: ${total_expenses:.2f}")
	print(f"Remaning Balance: ${data['income'] - total_expenses:.2f}")

	print("\nExpense Breakdown:")
	for exp in data["expenses"]:
		print(f"-{exp['category']}: ${exp['amount']:.2f}")
def main():
	#Main menu for budget tracking. 
	while True: 
		print("\n--- Personal Budget Tracker ---")
		print("1. Add Income")
		print("2. Add Expense")
		print("3. View Budget")
		print("4. Exit")

		choice = input("Choose an option (1-4): ")
		if choice == "1":
			add_income()
		elif choice == "2":
			add_expense()
		elif choice == "3":
			view_budget()
		elif choice == "4":
			print("Goodbye! Stay on top your budget!")
			break
		else:
			print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
	main()