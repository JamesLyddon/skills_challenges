def check_grammar(str):
    end_chars = {'.', '?', '!'}
    if str is None:
        raise Exception('please include a string to check')
    if str[0].isupper() and str[-1] in end_chars:
        return True
    return False
