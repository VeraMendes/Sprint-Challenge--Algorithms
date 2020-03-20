'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):

    ''' Recursive function to count the number of
    occurrences of 'th' in a string

    parameter: str'''

    # base case (for words less than 2 char long)
    if len(word) < 2:
        return 0

    # otherwise initialize occurrence
    occurrence = int(word[0:2] == 'th')

    # if word is 2 char long and this chars are 'th'
    # add to occurrence
    if len(word) == 2 and word == 'th':
        return occurrence

    # keep number of occurrences and move along the word,
    # 1 char at a time
    else:
        return occurrence + count_th(word[1:])      
