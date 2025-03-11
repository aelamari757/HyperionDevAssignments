# Asking user for input
str_manip = input("Enter a sentence: ")
print("The length of the sentence is:", len(str_manip))
last_letter = str_manip[-1]
str_manip_replaced = str_manip.replace(last_letter, '@')
print("Altered sentence:", str_manip_replaced)
last_3_letters_of_sentence = str_manip[-3:]  
reversed_last_3 = last_3_letters_of_sentence[::-1]  
print("Last 3 letters backwards:", reversed_last_3)
first_3_letters = str_manip[:3]  
last_2_letters = str_manip[-2:]  
new_word = first_3_letters + last_2_letters  
print("New word made from first 3 and last 2 letters:", new_word)