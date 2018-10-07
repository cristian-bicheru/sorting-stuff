import math

def sort(array):
    sortedlist = [array[0]]
    for i in range(1, len(array)):
        cval = array[i]
        lentry = sortedlist[-1]
        div = cval/lentry
        if div >= 1:
            sortedlist.append(cval)
        else:
            estindex = math.floor(div*len(sortedlist))
            while True:
                entry = sortedlist[estindex]
                if entry == cval:
                    sortedlist.insert(estindex, cval)
                    break
                elif entry > cval:
                    if estindex != 0:
                        if sortedlist[estindex-1] <= cval:
                            sortedlist.insert(estindex, cval)
                            break
                        else:
                            estindex += -1
                    else:
                        sortedlist.insert(0, cval)
                        break
                else:
                    if sortedlist[estindex+1] >= cval:
                        sortedlist.insert(estindex+1, cval)
                        break
                    else:
                        estindex += 1
    return sortedlist
