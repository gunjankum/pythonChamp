def toString(List):
    s = ""
    for x in List:
        if x == '\0':
            break
        s += x
    return s


def printPatternutil(string, buff, i, j, n):
    if i == n:
        buff[j] = '\0'
        print(toString(buff))
        return

    buff[j] = string[i]
    printPatternutil(string, buff, i+1, j+1, n)


    buff[j] = ' '
    buff[j+1] = string[i]
    printPatternutil(string, buff, i + 1, j + 2, n)



def printpattern(string):
    n = len(string)
    buff = [0] * (2 * n)
    buff[0] = string[0]
    printPatternutil(string, buff, 1, 1, n)


# Driver Code
string = "ABCD"
printpattern(string)
