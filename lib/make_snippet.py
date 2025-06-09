# A function called make_snippet that takes a string as an argument
# and returns the first five words and then a '...' 
# if there are more than that.

def make_snippet(str=''):
    if not str:
        return ''
    words = str.split()
    first_five = words[0:5]
    return ' '.join(first_five) + '...'