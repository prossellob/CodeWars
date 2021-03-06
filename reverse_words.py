'''
Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Every space should stay, so you cannot use words from Prelude.

Example:

reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"

reverseWords "An example!"    -- "nA !elpmaxe"
reverseWords "double  spaces" -- "elbuod  secaps"
'''
def reverse_words(str):
    a = str.split(' ')
    b = []
    for word in a:
        b.append(word[::-1])
    return ' '.join(b)

