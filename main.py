import random

#methods that will be used

#adds two numbers
def add(x, y):
    return x + y

#subtracts two numbers
def sub(x, y):
    return x - y
    
#multiplys two numbers
def multiply(x, y):
    return x * y

def difficulty():
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    try:
        user_answer = int(input())
    except ValueError:
        while (user_answer != 1) or (user_answer != 2):    #checks for answer, possible incorrect input
            print('Incorrect format.')
            try:
                user_answer = int(input())
                if (user_answer == 1) or (user_answer == 2):
                    return user_answer
            except ValueError:
                continue
    else:
        if (user_answer == 1) or (user_answer == 2):
            return user_answer
        else:
            while (user_answer != 1) or (user_answer != 2):
                print('Incorrect format.')
                try:
                    user_answer = int(input())
                    if (user_answer == 1) or (user_answer == 2):
                        return user_answer
                except ValueError:
                    continue

def simple_ops():
    answer_count = 0
    for question_count in range(5):             #asks 5 questions
        user_answer = 0
        x = random.randint(2,9)                 #sets variables used in question
        y = random.randint(2,9)
        operator = ['+', '*', '-']      
        operator = random.choice(operator)      #sets a pseudo-random operator
        equation = str(x) + operator + str(y)   #sets string for question


        #checks answer to problem based on operator
        if equation[1] == '+':
            answer = add(x, y)
        elif equation[1] == '-':
            answer = sub(x, y)
        else:
            answer = multiply(x, y)
        print(' '.join(equation))

        
        #user inputs the answer
        try:
            user_answer = int(input())
        except ValueError:
            while not int(user_answer):         #checks for answer, possible incorrect input
                print('Incorrect format.')
                try:
                    user_answer = int(input())
                except ValueError:
                    continue
            if user_answer == answer:
                print('Right!')
                answer_count += 1
            else:
                print('Wrong')
        else:
            #Output of program
            if user_answer == answer:
                print('Right!')
                answer_count += 1
            else:
                print('Wrong!')
    print('Your mark is ' + str(answer_count) + '/5')

def int_squares():
    answer_count = 0
    for question_count in range(5):             #asks 5 questions
        user_answer = 0
        x = random.randint(11,29) 
        equation = str(x)

        answer = multiply(x, x)
        print(equation)

        try:
            user_answer = int(input())
        except ValueError:
            while not int(user_answer):         #checks for answer, possible incorrect input
                print('Incorrect format.')
                try:
                    user_answer = int(input())
                except ValueError:
                    continue
            if user_answer == answer:
                print('Right!')
                answer_count += 1
            else:
                print('Wrong')
        else:
            #Output of program
            if user_answer == answer:
                print('Right!')
                answer_count += 1
            else:
                print('Wrong!')
    print('Your mark is ' + str(answer_count) + '/5')


int_squares()