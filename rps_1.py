import random


# So for a rock paper scissors game:
computer_choices = ['rock', 'paper', 'scissors']


def print_choices():
    for i in range(3):
        print('\t', computer_choices[i])


def print_choice(current_idx):
    print('\t', computer_choices[current_idx])


def generate_choice():
    choice = random.choice(computer_choices)
    return choice


def fetch_choice(idx):
    return computer_choices[idx]


print('Computer can choose between:')
# Function without input arguments or return
print_choices()

print('Computer can choose between:')
# Function without return value, accepting a single input
for i in range(3):
    print('\t', computer_choices[i])

# Function that returns a single value (choice) based on the first line
choice = random.choice(computer_choices)
choice = generate_choice()

# Function that takes an input argument (random_idx) and returns a single value (choice)
random_idx = random.randint(0, len(computer_choices))
choice = fetch_choice(random_idx)
print('And it randomly chooses:', choice)


# Recursive function definition
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)


# Reading number from user
number = int(input('Enter number: '))

# # Displaying factorial
if number < 0:
    print('Factorial does not exist!')
else:
    print('Factorial of', number, 'is', factorial(number))

# Lambda functions
square = lambda x: x*x  # Usually we do not assign lambda functions, this is only for showcase

number = int(input('Enter any number: '))  # Reading user input

result = square(number)

print('Square of', number, 'is', result)

# Sorting example with lambdas
computer_choices = ['rock', 'paper', 'scissors']
result = sorted(computer_choices)  # This is what sorted does when the cases are uniform
print('Sorted choices:', result)

# BUT - In this case Ball comes before apple because, sorted() function returns result on the basis of ASCII sorting
words = ['Ball', 'apple', 'cat', 'Ant', 'dog']
# Applying sorted function
result1 = sorted(words)
print('Result 1:', result1)
# Applying sorted function and lambda
result2 = sorted(words, key=lambda x: x.upper())
print('Result 2:', result2)

player_score = {'Esther': 2,
                'Someone else': 1
                }
name_sorted_dict = dict(sorted(player_score.items()))  # Sorting this dict by keys (name)
score_sorted_dict = dict(sorted(player_score.items(), key=lambda item: item[1]))  # Sorting the same dict by values (scores)
print(name_sorted_dict)
print(score_sorted_dict)
