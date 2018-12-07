# 1. Using input() function to get user input

my_name = input('Enter your name: ')

#print('Hello' + my_name)

greeting = ('Hello, {}')
final_greeting = greeting.format(my_name)
print(final_greeting)