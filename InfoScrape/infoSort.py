def combineTime(first,second):
    test = first.copy()
    test2 = second.copy()

    firstrange = []
    master = test.copy()
    master.extend(test2.copy())
    
    for time in master:
        time = time.split(':')
        (h,m) = time[0],time[1]
        t = int(h)*60 + int(m)
        firstrange.append(t)
    
    dictionary = dict(zip(firstrange,master))
    chunk_size = 2
    chunk = [firstrange[i:i+chunk_size] for i in range(0, len(firstrange), chunk_size)]
    chunk = merge(chunk)
    result = [item for sublist in chunk for item in sublist]
    final = []
    for thing in result:
        value = dictionary[thing]
        final.append(value)
    
    return final


def merge(intervals):
    si = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for tup in si:
        if not merged:
            merged.append(tup)
        else:
            b = merged.pop()
            if b[1] >= tup[0]:
                new_tup = (b[0], max(b[1], tup[1]))
                merged.append(new_tup)
            else:
                merged.append(b)
                merged.append(tup)
    return merged

rawData = {}

def StringtoAbstract(str1 = ""):
    data = str1.split('.')
    data[2] = eval(data[2])
    key = data[0] +'.'+data[1]
    
    thisdict = {data[0] + '.' + data[1] : data[2]}

    return thisdict

sortedData = {}

with open('result.txt', 'r') as fp:
    for line in fp:
        TempDict = StringtoAbstract(line)
        obj = list(TempDict.keys())[0]
        if  obj not in sortedData:
            sortedData.update(TempDict)
        else:
            #print(TempDict[obj])
            newValue = combineTime(sortedData[obj],TempDict[obj])
            sortedData[obj] = newValue

f = open('final.txt','w')
for diction in sortedData:
    f.write(diction + '.["' + '","'.join(sortedData[diction]) + '"]\n' )
    

