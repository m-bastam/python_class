def find_char(st, ch, start = 0, end = None):
    """this is a mothod to find a char in string
    If you want to use some (but not all) optional parameters with multiple parameters,
     make sure the optional ones are the last ones entered """
    
    str_index = start
    if end is None :
        end = len(st)
        
    while str_index < end:
        if st[str_index] == ch:
            return str_index
        str_index += 1
    return -1

str_sample = "bannana and apple"
char = "p"
# result = find_char(str_sample, char, end=15)
result = find_char(end = 50 , ch = char , st = str_sample)
print(result)
print(str_sample.find("nan"))

    