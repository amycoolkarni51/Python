def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        value = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[value] :
                value = j

        if value != i :
            temp = itemsList[i]
            itemsList[i] = itemsList[value]
            itemsList[value] = temp

    return itemsList


li = [21,6,9,33,3]

print(selectionSort(li))