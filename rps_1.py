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

print_choices()
for i in range(3):
    # print('\t', computer_choices[i])
    print_choice(i)


choice = random.choice(computer_choices)
choice = generate_choice()
random_idx = random.randint(0, len(computer_choices))
choice = fetch_choice(random_idx)
print('And it randomly chooses:', choice)


# Recursive function definition
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# # Reading number from user
# number = int(input('Enter number: '))
#
# # Displaying factorial
# if(number< 0):
#     print('Factorial does not exist!')
# else:
#     print('Factorial of %d is %d' %(number, factorial(number)))

# Lambda functions
# square = lambda x: x*x
#
# number = int(input('Enter any number: '))
#
# result = square(number)
#
# print('Square of %d is %d' %(number, result))

result = sorted(computer_choices)
print('Sorted choices:', result)

# BUT - Ball comes before apple because, sorted() function returns result on the basis of ASCII sorting
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
name_sorted_dict = dict(sorted(player_score.items()))
score_sorted_dict = dict(sorted(player_score.items(), key=lambda item: item[1]))
print(name_sorted_dict)
print(score_sorted_dict)