"""Write a program that prints a dictionary where the keys
are numbers between 1 and N, and the values are square of keys."""

input = int(input())
my_dict = {}

for i in range(1, input + 1):
    my_dict[i] = i ** 2

print (my_dict)
