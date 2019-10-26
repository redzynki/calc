# This method returns unduplicated,sorted common elements of few lists
def common_elements(x):

    a = [1,2,3,3,7,11,11,11]
    b = [2,5,7,11,13,15,20]
    c = [1,2,3,7,11,55,116]
    d = [1,1,1,2,3,4,4,7,8,11]

    x = sorted(list(set(a) & set(b) & set(c) & set(d)))

    return x

