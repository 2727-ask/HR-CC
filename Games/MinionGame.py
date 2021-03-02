def minion_game(string):
    kevin = 0
    stuart = 0
    for x in range(len(string)):
        if (string[x] in ['A', 'E', 'I', 'O', 'U']):
            kevin = kevin + len(string) - x
        else:
            stuart = stuart + len(string) - x
    if kevin > stuart:
        print("Kevin",kevin)
    elif stuart > kevin:
        print("Stuart",stuart)
    else:
        print("Draw")

    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)