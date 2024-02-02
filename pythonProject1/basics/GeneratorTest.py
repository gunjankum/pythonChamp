

def gen_test(n):

    val =0
    while val < n:
        yield n
        val +=1


for x in gen_test(3):
    print(x)
