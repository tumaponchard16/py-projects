# function inside a function
def enter_name():
    name = input("Enter your name")
    return name

def greeting():
    print("Hello " + enter_name())
    
greeting()

###############################################################################

# function to enter multiple name
def name_input():
    name_list = []
    name = ''
    while name != 'STOP':
        name_list.append(name)
        name = input('Enter a name, type "STOP" to end ')
    return name_list
    
def name_process():
    fin_list = name_input()
    count = 0
    while count != len(fin_list):
        print(fin_list[count])
        count = count + 1

name_process()
# Ticker print

###############################################################################

# Ticket maker function

first_name = ''
last_name = ''
age = ''
dest = ''

def data_retrieve():
    global first_name
    global last_name
    global age
    global dest
    first_name = input("Enter your name. ")
    last_name = input("Enter your last name. ")
    age = input("How old are you? ")
    dest = input("Enter your destination. ")
    
def data_process():
    result = "Name: " + first_name[0] + ". " + last_name + ", " + str(age) + ", " + "\nDestination: " + dest
    return result

def ticket_print():
    data_retrieve()
    print(data_process())

ticket_print()

### for loop for 3 chances

magic_numbers = [0,1,2,3,4,5,6,7,8,9]

def is_numbers():
    global magic_numbers
    chances = input("Please enter your chances: ")
    for attempt in range(chances):
        user_number = input("Please enter a number ")
        if user_number in magic_numbers:
            print ("This is attempt {}. You got it right!".format(attempt))
        if user_number not in magic_numbers:
            print ("This is attempt {}. You got it wrong!".format(attempt))
is_numbers()


#############################################
magic_numbers = [0,1,2,3,4,5,6,7,8,9]

def ask_user_check_number():
    user_number = input("Enter a number ")
    if user_number in magic_numbers:
        return "You got the right number."
    if not user_number in magic_numbers:
        return "You don't quite get it."

def run_program_x_times(chances):
    for attempt in range(chances):
        print (ask_user_check_number())

def enter_chances():
    chances = input("Enter your chances ")
    run_program_x_times(chances)
    
enter_chances()


########## The split strings ################

numbers = "5,10,16,29,40"
numbers.split(",")

user_input = "5,10,16,29,40"
user_number = user_input.split(",")

user_as_int = []

for number in user_number:
    user_as_int.append(int(number))

user_as_int

###############################################################################

# User can pick 6 numbers
# Loterry calculates 6 randoms numbers between 1, 20
# Then we match the user numbers to the lottery numbers 
# Calculate the winnings based on how many numbers the user matched

import random

def get_player_numbers():
    numbers_csv = input("Enter your 6 winning numbers, separated by commas: ")
    number_list = numbers_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set

def generate_lottery_numbers():
    values = set()
    while len(values) != 6:
        values.add(random.randint(1,20))
    return values
        
def get_winning_number():
    user_numbers = get_player_numbers()
    lottery_numbers = generate_lottery_numbers()
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print "User numbers: {a} \nWinning numbers are: {b} \nMatched numbers are: {c} \nYou won {d} ".format(a = user_numbers, b = lottery_numbers, c = matched_numbers, d = 10 * len(matched_numbers))

get_winning_number()
    

#################### Advanced dictionary #########################################

student = { "name": "Jose",
            "mark": [70,80,90.50],
            "exams": {"final": 70, 
                      "midterm": 80}
            }
print(student['mark'][0])
print(student['exams']['final'])

# Exercise for dictionary
student_list = []

def create_student():
    # Ask the user for the student's name
    student_name = input("Enter your name: ")
    # Create the dictionary in the format {'name': '<student name>', 'marks': []}
    student_data = {'name': student_name, 'marks': []}
    # Return that dictionary
    return student_data

s = create_student()

# create students marks
def student_marks(student):
    enter_marks = input("Enter student's marks ")
    student['marks'].append(enter_marks)

# calculate average mark
def calc_average_mark(student):
    student_marks(student)
    marks = student['marks']
    total = sum(marks[0])
    total_index_mark = len(marks[0])
    # dont calculate average if count is 0
    if total_index_mark == 0:
        return '0'
    else:
        return total / total_index_mark
    
def student_details(student):
    calc_average_mark(student)
    student_list.append(student)

student_details()

s = create_student()
print s
print student_list


#def student_details(student):
#    print("Hello! {}'s average mark is {}".format(student['name'],calc_average_mark(student)))
    
################ ANOTHER WAY ################################
student_list = []

def student_record():
    student_dictionary = {'name': '', 'marks': []}
    return student_dictionary

sr = student_record()

def create_student(student):
    # Ask the user for the student's name
    student_name = input("Enter your name: ")
    enter_marks = input("Enter student's marks ")
    student['name'] = student_name
    student['marks'].append(enter_marks)
    return student

def insert_student():
    global sr
    global student_list
    return student_list.append(create_student(sr))
    
def calc_avr(student):
    insert_student()
    total = sum(student['marks'][0])
    number = len(student['marks'][0])
    average = total / number
    return "{name}'s average is {avr}".format(name = student['name'], avr = average)

print calc_avr(sr)

print student_list

############################## Video way ########################################
student_list = []

class Student():
    def __init__(self, name):
        self.name = name
        self.marks = []
        
    def average_mark(self):
        number = len(self.marks)
        if number == 0:
            return 0
        total = sum(self.marks)
        return total / number
        

def create_student():
    name = input("Enter new student's name: ")
    student_data = Student(name)
    return student_data

def add_mark(student, mark):
    student.marks.append(mark)
    

def print_student_details(student):
    s_name = student.name
    print "{}'s average mark is {}".format(s_name, student.average_mark())
    
def print_student_list(students):    
    for i, student in enumerate(students):
        print "ID {}".format(i)
        print_student_details(student)
        
def menu():
    selection = input("Enter 'p' to print the student list,\n"
                      "'s' to add a new student,\n"
                      "'a' to add a mark to a student,\n"
                      "or 'q' to quit: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)
            
        selection = input("Enter 'p' to print the student list,\n"
                      "'s' to add a new student,\n"
                      "'a' to add a mark to a student,\n"
                      "or 'q' to quit: ")
        
menu()

################# Movie system with OOP #################################

ages = [5, 12, 17, 18, 24, 32]
  
x = filter(lambda x: x >= 18, ages)
print x
        
 

    
    





























    

    
 


    
    
















        
    
            
    
    





































    
        
        
        
        