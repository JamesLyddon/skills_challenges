def check_grammar(str):
    end_chars = {'.', '?', '!'}
    if str is None:
        raise Exception('please include a string to check')
    return str[0].isupper() and str[-1] in end_chars
