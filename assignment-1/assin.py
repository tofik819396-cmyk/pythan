#Name: Tofik ahmed
# Date: 10 Nov 2025
# Project: Daily Calorie Tracker CLI
print("Welcome to the Daily Calorie Tracker CLI!")
print("This tool helps you log your meals and track total calorie intake.")
meals = []
calories =[]
total_calories = sum(calories)
avg_calories = total_calories /len(calories)
if total_calories > daily_limit:
    print(" Warning: You have exceeded your daily calorie limit!")
else:
    print(" Good job! You are within your daily calorielimit.")
Meal Name       Calories

Breakfast       350
Lunch           600
Snack           150

Total           1100
Average         366.67
save = input("Do you want to save this session? (yes/no): ").lower()
if save == "yes":
    with open("calorie_log.txt", "w") as file:
        file.write(f"Date: {datetime.now()}\n")
        # Write meal details, total, average, limit status
        # Name: Tofik Ahmed
# Date: 10 Nov 2025
# Project: Daily Calorie Tracker CLI
# Description: A Python CLI tool to track daily calorie intake,
# calculate totals and averages, warn if limits are exceeded,
# and optionally save a session log to file.
# --------------------------------------------------------------

from datetime import datetime

# ---- Welcome Message ----
print("===========================================")
print("   Welcome to the Daily Calorie Tracker!   ")
print("===========================================")
print("This tool helps you log meals and track your calorie intake.\n")

# ---- Task 2: Input & Data Collection ----
meals = []
calories = []

# Ask how many meals user wants to enter
num_meals = int(input("How many meals do you want to log today? "))

# Loop to get meal data
for i in range(num_meals):
    print(f"\nMeal {i + 1}:")
    meal_name = input("Enter meal name (e.g., Breakfast): ")
    calorie_amt = float(input("Enter calorie amount: "))
    
    meals.append(meal_name)
    calories.append(calorie_amt)

print("\nAll meals logged successfully!\n")

# ---- Task 3: Calorie Calculations ----
total_calories = sum(calories)
average_calories = total_calories / len(calories)

# Ask for daily calorie limit
daily_limit = float(input("Enter your daily calorie limit: "))

# ---- Task 4: Exceed Limit Warning System ----
if total_calories > daily_limit:
    limit_status = "⚠ Warning: You have exceeded your daily calorie limit!"
else:
    limit_status = " Good job! You are within your daily calorie limit!"

# ---- Task 5: Neatly Formatted Output ----
print("\n===========================================")
print("            Calorie Summary Report         ")
print("===========================================")
print("Meal Name\tCalories")
print("-------------------------------------------")


for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")

print("-------------------------------------------")
print(f"Total\t\t{total_calories}")
print(f"Average\t\t{average_calories:.2f}")
print("-------------------------------------------")
print(limit_status)
print("===========================================\n")

# ---- Task 6 (Bonus): Save Session Log to File ----
save_log = input("Do you want to save this session log to a file? (yes/no): ").lower()

if save_log == "yes":
    filename = "calorie_log.txt"
    with open(filename, "w") as file:
        file.write("===========================================\n")
        file.write("        Daily Calorie Tracker Log\n")
        file.write("===========================================\n")
        file.write(f"Date/Time: {datetime.now()}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("-------------------------------------------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]}\t\t{calories[i]}\n")
        file.write("-------------------------------------------\n")
        file.write(f"Total\t\t{total_calories}\n")
        file.write(f"Average\t\t{average_calories:.2f}\n")
        file.write("-------------------------------------------\n")
        file.write(limit_status + "\n")
        file.write("===========================================\n")

    print(f"\n Session log saved successfully as '{filename}'!\n")
else:
    print("\nSession log not saved. Goodbye!\n")

print("Thank you for using the Daily Calorie Tracker CLI!")
print("Stay healthy and keep tracking your meals! ")

   Welcome to the Daily Calorie Tracker!
===========================================
This tool helps you log meals and track your calorie intake.

How many meals do you want to log today? 3

Meal 1:
Enter meal name (e.g., Breakfast): Breakfast
Enter calorie amount: 350

Meal 2:
Enter meal name (e.g., Lunch): Lunch
Enter calorie amount: 600

Meal 3:
Enter meal name (e.g., Snack): Snack
Enter calorie amount: 150

All meals logged successfully!

Enter your daily calorie limit: 1200

===========================================
            Calorie Summary Report
===========================================
Meal Name       Calories
-------------------------------------------
Breakfast       350
Lunch           600
Snack           150
-------------------------------------------
Total           1100
Average         366.67
-------------------------------------------
 Good job! You are within your daily calorie limit!
===========================================

Do you want to save this session log to a file? (yes/no): yes
 Session log saved successfully as 'calorie_log.txt'!

Thank you for using the Daily Calorie Tracker CLI!
Stay healthy and keep tracking your meals!
