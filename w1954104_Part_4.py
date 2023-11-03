# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: W19541048
# IIT Student ID: 20221035

# Date: 12/10/2022


# global

no_of_outcomes = [0]
Progress = [0]
Trailer = [0]
Retriever = [0]
Excluded = [0]
allowed_range_for_input = [0, 20, 40, 60, 80, 100, 120]
progression_outcomes = ['Progress', 'Progress (module trailer)', 'Do not Progress - module retriever', 'Exclude']
students_progress = []
students_id = []
total_incorrect = [0]
dict_students_progress = {}


# User-defined Functions

    # To validate the user input
def vallidation_of_pass_defer_fail(print_string):
    
    while(True):
        try:
            no_of_credits = int(input('Please enter your {}'.format(print_string)))     
            if(no_of_credits not in allowed_range_for_input):       # Out of Range Validation
                print('Out of range\n')
                continue
            break
        except ValueError:      # To validate the data type
            print('Integer required\n')

    return no_of_credits


    # Get student id / pass / defer / fail credits
def get_all_credits():      
    total_no_of_credits = 100
    student_id = input('Please enter student id: ')
    while student_id in students_id:
        print('Student ID already exist.\nPlease Try Again\n')
        student_id = input('Please enter student id: ')

    while(total_no_of_credits != 120):
        no_of_pass = vallidation_of_pass_defer_fail('credits at pass: ')
        no_of_defer = vallidation_of_pass_defer_fail('credit at defer: ')
        no_of_fail = vallidation_of_pass_defer_fail('credit at fail: ')
        total_no_of_credits = no_of_pass + no_of_defer + no_of_fail
        if ( total_no_of_credits != 120):       # To validate the incorrect Total
            print('Total incorrect\n')
            total_incorrect[0] = 1
            break
    
    students_id.append(student_id)


    return student_id, no_of_pass, no_of_defer, no_of_fail


    # Display the appropriate progression outcome
def progression_outcome(no_of_pass, no_of_defer, no_of_fail):
    while True:
        if total_incorrect[0] == 1:
            break
        if (no_of_pass == 120):     # For progress
            student_progress = progression_outcomes[0]
            Progress[0] += 1
        elif ((no_of_fail == 20 or no_of_defer == 20) and no_of_pass == 100):   # For Trailer
            student_progress =  progression_outcomes[1]
            Trailer[0] += 1
        elif (no_of_fail >= 80):    # For Excluded
            student_progress = progression_outcomes[3]
            Excluded[0] += 1
        else:   
            student_progress = progression_outcomes[2]
            Retriever[0] += 1
        no_of_outcomes[0] += 1
        print(student_progress)
        total_incorrect[0] = 0
        break
    if total_incorrect[0] != 1:
        return student_progress
    

    # Get multiple inputs
def Multiple_incomes():
    total_incorrect[0] = 0
    loop_for_staff = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
    while True:
        print('\n')
        if (loop_for_staff.upper() == 'Y') :    # Want to loop
            student_id, no_of_pass, no_of_defer, no_of_fail = get_all_credits()
            
            student_progress = progression_outcome(no_of_pass, no_of_defer, no_of_fail)
            if total_incorrect[0] != 1:
                students_progress.append([student_id, student_progress, no_of_pass, no_of_defer, no_of_fail])

        elif (loop_for_staff.upper() == 'Q'):   # Don't want to loop
            print("--------------------------------------------------------------- \nHistogram ")
            
            print("\nProgress {}  : ".format(Progress[0]), end=' ')
            print('*'*Progress[0])
    
            print("\nTrailer {}   : ".format(Trailer[0]), end=' ')
            print('*'*Trailer[0])
    
            print("\nRetriever {} : ".format(Retriever[0]), end=' ')
            print('*'*Retriever[0])
    
            print("\nExcluded {}  : ".format(Excluded[0]), end=' ')
            print('*'*Excluded[0])
    
            print(f"\n{no_of_outcomes[0]} outcomes in total.")
    
            print('---------------------------------------------------------------')
            break
        else:
            print('\nInvalid Input\n')  # Validate the loop choice
        loop_for_staff = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")



# Welcome Prompt

print('\n\nWelcome, \nThis is a program used to predict the progression outcomes of students at the end of each academic year. \nPlease follow the given instructions properly. Thank you.')

to_begin = 'n'

while(to_begin.upper() != 'Y'):     # To start the program
    to_begin = input("\n\nTake your time, And Press key 'Y' to start predicting the progression outcome.\n")
    print('\n')


student_id, no_of_pass, no_of_defer, no_of_fail = get_all_credits()

student_progress = progression_outcome(no_of_pass, no_of_defer, no_of_fail)

# appending as a nested list with all progress details
if total_incorrect[0] != 1:
    students_progress.append([student_id, student_progress, no_of_pass, no_of_defer, no_of_fail])


Multiple_incomes()

# part 2
print(' ')

def print_list():  
    for i in range(0, len(students_progress)):
        for x in range(1,5):
            if x == 1:
                print(students_progress[i][x], ' - ', end = ' ')
            elif x == 4:
                print(students_progress[i][x])
            else:
                print(students_progress[i][x], end= ', ')

print('Part 2:')
print_list()

# part 3
print('\n---------------------------------------------------------------')
print('\nPart 3:')

    # writes in text file
f = open('StudentProgression.txt', 'w')

for i_1 in range(0, len(students_progress)):
    for x_1 in range(1, 5):
        if x_1 == 1:
            f.write(f'{students_progress[i_1][x_1]} - ')
        elif x_1 == 4:
            f.write(f'{students_progress[i_1][x_1]}\n')
        else:
            f.write(f'{students_progress[i_1][x_1]}, ')    
            
f.close()

    # Reads from text file
f = open('StudentProgression.txt', 'r')

print(f.read())

f.close()


# Part 4
print('---------------------------------------------------------------')
print('\nPart 4:')

for i_2 in range(0, len(students_progress)):
    dict_students_progress[students_progress[i_2][0]] = students_progress[i_2][1:5]

for k, v in dict_students_progress.items():
    print('{} :'.format(k), end=' ')
    vi = 0
    for vi in range(0, 4):
        if vi == 0:
            print(v[vi], ' -', end=' ')
        elif vi == 3:
            print(v[vi])
        else:
            print(v[vi], end=', ')

print('\n---------------------------------------------------------------')
