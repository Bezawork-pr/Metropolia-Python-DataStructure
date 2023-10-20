"""Write a program that takes two integers, a and b, as input.
Your program should compute and display:
The sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The remainder when a is divided by b
The result of log10 a
The result of """
first_num = int(input())
second_num = int(input())

result = first_num + second_num

print('{} + {} is {}'.format(first_num, second_num, result))

result =  first_num - second_num

print('{} - {} is {}'.format(first_num, second_num, result))

result = first_num * second_num
print('{} * {} is {}'.format(first_num, second_num, result))

result = first_num / second_num
print('{} / {} is {}'.format(first_num, second_num, result))

result = first_num % second_num
print('{} % {} is {}'.format(first_num, second_num, result))

result = first_num ** second_num

print('{} ^ {} is {}'.format(first_num, second_num, result))
