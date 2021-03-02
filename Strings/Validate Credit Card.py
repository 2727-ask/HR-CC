import re
import textwrap
#print(help(re))
for x in range(6):
    a = input().replace('-','')
    a_n=textwrap.wrap(a,4)
    print(a_n)
    listToStr = ' '.join([str(elem) for elem in a_n])
    print(listToStr)

    if len(a) >16 or re.findall("0000|1111|2222|3333|4444|5555|6666|7777|8888|9999",a) :
        print('invalid')
    else:
        print('valid')

