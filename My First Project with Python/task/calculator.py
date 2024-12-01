# Write your code here
Bubblegum = "Bubblegum"
Toffee = "Toffee"
Ice_cream = "Ice cream"
Milk_chocolate = "Milk chocolate"
Doughnut = "Doughnut"
Pancake = "Pancake"

Bubblegum_Price = 2
Toffee_Price = 0.2
Ice_cream_Price = 5
Milk_chocolate_Price = 4
Doughnut_Price = 2.5
Pancake_Price = 3.2

Bubblegum_Earned = 202
Toffee_Earned = 118
Ice_cream_Earned = 2250
Milk_chocolate_Earned = 1680
Doughnut_Earned = 1075
Pancake_Earned = 80

Income = "Income"
Income_Generated = Bubblegum_Earned + Toffee_Earned + Ice_cream_Earned + Milk_chocolate_Earned + Doughnut_Earned + Pancake_Earned


print("\nEarned amount: ")
print(f"{Bubblegum}: ${Bubblegum_Earned} \n{Toffee}: ${Toffee_Earned}\n{Ice_cream}: ${Ice_cream_Earned}\n{Milk_chocolate}: ${Milk_chocolate_Earned}\n{Doughnut}: ${Doughnut_Earned}\n{Pancake}: ${Pancake_Earned}")
print(f"\n{Income}: ${Income_Generated}")

Staff_Expenses = input("Enter the staff expenses: ")
Other_Expenses = input("Enter the other expenses: ")

Total_Expenses = int(Staff_Expenses) + int(Other_Expenses)
Net_Income = Income_Generated - Total_Expenses
print(f"Net income: ${Net_Income}")
