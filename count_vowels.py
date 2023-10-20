"""Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'."""
string = input()
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
sum = 0
for i in string:
    if i in vowels:
        sum += 1
print("Number of vowels: {}".format(sum))
