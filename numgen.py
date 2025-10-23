def number_pattern(n):

    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'

    pattern = ''
    for i in range(n):
        i = i + 1
        if i == 1:
            pattern = pattern + str(i)  # First number is without a space
        else:
            pattern = pattern + ' ' + str(i)  # The following numbers should be separated by a space
    
    return pattern

print(number_pattern(7))
