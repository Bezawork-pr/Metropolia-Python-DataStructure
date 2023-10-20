"""Write a program that takes a positive integer, n, as input
and then displays the sum of all of the integers from 1 to n. """
sum = 0

num = int(input())

for i in range(num + 1):
    sum += i
print("The sum of the first {} positive integers is {}".format(num, sum))
