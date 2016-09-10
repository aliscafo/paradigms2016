# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
#
# Example input: 'read'
# Example output: 'reading'
def verbing(s):
    res = ''
    n = len(s)
    
    if n >= 3:
        if s[n - 3:] == 'ing':
            s = s[0:n-3] + 'ly'
        else:
            s += 'ing'
    
    return s

 
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
#
# Example input: 'This dinner is not that bad!'
# Example output: 'This dinner is good!'
def not_bad(s):
    n = len(s)
    first_not = s.find('not')
    first_bad = s.find('bad')
    
    if first_not != -1 and first_not < first_bad:
        s = s[:first_not] + 'good' + s[first_bad+3:]
        
    return s
 
 
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
#
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
#
# Example input: 'abcd', 'xy'
# Example output: 'abxcdy'
def front_back(a, b):
    s = ''
    n, m = len(a), len(b)
    mid_a = (n + 1) // 2
    mid_b = (m + 1) // 2
    
    s = a[:mid_a] + b[:mid_b] + a[mid_a:] + b[mid_b:]
    
    return s