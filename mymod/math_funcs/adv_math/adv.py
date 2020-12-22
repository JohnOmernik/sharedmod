

def math_sqr(val, inttimes):
    retval = val
    if inttimes == 0:
        retval = 1
    elif inttimes == 1:
        retval = val
    elif inttimes > 1:
        for x in range(inttimes - 1):
            retval = retval * val
    else:
        print("Error")
        retval = 0
    return retval
