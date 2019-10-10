# This metod returns strings with elements marked as even or odd.

def numbers_parity(limit):
    result = []
    for element in range(0, limit + 1):
        if element % 2 == 0:
            result.append(str(element) + " EVEN")
            #result.append("{} EVEN".format(str(element)))
        else:
            result.append(f"{element} ODD")
    return "\n".join(result)

