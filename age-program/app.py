# Ask the user age and print into seconds
age = input('Enter your age: ')
print("You have lived for {} seconds. This corresponds to {} years.".format(int(age) * 365 * 24 * 60 * 60, age))
