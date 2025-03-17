sum_total = 0

count = 0

while True: 
    user_input = input("Please enter a number: ")

    if user_input == "-1":
        break

    if user_input == "0":
        continue
# This will ensure that if any negative number is added aside of -1, message will appear
    num = int(user_input)
    if num < 0:
        print("Negative numbers entered, not valid. Please enter only positive numbers")

    sum_total += num
    count += 1

if count > 0:
    average = sum_total / count
    print(f"The average is: {average}")
else:
    print("No valid number has been entered")