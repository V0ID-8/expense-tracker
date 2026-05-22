def show_menu():
    print("\n" + "="*40)
    print("         Expense Tracker")
    print("="*40)
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Total spending")
    print("4. Exit")
    print("="*40)\
    

def main():
    while True: 
        show_menu()
        choice = input("Enter your choice(1-4): ").strip()

        if choice == '1':
            print("\n [add Expense - Coming Soon]")
        elif choice == '2':
            print("\n [view Expenses - Coming Soon]")
        elif choice == '3':
            print("\n [view Total Spending - Coming Soon]")
        elif choice == '4':
            print("\n Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("\n Invalid choice. Please enter a number between 1 to 4.")

if __name__ == "__main__":
    main()    