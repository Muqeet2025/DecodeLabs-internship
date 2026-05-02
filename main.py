
total = 0
while True:
    expense = input("Enter expense(or 'q' to quit):")
    if expense == 'q':
        break
    total += float(expense)
print("Total spent:", total)