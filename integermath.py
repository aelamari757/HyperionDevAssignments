# Asking the user to enter three different integers.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum_of_all_numbers = num1 + num2 + num3
subtraction = num1 - num2
multiplication = num3 * num1
division = (num1 + num2 + num3) / num3

print("The sum of all the numbers is:", sum_of_all_numbers)
print("The first number minus the second number is:", subtraction)
print("The third number multiplied by the first number is:", multiplication)
print("The sum of all three numbers divided by the third number is:", division)