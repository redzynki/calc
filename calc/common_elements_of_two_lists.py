# This method returns common elements of two lists
def common_elements(x):

    a = [1,1,2,3,5,8,13,21,34,55,89]
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13]


    x = list(set(a) & set(b))

    return x

