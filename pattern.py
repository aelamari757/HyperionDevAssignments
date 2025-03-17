# Pattern example ascends to 5 stars for top half
top_row = 5

for i in range(1, top_row + 1):
    for h in range(i):
        print("*", end="") # Will print stars on the same line
    print()  
# Allows the stars to be printed on seperate lines instead of just one after code is executed

# bottom half goes down from 4 stars
for i in range(top_row - 1, 0, -1):
    for h in range(i):
        print("*", end="")
    print()  