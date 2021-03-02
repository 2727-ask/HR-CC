list = ['c','b','a']
print('c'.center(9,'-'))
print('c-b-c'.center(9,'-'))
print('c-b-a-b-c'.center(9,'-'))
print('c-b-c'.center(9,'-'))
print('c'.center(9,'-'))

string = "c"
for x in range(1,len(list)):
    string = f'{string}-{list[x]}'
    print(string.center(9,'-'))
    string = string.ljust(9,'-')
    print(string)
