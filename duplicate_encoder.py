'''
The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))((" 
'''
def duplicate_encode(word):
    a,b,word = [],{},word.lower()
    for letter in word:
        b[letter] = 0
    for letter in word:
        b[letter] += 1
    for letter in word:
        if b[letter] >= 2:
            a.append(')')
        elif b[letter] < 2:
            a.append('(')
    return ''.join(a)
