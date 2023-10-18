#ex1
'''
myTable = [12,89,53]

ind1 = 1
ind2 = 2


val = myTable[ind1]

myTable[ind1] = myTable[ind2]
myTable[ind2] = val


print(myTable)
'''


#ex3

'''
myTable = [53, 89, 12]

def exo(myTable):
    n = len(myTable)
    for i in range(n):
        for j in range(0, n-i-1):
            if myTable[j] > myTable[j+1]:
                myTable[j], myTable[j+1] = myTable[j+1], myTable[j]

exo(myTable)
print(myTable)
'''













