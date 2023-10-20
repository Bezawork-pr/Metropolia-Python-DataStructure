"""Write a function called "custom_encoder" that accepts
a string text as parameter and for each char of the text it
calculates its 0-based position in the following reference string"""
def custom_encoder( my_string):
  reference_string = list('abcdefghijklmnopqrstuvwxyz')
  position = [ ]
  my_string = my_string.lower()
  for i in my_string:
    if i in reference_string:
        position.append(reference_string.index(i))
    else:
        position.append(-1)
  return position
