import csv

class ExpenseTracker:
    def __init__(self):
        self.transactions = {
            "expenses": [],
            "income": []
        }

    def add_transaction(self, description, amount, transaction_type):
        if transaction_type not in ["expenses", "income"]:
            raise ValueError("Transaction type must be 'expenses' or 'income'")
        
        self.transactions[transaction_type].append({"Description": description, "Amount": amount})

    def view_transactions(self):
        return self.transactions

    def calculate_total(self):
        total_expense = sum(item["Amount"] for item in self.transactions["expenses"])
        total_income = sum(item["Amount"] for item in self.transactions["income"])
        return total_expense, total_income

    def export_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Description', 'Amount', 'Transaction Type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for transaction_type, transactions in self.transactions.items():
                for transaction in transactions:
                    writer.writerow({
                        'Description': transaction["Description"],
                        'Amount': transaction["Amount"],
                        'Transaction Type': transaction_type
                    })

# Example usage:

tracker = ExpenseTracker()
tracker.add_transaction("Groceries", 50.0, "expenses")
tracker.add_transaction("Salary", 2000.0, "income")
tracker.add_transaction("Dinner", 30.0, "expenses")

print("Transactions:")
print(tracker.view_transactions())

total_expense, total_income = tracker.calculate_total()
print(f"Total Expenses: {total_expense}")
print(f"Total Income: {total_income}")

tracker.export_to_csv("transactions.csv")
