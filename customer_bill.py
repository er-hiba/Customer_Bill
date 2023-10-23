VAT = float(input("Enter the value-added tax rate: "))
while VAT < 0 :
    VAT = float(input("Please enter a valid positive VAT rate: "))

discount = float(input("Enter the discount rate: "))
while discount < 0 :
    discount = float(input("Please enter a valid positive discount rate: "))

n_customers = int(input("Enter the number of customers: "))
while n_customers <= 0:
    n_customers = int(input("Enter a valid positive number of customers: "))

names = []
bills = []

for i in range(1, n_customers + 1):
    full_name = input(f"\nEnter the full name of customer n° {i}: ")
    names.append(full_name)

    n_items = int(input(f"Enter the items' number for customer n° {i}: "))
    while n_items <= 0:
            n_items = int(input(f"Enter a valid positive number of items for customer n° {i}: "))

    Sum = 0
    for j in range(1, n_items + 1):
        IP = float(input(f"Enter the initial price of item {j}: "))
        while IP <= 0:
            IP = float(input(f"Enter a valid positive price for item {j}: "))

        # ATI stands for All Taxes Included.
        ATI = IP * (1 + VAT/100)
        Sum += ATI
    total = Sum - Sum * discount/100
    bills.append(total)

print("\nBills:")
for a in range(0, n_customers):
    print(f"The total bill for customer {names[a]} is: {bills[a]:.2f}")
