friends_names = ['Peter', 'Barry', 'Joni']

print(friends_names[0])

print(friends_names[-1])

print(len(friends_names))

friends_ages = [31, 29, 33]

ages_list = friends_ages

print(ages_list)

for i in range(len(friends_names)):
    print(f"{friends_names[i]} is {friends_ages[i]} years old.")
