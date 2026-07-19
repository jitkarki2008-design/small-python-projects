# Project 05 - Expense Tracker using Dict and CSV
import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"
FIELDS = ["date", "category", "amount", "note"]

def load_expenses():
    # Returns list of dicts like [{"date": "2026-07-19", "category": "food", "amount": "100"...},...]
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

def add_expense():
    print("\n--- Add New Expense ---")
    today = date.today()
    print(f"Date: {today} (press Enter to use today)")
    expense_date = input("Enter date (YYYY-MM-DD) or press Enter: ").strip()
    if not expense_date:
        expense_date = str(today)

    category = input("Category (food/travel/shopping/other): ").strip().lower()
    amount = input("Amount: ").strip()
    note = input("Note (e.g., momos): ").strip()

    # dict for one expense
    new_expense = {
        "date": expense_date,
        "category": category,
        "amount": amount,
        "note": note
    }

    # check if file exists to write header
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if not file_exists:
            writer.writeheader() # write header only first time
        writer.writerow(new_expense)

    print(f"Saved! {amount} Rs in {category}")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses yet!")
        return

    print(f"\n--- All Expenses ({len(expenses)}) ---")
    print(f"{'DATE':<12} {'CATEGORY':<10} {'AMOUNT':<8} NOTE")
    print("-" * 45)
    for exp in expenses: # exp is a dict
        print(f"{exp['date']:<12} {exp['category']:<10} {exp['amount']:<8} {exp['note']}")

def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("\nNo data to summarize!")
        return

    total = 0
    category_total = {} # dict for category wise sum: {"food": 500, "travel": 200}

    for exp in expenses:
        try:
            amt = float(exp['amount'])
            total += amt

            cat = exp['category']
            if cat in category_total:
                category_total[cat] += amt
            else:
                category_total[cat] = amt
        except:
            continue

    print(f"\n--- Summary ---")
    print(f"Total Spent: {total} Rs")
    print("\nCategory Wise:")
    for cat, amt in category_total.items():
        print(f" {cat} : {amt} Rs")

# --- Main Loop ---
print("--- Expense Tracker ---")

while True:
    print("\n1. Add Expense 2. View Expenses 3. Summary 4. Exit")
    choice = input("Choose (1-4): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        show_summary()
    elif choice == '4':
        print("Bye! Data saved in expenses.csv")
        break
    else:
        print("Invalid choice")