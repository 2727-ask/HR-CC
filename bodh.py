def print_formatted(no):
    width = len(bin(no)) - 2
    for x in range(1,no+1):
        b=bin(x)
        o=oct(x)
        h=hex(x)
        c=h.upper()
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(x,width = width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)