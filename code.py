list1 = []

listinput = '1'
listlen = 0
listpos = 0
v1 = 0

while listinput != 'end':
    listinput = input('input a number into the list of data ')
    if listinput == 'end':
        print('done')
    else:  
        list1.append(listinput)
        listlen += 1

for listn in list1:
    try:
        listn = list(map(int, list1))
    except:
        listn = list(map(float, list1))

print('\nthe data:') 
for lis1 in list1:
    print(lis1)

print('\nthe list length =',listlen)

while listpos < listlen:
    v1 += listn[listpos]
    listpos += 1

v1 /= listlen
print('\nthe mean =',v1)

print('testlistnotright',listn)
print(type(listn[0]))

listpos = 0

for listn in list1:
    print(type(listn[0]))
    try:
        listn[listpos] = int(listn[listpos])
        print(type(listn[0]))
    except:
        listn[listpos] = float(listn[listpos])
        print(type(listn[0]))
    listn[listpos] = pow(listn[listpos], 2)
    lispos += 1

listpos = 0

while listpos < listlen:
    v2 += listn[listpos]
    listpos += 1

print('v2',v2)
