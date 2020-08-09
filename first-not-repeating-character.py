# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
# If there is no such character, return '_'.

# Example
#
#    For s = "abacabad", the output should be
#    first_not_repeating_character(s) = 'c'.
#
#    There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.
#
#    For s = "abacabaabacaba", the output should be
#    first_not_repeating_character(s) = '_'.
#
#    There are no characters in this string that do not repeat.

def first_not_repeating_character(s):
    Non_Repeats = []
    Remember = set()
    
    for char in s:
        if char in Remember:
            continue
        
        try:
            Non_Repeats.remove(char)
            Remember.add(char)
        except:
            Non_Repeats.append(char)
            
    if Non_Repeats.__len__() < 1:
        return "_"            

    return Non_Repeats[0]