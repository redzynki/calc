# This method returns unduplicated,sorted common elements of few lists

def common_elements(x):
    result = set(x[0])
    for lst in x:
        result = result & set(lst)
    return sorted(list(result))

