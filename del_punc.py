import string

def del_punctuation(st):
    """ this is a function to eliminate punctuations fron a sentences"""
    new_st=""
    for element in st:
        if element not in string.punctuation:
            new_st+=element
    # st=new_st
    # print(st)
    return new_st