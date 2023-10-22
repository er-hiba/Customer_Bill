VAT = float(input("Enter the value-added tax rate: "))
discount = float(input("Enter the discount rate: "))
n_clients = int(input("Enter the number of clients: "))
names = []
bills = []
for i in range(1, n_clients + 1):
    full_name = input(f"\nEnter the full name of client n° {i}: ")
    names.append(full_name)
    n_items = int(input(f"Enter the items' number for client n° {i}: "))
    Sum = 0
    for j in range(1, n_items + 1):
        IP = float(input(f"Enter the initial price of item {j}: "))
        # ATI stands for All Taxes Included.
        ATI = IP * (1 + VAT/100)
        Sum += ATI
    total = Sum - Sum * discount/100
    bills.append(total)

print("\nBills:")
for a in range(0, n_clients):
    print(f"The total bill for client {names[a]} is: {bills[a]:.2f}")
