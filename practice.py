#inputs
name = input("What is your name: ")
daily_cal = int(input("Calories Eaten: "))
daily_cal_target = int(input("Target Calories: "))
#output line
print(f"{name}, you ate {daily_cal} kcal")
#conditions to be met
difference = daily_cal - daily_cal_target

if daily_cal <= daily_cal_target:
   print(f"Good job you are {difference} kcal under target")
else:
   print(f"Over Target by {difference} kcal under target ")
