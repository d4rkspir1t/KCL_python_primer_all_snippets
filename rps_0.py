# ===================
print('Hello World!')


# ===================
score = 2  # integer
time_to_decide = 1.4  # float
time_for_opponent = 0.234  # a longer float
greeting_text = 'Player'  # string
player_win = False  # boolean

# we will talk about how to do this later in topic 4
print(score, 'is type', type(score))
print(time_to_decide, 'is type', type(time_to_decide))
print(time_for_opponent, 'is type', type(time_for_opponent))
print(greeting_text, 'is type', type(greeting_text))
print(player_win, 'is type', type(player_win))

score = 2.0
print(score, 'is type', type(score))

# conversion
score_int = int(score)
print(score_int, 'is type', type(score_int))

player_win_int = int(player_win)
print(player_win_int, 'is type', type(player_win_int))

numeric_name = '0.864'
print('The name is:', numeric_name, 'and type', type(numeric_name),
      ', but when converted,', float(numeric_name), 'is type', type(float(numeric_name)))
#  notice how in the print the string and float display identically


# ===================
scores_of_single_player = [0, 1, 0, 0, 1, 1, 1]  # list
print('Score from game', 3, 'is', scores_of_single_player[3])


player_info = ('Esther', 32, 'Denmark', 'Copenhagen')  # tuple - packing

# ways of unpacking a tuple
name, age, country, city = player_info
print(name, age, country, city, '---', player_info)

# if you do not need some unpacked variables, use '_'
name, age, _, _ = player_info
print(name, age, '---', player_info)
# or in short
name, age, *_ = player_info
print(name, age, '---', player_info)
name, *_, city = player_info
print(name, city, '---', player_info)

player_score = {name: score, 'Someone else': 1}  # creating a dictionary - 1 physical line, 1 logical line
player_score = {name: score,
                'Someone else': 1
                }  # creating a dictionary - 3 physical line, 1 logical line
print(player_score)
print(player_score[name])  # to access elements, use the given keys
print(name, 'with a score of', player_score['Esther'], 'did better than Someone else with a score of', player_score['Someone else'])

# ===================
x = range(4)  # STOP value
x = list(x)
print(x)

# The reason list(x) is needed is that the type of a range variable is range so without the conversion:
x = range(4)  # STOP value
print(type(x))
print(x)

x = range(3, 12)  # START and STOP values
x = list(x)
print(x)

x = range(6, 27, 3)  # START, STOP, and STEP values
x = list(x)
print(x)

import random
number = random.random()
print('Generated random number is:', number)

# uniform: random FLOAT in range (START, STOP)
number = random.uniform(2, 9)
print('Generated random number is', number)

# randint: random INT in range (START, STOP)
number = random.randint(1,20)
print('Generated random number is:', number)

# choice: randomly select 1 value from a list of choices
sequence = [0, 3, 13, 669, 3381]
number = random.choice(sequence)
print('Generated random number is:', number)

# So for a rock paper scissors game:
computer_choices = ['rock', 'paper', 'scissors']
choice = random.choice(computer_choices)
print('The computer randomly chooses:', choice)

# ===================
# As you saw above Range can be used for looping
for i in range(4):
    print(i)

for i in range(3, 12):
    print(i)

for i in range(6, 27, 3):
    print(i)
# Notice that the STOP value is never printed, that's because the range goes from START to STOP-1

# Can also be used with _ for unused values, e.g. for printing something x times
for _ in range(3):
    print('Printing this 3 times')

# Reversing the loop - STEP needs to be negative, (START, STOP, STEP), but START > STOP
print('Time to liftoff:')
for i in range(5, 0, -1):
    print('\tT-', i)
# Notice that the STOP value is never printed, and in a reverse loop the range goes from START to STOP+1

# So for a rock paper scissors game:
computer_choices = ['rock', 'paper', 'scissors']
print('Computer can choose between:')
for i in range(3):
    print('\t', computer_choices[i])
choice = random.choice(computer_choices)
print('And it randomly chooses:', choice)

# Looping list items
computer_choices = ['rock', 'paper', 'scissors']
print('Computer can choose between:')
for choice in computer_choices:
    print('\t', choice)

# Looping list items with indexing
computer_choices = ['rock', 'paper', 'scissors']
print('Computer can choose between:')
for idx, choice in enumerate(computer_choices):  # You need to surround the list you're iterating with enumerate(), which can be unpacked to an index, and a value.
    print('\t', choice)

for idx, choice in enumerate(computer_choices):  # You can name the unpacked index variable anything, including _
    print('\t', choice)

# Looping dict elements
player_scores = {name: score,
                'Someone else': 1
                }
print('Leaderboard:')
for key, val in player_scores.items():  # .items() needs to be unpacked to key:value pairs
    print(key, '\t', val)

print('Leaderboard:')
for name, score in player_scores.items():  # the key and value variables can be named anything, even a _ ...
    print(key, '\t', val)

# ...but instead of naming the unpacked tuple element _, it is better to only iterate keys or values:
# Loop keys only
print('Leaderboard names:')
for name in player_scores.keys():  # use .keys()
    print('\t', name)

# Loop values only
print('Leaderboard scores:')
for scores in player_scores.values():  # use .values()
    print(scores)


# ===================
# We want to compare a user's choice to the computer's
choice = 'scissors'
user_choice = 'rock'
if user_choice == choice:
    print('Matching!')
else:
    print('Not Matching.')

computer_score = 3
win_score = 5

user_score = 2
# user_score = 3
if user_score < computer_score:
    print('Play better')
else:
    print('Doing alright')

# Try the following with both user_scores by swapping the commented line.
user_score = 3
# user_score = 4
if user_score <= computer_score:
    print('Play better')
else:
    print('Doing alright')

# Here is an example of a ternary operator doing the above, but in one line.
print('Play better') if user_score <= computer_score else print('Doing alright')

user_score = 4
if user_score > computer_score and user_score < win_score:
    print('Doing good, but keep at it')

if computer_score < user_score < win_score:
    print('Doing good, but keep at it')

if computer_score >= win_score or user_score >= win_score:
    print('Game over')

# You can try the below comparison with the following user_score values
user_score = 2
# user_score = 3
# user_score = 4
# user_score = 5
if user_score <= computer_score:
    print('Not good, chief')
elif computer_score < user_score < win_score:
    print('Keep up the good work')
else:
    print('You\'ve managed to win? Amazing...')

# ===================
# While loops
count = 1
condition = True
while condition:
    print('I have now printed this', count, 'times')
    count = count + 1
    condition = count <= 5

count = 1
while True:
    print('I have now printed this', count, 'times')
    count = count + 1
    if count > 5:
        break

# ===================
# Augmented assignments
# Addition
count = 1
increment = 3
count += 1
print('Count is now:', count)
count += increment  # addition
print('Count is now:', count)
count -= 2  # subtraction
print('Count is now:', count)

count = 23
multiplier = 3
count *= multiplier  # multiplication
print('Count is now:', count)
count /= multiplier  # division - results in a float
print('Count is now:', count)
count //= multiplier  # integer division - results in an integer
print('Count is now:', count)

count = 3
multiplier = 3
count **= multiplier  # power
print('Count is now:', count)
count %= 7  # remainder
print('Count is now:', count)

count = 81
count_int_div = count // 7
count_rem = count % 7
print(count_int_div, '*', 7, '+', count_rem, '=', count_int_div*7+count_rem, 'which equals', count)
