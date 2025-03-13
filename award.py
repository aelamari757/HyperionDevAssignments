# Task 6 - Logical Programming – Operators Assignment
swimming = int(input("Enter swimming time in minutes: "))
cycling = int(input("Enter cycling time in minutes: "))
running = int(input("Enter running time in minutes: "))

total_time = swimming + cycling + running

print("Total time for triathlon: ", total_time, "minutes")

if total_time <= 100:
    award = "Provincial colors"
elif total_time <= 105:
    award = "Provincial half colors"
elif total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

print("Award:", award)