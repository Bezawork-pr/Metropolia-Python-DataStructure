"""Sort characters Write a program that takes a single string as
its input and sort its characters from the lowest Unicode value
to the highest Unicode value. The program should print the new string."""

input = input()
result = "".join(sorted(input))
print(result)
